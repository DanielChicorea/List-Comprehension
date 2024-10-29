# 9 - Dada uma lista de números, crie uma nova lista com o dobro de cada 
# número, mas apenas se o número for ímpar

lista = [numero for numero in range(1, 11)]
lista_dobro_impar = [
  numero * 2
  for numero in lista
  if numero % 2 == 1 
]

lista_impar = [
  numero
  for numero in lista
  if numero % 2 == 1
]

print('Exercicio 9: ', lista_impar, 'Lista de Impares')
print('Exercicio 9: ', lista_dobro_impar, 'Lista do dobro dos Impares')