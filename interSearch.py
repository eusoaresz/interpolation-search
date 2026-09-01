# import csv

# numeros = []

# with open("./datasets/numeros_1M_ordenado.csv", mode="r") as arq:
#   dados_csv = csv.DictReader(arq)
#   for linha in dados_csv:
#     numeros.append(int(linha['numero']))

# # pos = primeira_pos + ((alvo - lista[primeira_pos]) * (ultima_pos - primeira_pos)) // (lista[ultima_pos] - lista[low])

numero = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def interSearch(lista, alvo):
    primeira_pos = 0
    ultima_pos = len(lista) - 1

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

    return -1
executando = interSearch(numero, 70)
print(f"Executando a busca Interpolation Search: {executando}")