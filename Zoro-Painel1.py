import os
import time

#Cores:
#\033[1;30m Branco
#\033[1;31m Vermelho
#\033[1;32m Verde
#\033[1;33m Amarelo
#\033[1;34m Azul
#\033[1;35m Roxo
#\033[1;36m Ciano
#\033[1;37m Cinza Claro


os.system("clear")
cpf1 = input("Digite o cpf para ser validado:\n")
os.system("clear")

print("""\033[1;33m
~<>~<>~<>~<>~<>~<>~<>~\033[1;37m
1 cpf
2 cpf
3 Cpf
4 Sair\033[1;33m
~<>~<>~<>~<>~<>~<>~<>~
""")
op = input(">>")

if op == "1":
    os.system("clear")
    print("====================")
    print("=   CPF GERADO!!   =")
    print("====================")
    print("Cpf: {}".format(cpf1))
    time.sleep(4)
    print("Validando Cpf...")
    time.sleep(9)
    print("Cpf Validado!!")
    time.sleep(9)
    os.system("clear")
    os.system("python3 Zoro-Painel1.py")
elif op == "2":
    print("""\033[1;36m
    =×=×=×=×=×=×=×=×=×==
    = ERROR      ERROR =
    =×=×=×=×=×=×=×=×=×==
    """)
    time.sleep(4)
    os.system("clear")
    os.system("python3 Zoro-Painel1.py")
elif op == "3":
    cpf2 = input("Digite Mais um Cpf:\n")
    cpf3 = input("Digite mais um cpf:\n")
    os.system("clear")
    print("""
    Vc deseja msm Validar esses três Cpf's?
    [1]Sim
    [2]Não
    """)
    op = input(">>")
    if op == "1":
        print("Ok!!")
        time.sleep(4)
        print("Validando Os 3 Cpf's...")
        time.sleep(4)
        print("Validado {}!".format(cpf1))
        time.sleep(4)
        print("Validado {}!".format(cpf2))
        time.sleep(4)
        print("Validado {}!".format(cpf3))
    elif op == "2":
        print("Ok estamos saindo do Script!!")
        time.sleep(4)
        os.system("clear")
        time.sleep(4)
        exit()
elif op == "4":
    print("\033[1;34m")
    os.system("""
    clear
    figlet Saindo...
    """)
    time.sleep(4)
    exit()
else:
    os.system("python3 Zoro-Painel1.py")
