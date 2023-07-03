entrada = input('Digite um número inteiro: ')   # entrada no formato str
 
try:
    check_int = int(entrada)                    # convertendo de str pra int
    if check_int % 2 == 0:                      # check se é par ou impar
        print(f'O número {entrada} é par')  
    else:
        print(f'O número {entrada} é ímpar')
 
except:                                        # usuario digitou outra coisa
    print('Você não digitou um número inteiro')