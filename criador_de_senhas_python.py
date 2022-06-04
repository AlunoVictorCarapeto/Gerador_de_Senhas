import random

'''
Universidade São Judas Tadeu (USJT)
Nome: Victor Licnerski Carapeto
R.A: 819144457
Desafio final do curso de extensão #acampamento_python
'''
# Entrada
print("---------------------------")
print("GERADOR DE SENHAS EM PYTHON")
print("---------------------------")
qtd_letras = int(input("digite o número de letras que você deseja ter em sua senha:\n"))
qtd_nuns = int(input("digite o número de números que você deseja ter em sua senha:\n"))
qtd_char = int(input("digite o número de caracteres especiais que você deseja ter em sua senha:\n"))
opcao = int(input('''Selecione as seguintes opções:
Digite 1 para uma ordem sequencial (Letras + Números + Caracteres)
Digite 2 para uma ordem aleatoria\n'''))
print("-------------------------------------------------------------------------")

# Tratamento
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
          'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

senha = []

#utilizando .append() para inserir os valores na lista e random.choice() para para escolher os valores de forma aleatória
for a in range(qtd_letras):
    senha.append(random.choice(letras)) 

for a in range(qtd_nuns):
    senha.append(random.choice(numeros))

for a in range(qtd_char):
    senha.append(random.choice(simbolos))

# Saída
#utilizando random.shuffle() para embaralhar a senha 
#utilizando .join() para transformar uma lista em string
if(opcao == 1):
    print("Sua senha é:","".join(senha))
elif(opcao == 2):
    random.shuffle(senha)
    print("Sua senha é:","".join(senha))
elif(opcao < 1 or opcao > 2):
    print("Digite uma opção valida")
print("-------------------------------------------------------------------------")