# 6 - Dada uma lista de números, crie uma nova lista contendo 
# apenas os números pares e maiores que 10.

lista_numeros = [3, 10, 34, 37, 8, 1, 12, 13, 40, 56]

lista_pares_maiores = [
  numero
  for numero in lista_numeros
  if numero % 2 == 0 and numero > 10
]

print('Exercicio 6: ', lista_pares_maiores)