# 5 - Crie uma lista com as letras maiúsculas de uma string.

strings_variadas = ['caMINHAO', 'forTAO']

string_maiuscula = [
  letra
  for string in strings_variadas
  for letra in string
  if letra == letra.upper()
]

print('Exercicio 5: ', string_maiuscula)