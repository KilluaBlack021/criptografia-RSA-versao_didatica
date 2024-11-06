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
q = 11 # primo 2

n = p * q
phi_n = (p-1) * (q-1) # inverso multiplicativo de N

e = gerador_chave_publica(phi_n) # 181 é um bom valor quando usamos p=17 e q=19
d = gerador_chave_privada(phi_n, e) # 253 é um bom valor


print(f'Chave publica: {e}, {n}\n\nChave privada: {d, n}\n\n\n')

msg = cifrar(msg, n, e)
print(f'MSG CIFRADA: \n\n{msg}\n\n')
msg = decifrar(msg, n, d)
print(f'MSG DECIFRADA: \n\n{msg}\n\n')
