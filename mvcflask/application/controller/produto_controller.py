from flask import render_template
from application import app
from application.model.dao import produto_dao
from application.model.dao.produto_dao import ProdutoDao


@app.route("/produtos")
def lista_produto():
    produto_dao = ProdutoDao()
    lista_produto = produto_dao.listar_produto()     
    return render_template("produtos.html", produtos = lista_produto)