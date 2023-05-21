from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from api.HelloApiHandler import HelloApiHandler

# from PIL import Image
# import pytesseract
# import numpy as np

from PyPDF2 import PdfReader
from pdf2image import convert_from_path


path = "test.pdf"

reader = PdfReader(path)

doc = convert_from_path("test.pdf")

print(len(reader.pages))

# for page_number, page_data in enumerate(doc):
#     ocr = pytesseract.image_to_string(page_data).encode("utf-8")
#     print("Page # {} - {}".format(str(page_number),ocr))
# print(ocr)
#
text = ""
for page in reader.pages:
    text += page.extract_text();


app = Flask(__name__, static_url_path="", static_folder="frontend/build")
CORS(app)
api = Api(app)


# @app.route("/", defaults={"path": ""})
@app.route("/data")
def get_time():
    return {
            "feild1" : "test1",
            "text" : text
            }
# def serve(path):
#     return send_from_directory(app.static_folder, "index.html")


# api.add_resource(HelloApiHandler, "/flask/hello")
