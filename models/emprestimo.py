from datetime import datetime
import json
from models.modelo import Modelo

class Emprestimo:
    def __init__(self, id:int, id_agiota:int, id_cliente:int, id_cobrador:int, solicitado:bool, aprovado:bool, quitado:bool, cobrado:bool, valor:float, duracao:int, data:datetime, juros:float):
        self.__id = id   
        self.__id_agiota = id_agiota
        self.__id_cliente = id_cliente
        self.__id_cobrador = id_cobrador 
        
        self.__solicitado = solicitado
        self.__aprovado = aprovado
        self.__quitado = quitado           
        self.__cobrado = cobrado
        
        self.__valor = valor
        self.__data = data       
        self.__duracao = duracao 
        self.__juros = juros     
        
    def get_id(self):
        return self.__id
    def get_id_agiota(self):
        return self.__id_agiota
    def get_id_cliente(self):
        return self.__id_cliente
    def get_id_cobrador(self):
        return self.__id_cobrador
    def get_solicitado(self):
        return self.__solicitado
    def get_aprovado(self):
        return self.__aprovado
    def get_quitado(self):
        return self.__quitado
    def get_cobrado(self):
        return self.__cobrado
    def get_valor(self): 
        return self.__valor 
    def get_data(self):
        return self.__data
    def get_duracao(self):
        return self.__duracao
    def get_juros(self):
        return self.__juros
    
    def set_id(self, id:int):
        self.__id = id 
    def set_id_agiota(self, id:int):
        self.__id_agiota = id
    def set_id_cliente(self, id:int):
        self.__id_cliente = id
    def set_id_cobrador(self, id:int):
        self.__id_cobrador = id
    def set_solicitado(self, solicitado:bool):
        self.__solicitado = solicitado
    def set_aprovado(self, aprovado: bool):
        self.__aprovado = aprovado
    def set_quitado(self, quitado: bool):
        self.__quitado = quitado
    def set_cobrado(self, cobrado:bool):
        self.__cobrado = cobrado
    def set_valor(self, valor:float): 
        self.__valor = valor 
    def set_data(self, data:datetime):
        self.__data = data
    def set_duracao(self, duracao: int):
        self.__duracao = duracao
    def set_juros(self, juros: float):
        self.__juros = juros

    def __str__(self):
        return f"{self.__id} - {self.__id_agiota} - {self.__id_cliente} - {self.__id_cobrador} - {self.__solicitado} - {self.__aprovado} - {self.__quitado} - {self.__cobrado} - {self.__valor} - {self.__duracao} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__juros}"

class Emprestimos(Modelo):
    @classmethod
    def salvar(cls):    
        with open("../emprestimos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("../emprestimos.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  e = Emprestimo(obj["id"], obj["id_agiota"], obj["id_cliente"], obj["id_cobrador"], obj["solicitado"], obj["aprovado"], obj["quitado"], obj["cobrado"], obj["valor"], obj["duracao"], datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"), obj["juros"])
                  cls.objetos.append(e)
        except FileNotFoundError:
          pass 
