# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

repeatname = 'on'
while repeatname == 'on':
    name = input('Informe um nome: ')
    name = str(name)
    if len(name) < 4:
        print('O nome deve ser maior que 3 caracteres. Tente novamente.')
        repeatname = 'on'
    else:
        repeatname = 'off'

repeatage = 'on'
while repeatage == 'on':
    age = input('Informe a idade: ')
    age = int(age)
    if age < 0 :
        print('A idade deve ser maior que 0. Tente novamente.')
        repeatage = 'on'
    elif age > 150 :
        print('A idade deve ser menor que 150. Tente novamente.')
        repeatage = 'on'
    else:
        repeatage = 'off'

repeatsalary = 'on'
while repeatsalary == 'on':
    salary = input('Informe o salário: ')
    salary = float(salary)
    if salary < 0:
        print('O salário deve ser maior que 0. Tente novamente.')
        repeatsalary = 'on'
    else:
        repeatsalary = 'off'

repeatgender = 'on'
while repeatgender == 'on':
    gender = input('Informe o sexo: ')
    if gender != 'f':
        if gender != 'm':
            print('O sexo deve ser "f" ou "m". Tente novamente.')
            repeatgender = 'on'
        else:
            repeatgender = 'off'
    else:
        repeatgender = 'off'

repeatmarital = 'on'
while repeatmarital == 'on':
    marital = input('Informe o estado civil: ')
    if marital != 's':
        if marital != 'c':
            if marital != 'v':
                if marital != 'd':
                    print('O sexo deve ser "s", "c", "v" ou "d". Tente novamente.')
                    repeatmarital = 'on'
                else:
                    repeatmarital = 'off'
            else:
                repeatmarital = 'off'
        else:
            repeatmarital = 'off'
    else:
        repeatmarital = 'off'

print('Bom trabalho!')