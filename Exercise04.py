# 4 - Dada uma lista de números, crie uma nova lista apenas com 
# os números maiores que 5.

lista_de_numeros = [numero for numero in range(0, 11)]

numeros_maiores_que_cinco = [
  numero
  for numero in lista_de_numeros
  if numero > 5
]
print('Exercicio 4: ', numeros_maiores_que_cinco)