class Noticia:

    def __init__(self, id, titulo, conteudo, estado):
        self.__id = id
        self.__titulo = titulo
        self.__conteudo = conteudo
        self.__estado = estado

    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo

    def get_estado(self):
        return self.__estado

