import random
import string

tamanho = int(input('Quantidade de caracteres: ')) 
# quantidade de caracteres da senha

chars = string.ascii_letters + string.digits + '!@#$%&*-=++.,;:/?'
# definição dos caracteres que podem compor a senha

rnd = random.SystemRandom()

print()
print(''.join(rnd.choice(chars) for i in range(tamanho)))
print()