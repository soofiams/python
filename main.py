from funcoes import *

limpa()

opcao = None

while(opcao != 0):
    opcao = menu()
    animar("Aguarde")
    if (opcao == 1):
        registar_produto()
    elif (opcao == 2):
        listar_produtos()
    elif (opcao == 3):
        editar_produto()
    elif (opcao== 4):
        apagar_produto()
    elif (opcao == 5):
        vender_produto()
    elif (opcao == 6):
        listar_vendas()
    elif (opcao== 0):
         animar("A sair")
         print("Até logo!")
    else:
        print("Opção inválida. Tente de novo.")


print("\n\n")


