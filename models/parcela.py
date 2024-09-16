from datetime import datetime
class Parcela:
    def __init__(self, id:int, data_vencimento:datetime, valor: float):
        self.__id = id
        self.__data_vencimento = data_vencimento
        self.__valor = valor
        #self.__pago = pago
        #self.__id_emprestimo = id_emprestimo
    
    def set_id(self, id: int):
        self.__id = id
    def set_data_vencimento(self, data: str):
        self.__data_vencimento = data
    def set_valor(self, valor):
        self.__valor = valor
    
    def get_id(self):
        return self.__id
    def get_data_vencimento(self):
        return self.__data_vencimento
    def get_valor(self):
        return self.__valor
    def __str__(self):
        return f'{self.__id} - {self.__set_data_vencimento} - {self.__valor}R$'
