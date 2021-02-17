import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket Criado com Sucesso!!!!")

host = 'localhost'
porta = 5433
mensagem = 'olá servidor, firmeza?'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("cliente: " + dados)

finally:
    print("Cliente: Fechando a Conexão")
    s.close()
