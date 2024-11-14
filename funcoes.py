#from random import randrange


''' Essa parte só é util se fossemos gerar uma chave publica
def mdc(n1, n2): # MDC pelo algoritmo de euclides
    """
    Retorna o maior divisor comum de dois números inteiros por meio do algoritmo de Euclides
    """

    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1


def gerador_chave_publica(phi_n):
    """
    Retorna 'E', o primeiro elemento da chave publica.
    :param totiente: int
    :return int maior divisor comum entre E e o inverso multiplicativo de N
    """

    while True:
        e = randrange(phi_n/2, phi_n)
        if mdc(phi_n, e) == 1: # serve para sabermos se ambos os números são primos entre si
            return e
'''


def cifrar(msg, n, e):
    """
    Fazendo uso da chave publica(n, e), é possivel cifrar a mensagem(msg)
    """

    msg_cifrada = ''

    for letra in msg:
        k = ord(letra) ** e % n # ord retorna o unicode do caractere informado como parametro
        msg_cifrada += chr(k) # chr retorna o caractere equivalente ao resultado de K
    return msg_cifrada


def gerador_chave_privada(phi_n, e):
    """
    Retorna 'D', o primeiro elemento da chave privada. 
    :param inverso_n é o inverso da variavel n
    :param e e uma parte da chave publica
    """

    d = 0

    while d*e % phi_n != 1:
        d += 1
    return d


def decifrar(msg, n, d):
    """
    Fazendo uso da chave privada(n, d), é possivel decifrar a mensagem(msg)
    """

    msg_decifrada = ''

    for letra in msg:
        k = ord(letra) ** d % n
        msg_decifrada += chr(k)

    return msg_decifrada