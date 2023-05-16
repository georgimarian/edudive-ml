from flask import Flask
from document_process import document_process

app = Flask(__name__)

@app.route("/")
def hello_world():
    document_process()
    return "hello world"