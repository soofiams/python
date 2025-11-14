import os
import time
import globais 

# Funções
def menu():
    animar("Aguarde")
    print("\n==== Loja Python ====")
    print("1. Registar Produto")
    print("2. Listar Produtos")
    print("3. Editar Produto")
    print("4. Apagar Produto \n")
    print("5. Vender Produto")
    print("6. Listar Vendas \n")
    print("0. Sair")
    return int(input("Opção: "))

def registar_produto():
    nome = input("Nome do produto: ")
    preco = float(input("Preço: €"))
    quantidade = int(input("Quantidade em stock: "))
    novo_id = 1
    if globais.produtos:
        novo_id = globais.produtos[-1]["id"] + 1

    novo_produto = {
        "id": novo_id,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    globais.produtos.append(novo_produto)
    print(f"\nProduto '{nome}' registado com sucesso!")
    input("\nPressiona Enter para continuar...")

def listar_produtos():
    limpa()
    print("\n--- Lista de Produtos ---")
    for p in globais.produtos:
        print(f"#{p['id']} - (Nome:{p['nome']}) (Preço:{p['preco']}€ ) (Quantidade: {p['quantidade']}) ")
    input("\nPressiona Enter para continuar...")

def editar_produto():
    listar_produtos()
    id_prod = int(input("ID do produto a editar: "))
    for p in globais.produtos:
        if p["id"] == id_prod:
            print(f"\nProduto selecionado: {p['nome']} | €{p['preco']} | Stock: {p['quantidade']}")
            print("O que deseja editar?")
            print("1. Nome")
            print("2. Preço")
            print("3. Quantidade em stock")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                novo_nome = input(f"Digite o nome para substituir({p['nome']}):")
                p["nome"] = novo_nome
                print("Nome atualizado com sucesso.")

            elif opcao == "2":
                novo_preco = float(input(f"Digite o preço que quer substituir({p['preco']}€)"))
                p["preco"] = novo_preco
                print("Preço atualizado com sucesso.")

            elif opcao == "3":
                nova_quantidade = int(input(f"Digite a nova quantidade para ({p['quantidade']})"))
                p["quantidade"] = nova_quantidade
                print("Quantidade atualizada com sucesso.")

            else:
                print("Opção inválida.")

            input("Prima Enter para continuar...")
            return

    print("Produto não encontrado.")
    input("Prima Enter para continuar...")


def apagar_produto():
    listar_produtos()
    id_prod = int(input("ID do produto a apagar: "))
    for p in globais.produtos:
        if p["id"] == id_prod:
            globais.produtos.remove(p)
            print("Produto apagado com sucesso!")
            input("\nPressiona Enter para continuar...")
            return
    print("Produto não encontrado.")
    input("\nPressiona Enter para continuar...")

def vender_produto():
    listar_produtos()
    id_prod = int(input("ID do produto a vender: "))
    for p in globais.produtos:
        if p["id"] == id_prod:
            quantidade = int(input("Quantidade a vender: "))
            if quantidade <= p["quantidade"]:
                p["quantidade"] -= quantidade
                venda = {
                    "produto": p["nome"],
                    "quantidade": quantidade,
                    "valor_total": quantidade * p["preco"],
                }
                globais.vendas.append(venda)
                print(f"Venda realizada: {quantidade}x {p['nome']} por €{venda['valor_total']:.2f}")
            else:
                print("Stock insuficiente.")
            input("\nPressiona Enter para continuar...")
            return
    print("Produto não encontrado.")
    input("\nPressiona Enter para continuar...")

def listar_vendas():
    limpa()
    print("\n--- Histórico de Vendas ---")
    total = 0
    for v in globais.vendas:
        print(f" {v['produto']} x{v['quantidade']} - €{v['valor_total']:.2f}")
        total += v["valor_total"]
    print(f"\nTotal de vendas: €{total:.2f}")
    input("\nPressiona Enter para continuar...")



# Funções Especiais
def limpa():
  if(os.name == "nt"): os.system("cls")
  else: os.system("clear")

def aguarde(segundos): time.sleep(segundos)

def prima_enter(): input("\nPrima <ENTER> para continuar...")

def animar(frase):
  tempo = 0.2
  limpa()
  print(frase, end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  print(".", end="", flush=True)
  aguarde(tempo)
  limpa()