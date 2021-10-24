lista_lazer = []

while True:
    lazer_pessoa1 = input("Pessoa 1, o que você gosta de fazer no seu tempo livre?")
    lista_lazer.append(lazer_pessoa1)
    lazer_pessoa2 = input("Pessoa 2, o que você gosta de fazer no seu tempo livre?")
    lista_lazer.append(lazer_pessoa2)

    res = input("Deseja adicionar mais opções de lazer? (S/N)")

    if res.lower() != "s":
        break

for lazer in lista_lazer:
    if lista_lazer.count(lazer) > 1:
        print(f"O lazer em comum é {lazer}")

print("Lista de lazer pessoa 1:")
for lazer_pessoa1 in lista_lazer[0::2]:
    print(lazer_pessoa1)

print("Lista de lazer pessoa 2:")
for lazer_pessoa2 in lista_lazer[1::2]:
    print(lazer_pessoa2)

print("Lista de lazer da pessoa 1 e pessoa 2:")
for lazer in lista_lazer:
    print(lazer)