# AI Agent

An intelligent agent system built with LangChain, LangGraph, and FastAPI that combines graph-based routing with advanced language models to handle various types of queries including Q&A, real-time information retrieval, image generation, and social media content tailoring.

## Architecture

![Agent Architecture](img/agent_architecture.PNG)

## Features

- **Multi-Modal Capabilities**

  - Question & Answer
  - Real-time Web Search
  - Image Generation
  - Social Media Content Optimization

- **Intelligent Routing**

  - Automatic query classification
  - Task-specific node handling
  - State management with MemorySaver

- **Authentication & Security**

  - JWT-based authentication
  - Password hashing with bcrypt
  - Rate limiting
  - CORS support

- **API Integration**
  - FastAPI backend
  - Model Context Protocol (MCP) integration
  - Exa AI tools integration

## Tech Stack

- **Backend Framework**: FastAPI
- **AI/ML**:
  - LangChain
  - LangGraph
  - MCP (Model Context Protocol)
  - Models:
    - Llama 3.3 70B Versatile (Main LLM)
    - OpenAI GPT-OSS 20B (Agent LLM)
- **Tools & Services**:
  - Smithy AI (MCP Tools Provider)
  - Exa AI Search Integration
- **Database**: SQLite with SQLAlchemy
- **Authentication**: JWT with OAuth2
- **Testing**: Built-in backtest functionality

## Project Structure

```
.
├── auth/                           # Authentication related code
│   ├── __init__.py
│   ├── auth.py                    # Authentication logic
│   ├── db.py                      # Database configuration
│   ├── models.py                  # SQLAlchemy models
│   ├── routes.py                  # API routes
│   ├── schemas.py                 # Pydantic models
│   └── security.py                # Security utilities
├── backtest_result/               # Testing results and metrics
│   ├── content_result.csv        # Content generation test results
│   ├── image_result.csv         # Image generation test results
│   ├── latest_result.csv        # Real-time info test results
│   ├── qa_accuracy.png         # Q&A accuracy visualization
│   └── qa_result.csv           # Q&A test results
├── logs/                         # Application logs
│   ├── log_2025-08-16.log      # Daily logs
│   └── log_2025-08-17.log
├── notebook/                     # Jupyter notebooks
│   ├── ai_agent.ipynb          # Development notebook
│   └── image.png               # Test image
├── src/                         # Source code
│   ├── __init__.py
│   ├── components/             # Core components
│   │   ├── __init__.py
│   │   ├── agent.py           # Agent implementation
│   │   ├── graph.py           # Graph structure
│   │   ├── model.py           # LLM models
│   │   ├── node.py            # Node definitions
│   │   └── tools.py           # MCP tools
│   ├── config/                # Configuration
│   │   ├── __init__.py
│   │   └── config.py         # Configuration settings
│   └── utils/                 # Utilities
│       ├── __init__.py
│       ├── custom_exception.py # Custom error handling
│       └── logger.py          # Logging configuration
├── auth.db                     # SQLite database
├── backtest.py                # Testing script
├── main.py                    # Application entry point
├── pyproject.toml            # Project metadata and dependencies
├── README.md                 # Project documentation
├── requirements.txt          # Project dependencies
└── uv.lock                  # Dependency lock file
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/Root007x/ai_agent.git
cd ai_agent
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

```bash
GROQ_API_KEY = your-secret-key
TOOL_API = your-mcp-api-key
```

4. Run the application:

```bash
uvicorn main:app --host 0.0.0.0 --port 5555 --reload
```

## API Endpoints

- **POST /register/** - Register new user
- **POST /token** - Get authentication token
- **POST /task** - Submit task to AI agent

## Security

- Implements JWT authentication
- Password hashing using bcrypt
- CORS middleware for frontend integration
- Input validation using Pydantic models

## License

This project is licensed under the MIT License - see the LICENSE file for details.
