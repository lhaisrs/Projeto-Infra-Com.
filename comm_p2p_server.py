#-------------------------------------------------------------------CLIENTE-----------------------------------------------------------#

import socket

# criando um socket para estabelecer a comunicacao com o servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# nome do host e da porta para estabelecer a comunicacao
host = 'localhost'
port = 1271

# variaveis de controle sobre o que ele vai pedir ao servidor
infos = 0
ping = 0

# lista do que ele vai mandar ao servidor e os dados que ele possui
mandar = []
possui = "[F1P1,F2P1]"

# socket se comunicando o servidor
variavel = (host, port)
s.connect( variavel )

# inicio: cliente manda ao servidor os dados que ele possui
data = "/" + host + "/" + str(port) + "/" + possui + "/"
s.send(data)

print "Cliente"

while True:
    infos = 0
    ping = 0

    # dado a ser enviado para o servidor: pedido de informacoes dos outros usuarios ou ping (atualizar informacoes)
    data = raw_input('O que voce quer pedir ao servidor: 1-Infos dos outros / 2-Ping')

    # cliente vai mandar ao servidor: string contendo data + host + porta
    mandarst = data + '/' + host + '/' + str(port) + '/'
    s.send(str(mandarst))
    print mandarst

    if (data == "1"):
        # infos
        infos = 1

        # dado que o servidor manda: informacoes dos outros usuarios (cliente vai receber cada um como uma lista de strings. Tem que percorrer elas pelo indice)
        
        # dado recebido 1 - lista dos hosts dos peers
        data1 = s.recv(1024)
        print "Received data 1: ", data1
        s.send("mande mais")

        # dado recebido 2 - lista das portas dos peers
        data2 = s.recv(1024)
        print "Received data 2: ", data2
        s.send("mande mais 2")

        # dado recebido 3 - lista dos arquivos que os peers tem
        data3 = s.recv(1024)
        print "Received data 3: ", data3
        s.send("mande mais 3")

    elif (data == "2"):
        # ping
        ping = 1

        # para atualizar, cliente vai mandar ao servidor os dados que ele possui
        s.send(possui)
		
    if (data == "quit"):
        # sair da conexao
        break

s.close();
