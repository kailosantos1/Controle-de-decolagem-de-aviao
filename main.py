from collections import deque
import re


aviao = deque()
lista_decolados = deque()
padrao = r"^[A-Z]{3}-\d{4}$"


def cadastrar_aviao():
    decisao = "S"
    while decisao == "S":
        cadastro = input("Qual o número de cadastro do avião: ").upper()
        if re.match(padrao, cadastro):
            aviao.append(cadastro)
            print("Cadastro realizado com sucesso!")
        else:
            print(
                "Formato de cadastro inválido. Por favor, use o formato XXX-0000."
            )
        decisao = input("Deseja cadastrar outro avião? (S/N): ").upper()

def listar_cadastrados():
    if len(aviao) == 0:
        print("Não há aviões cadastrados na fila no momento.")
    else:
        print(f"Aviões cadastrados na fila de espera: ({', '.join(aviao)})")


def decolar_aviao():
    if len(aviao) == 0:
        print("Não há aviões na fila para decolagem.")
        return

    print(f"Aviões aguardando decolagem: ({', '.join(aviao)})")
    decisao = input(f"Deseja decolar o avião {aviao[0]}? (S/N): ").upper()

    while decisao == "S" and len(aviao) > 0:
        decolado = aviao.popleft()
        lista_decolados.append(decolado)
        print(f"O avião {decolado} decolou com sucesso!")

        if len(aviao) > 0:
            print(
                f"Lista de aviões que decolaram: ({', '.join(lista_decolados)})"
            )
            print(f"Aviões aguardando decolagem: ({', '.join(aviao)})")
            decisao = input(
                f"Deseja decolar o avião {aviao[0]}? (S/N): "
            ).upper()
        else:
            print("Não há mais aviões na fila de decolagem!")


def listar_decolados():
    if len(lista_decolados) == 0:
        print("Nenhum avião decolou ainda.")
    else:
        print(
            f"Lista de aviões que já decolaram: ({', '.join(lista_decolados)})"
        )


def retornar_aviao_fila():
    if len(lista_decolados) == 0:
        print("Não há aviões decolados para retornar à fila.")
        return

    print(f"Aviões que já decolaram: ({', '.join(lista_decolados)})")
    codigo = input(
        "Digite o código do avião que precisa retornar à fila: "
    ).upper()

    if codigo in lista_decolados:
        lista_decolados.remove(codigo)
        aviao.append(codigo)
        print(
            f"O avião {codigo} retornou com sucesso para o final da fila de decolagem!"
        )
    else:
        print(
            "Código não encontrado na lista de aviões que já decolaram."
        )

while True:
    print("\n--- SISTEMA DE CONTROLE DE DECOLAGEM ---")
    print("1 - Cadastrar avião")
    print("2 - Listar aviões cadastrados na fila")
    print("3 - Decolar avião")
    print("4 - Listar aviões que já decolaram")
    print("5 - Retornar avião à fila")
    print("6 - Sair")

    menu = input("Escolha a opção desejada: ")

    if menu == "1":
        cadastrar_aviao()
    elif menu == "2":
        listar_cadastrados()
    elif menu == "3":
        decolar_aviao()
    elif menu == "4":
        listar_decolados()
    elif menu == "5":
        retornar_aviao_fila()
    elif menu == "6":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida! Tente novamente.")