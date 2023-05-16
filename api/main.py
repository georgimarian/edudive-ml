from flask import Flask
from util.document_process import document_process

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/process")
def process_document():
    return document_process()