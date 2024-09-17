class Usuario:
    def __init__(self, id:int, nome:str, celular:str, endereco:str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_celular(celular)
        self.set_endereco(endereco)
    def set_id(self, id:int):
        self.__id = id
    def set_nome(self, nome:str):
        self.__nome = nome
    def set_celular(self, celular:str):
        self.__celular = celular
    def set_endereco(self, endereco:str):
        self.__endereco = endereco
    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_celular(self):
        return self.__celular
    def get_endereco(self):
        return self.__endereco