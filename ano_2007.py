import os
def boas_vindas_desse_prog_super_legal(nome: "aluno"):
	'''
	boas_vindas_desse_prog_super_legal: deve receber por parâmetro o nome do aluno e imprimir na tela uma
	mensagem de boas vindas que contenha “Aluno(a): <Nome>”.
	'''
	print(f"Bem vindo Aluno(a): {nome}\nÉ um prazer ter você no nosso programa")

def ate_logo_desse_prog_super_legal():
	'''
	ate_logo_desse_prog_super_legal: deve imprimir na tela uma mensagem de despedida que contenha “Nome
	do computador: <nome_os>”. OBS: use a função da biblioteca os: os.name.
	'''
	print(f"Muito obrigado e até logo, Nome do Computador: <{os.name}>")



def limpar_tela_desse_prog_super_legal():
	'''
	limpar_tela_desse_prog_super_legal: faça uma função que limpe a tela utilizando o método os.system. Trate
	diferentes SOs (Windows e Linux)
	'''
	input('Pressione Enter para continuar...')
	os.system('cls' if os.name == 'nt' else 'clear')

def valida_entrada_int(text = ""):
	'''
	valida_entrada_int: deve receber por parâmetro um texto/mensagem de solicitação para ser exibido ao
	usuário. Deve retornar para o usuário um valor numérico. A função de alguma forma deve validar o que o
	usuário digita para que possa ser convertido para inteiro. Enquanto o usuário não digitar um valor inteiro válido,
	ele não pode sair da função
	'''
	while True:
		x = input(text)
		try:
			x = int(x)
		except:
			print("Digite um valor númerico válido")
			x = input(": ")
		else:
			break
	return(x)
	

