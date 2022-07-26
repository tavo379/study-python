def run():
    try:
        num = int(input("Ingresa un número: "))

        def divisors(num): return [
            i for i in range(1, num + 1) if num % i == 0]
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == "__main__":
    run()
