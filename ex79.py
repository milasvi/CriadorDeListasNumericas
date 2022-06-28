lista = list()
while True:
    num = int(input('Digite um valor: '))
    res = str(input('Deseja continuar?'))
    if num not in lista:
        lista.append(num)
    while res.capitalize().split()[0] != 'S' and res.capitalize().split()[0]  != 'N':
        res = str(input('\033[0;31mResposta inválida\033[m'))
    if res.capitalize().split()[0] == 'N':
        break
lista.sort()
print(f'Sua lista é {lista}.')