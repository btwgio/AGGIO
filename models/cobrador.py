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
        return f"{super().get_id()} - {super().get_nome()} - {super().get_celular()} - {super().get_endereco()} - {self.placa_veiculo} - {self.id_agiota}"

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
