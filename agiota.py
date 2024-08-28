import json 

class Agiota:
    def __init__ (self, id: int, nome: str, celular: int, placa_carro: str, id_arma: str, credito: float):
        self.__id = id                     #número ID do agiota
        self.__nome = nome                 #nome do agiota  
        self.__celular = celular           #número de celular do agiota
        self.__placa_carro = placa_carro   #número da placa do carro do agiota
        self.__id_arma = id_arma           #ID da arma do agiota
        self.__credito = credito           #quanto crédito ele tem disponível para emprestar

    def get_id(self):
        return self.__id 
    def get_nome(self): 
        return self.__nome 
    def get_celular(self):
        return self.__celular
    def get_placa_carro(self):
        return self.__placa_carro 
    def get_id_arma(self):
        return self.__id_arma
    def get_credito(self):
        return self.__credito
    
    def set_id(self, id:int):
        self.__id = id
    def set_nome(self, nome:str): 
        self.__nome = nome 
    def set_celular(self, celular:int):
        self.__celular = celular 
    def set_placa_carro(self, placa_carro:str):
        self.__placa_carro = placa_carro
    def set_id_arma(self, id_arma: str):
        self.__id_arma = id_arma
    def set_credito(self, credito: float):
        self.__credito = credito

    def __str__(self):
        return f" {self.__id} - {self.__nome} - {self.__celular} - {self.__placa_carro} - {self.__arma} - {self.__credito}R$"

class Agiotas:
    agiotas = []
    
    @classmethod
    def inserir(cls, obj):      # create - C
        cls.abrir()             # abre a lista de objetos do arquivo
        id = 0                  # cálculo do id do novo objeto
        for x in cls.agiotas:
            if x.get_id() > id: id = x.get_id()
        id += 1    
        obj.set_id(id)          # novo objeto recebe o id calculado
        cls.agiotas.append(obj) # insere o objeto a lista
        cls.salvar()            # salva o arquivo
    @classmethod
    def listar(cls):            # read - R
        cls.abrir()
        return cls.agiotas  
    @classmethod
    def listar_id(cls, id):           
        cls.abrir() 
        for x in cls.agiotas:   # percorre a lista procurando o objeto com o id informado
            if x.get_id() == id: return x
        return None      
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None:
            x.set_nome(obj.get_nome())
            x.set_celular(obj.get_celular())
            x.set_placa_carro(obj.get_placa_carro())
            x.set_arma(obj.get_arma())
            x.set_credito(obj.get_credito())
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id()) # x é o objeto que já está na lista com o mesmo id do objeto novo
        if x != None: 
            cls.agiotas.remove(x)
            cls.salvar()
    @classmethod
    def salvar(cls):    
        with open("agiotas.json", mode="w") as arquivo:
            json.dump(cls.agiotas, arquivo, default = vars)
    @classmethod
    def abrir(cls):
        cls.agiotas = []
        with open("agiotas.json", mode="r") as arquivo:
            texto_arquivo = json.load(arquivo)
            for obj in texto_arquivo:
                c = Agiota(obj["id"], obj["nome"], obj["celular"], obj["placa_carro"], obj["arma"], obj["credito"])
                cls.agiotas.append(c)
