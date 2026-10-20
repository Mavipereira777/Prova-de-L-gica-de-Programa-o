from ano_2007 import boas_vindas_desse_prog_super_legal as bemvindo, ate_logo_desse_prog_super_legal as xau, limpar_tela_desse_prog_super_legal as limpar, valida_entrada_int as valida
from niver_3001 import gera_array as ga, gera_matrix as gm, imprime_matrix as imp, conta_geral as cg
import os
'''
Crie também um um menu com as opções abaixo, tratando maiúsculas, minúsculas e opções
inválidas e limpando a tela sempre que possível.
S ou 0 - Sair
T ou 1 - Textos
M ou 2 - Matrizes

Na opção T, solicite ao usuário que digite um texto qualquer. A seguir devem ser impressos na tela este mesmo
texto em letras maiúsculas, minúsculas, formato Título (a primeira letra maiúscula de cada palavra) como também
a quantidade de vogais, consoantes, numéricos e caracteres especiais.
Na opção M solicite ao usuário os seguintes valores: a) valor inicial, b) valor final, c) linhas, d) colunas. Gere uma
matriz com os valores mencionados pelo usuário, e imprima na tela a matriz (linha abaixo de linha), o somatório e
a média.
'''
nome = input("Digite seu nome: ")
while True:
	print("_"*60)
	print(bemvindo(nome))
	print("_"*60)

	print("O que deseja fazer: \nS ou 0 - Sair\nT ou 1 - Textos\nM ou 2 - Matrizes")
	opcao = input(": ")
	match opcao.upper():
		case "S"|"0":
			xau()
			break
		case "T"|"1":
			frase = input("Digite uma frase: ")
			qtd = cg(frase)
			print(f"Maiúsculo - {frase.upper()}\nMinúsculo - {frase.lower()}\nTítulo - {frase.title()}\nQuantidade de vogais - {qtd[0]}\nQuantidade de Consoantes - {qtd[1]}\nQuantidade de Números - {qtd[2]}\n Quantidade de Caracteres Especiais - {qtd[3]}")
		case "M"|"2":
			valor_ini = valida("Digite o valor inicial: ")
			valor_final = valida("Digite o valor final: ")
			linhas = valida("Digite a quantidade de Linhas: ")
			colunas = valida("Digite a quantidade de Colunas: ")
			matriz = gm(linhas,colunas,valor_ini,valor_final)
			imp(matriz)
			somatorio = 0
			qtd_elem = 0
			for elementos in matriz:
				for caracteres in elementos:
					somatorio += caracteres
					qtd_elem += 1
			print(f"A soma de todos os elementos é igual a {somatorio}\nA média é igual a {somatorio/len(matriz)}")
		case _:
			print("Digite algo valido")
	limpar()
			
