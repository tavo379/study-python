numeros = [2, 4, 5, 'perros', True]

print(numeros)
print(numeros[3])

numeros.append('gatos')

print(numeros)

numeros.pop(0)

print(numeros)

for element in numeros:
  print(element)

numeros = numeros[::-1]

print(numeros)

numeros = numeros[0:2]

print(numeros)