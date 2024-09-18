import json 
from models.usuario import Usuario
from models.modelo import Modelo

class Agiota(Usuario):
    def __init__(self, id: int, nome: str, celular: str, endereco: str, credito: float):
        super().__init__(id, nome, celular, endereco) # ID, nome, número de celular e endereço do agiota
        self.set_credito(credito)                     # quanto crédito ele tem disponível para emprestar
    def get_credito(self):
        return self.credito
    def set_credito(self, credito: float):
        self.credito = credito
    def __str__(self):
        return f"ID: {super().get_id()} - NOME: {super().get_nome()} - CELULAR: {super().get_celular()} - ENDEREÇO: {super().get_endereco()} - CRÉDITO: {self.credito}R$"

class Agiotas(Modelo):
    @classmethod
    def salvar(cls):    
        with open("./agiotas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("./agiotas.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  a = Agiota(obj["id"], obj["nome"], obj["celular"], obj["endereco"], obj["credito"])
                  cls.objetos.append(a)
        except FileNotFoundError:
          pass 
