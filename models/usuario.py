class Usuario:
    def __init__(self, id:int, nome:str, celular:str, endereco:str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_celular(celular)
        self.set_endereco(endereco)
    def set_id(self, id:int):
        self.id = id
    def set_nome(self, nome:str):
        self.nome = nome
    def set_celular(self, celular:str):
        self.celular = celular
    def set_endereco(self, endereco:str):
        self.endereco = endereco
    def get_id(self):
        return self.id
    def get_nome(self):
        return self.nome
    def get_celular(self):
        return self.celular
    def get_endereco(self):
        return self.endereco