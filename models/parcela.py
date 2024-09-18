from datetime import datetime
import json
from models.modelo import Modelo

class Parcela:
    def __init__(self, id:int, id_emprestimo:int, data_vencimento:datetime, valor: float, pago:bool):
        self.__id = id
        self.__id_emprestimo = id_emprestimo
        self.__data_vencimento = data_vencimento
        self.__valor = valor
        self.__pago = pago
    def get_id(self):
        return self.__id
    def get_id_emprestimo(self):
        return self.__id_emprestimo
    def get_data_vencimento(self):
        return self.__data_vencimento
    def get_valor(self):
        return self.__valor
    def set_id(self, id: int):
        self.__id = id
    def set_id_emprestimo(self, id: int):
        self.__id_emprestimo = id
    def set_data_vencimento(self, data: datetime):
        self.__data_vencimento = data
    def set_valor(self, valor:float):
        self.__valor = valor
    def __str__(self):
        return f'{self.__id} - {self.__id_emprestimo} - {self.__data_vencimento.strftime('%d/%m/%Y %H:%M')} - {self.__valor}R$ - {self.__pago}'

class Parcelas(Modelo):
    @classmethod
    def salvar(cls):    
        with open("../parcelas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
          with open("../parcelas.json", mode="r") as arquivo:
              texto_arquivo = json.load(arquivo)
              for obj in texto_arquivo:
                  p = Parcela(obj["id"], obj["id_emprestimo"], datetime.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"), obj["valor"], obj["pago"])
                  cls.objetos.append(p)
        except FileNotFoundError:
          pass 