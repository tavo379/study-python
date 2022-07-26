def conversor(coin, value):
    pesos = input(f"Ingresa los pesos {coin}: ")
    pesos = float(pesos)
    valor_dolar = value
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print(f"Tienes ${dolares} dolares")


menu = """
Bienvenido al conversor de monedas 💸
1 - COP
2 - ARG
3 - MXN

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor('Colombianos', 4050.448)
elif opcion == 2:
    conversor('Argentinos', 118.35)
elif opcion == 3:
    conversor('Mexicanos', 19.92)
else:
    print("Ingresa una opción valida")
