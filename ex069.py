tot18 = homenscadastrados = mulheresmenosde20 = 0
print('-' * 20)
print('CADRASTRE UMA PESSOA')
print('-' * 20)
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper() [0]
    if idade >= 18:
        tot18 +=1
    if sexo =='M':
        homenscadastrados +=1
    if sexo == 'F' and idade < 20:
        mulheresmenosde20 +=1
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if opção == 'N':
        break
print('='*6, 'FIM DO PROGRAMA','='*6)
print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {homenscadastrados} homen(s) cadastrado(s).')
print(f'E temos {mulheresmenosde20} mulher(es) com menos de 20 anos.')
