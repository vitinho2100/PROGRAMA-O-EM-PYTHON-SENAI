idade = int(input('idade' ))
match idade:
    case idade if idade >= 65:
        print('idoso')
    case idade if idade <= 12:
         print('criança')
    case idade if idade > 35 and idade <=64:
         print('adulto')
    case idade if idade > 12 and idade <=17:
        print('adolesente')
    case idade if idade > 17 and idade <= 35:
        print('jovem')
        