#considerando toda a comunicacao client-server ja implementada
#considerando a divisao de arquivos ja implementada
#considerando a transferencia de arquivos ja implementada

#recebe as infos do servidor sobre os clientes e seus dados
list_clients = []

#dentro da lista de clientes devem ter os dados sobre os arquivos
#que o cliente possui e a qtd de bytes que aquele cliente possui

if len(list_clients) == 0:
    print 'Nao ha arquivos para serem transferidos'
else:
    print list_clients
    #onde devera mostrar os dados dos clientes online e os arquivos
    #que cada cliente possui com seus tamanhos
