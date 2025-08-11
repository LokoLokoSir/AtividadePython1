natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]

tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def juntarListas(obj1 = [], obj2 = []):
    terceiraLista = []
    for i in obj1:
        terceiraLista.append(i)
    for i in obj2:
        terceiraLista.append(i)
    return terceiraLista
    
print(juntarListas(natureza, tecnologia))