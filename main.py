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

p = 53 # primo 1      exemplos de primos: 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103
q = 137 # primo 2                        107 109 113 127 131 137 139 149 151 157 163 167 173 179 181 191 193 197

n = p * q
phi_n = (p-1) * (q-1) # inverso multiplicativo de N

e = 65537 # gerador_chave_publica(phi_n) # motivo 1 pelo qual usei esse número: https://pt.wikipedia.org/wiki/65537; Motivo 2: é um número primo grande o suficiente, mas não perde eficiência na hora dos calculos
d = gerador_chave_privada(phi_n, e)


print(f'Chave publica: {e}, {n}\n\nChave privada: {d, n}\n\n\n')

msg = cifrar(msg, n, e)
print(f'MSG CIFRADA: \n\n{msg}\n\n')

msg = decifrar(msg, n, d)
print(f'MSG DECIFRADA: \n\n{msg}\n\n')
