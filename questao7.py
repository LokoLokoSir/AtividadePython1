objetos = [
    {"ID": 1, "Nome": "Mesa"},
    {"ID": 2, "Nome": "Cadeira"},
    {"ID": 3, "Nome": "Pote"},
    {"ID": 4, "Nome": "Garrafa"},
    {"ID": 5, "Nome": "Teclado"}
]

def printarNome(obj = []):
    nomes = []
    for i in obj:
        nomes.append(i["Nome"])
    return nomes
        
print(printarNome(objetos))