from random import randint
def gera_array(tamanho = 0, valor_ini = 0, valor_final = 0):
	'''
	gera_array: deve receber por parâmetro três valores: tamanho, valores inicial e final, e retornar um array do
	tamanho indicado preenchido de números aleatórios entre valor inicial e final. Utilize list comprehensions para
	gerar o Array.
	'''
	
	lista = [randint(valor_ini,valor_final) for i in range(tamanho)]
	return(lista)

def gera_matrix(linhas = 0, colunas = 0,valor_ini = 0,valor_final = 0):
	'''
	gera_matrix: deve receber por parâmetro o tamanho da matriz, em linhas e colunas. Deve retornar uma
	matriz de números aleatórios. Use a função gera_array para gerar as linhas e adicioná-las à matriz
	'''
	
	matrix = []
	for i in range(linhas):
		for j in range(colunas):
			x = gera_array(colunas,valor_ini,valor_final)
		matrix.append(x)
	return(matrix)

def imprime_matrix(matrix = [[0]]):
	'''
	imprime_matrix: deve receber por parâmetro uma matriz e imprimir na tela linha a linha
	'''
	
	for elementos in matrix:
		for caracteres in elementos:
			print(f"|{caracteres}", end= "| ")
		print()

def conta_geral(frase = " "):
	'''
	conta_geral: deve receber por parâmetro um texto e retornar valores na seguinte ordem a quantidade de:
	vogais, consoantes, numerais, caracteres especiais
	'''
	
	vogais = "aeiou"
	consoantes = "bcdfghjklmnpqrstvwxyz"
	numerais = "1234567890"
	cara_esp = '!@#$%¨&*().,;:^~´`{}[]ºª?°'
	qtd_vogais = 0
	qtd_cons = 0
	qtd_num = 0
	qtd_esp = 0
	for i in frase.lower():
		for v in vogais:
			if i == v:
				qtd_vogais += 1
		for c in consoantes:
			if i == c:
				qtd_cons += 1
		for n in numerais:
			if i == n:
				qtd_num += 1
		for esp in cara_esp:
			if i == esp:
				qtd_esp += 1
	return(qtd_vogais,qtd_cons,qtd_num,qtd_esp)
