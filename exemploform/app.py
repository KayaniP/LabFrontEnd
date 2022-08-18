from flask import Flask, render_template, request
from pessoa import Pessoa

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/click", methods=['GET'])
def click():
    return render_template("index.html")

@app.route("/salvar", methods=['POST', 'GET'])
def salvar():
    nome = request.form.get('nome', 'none')
    idade = request.form.get('idade', '0')
    pessoa = Pessoa(nome, idade)  
    return render_template("index.html", pessoa = pessoa)
