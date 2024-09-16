from view import View

class UIa:
    @staticmethod
    def menu():
        print("Clientes")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
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
    @staticmethod
    def cliente_inserir():
        #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        celular = input("Informe o celular: ")
        endereco = input("Informe o endereço: ")
        #saldo = input("Informe o saldo: ")
       
        View.cliente_inserir(nome, celular, endereco)
    @staticmethod
    def cliente_listar():
        for cliente in View.cliente_listar(): 
            print(cliente)
    @staticmethod
    def cliente_atualizar():
        UIa.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        celular = input("Informe o novo celular: ")
        endereco = input("Informe o novo endereco: ")
    
        View.cliente_atualizar(id, nome, celular, endereco)
    @staticmethod
    def cliente_excluir():
        UIa.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        View.cliente_excluir(id)

UIa.main()
