import torch
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    "pszemraj/long-t5-tglobal-xl-16384-book-summary",
    device=0 if torch.cuda.is_available() else -1,
)
long_text = "Here is a lot of text I don't want to read. Replace me"

result = summarizer(long_text)
print(result[0]["summary_text"])