# 8 - Dada uma lista de frutas, crie uma nova lista com o comprimento 
# de cada fruta, apenas para as frutas com mais de 5 letras.

lista_frutas = ['Abacaxi', 'Morango', 'Uva', 'Maça', 'Pitaia']

lista_frutas_comprimento = [
  f'{fruta} | Comprimento: {len(fruta)}'
  for fruta in lista_frutas
  if len(fruta) > 5
]

print('Exercicio 8: ', lista_frutas_comprimento)