from flask import render_template, request
from application import app 

from application.model.entity.Postagem import Postagem
from application.model.dao import postagemDao

@app.route("/", methods=["GET"])
def timeline():
    lista_postagens = postagemDao.ordenar_data()
    return render_template('home.html', postagens=lista_postagens )

@app.route("/postar", methods=["GET", "POST"])
def postar():
    if request.method == "POST":
        id = postagemDao.gerar_id()
        titulo = request.form.get("titulo", "")
        mensagem = request.form.get("mensagem", "")
        nova_postagem = Postagem(id, titulo, mensagem)
        postagemDao.inserir_postagem(nova_postagem)
    
    return render_template("form.html")
