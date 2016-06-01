def LerArquivo():

	arq = open('Entrada.txt', 'r')
	nome = []
	tamanho = []
	ja_possui = []


	server_host = arq.readline() # a primeira linha do arquivo eh o server_host
	print server_host
	server_port = arq.readline() # a segunda eh o server_port
	print server_port

	str = arq.readline()   # 
	
	while(str != ''): # la o arquivo enquanto for != da string vazia

		line = str.split() # quebra a linha em palavras, e retorna uma lista de palavras
		if(len(line) == 1 and str != "*" and str != "*\n"): # se a lista tem tamanho 1, e nao eh o delimitador *, entao salva a palavra na lista de arquivos que ja possui
			ja_possui.append(str)

		if(len(line) == 2): # se a lista tem tamanho 2, salva a primeira palavra na lista de nome de arquivos que o cliente quer, e a segunda palavra na lista dos tamanhos desses arquivos
			nome.append(line[0])
			tamanho.append(line[1])

		str = arq.readline() # le a proxima linha

	print "Arquivos que o cliente quer:" 
	print nome 
	print "\n"

	print "Tamanho desses arquivos:" 
	print tamanho 
	print "\n"

	print "Arquivos que o cliente ja possui:" 
	print ja_possui 
	print "\n"

LerArquivo()
