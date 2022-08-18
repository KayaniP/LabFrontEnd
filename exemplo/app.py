from flask import Flask, render_template
from estado import Estado
from noticia import Noticia

app = Flask(__name__)

estado_rio = Estado(1, "Rio de Janeiro", "RJ")

estado_minas = Estado(2, "Minas Gerais", "MG")

estado_espirito = Estado(3, "Espirito Santo", "ES")

noticia_minas_lista = [
    Noticia(1, "Vacinacao contra a Covid: mais de 160 milhoes de brasileiros", "Os dados do consorcio de veiculos de imprensa desta segunda-feira (28) mostram que 160.074.934 brasileiros estao totalmente imunizados. Este numero representa 74,51...", estado_minas),
    Noticia(2, "Brasil tem 86 mortes por Covid-19 em 24 horas", "O Brasil registrou nesta segunda-feira (28) 86 mortes pela Covid-19 nas ultimas 24 horas, totaliza...", estado_minas)
]

noticia_rio_lista = [
    Noticia(3, "Covid: como proteger crianca de ate 5 anos", "No Brasil, nao existem imunizantes contra a covid aprovados para quem...", estado_rio)
]

noticia_espirito_lista = [
    Noticia(4, "Com Covid em alta, Xangai decide...", "A cidade de Xangai vai impor confinamentos por setores par...", estado_espirito)
]

estado_rio.set_noticia_lista(noticia_rio_lista)
estado_minas.set_noticia_lista(noticia_minas_lista)
estado_espirito.set_noticia_lista(noticia_espirito_lista)

#noticias_lista = [noticia_espirito_lista, noticia_minas_lista, noticia_rio_lista]

estado_lista = [
    estado_rio,
    estado_minas,
    estado_espirito
]

@app.route("/")
def home():
    return render_template("home.html", estados=estado_lista) 

@app.route("/estado/<string:uf>")
def noticias_do_estado(uf):
    for estado in estado_lista:
        if estado.get_uf() == uf:
            return render_template("noticias-estado.html", noticias=estado.get_noticia_lista())
    return render_template("home.html", estados=estado_lista)


