from flask import render_template
from application import app
from application.model.entity import produtos
from application.model.dao import produtos_dao
from application.model.dao.produtos_dao import ProdutosDao
produtos = produtos_dao

@app.route("/produtos")
def listar_produtos():
    produtos_lista = produtos.listar_produtos()
    return render_template('produtos.html', produtos = produtos_lista)