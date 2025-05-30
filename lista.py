import random

numero_da_sorte = random.randint(1,3)
meu_numero = int(input('Digite seu número da sorte: '))

if numero_da_sorte == meu_numero:
    print('VOCÊ SORTUDO(A), ACERTOU EM CHEIO * . *', 'O Nº É',numero_da_sorte )
    
else:
    print('VOCÊ ERROU FEIO, NÃO SABE ESCOLHER : p O Nº É', numero_da_sorte)
