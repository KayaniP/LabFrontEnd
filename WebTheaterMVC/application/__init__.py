from distutils.log import debug
from flask import Flask
import os

app = Flask(__name__,
            static_folder = os.path.abspath("application/view/static"),
            template_folder = os.path.abspath("application/view/templates"),
             )


from application.controller import postagem_controller
