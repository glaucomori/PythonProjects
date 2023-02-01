# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

repeat = 'on'
while repeat == 'on':
    usuario = input('Informe um usuário: ')
    senha = input('Informe uma senha: ')
    usuario = str(usuario)
    senha = str(senha)
    if usuario == senha:
        print('A senha não pode ser igual ao usuario. Tente novamente')
        repeat = 'on'
    else:
        print('Senha aceita.')
        repeat = 'off'