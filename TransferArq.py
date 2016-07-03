#considerando toda a comunicacao client-server ja implementada
#considerando a divisao de arquivos ja implementada
import sys
import time

list_pacotes = []

#consideracoes dentro do client

receptor = open(arquivo, 'wb')
#arquivo == ao atual arquivo da lista de arquivos

porc = 0.0
sent = 0.0
index = 0

size #receber o retorno da divisao de arquivos
size_read = size/float(100)
int_read = int(size_read)

pacote = arquivo.read(int_read)

while (pacote):
    porc = (sent/size) * 100
    sent = sent + size_read

    #verificar com o grupo se iniciaremos a lista de arquivos por 0 ou 1
    list_pacotes.append(index)
    index = index + 1 

    print '{0:.2f} %r' .format(porc) #status da transferencia de arquivo
    time.sleep(0.2)

    #envia o pacote
    pacote = arquivo.read(int_read)

pacote.close()

print list_pacotes #imprimi a atual lista de pacotes apos transferencia


#consideracoes por parte do servidor
#tenta a conexao com o cliente
#obtem controle sob os clientes conectados na rede
global clients
clients = clients + 1

#faz a conexao e envia os dados para o cliente



