from application.model.entity.produto import Produto

class ProdutoDao:

    def listar_produto(self):
        #Retorar uma lista de produtos!
        self._lista = [
            Produto('Celular',20,5000),
            ]


    def listar_produtos(self):
        return self._lista
