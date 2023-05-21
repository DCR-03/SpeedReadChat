from flask import Flask, send_from_directory
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
#from api.HelloApiHandler import HelloApiHandler
from api.ParsePDFHandler import ParsePDFHandler


# from PIL import Image
# import pytesseract
# import numpy as np

from PyPDF2 import PdfReader




app = Flask(__name__, static_url_path="", static_folder="frontend/build")
CORS(app)
api = Api(app)


@app.route("/", defaults={"path": ""})
def serve(path):
    return send_from_directory(app.static_folder, "index.html")


api.add_resource(ParsePDFHandler, "/flask/parse")
