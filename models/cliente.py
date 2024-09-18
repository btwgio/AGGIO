import json 
from models.usuario import Usuario
from models.modelo import Modelo

class Cliente(Usuario):
    def __init__(self, id:int, nome:str, celular:str, endereco:str, saldo:float):
        super().__init__(id, nome, celular, endereco) # ID, nome, número de celular e endereço do cliente
        self.set_saldo(saldo)                         # saldo do cliente   
    def get_saldo(self):
        return self.saldo
    def set_saldo(self, saldo:int):
        self.saldo = saldo

    def __str__(self):
        return f"ID: {super().get_id()} - NOME: {super().get_nome()} - CELULAR: {super().get_celular()} - ENDEREÇO: {super().get_endereco()} - SALDO: {self.get_saldo()}R$"

class Clientes(Modelo):
    @classmethod
    def salvar(cls):    
        with open("./clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("./clientes.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  c = Cliente(obj["id"], obj["nome"], obj["celular"], obj["endereco"], obj["saldo"])
                  cls.objetos.append(c)
        except FileNotFoundError:
          pass 
