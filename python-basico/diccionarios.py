def run():
    mi_diccionario = {
        "nombre": "Fredo",
        "edad": 28,
        "sexo": "Masculino"
    }

    print(mi_diccionario)
    print(mi_diccionario['nombre'])
    print(mi_diccionario['edad'])

    for llave in mi_diccionario.keys():
        print(llave)

    for llave in mi_diccionario.values():
        print(llave)

    for llave, valor in mi_diccionario.items():
        print(f"{str(llave)} : {str(valor)}")


if __name__ == '__main__':
    run()
