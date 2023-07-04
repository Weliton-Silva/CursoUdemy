nome = input('Digite seu nome: ')
if len(nome) <= 1:
    print('Digite mais de uma letra.')
elif len(nome) <= 4:
    print('Seu nome é curto !')
elif len(nome) <= 6:
    print('Seu nome é normal !')
else:
    print('Seu nome é muito grande !')