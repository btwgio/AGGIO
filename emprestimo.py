class Emprestimo:
    def __init__ (self,  id:int, valor:float, duracao:int, aliquota:float, id_agiota:int, id_cliente:int, quitacao:bool):
        self.__id = id                          #número ID do empréstimo 
        self.__valor = valor                    #valor total do empréstimo, acrescido dos juros
        self.__duracao = duracao                #tempo de duração do empréstimo em meses
        self.__aliquota = aliquota              #alíquota/valor de juros do empréstimo
        self.__id_agiota = id_agiota            #número ID do agiota
        self.__id_cliente = id_cliente          #número ID do cliente
        self.__quitacao = quitacao              #se a pessoa quitou o empréstimo ou não 

    def get_id(self):
        return self.__id 
    def get_valor(self): 
        return self.__valor 
    def get_duracao(self):
        return self.__duracao 
    def get_aliquota(self):
        return self.__aliquota  
    def get_id_agiota(self):
        return self.__id_agiota
    def get_id_cliente(self):
        return self.__id_cliente
    def get_quitacao(self):
        return self.__quitacao 
    
    def set_id(self, id:int):
        self.__id = id 
    def set_valor(self, valor:float): 
        self.__valor = valor 
    def set_duracao(self, duracao:int): #valor em MESES
        self.__duracao = duracao 
    def set_aliquota(self, aliquota:float):
        self.__aliquota = aliquota   
    def set_id_agiota(self, id_agiota:int):
        self.__id_agiota = id_agiota 
    def set_id_cliente(self, id_cliente:int):
        self.__id_cliente = id_cliente 
    def set_quitacao(self, quitacao:bool):
        self.__quitacao = quitacao  

    def __str__(self):
        return f"{self.__id} - {self.__valor} - {self.__duracao} - {self.__aliquota} - {self.__id_agiota} - {self.__id_cliente} - {self.__quitacao}"
