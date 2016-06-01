def StatusCliente():
	print "StatusCliente"
def Sair():
	print "Sair"

def Menu():

	print "1. Status do Cliente"
	print "2. Sair"
	print "Escolha um:"
	Bla()
	while True:
		opt = raw_input()	
		if(opt == "1"):
			StatusCliente()
			break
		elif(opt == "2"):
			Sair()
			break
		else:
			print "Digite uma opcao valida!!!"


Menu()
