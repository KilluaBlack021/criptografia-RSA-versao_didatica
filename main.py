from random import randrange


def mdc(n1, n2): # algoritmo de euclides
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1


def gerador_chave_publica(totiente):
    while True:
        e = randrange(2, totiente)
        if mdc(totiente, e) == 1:
            return e


def cifrar(msg, e, n):
    msg_cifrada = ''
    for letra in msg:
        k = ord(letra) ** e % n
        msg_cifrada += chr(k)
    return msg_cifrada


def gerador_chave_privada(totiente, e):
    d = 0
    while d*e % totiente != 1:
        d += 1
    return d


def decifrar(msg, n, d):
    msg_decifrada = ''

    for letra in msg:
        k = ord(letra) ** d % n
        msg_decifrada += chr(k)

    return msg_decifrada


# main
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
totiente = (p-1) * (q-1) # inverso multiplicativo de N

e = gerador_chave_publica(totiente)
d = gerador_chave_privada(totiente, e)


print(f'Chave publica: {e}, {n}\n\nChave privada: {d, n}\n\n\n')

msg = cifrar(msg, e, n)
print(f'MSG CIFRADA: \n\n{msg}\n\n')
msg = decifrar(msg, n, d)
print(f'MSG DECIFRADA: \n\n{msg}\n\n')
