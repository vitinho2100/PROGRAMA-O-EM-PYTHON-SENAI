# pedra papel e tesoura
import random

lista  =  ['Pedra','Papel','Tesoura']
escolha_computador =  random.choice(lista)

escolha_usuario =  input('Digite sua opção')

if escolha_computador == escolha_usuario:
    print('EMPATE')
    print('O computador escolheu', escolha_computador)
elif escolha_computador == 'Papel' and escolha_usuario == 'Pedra':
    print('O COMPUTADOR TE VENCEU, QUEBRE O COMPUTADOR')
    print('O computador escolheu', escolha_computador)
elif escolha_computador == 'Papel' and escolha_usuario == 'Tesoura':
    print('VOCÊ VENCEU A MÁQUINA')
    print('O computador escolheu', escolha_computador)
elif escolha_computador == 'Pedra' and escolha_usuario == 'Tesoura':
    print('O COMPUTADOR TE VENCEU, QUEBRE O COMPUTADOR')
    print('O computador escolheu', escolha_computador)
elif escolha_computador == 'Tesoura' and escolha_usuario == 'Tesoura':
    print('O COMPUTADOR TE VENCEU, QUEBRE O COMPUTADOR')
    print('O computador escolheu', escolha_computador)
        

enter  = input('digite enter para sair!')