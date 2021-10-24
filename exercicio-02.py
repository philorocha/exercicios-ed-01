albuns = []

while True:
    album = {}
    album['nome'] = input('Informe o nome do album: ')
    album['artista'] = input('Informe o nome do artista: ')
    album['ano'] = int(input('Informe o ano do album: '))
    albuns.append(album)

    res = input('Deseja adicionar outro album? (S/N): ')
    if res.lower() != 's':
        break

for item in albuns:
    for key, value in item.items():
        print(key, value)

