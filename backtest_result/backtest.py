import asyncio
import csv
import time
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import matplotlib.pyplot as plt 
import unicodedata

from src.components.graph import build_agent
from src.utils.custom_exception import CustomException
from src.utils.logger import logger

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

# output = asyncio.run(main(query=prompt))
        
## Testing
### Q&A
qa_inputs = [
    "Instagram: Coffee brand promo",
    "LinkedIn: Tech company announcement"
]

# expected_answers = [
#     "The capital of Bangladesh is Dhaka.",
#     "Photosynthesis is the process by which green plants use sunlight to convert carbon dioxide and water into glucose and oxygen.",
#     "'Pride and Prejudice' was written by Jane Austen."
# ]

qa_result = []

for q in qa_inputs:
    start = time.time()
    output = asyncio.run(main(query=q))
    end = time.time()
    # smooth_fn = SmoothingFunction().method1
    # score = sentence_bleu([expected_answers[i].split()], output["output"].split(), smoothing_function=smooth_fn)
    normalized_text = unicodedata.normalize('NFC', output["output"])
    qa_result.append(
        {
            "Question" : q,
            "Answer" : normalized_text,
            "Response Time (s)" : round(end - start, 2),
            # "Accuracy (BLEU)" : score
        }
    )

# Save csv
keys = qa_result[0].keys()

with open("backtest_result/content_result.csv","w", newline="", encoding="utf-8") as file:
    write = csv.DictWriter(file,fieldnames=keys)
    write.writeheader()
    write.writerows(qa_result)


# Chart

# plt.bar([f"Question + {r+1}" for r in range(len(qa_result))], [r["Accuracy (BLEU)"] for r in qa_result])
# plt.title("Q&A Node Accuracy")
# plt.ylabel("Accuracy")
# plt.tight_layout()
# plt.savefig("backtest_result/qa_accuracy.png")
# plt.clf()
