from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from pydantic import BaseModel
from fastapi.responses import JSONResponse
from src.components.graph import build_agent
import unicodedata

from auth import auth, models, schemas, security
from auth.db import get_db

from src.utils.custom_exception import CustomException
from src.utils.logger import logger

router = APIRouter()


logger = logger(__name__)

async def main(query : str):
    try:
        graph = await build_agent()
        
        result = await graph.ainvoke(
            {
                "input": query
            }
        )
        
        return result
    
    except Exception as e:
        error = CustomException("An error occurred",e)
        logger.error(error)


class Request(BaseModel):
    task : str


@router.post("/register/", response_model=schemas.UserInDBBase)
async def register(user_in : schemas.UserIn, db : Session = Depends(get_db)):
    
    db_user = auth.get_user(db, username = user_in.username)
    
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    db_user = db.query(models.User).filter(models.User.email == user_in.email).first()
    
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = security.get_password_hash(user_in.password)
    
    db_user = models.User(
        **user_in.model_dump(exclude={"password"}),
        hashed_password = hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)
):
    user = auth.get_user(db, username=form_data.username)
    
    if not user or not security.pwd_context.verify(
        form_data.password,
        user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers = {"WWW-Authenticate" : "Bearer"}
        )
        
    access_token_expire = timedelta(minutes=security.ACCESS_TOKEN_EXPIRE)
    
    access_token = security.create_access_token(
        data = {'sub' : user.username},
        expires_delta=access_token_expire
    )
    
    return {"access_token" : access_token, "token_type" : "bearer"}
    


@router.post("/task")
async def task(request : Request, current_user : schemas.UserInDB = Depends(auth.get_current_user)):
    
    query = request.task
    result = await main(query=query)
    output = result.get("output", "") if result else ""
    normalize_output = unicodedata.normalize('NFC', output)
    
    try:
        return JSONResponse(
            status_code=200,
            content={
                "response" : normalize_output
            }
        )
    except Exception as e:
        return JSONResponse(status_code=200, content=str(e))
    
    
    