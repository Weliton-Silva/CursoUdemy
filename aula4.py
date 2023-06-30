print('--'*20)
nome = str(input('Qual seu nome ? '))
idade = int(input('Qual a sua idade ? '))

if nome != ' ' and idade != ' ' :
    print(f'Seu nome é {nome}.')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print(f'Seu nome possui espaço.')
    else:
        print(f'Seu nome não possui espaço.')
    print(f'Seu nome possui {len(nome)} letras.')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpa você deixou os campos vazios.')
