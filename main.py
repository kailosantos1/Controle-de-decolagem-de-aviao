import re
from collections import deque

aviao = deque()
lista_decolados = deque()
sem_cadastro = len(aviao)
decisao_cadastro = str(input("Deseja cadastrar um avião? (S/N): ")).upper()
padrao = r"^[A-Z]{3}-\d{4}$" #^ inicio do codigo, [A-Z]{3} 3 letras maiusculas, - traço, \d{4} escolher 4 numeros de 0 a 9, $ fim do codigo


while decisao_cadastro == "S":
    cadastro = str(input("Qual o numero de cadastro do avião: ").upper())
    if re.match(padrao,cadastro):
        aviao.append(cadastro)
        print("Cadastro realizado com sucesso!")
    else:
        print("Formato de cadastro inválido. Por favor, use o formato XXX-0000.")
    decisao_cadastro = str(input("Deseja cadastrar outro avião? (S/N): ")).upper()

if  decisao_cadastro  == "N":
        if len(aviao) == 0:
            print(f"Não há mais aviões cadastrados. Total de aviões cadastrados: {sem_cadastro}")
        else:
            print(f"Avioes aguardando decolagem: ({", ".join(aviao)})")
            decisao_decolagem = str(input(f"Deseja decolar o avião {aviao[0]}? (S/N): ")).upper()
            while decisao_decolagem == "S" and len(aviao) > 0:  
                decolados = aviao.popleft()
                print(f"O avião {decolados} decolou!")
                lista_decolados.append(decolados)

                if len(aviao) > 0:
                    print(f"Lista de aviões que decolaram: ({", ".join(lista_decolados)})")
                    print(f"Avioes aguardando decolagem: ({", ".join(aviao)})")
                    decisao_decolagem = str(input(f"Deseja decolar o avião {aviao[0]}? (S/N): ")).upper()
                else:
                    print(f"Não há mais aviões cadastrados. Total de aviões cadastrados: {sem_cadastro}")
            if len(aviao) > 0 and decisao_decolagem == "N":
                print(f"\nDecolagens encerradas. Aviões que ainda sobraram na fila: ({", ".join(aviao)})")
print(f"Lista de aviões que decolaram: ({", ".join(lista_decolados)})")
