import os #importar a biblioteca OS, integra os programas e recursos
#do sistema operacional

print("#" *  60)

ip_ou_host = input("Digite o IP ou Host a ser verificado: ")

print("-" *  60)

os.system('ping -n 6 {}'.format(ip_ou_host))

print("-" *  60)

