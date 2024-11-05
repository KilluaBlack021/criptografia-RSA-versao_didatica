from funcoes import *

msg = '''
Say your prayers, little one
Don't forget, my son
To include everyone
I tuck you in, warm within
Keep you free from sin
'Til the sandman, he comes

Sleep with one eye open
Gripping your pillow tight

Exit light
Enter night
Take my hand
We're off to never-never land
'''

p = 17 # primo 1
q = 19 # primo 2

n = p * q
inverso_n = inversor_multiplicativo(p, q) # inverso multiplicativo de N

e = gerador_chave_publica(inverso_n)
d = gerador_chave_privada(inverso_n, e)


print(f'Chave publica: {e}, {n}\n\nChave privada: {d, n}\n\n\n')

msg = cifrar(msg, e, n)
print(f'MSG CIFRADA: \n\n{msg}\n\n')
msg = decifrar(msg, n, d)
print(f'MSG DECIFRADA: \n\n{msg}\n\n')
