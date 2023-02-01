# Desafio #02

'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado
pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua
preferência ou pode ser previamente definido no código;
'''


# Solução

num = int(input('Digite um número: '))

a, b = 0, 1

fibonacci = [a, b]

while b < num:
    a, b = b, a + b
    fibonacci.append(b)
    print(fibonacci)

print(fibonacci)
if num in fibonacci:
    print('O número informado pertence a sequência de Fibonacci.')
else:
    print('O número informado não pertence a sequência de Fibonacci.')
