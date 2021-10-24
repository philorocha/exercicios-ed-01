tupla = "x", "Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"

while True:
    mes = int(input("Informe o número do mês: "))

    if mes < 1 or mes > 12:
        print("O valor informado esta incorreto. Tente novamente")
        continue

    print(f"O mês digitado foi: {tupla[mes]}")
    break