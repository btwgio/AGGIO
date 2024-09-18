import json 
from models.usuario import Usuario
from models.modelo import Modelo

class Cobrador(Usuario):
    def __init__(self, id:int, nome:str, celular:str, endereco: str, placa_veiculo:str, id_agiota:int):
        super().__init__(id, nome, celular, endereco)
        self.set_id_agiota(id_agiota)
        self.set_placa_veiculo(placa_veiculo)
    def get_placa_veiculo(self):
        return self.placa_veiculo
    def get_id_agiota(self):
        return self.id_agiota 
    def set_placa_veiculo(self, placa_veiculo:str):
        self.placa_veiculo = placa_veiculo
    def set_id_agiota(self, id_agiota:int):
        self.id_agiota = id_agiota
    def __str__(self):
        return f"ID: {super().get_id()} - NOME: {super().get_nome()} - CELULAR: {super().get_celular()} - ENDERECO: {super().get_endereco()} - PLACA DO VEICULO: {self.placa_veiculo} - ID_AGIOTA: {self.id_agiota}"

class Cobradores(Modelo):
    @classmethod
    def salvar(cls):    
        with open("./cobradores.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("./cobradores.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  c = Cobrador(obj["id"], obj["nome"], obj["celular"], obj["endereco"], obj["placa_veiculo"], obj["id_agiota"])
                  cls.objetos.append(c)
        except FileNotFoundError:
          pass 
