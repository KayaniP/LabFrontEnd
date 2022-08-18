from flask import Flask, render_template
from application.model.entity.produto import Produto

app = Flask(__name__)

lista_produtos = [
    Produto(0, "AllStar Sei la", 100, 10),
    Produto(1, "Chinelao Havaiana", 200, 40),
    Produto(2, "Bone Bilabong", 100, 20)
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/produto")
def listar_produto():   
    return render_template("lista-produto.html", produtos=lista_produtos)

@app.route("/produto/<id>")
def exibir_produto(id):
    return render_template("exibir-produto.html", produto=lista_produtos[int(id)])
