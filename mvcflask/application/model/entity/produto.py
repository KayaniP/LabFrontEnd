class Produto:

    def __init__(self, nome, quantidade, valor) -> None:
        self.__nome = nome
        self.__quantidade = quantidade
        self.__valor = valor

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, quantidade):
        self.__quantidade = quantidade
    
    def get_valor(self):
        return self.__valor
    def set_valor(self, valor):
        self.__valor = valor