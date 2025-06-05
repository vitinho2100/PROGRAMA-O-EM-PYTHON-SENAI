# 1
def comparar():
    n1 =  int(input('Digite um número> '))
    n2 =  int(input('Digite um número> '))

    if n1 % 2 == 0 and n2 % 2 == 0:
        print('Ambos sã pares')
    elif n1 % 2 == 0 or n2 % 2 == 0:
        print('Um deles é par')
    else:
        print('Ambos impares')
# 2
def mult():
    print(3*4*5)
    
    
#3
def elevado():
  n  = 10
  n2 = int(input('valor elevado'))
  print(n**n2)
  
# 4
def verificar_idade():
    idade =  int(input('idade: '))
    if idade == 18:
        print('18  anos')
    else:
        print('Não tem 18')


# verificar_idade()



# 5
def mostrar_ano():
    ano_atual = 2025
    ano_nascimento = int(input('Ano nascimento:'))
    mes =  int(input('digite o numero do mês 1'))
    cal  =  2025 - ano_nascimento

    if mes <=6:
        print('Ano nascimento', cal)
    else:

         print('Ano nascimento', cal - 1)

#mostrar_ano()

def verificar():
    copas = [1958,1962,1970,1994,2002]

    ano =  int(input('Digite o ano que vc acha que o br granhou'))
    if ano in copas:
        print('ganhou!')
    else:
        print('Não ganhou!')

#verificar()

def restaurante():
    lista =  ['Macarronada', 'Salada', 'Sanbuiche', 'Sorvete']
    print(lista)
    escolha  =  int(input('Digite o id do produto: '))
    print('Escolha: ',  lista[escolha])

while True:
      restaurante()