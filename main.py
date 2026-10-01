from produto import Produto
from cliente import Cliente
import os

VERDE = "\033[92m"
AZUL = "\033[94m"
CIANO = "\033[96m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
BRANCO = "\033[97m"
RESET = "\033[0m"

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def cabecalho(titulo):
    print(CIANO + "╔══════════════════════════════════════════╗")
    print(f"║{titulo:^42}║")
    print("╚══════════════════════════════════════════╝" + RESET)

listaCliente = []
listaProduto = []

def MenuPrincipal():

    while True:

        limpar()
        cabecalho(" SISTEMA DE GESTÃO ")

        print(f"""
{AZUL}╔══════════════════════════════════════════╗
║              MENU PRINCIPAL              ║
╠══════════════════════════════════════════╣
║  {BRANCO}1{AZUL}  →  Menu de Clientes                  ║
║  {BRANCO}2{AZUL}  →  Menu de Produtos                  ║
║  {VERMELHO}3{AZUL}  →  Finalizar Sistema                 ║
╚══════════════════════════════════════════╝{RESET}
""")

        opcs = input(f"{AMARELO}➜ Inserir opção: {RESET}")

        if opcs == "1":
            MenuClientes()

        elif opcs == "2":
            MenuProdutos()

        elif opcs == "3":
            limpar()
            print(f"{VERDE}✔ Sistema finalizado com sucesso!{RESET}")
            break

        else:
            print(f"{VERMELHO}✘ Opção inválida! Tente novamente.{RESET}")
            input("\nPressione ENTER para continuar...")


def MenuClientes():

    while True:

        limpar()
        cabecalho(" MENU DE CLIENTES ")

        print(f"""
{AZUL}╔══════════════════════════════════════════╗
║              MENU DE CLIENTES            ║
╠══════════════════════════════════════════╣
║  {BRANCO}1{AZUL}  →  Cadastrar Cliente                 ║
║  {BRANCO}2{AZUL}  →  Listar Clientes                   ║
║  {VERMELHO}3{AZUL}  →  Voltar ao Menu Principal          ║
╚══════════════════════════════════════════╝{RESET}
""")

        opc = input(f"{AMARELO}➜ Inserir opção: {RESET}")

        
        if opc == "1":

            limpar()
            cabecalho(" CADASTRO DE CLIENTE ")

            nome = input(f"{CIANO}Nome: {RESET}")
            telefone = input(f"{CIANO}Telefone: {RESET}")
            endereco = input(f"{CIANO}Endereço: {RESET}")

            novocli = Cliente(nome, telefone, endereco)

            listaCliente.append(novocli)

            print(f"\n{VERDE}✔ Cliente cadastrado com sucesso!{RESET}")
            input("\nPressione ENTER para continuar...")

       
        elif opc == "2":

            limpar()
            cabecalho(" CLIENTES CADASTRADOS ")

            if len(listaCliente) == 0:

                print(f"\n{AMARELO}⚠ Nenhum cliente cadastrado.{RESET}")

            else:

                for novocli in listaCliente:
                    novocli.imprimir()

            input("\nPressione ENTER para continuar...")

    
        elif opc == "3":
            break

        else:

            print(f"\n{VERMELHO}✘ Opção inválida!{RESET}")
            input("\nPressione ENTER para continuar...")

def MenuProdutos():

    while True:

        limpar()
        cabecalho(" MENU DE PRODUTOS ")

        print(f"""
{AZUL}╔══════════════════════════════════════════╗
║              MENU DE PRODUTOS            ║
╠══════════════════════════════════════════╣
║  {BRANCO}1{AZUL}  →  Cadastrar Produto                 ║
║  {BRANCO}2{AZUL}  →  Listar Produtos                   ║
║  {VERMELHO}3{AZUL}  →  Voltar ao Menu Principal          ║
╚══════════════════════════════════════════╝{RESET}
""")

        opcs = input(f"{AMARELO}➜ Inserir opção: {RESET}")

       
        if opcs == "1":

            limpar()
            cabecalho(" CADASTRO DE PRODUTO ")

            codigo = input(f"{CIANO}Código: {RESET}")
            descricao = input(f"{CIANO}Descrição: {RESET}")
            categoria = input(f"{CIANO}Categoria: {RESET}")
            preco = input(f"{CIANO}Preço: R$ {RESET}")

            novoPro = Produto(
                codigo,
                descricao,
                categoria,
                preco
            )

            listaProduto.append(novoPro)

            print(f"\n{VERDE}✔ Produto cadastrado com sucesso!{RESET}")
            input("\nPressione ENTER para continuar...")

      
        elif opcs == "2":

            limpar()
            cabecalho(" PRODUTOS CADASTRADOS ")

            if len(listaProduto) == 0:

                print(f"\n{AMARELO}⚠ Nenhum produto cadastrado.{RESET}")

            else:

                for novoPro in listaProduto:
                    novoPro.imprimir()

            input("\nPressione ENTER para continuar...")

      
        elif opcs == "3":
            break

        else:

            print(f"\n{VERMELHO}✘ Opção inválida!{RESET}")
            input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    MenuPrincipal()