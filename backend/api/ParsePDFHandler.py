from flask_restful import Api, Resource, reqparse
import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from PyPDF2 import PdfReader
from typing import TextIO
def parsepdf(pdf,pageStart : int,pageEnd : int):

    reader = PdfReader(pdf)

    FileContent = ""

    for i,page in enumerate(reader.pages):
        if i <= pageEnd and i >= pageStart:
            FileContent += page.extract_text()



    checkpoint = "sshleifer/distilbart-cnn-12-6"

    tokenizer = AutoTokenizer.from_pretrained(checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

    #print(len(FileContent))

    #print(tokenizer.model_max_length)

    #print(tokenizer.model_max_length)

    sentences = nltk.tokenize.sent_tokenize(FileContent)

    #print(max([len(tokenizer.tokenize(sentence)) for sentence in sentences]))


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
    #print(len(chunks))

    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

    outputs = []

    for i, input in enumerate(inputs):
    #if i  < 3 and i > 0:
        output = model.generate(**input)
        outputs.append(tokenizer.decode(*output, skip_special_tokens=True))
    
    return outputs


class ParsePDFHandler(Resource):
    #def get(self):
     #   return {
      #      "feild1" : "test1",
       #     "text" : text
        #    }
    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument("pdf_input", required=True, type=TextIO)
        parser.add_argument("pageStart", required=True, type=int)
        parser.add_argument("pageEnd", required=True, type=int)

        args = parser.parse_args()

        print(args)

        request_file = args["pdf_input"]
        page_start = args["pageStart"] if args["pageStart"] else 0
        page_end = args["pageEnd"] if args["pageEnd"] else 4294967296
        ret_msg = request_file

        if ret_msg:
            message = parsepdf(request_file,page_start,page_end).toString()
        else:
            message = "No Msg"

        final_ret = {"status": "Success", "message": message}

        return final_ret

