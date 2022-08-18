from flask import Flask, render_template
from flask import Flask, render_template, request
from application.model.entity.produto import Produto
from application import app


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/click", methods=['GET'])
def click():
    return render_template("index.html")

@app.route("/salvar", methods=['POST', 'GET'])
def salvar():
    nome = request.form.get('nome', 'none')
    valor = request.form.get('valor', '0')
    quantidade = request.form.get('quantidade', '0') 

    return render_template("index.html", produto = Produto, nome = nome, valor = valor, quantidade = quantidade)


