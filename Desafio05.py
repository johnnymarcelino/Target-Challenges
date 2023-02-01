# Desafio #05

'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência
ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

# Solução

# Definindo a string
string = input('Informe a string que deseja inverter: ')

# Invertendo a string
invertida = ''
for i in range(len(string)-1, -1, -1):
    invertida += string[i]

# Imprimindo a string invertida
print(f'String invertida: {invertida}')
