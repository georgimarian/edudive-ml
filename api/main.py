from flask import Flask

from document_process import document_process, showcase_model, multilingual_model, text_summarization

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


@app.route("/simpleExample")
def simple_example():
    result = showcase_model()
    result_as_list = list(result)
    stringResp = ''
    for i in range(len(result_as_list)):
        stringResp += "<tr><td>{}</td><td>{}</td><td>{:.4f}</td></tr>".format(
            result_as_list[i]['element'], result_as_list[i]['skill'], result_as_list[i]['score'])
    return '<table style="width:50%"><th>Skill set</th><th>Sentence</th><th>Score</th>' + stringResp + '</table>'


@app.route("/multilingualSimpleExample")
def multilingual_simple_example():
    result = multilingual_model()
    result_as_list = list(result)
    print(result)
    stringResp = ''
    for i in range(len(result_as_list)):
        stringResp += "<tr><td>{}</td><td>{}</td><td>{:.4f}</td> </tr>".format(
            result_as_list[i]['element'], result_as_list[i]['skill'], result_as_list[i]['score'])
    return '<table style="width:50%"><th>Skill set</th><th>Sentence</th><th>Score</th>' + stringResp + '</table>'


@app.route("/summarizationExample")
def summarization_simple_example():
    result = text_summarization()
    result_as_list = list(result)
    stringResp = """<div><h1>Summarization</h1><div><h4>Initial: </h4><p>
    As for the future, I plan to develop my Software Engineer career by studying at a Software Engineering Master’s program in Computer Science, learning about technologies and methodologies at the highest level. 
    Software Engineering is strongly coupled with the developer career, and I believe such a Master would aid me in becoming a better developer for the following two years.
    I would like to apply the gained knowledge in the context of a Distributed Web and Mobile application, having both microservices on the back-end and micro-frontend architectures on the front-end. 
    The proposed application domain is that of an Erasmus application/management tool, in which students’ access to Erasmus+ scholarships is facilitated.
    Such an application would enable me to strengthen my backend and mobile skills, while also researching the domain of micro-frontends.
    Upon finishing my Master’s degree, I would like to further my career in Computer Science by aiming to become a Software Architect in a company, while also applying for a PhD in a related field. 
    I would like for my education to strongly support my professional development and to make me a better programmer and leader. 
    If possible, I would like to offer my knowledge in teaching other young students how to better themselves as coders and to learn from all the mistakes I have made during my career path. 
    I believe that my professional and academic performance, together with my Erasmus experience, would help me bring innovation as a teacher and make Computer Science more attractive to students.
    </p></div></div><h4>Summary:</h4><p>"""
    for i in range(len(result_as_list)):
        stringResp += "<p>{}</p>".format(result[i])
    return '<div style="width:50%">' + stringResp + '</p></div>'


@app.route("/demo-process")
def demo_process_document():
    filename = 'saved_model.pkl'
    if os.path.isfile(filename):
        model = pickle.load(open(filename, 'rb'))
        if os.path.isfile('cos_sim.pkl'):
            cos_sim = pickle.load(open('cos_sim.pkl', 'rb'))
            results = document_process(model, cos_sim)
        else:
            results = document_process(model)
    else:
        results = document_process()
    filteredResult = filter(filterFunction, results)
    # print(result)
    result_as_list = list(filteredResult)
    stringResp = ''
    for i in range(len(result_as_list)):
        stringResp += "<tr><td>{}</td><td>{}</td><td>{:.4f}</td> </tr>".format(
            result_as_list[i]['element'], result_as_list[i]['skill'], result_as_list[i]['score'])
    return '<div><h1>Document Process Demo</h1><a href="https://www.cs.ubbcluj.ro//files/curricula/2022/syllabus/IS_sem1_MME8025_en_grigo_2022_6966.pdf">RE</a>' + stringResp + '</table></div>'


@app.route("/process")
def process_document():
    filename = 'saved_model.pkl'
    if os.path.isfile(filename):
        model = pickle.load(open(filename, 'rb'))
        if os.path.isfile('cos_sim.pkl'):
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


if __name__ == "__main__":
    from waitress import serve
    serve(app, host=os.getenv("HOST", default="0.0.0.0"),
          port=os.getenv("PORT", default=8080))
