#-------------------------------------------------------------------SERVIDOR-----------------------------------------------------------#

import socket

# criando um socket para estabelecer a comunicacao com o cliente
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# nome do host e da porta para estabelecer a comunicacao
host = ''
port = 1271

# lista dos dados armazenados pelo servidor: host, porta e arquivos que cada cliente possui
lista_host = []
lista_port = []
lista_dados = []

# variaveis de controle sobre a opcao do cliente
infos = 0
ping = 0
dado = [1,2,3,4]

# servidor tenta dar um bind no endereco para estabelecer a comunicacao
try:
	variavel = (host, port)
	s.bind( variavel )
except socket.error as e: #se nao conseguir, da um erro
	print (e)
	exit(0)

# servidor fica ouvindo e esperando que o cliente estabeleca uma comunicacao com ele 
s.listen(1)

# quando o servidor aceitar a comunicacao, cria-se um novo socket para a conexao
conn, addr = s.accept()

# inicio: servidor recebe do cliente os dados iniciais que este possui
datai = conn.recv(1234)

print "Received data i: "
print datai

dataStr = str(datai)

# quebra a linha em palavras, e retorna uma lista de palavras
line = dataStr.split('/') 

# atualiza no seu banco de dados as informacoes do cliente
lista_host.append(line[1])
lista_port.append(line[2])
lista_dados.append(line[3])

# impressao dos dados do servidor como estao no momento
print "host: "
print lista_host
print "porta: "
print lista_port
print "info: "
print lista_dados


print"Servidor"

while True:
    infos = 0
    ping = 0

    # dado recebido da aplicacao: opcao + host + porta
    data = conn.recv(1024)
    print("Received data: ", data)


    if (data[0] == "1"): 
        #infos
        infos = 1

        # dado que o servidor manda: informacoes dos outros usuarios

        # dado enviado 1 - lista dos hosts dos peers
        conn.send(str(lista_host))
        data = conn.recv(1024)

        # dado enviado 2 - lista das portas dos peers
        conn.send(str(lista_port))
        data = conn.recv(1024)

        # dado enviado 3 - lista dos arquivos que os peers tem
        conn.send(str(lista_dados))
        data = conn.recv(1024)

    elif (data[0] == "2"): 
        # ping
        ping = 1

        # divide o dado recebido do cliente em varias strings e coloca numa lista de strings
        linha = data.split('/')

        # pega o host do cliente que fez o ping e procura na lista de hosts pelo seu indice 
        host_ping = linha[1]
        print host_ping

        index = lista_host.index(host_ping)
        print index

        # recebe do cliente a lista de dados que ele possui
        data = conn.recv(1024)
        print data

        # atualiza no seu banco de dados as arquivos que o cliente possui
        lista_dados[index] = data
        print str(lista_dados[index])

    if (data == "quit"):
        # sair
        break

conn.close();
