from random import randrange
from com_arquivos_txt.auxiliares import escreva, leia


def mdc(n1, n2):
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


def gerador_chave_privada(totiente, e):
    d = 0
    while d*e % totiente != 1:
        d += 1
    return d


def cifrar(msg, e, n):
    msg_cifrada = ''
    for letra in msg:
        k = ord(letra) ** e % n
        msg_cifrada += chr(k)
    escreva('mensagem_criptografada.txt', msg_cifrada)
    return msg_cifrada


def decifrar(msg, n, d):
    msg_decifrada = ''
    for letra in msg:
        k = ord(letra) ** d % n
        msg_decifrada += chr(k)
    return msg_decifrada


# main
msg = leia(input('Arquivo.txt da mensagem: '))
p = 17
q = 19
n = p * q
totiente = (p-1) * (q-1)
e = gerador_chave_publica(totiente)
d = gerador_chave_privada(totiente, e)


#print(f'chave publica: {e}, {n}\n chave privada: {d, n}')

msg = cifrar(msg, e, n)
#print(f'msg cifrada: {msg}\n')
msg = decifrar(msg, n, d)
#print(f'msg decifrada: {msg}\n')
