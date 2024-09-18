from view import View

class UI:
    @staticmethod
    def menu():
        print("Olá! Tudo bem? Quem é você no sistema?")
        print("1-Cliente\n2-Agiota\n3-Cobrador\n4-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 4:
            op = UI.menu()
            print("==============================================================================")
            if op == 1: # Cliente
                op1 = 0 
                while op1 != 6:
                    op1 = UI.cliente_menu()
                    if op1 == 1: # Criar conta cliente
                        UI.cliente_inserir()
                        print("==============================================================================")
                    if op1 == 2: # Editar uma conta cliente
                        UI.cliente_atualizar()
                        print("==============================================================================")
                    if op1 == 3: # Solicitar empréstimo
                        print('Em desenvolvimento!')
                    if op1 == 4: # Ver minhas parcelas
                        print('Em desenvolvimento!')
                    if op1 == 5: # Pagar parcela
                        print('Em desenvolvimento!')
                    if op1 == 6: # Voltar
                        print("==============================================================================")
                        break
                    if op1 == 7: # Sair
                        print("==============================================================================")
                        op = 4
                        break
                    else: print("Opção inválida")
                    
            if op == 2:  # Agiota
                op1 = 0 
                while op1 != 12:
                    op1 = UI.agiota_menu()
                    if op1 == 1: # Criar conta agiota
                        UI.agiota_inserir()
                        print("==============================================================================")
                    if op1 == 2: # Editar uma conta agiota
                        UI.agiota_atualizar()
                        print("==============================================================================")
                    if op1 == 3: # Atualizar cliente
                        print('Em desenvolvimento!')
                    if op1 == 4: # Atualizar cobrador
                        print('Em desenvolvimento!')
                    if op1 == 5: # Listar agiotas
                        UI.agiota_listar()
                        print("==============================================================================")
                    if op1 == 6: # Listar clientes
                        UI.cliente_listar()
                        print("==============================================================================")
                    if op1 == 7: # Listar cobradores
                        UI.cobrador_listar()
                        print("==============================================================================")
                    if op1 == 8: # Ver empréstimos
                        print('Em desenvolvimento!')
                    if op1 == 9: # Ver parcelas
                        print('Em desenvolvimento!')
                    if op1 == 10: # Aceitar empréstimo
                        print('Em desenvolvimento!')
                    if op1 == 11: # Voltar
                        print("==============================================================================")
                        break
                    if op1 == 12: # Sair
                        op = 4
                        break
                    else: print("Opção inválida")
            if op == 3: #Cobrador
                op1 = 0 
                while op1 != 12:
                    op1 = UI.cobrador_menu()
                    if op1 == 1: # Criar conta cobrador
                        UI.cobrador_inserir()
                        print("==============================================================================")
                    if op1 == 2: # Editar uma conta cobrador
                        UI.cobrador_atualizar()
                        print("==============================================================================")
                    if op1 == 3: # Ver parcelas não pagas
                        print('Em desenvolvimento!')
                    if op1 == 4: # Cobrar parcelas
                        print('Em desenvolvimento!')
                    if op1 == 5: # Voltar
                        print("==============================================================================")
                        break
                    if op1 == 6: # Sair
                        op = 4
                        break
            if op == 4: # Fim
                print("Obrigado por usar AGGIO!")
                break
            else: print("Opção inválida")
    
    def cliente_menu():
        print("Seja bem-vindo senhor(a) cliente, o que deseja?")
        print("1-Criar uma conta\n2-Editar minha conta\n3-Solicitar empréstimo\n4-Ver minhas parcelas\n5-Pagar parcela\n6-Voltar\n7-Sair")
        return int(input("Escolha uma opção: "))
    
    def agiota_menu():
        print("Seja bem-vindo senhor(a) agiota, o que deseja?")
        print("1-Criar uma conta\n2-Atualizar agiotas\n3-Atualizar clientes\n4-Atualizar cobradores\n5-Ver agiotas\n6-Ver clientes\n7-Ver cobradores\n8-Ver empréstimos\n9-Ver parcelas\n10-Aceitar empréstimo\n11-Voltar\n12-Sair")
        return int(input("Escolha uma opção: "))
    
    def cobrador_menu():
        print("Seja bem-vindo senhor(a) cobrador(a), o que deseja?")
        print("1-Criar uma conta\n2-Editar minha conta\n3-Ver parcelas não pagas\n4-Cobrar parcela\n5-Voltar\n6-Sair")
        return int(input("Escolha uma opção: "))
    
    def cliente_inserir():
        nome = input("Informe o nome do cliente: ")
        celular = input("Informe o celular do cliente: ")
        endereco = input("Informe o endereço do cliente: ")
        saldo = float(input("Informe o saldo do cliente: "))
        View.cliente_inserir(nome, celular, endereco, saldo)
        
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome do cliente: ")
        celular = input("Informe o novo celular do cliente: ")
        endereco = input("Informe o novo endereco do cliente: ")
        saldo = float(input("Informe o novo saldo do cliente: "))
        View.cliente_atualizar(id, nome, celular, endereco, saldo)
    
    def cliente_listar():
        for cliente in View.cliente_listar(): 
            print(cliente)
        
    def agiota_inserir():
        nome = input("Informe o nome do agiota: ")
        celular = input("Informe o celular do agiota: ")
        endereco = input("Informe o endereço do agiota: ")
        credito = float(input("Informe o crédito do agiota: "))
        View.agiota_inserir(nome, celular, endereco, credito)
        
    def agiota_atualizar():
        UI.agiota_listar()
        id = int(input("Informe o id do agiota a ser atualizado: "))
        nome = input("Informe o novo nome do agiota: ")
        celular = input("Informe o novo celular do agiota: ")
        endereco = input("Informe o novo endereco do agiota: ")
        credito = float(input("Informe o novo credito do agiota: "))
        View.agiota_atualizar(id, nome, celular, endereco, credito)
        
    def agiota_listar():
        for agiota in View.agiota_listar(): 
            print(agiota)
    
    def cobrador_inserir():
        nome = input("Informe o nome do cobrador: ")
        celular = input("Informe o celular do cobrador: ")
        endereco = input("Informe o endereço do cobrador: ")
        placa = input("Informe a placa do veículo do cobrador: ")
        UI.agiota_listar()
        id_agiota = int(input("Informe o ID de para qual agiota o cobrador trabalha: "))
        View.cobrador_inserir(nome, celular, endereco, placa, id_agiota)
        
    def cobrador_atualizar():
        UI.cobrador_listar()
        id = int(input("Informe o id do cobrador a ser atualizado: "))
        nome = input("Informe o novo nome do cobrador: ")
        celular = input("Informe o novo celular do cobrador: ")
        endereco = input("Informe o novo endereco do cobrador: ")
        placa = input("Informe a nova placa do veículo do cobrador: ")
        UI.agiota_listar()
        id_agiota = int(input("Informe o ID de para qual agiota o cobrador trabalha agora: "))
        View.cobrador_atualizar(id, nome, celular, endereco, placa, id_agiota)
        
    def cobrador_listar():
        for cobrador in View.cobrador_listar(): 
            print(cobrador)
        
    
UI.main()