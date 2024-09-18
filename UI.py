from view import View

class UIa:
    @staticmethod
    def menu():
        print("Olá! Tudo bem? Insira a opção mais adequada para ação que deseja realizar.")
        print("1-Inserir empréstimo\n2-Listar empréstimos\n3-Atualizar\n4-Excluir empréstimo\n9-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UIa.menu()
            if op == 1: UIa.cliente_inserir()
            if op == 2: UIa.cliente_listar()
            if op == 3: UIa.cliente_atualizar()
            if op == 4: UIa.cliente_excluir()
            if op == 9: UIa.cliente_fim()
            #inserir exceção de ERRO
    @staticmethod
    def cliente_inserir():
        nome = input("Informe o nome: ")
        celular = input("Informe o celular: ")
        endereco = input("Informe o endereço: ")
        View.cliente_inserir(nome, celular, endereco)
    @staticmethod
    def cliente_listar():
        for cliente in View.cliente_listar(): 
            print(cliente)
    @staticmethod
    def cliente_atualizar():
        UIa.cliente_listar()
        #id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        celular = input("Informe o novo celular: ")
        endereco = input("Informe o novo endereco: ")
        View.cliente_atualizar(id, nome, celular, endereco)
    @staticmethod
    def cliente_excluir():
        UIa.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)  
    #COBRADOR
    @staticmethod
    def cobrador_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        celular = input("Informe o celular: ")
        endereco = input("Informe o endereço: ")
        placa = input("Informe o número da placa do veículo: ")
        View.inserir_cobrador(nome, celular, endereco, placa)  
    @staticmethod
    def cobrador_listar():
        for cobrador in View.listar_cobrador():
            print(cobrador)

    @staticmethod
    def cobrador_atualizar():
        UIa.cobrador_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        celular = (input("informe o novo Celular: "))
        endereco = (input("informe o novo endereço: "))
        placa = (input("informe o novo  número da placa do veículo: "))

        View.atualizar_Cobrador(id, nome, celular, endereco, placa)

    @staticmethod
    def cobrador_excluir():
        UIa.cobrador_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.excluir_cobrador(id)

    #AGIOTA
    @staticmethod
    def agiota_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        celular = input("Informe o celular: ")
        endereco = input("Informe o endereço: ")
        credito = input("Informe o credito: ")
        View.inserir_agiota(nome, celular, endereco, credito)
    
    @staticmethod
    def agiota_listar():
        for agiota in View.listar_agiota():
            print(agiota)

    @staticmethod
    def agiota_atualizar():
        UIa.agiota_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        celular = (input("informe o novo Celular: "))
        endereco = (input("informe o novo endereço: "))
        credito = (input("informe o novo valor de crédito: "))

        View.atualizar_agiota(id, nome, celular, endereco, credito)

    @staticmethod
    def agiota_excluir():
        UIa.agiota_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.excluir_agiota(id)
   

UIa.main()
