from flask import Flask, request, render_template
import numpy as np
import spacy
import en_core_web_lg

nlp = en_core_web_lg.load()

app = Flask(__name__)


@app.route('/')
def index():
    query = request.args.get("query", None)
    if query:
        app.logger.info("Query {} received".format(query))
        results = retrieve(query)
        return render_template('results.html', query=query, results=results)
    else:
        return render_template('index.html')


def retrieve(query):
    doc = nlp(query)
    app.logger.debug("Ran NLP on query.")
    return ["https://google.com/" for i in range(9)]


#app = Flask(__name__)

@app.route("/home")
def hello():
    return "<h1>Home ddsafdddddddddddddddddsafsPage !</h1>"

#we create a sub-page "/about" and defination a different page for it 
@app.route("/about")
def about():
    return "<a>ABOUT!</a>"

#tradionaly we use "set FLASK_ENV=development" or "set FLASK_DEBUG=1" to enable dubug mode
#In powershell(termianl) we should "set FLASK_APP=app.py" which app.py is fixed name
#in termianl we can use "flask run"
if __name__=="__main__":
    #in here we can directly use this line to activate debug mode
    app.run(debug=True)