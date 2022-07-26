def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    # divisors = [i for i in range(1, num + 1) if num % i == 1]
    return divisors


# def divisors(num): return [x for x in range(1, num + 1) if num % x == 0]


def run():
    num = int(input("Ingresa un numero: "))
    print(divisors(num))
    print("Terminó programa")


""" def run():
    num = int(input("Ingresa un número: "))
    divisors = lambda num: [i for i in range(1, num + 1) if num % i == 0]
    print(divisors(num))
    print("Terminó mi programa") """


if __name__ == '__main__':
    run()
