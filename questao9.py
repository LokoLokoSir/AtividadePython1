numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]
buscar = int(input("Digite um numero para buscar: "))

def ocorrenciaLista(x, obj = []):
    ocorrencias = 0
    for i in obj:
        if x == i:
            ocorrencias += 1
    return ocorrencias

print(ocorrenciaLista(buscar, numeros))