# 7 - Dada uma lista de nomes, crie uma nova lista apenas com os 
# nomes que começam com a letra "A".

lista_de_nomes = ['Daniel', 'Alice', 'Ana Flavia', 'Igor', 'Ana Julia', 'Antony']

lista_nomes_com_A = [
  nome
  for nome in lista_de_nomes
  if nome[0] == 'A' or nome[0] == 'a'
]

print('Exercicio 7: ', lista_nomes_com_A)