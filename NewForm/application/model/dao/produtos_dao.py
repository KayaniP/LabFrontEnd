from application.model.entity.produtos import Produto

class ProdutosDao:
    def __init__(self) -> None:
        self._lista = [
            Produto(98824834, 'Melancia', 50, 20, True)
        ]

    def listar_produtos(self):
        return self._lista
