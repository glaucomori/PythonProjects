# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?"
#     O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

question1 = input('Telefonou para a vítima? (S/N) >> ')
question2 = input('Esteve no local do crime? (S/N) >> ')
question3 = input('Mora perto da vítima? (S/N) >> ')
question4 = input('Devia para a vítima? (S/N) >> ')
question5 = input('Já trabalhou com a vítima? (S/N) >> ')
point = 0
if question1 == 'S':
    point += 1
if question2 == 'S':
    point += 1
if question3 == 'S':
    point += 1
if question4 == 'S':
    point += 1
if question5 == 'S':
    point += 1

if point == 2:
    classification = 'Suspeita'
elif point == 3 or point == 4:
    classification = 'Cúmplice'
elif point == 5:
    classification = 'Assassino'
else:
    classification = 'Inocente'

print(classification)