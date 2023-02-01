#Desafio - 04

'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada
estado teve dentro do valor total mensal da distribuidora.
'''

# Solução

#Definindo o valor total mensal da distribuidora
total_mensal = sum([67836.43, 36678.66, 29229.88, 27165.48, 19849.53])

#Calculando o percentual de representação dos estados
porc_sp = (67836.43/total_mensal)*100
porc_rj = (36678.66/total_mensal)*100
porc_mg = (29229.88/total_mensal)*100
porc_es = (27165.48/total_mensal)*100
porc_outros = (19849.53/total_mensal)*100

#Imprimindo os resultados
print(f'SP: {porc_sp:.2f}%')
print(f'RJ: {porc_rj:.2f}%')
print(f'MG: {porc_mg:.2f}%')
print(f'ES: {porc_es:.2f}%')
print(f'Outros: {porc_outros:.2f}%')
