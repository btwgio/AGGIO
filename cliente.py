class Agiota:
    def __init__ (self, id:int, nome:str, celular:int, endereco:str, parcelas:int):
        self.__id = id              #id do cliente. por ex.: nathan tem o ID 40 e esse nome o identifica no sistema
        self.__nome = nome          #nome do cliente
        self.__celular = celular    #celular do cliente 
        self.__endereco = endereco  #endereco do cliente
        self.__parcelas = parcelas  #quantas parcelas o cliente tem em aberto

    def get_id(self):
        return self.__id 
    def get_nome(self): 
        return self.__nome 
    def get_celular(self):
        return self.__celular
    def get_endereco(self):
        return self.__endereco  
    def get_parcelas(self):
        return self.__parcelas 
    
    def set_id(self, id:int):
        self.__id = id
    def set_nome(self, nome:str): 
        self.__nome = nome 
    def set_celular(self, celular:int):
        self.__celular = celular 
    def set_endereco(self, endereco:str):
        self.__endereco = endereco 
    def set_parcelas(self, parcelas:int):
        self.__parcelas = parcelas

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__celular} - {self.__endereco} - {self.__parcelas}"
