from flask import Flask

from document_process import document_process

import json
import pickle
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world"

def filterFunction(result):
    print(result)
    if result['score'] > 0.2:
        return True
    return False

@app.route("/process")
def process_document():
    filename = 'saved_model.pkl'
    if os.path.isfile(filename):
        model = pickle.load(open(filename, 'rb'))
        if os.path.isfile( 'cos_sim.pkl'):
            print('aici')
            cos_sim = pickle.load(open('cos_sim.pkl', 'rb'))
            results = document_process(model, cos_sim)
        else:
            print('here')
            results = document_process(model)
    else:
        results = document_process()
    filteredResult = filter(filterFunction, results)
    # print(result)
    return json.dumps(list(filteredResult))