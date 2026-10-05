A = []

for i in range(1, 4):
    linha = []

    for j in range(1, 5):

        if i > j:
            valor = i + j
        else:
            valor = i - 2 * j

        linha.append(valor)

    A.append(linha)

for linha in A:
    print(linha)