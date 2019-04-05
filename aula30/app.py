from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello_inicial():
    return "Hello World!"


@app.route("/index")
def hello_url():
    return "Url 2!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

app.run()
