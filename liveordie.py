# -*- coding: utf-8 -*-
# SCRIPT CRIADO POR SAMUEL RODRIGUES DA SILVA
# O SCRIPT TEM COMO FUNCAO VERIFICAR AS MAQUINAS ATIVAS NA REDE!
# LINUX IS FREE!
# LINUX IS OPEN SOURCE
# THE FUTURE IS NOW ! ;)

vermelho = '\033[31m'
branco = '\033[37m'
verde = '\033[32m'
amarelo = '\033[33m'
def banner():
    print("               _     _____     _______           ____ ___ _____ ")
    print("              | |   |_ _\ \   / / ____|___  _ __|  _ \_ _| ____|")
    print("              | |    | | \ \ / /|  _| / _ \| '__| | | | ||  _| ")
    print("              | |___ | |  \ V / | |__| (_) | |  | |_| | || |___")
    print("              |_____|___|  \_/  |_____\___/|_|  |____/___|_____|")
    print("                         By Samuel Rodrigues da Silva")
try:
    try:
        import os
        os.system("clear")
        import subprocess
        import sys
        import time
        import platform
        banner()
        print("\nMódulos importados com sucesso!" + verde + " [OK]" + branco)
        if platform.python_version() < "3.4.2":
            print("Sua versão do python é antiga! Baixe a mais atual!" + vermelho + " [ERRO]" + branco)
            exit()
        else:
            print("Versão do python aceita com sucesso!" + verde + " [OK]" + branco)
        time.sleep(2)
        os.system("clear")
        banner()
        try:
            ip = sys.argv[1]
        except IndexError:
            print(vermelho + "\n                        -=  [ MODO DE USO ERRADO! ]  =-" + branco)
            print(verde + "\nModo de uso:" + branco + " python3 liveordie.py (começo do IP)")
            print(verde + "Ex.: " + branco + "~# python3 liveordie.py 192.168.0.")
            print(amarelo + "\nOBS: Não se esqueça do ponto final no IP!" + branco)
            exit()
        print("\nComeço de IP selecionado: " + verde + ip + branco)
        print("Por padrão testamos as 254 maquinas! ")
        print("\nIniciado:\n")
        with open(os.devnull, "wb") as limbo:
                for n in range(2,254):
                        new_ip=("%s{0}"%ip).format(n)
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", new_ip],
                                stdout=limbo, stderr=limbo).wait()
                        if result:
                                print (new_ip + vermelho + " [DIE] " + branco)
                        else:
                                print (new_ip + verde + " [LIVE] " + branco)
                print(verde + "\nFinalizado ;)" + branco + "\nBy Samuel Rodrigues.")
                exit()
    except ImportError:
        print("Não foi possivel importar os módulos!" + vermelho + " [ERRO]" + branco)
        exit()
except KeyboardInterrupt:
    print("\nByye, script feito por Samuel Rodrigues.")
# FIM DO SCRIPT ;)
# FINALIZADO: TERÇA, 04/07/17, AS 17:59 ;)
