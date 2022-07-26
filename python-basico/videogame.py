import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero entre el 1 y el 100 '))
    while numero_aleatorio != numero_elegido:
        if numero_elegido < numero_aleatorio:
            print('Busca un número más grande ')
        else:
            print('Busca un número más pequeño ')
        numero_elegido = int(input('Elige otro número '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()
