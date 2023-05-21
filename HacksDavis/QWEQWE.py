from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained(
    "pszemraj/long-t5-tglobal-xl-16384-book-summary"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "pszemraj/long-t5-tglobal-xl-16384-book-summary",
    load_in_8bit=True,
    device_map="auto",
)

print(tokenizer)