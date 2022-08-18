class Produto:
    def __init__(self, id, nome, valor, quantidade, ativo, imagem ) -> None:
        self._id = id 
        self.__nome = nome
        self._valor = valor
        self._quantidade = quantidade
        self._ativo = ativo
        self._imagem = imagem 

    
    def get_id(self):
        return self._id
    
    def get_nome(self):
        return self.__nome
    
    def get_valor(self):
        return self._valor

    def get_quantidade(self):
        return self._quantidade

    def get_ativo(self):
        return self._ativo
    
    def get_imagem(self):
        return self._imagem
