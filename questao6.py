numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
buscar = int(input("Digite um numero para buscar: "))

def buscarNumero(x: int, obj = []):
    for i in obj:
        if i == x:
            return True
    return False

print(buscarNumero(buscar, numeros))