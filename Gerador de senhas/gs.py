import random
import string

tamanho = int(input('Digite o tamanho de senha desejada: '))


chars = string.ascii_letters + string.digits + ',.!@#Ç$%*()-=+'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))