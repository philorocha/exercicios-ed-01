#Faça um programa que preencha uma lista contendo um número indefinido de nome de
#carros e seus consumos (quantos km cada carro faz com 1 litro de combustível). Calcule e
#mostre:
#a. O modelo de carro mais econômico
#b. O modelo de carro menos econômico
#c. Quantos litros de combustível cada um dos carros cadastrados consome para
#percorrer uma distância de 1000 km

carros = []

while True:
    nome = input("Informe o nome do carro: ")
    carros.append(nome)
    consumo = float(input("Infome o consumo (km/l) do carro: "))
    carros.append(consumo)

    res = input("Deseja cadastrar outro carro? (S/N)")
    if res.lower() != "s":
        break


print(f"O modelo mais econômico é: {carros[carros.index(max(carros[1::2])) - 1]}")
print(f"O modelo menos econômico é: {carros[carros.index(min(carros[1::2])) - 1]}")

for index, carro in enumerate(carros):
    if index % 2 == 0:
        print(f"O carro {carros[index]} consumirá {1000 / carros[index+1]:.2f} litros num percurso de 1000km")