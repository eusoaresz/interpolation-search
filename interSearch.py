import csv

numeros = []

with open("./datasets/numeros_1M_ordenado.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    numeros.append(int(linha['numero']))

teste = []

def interSearch(lista, alvo):
    primeira_pos = 0
    ultima_pos = len(lista) - 1

    if lista is None or len(lista) == 0:
        print("A lista está vazia ou nula.")
        return -1
    while primeira_pos <= ultima_pos and alvo >= lista[primeira_pos] and alvo <= lista[ultima_pos]:
        if primeira_pos == ultima_pos:
            if lista[primeira_pos] == alvo:
                return primeira_pos
            return -1

        pos = primeira_pos + ((alvo - lista[primeira_pos]) * (ultima_pos - primeira_pos)) // (lista[ultima_pos] - lista[primeira_pos])
        # 0 + ((70 - 10) * (8 - 0)) // (90 - 10)
        if lista[pos] == alvo:
            return pos
        if lista[pos] < alvo:
            primeira_pos = pos + 1
        else:
            ultima_pos = pos - 1

    if alvo not in lista:
        print(f"O número {alvo} não está presente na lista.")
    return -1
    
executando = interSearch(numeros, 585707)
print(f"Executando a busca Interpolation Search: {executando}")