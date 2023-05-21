import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from PyPDF2 import PdfReader


path = "/Users/dr1229/Desktop/Davis/SpeedReadChat/HacksDavis/Anth3_Workbook_Winter_2023.pdf"

reader = PdfReader(path)

FileContent = ""

for i,page in enumerate(reader.pages):
    #if i < 40 and i > 30:
    FileContent += page.extract_text()



checkpoint = "sshleifer/distilbart-cnn-12-6"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

print(len(FileContent))

print(tokenizer.model_max_length)

print(tokenizer.model_max_length)

sentences = nltk.tokenize.sent_tokenize(FileContent)

print(max([len(tokenizer.tokenize(sentence)) for sentence in sentences]))


length = 0
chunk = ""
chunks = []
for count, sentence in enumerate(sentences):
  combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

  if combined_length  <= tokenizer.max_len_single_sentence: # if it doesn't exceed
    chunk += sentence + " " # add the sentence to the chunk
    length = combined_length # update the length counter

    # if it is the last sentence
    if count == len(sentences) - 1:
      chunks.append(chunk.strip()) # save the chunk
    
  else: 
    chunks.append(chunk.strip()) # save the chunk
    
    # reset 
    length = 0 
    chunk = ""

    # take care of the overflow sentence
    chunk += sentence + " "
    length = len(tokenizer.tokenize(sentence))
print(len(chunks))

inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

for i, input in enumerate(inputs):
  if i  < 3 and i > 0:
    output = model.generate(**input)
    print(tokenizer.decode(*output, skip_special_tokens=True))