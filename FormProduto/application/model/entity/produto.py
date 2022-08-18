class Produto:
    def __init__(self, nome, valor, quantidade, img):
        self.__nome = nome 
        self.__valor = valor 
        self.__quantidade = quantidade
        self.__img = img
    def get_nome(self):
        return self.__nome
    def get_valor(self):
        return self.__valor
    def get_quantidade(self):
        return self.__quantidade
    def get_img(self):
        return self.__img
