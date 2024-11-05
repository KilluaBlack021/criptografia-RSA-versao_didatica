from random import randrange


def mdc(n1, n2): # algoritmo de euclides
    """Retorna o maior divisor comum de dois números por meio do algoritmo de Euclides"""
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1


def inversor_multiplicativo(n1, n2):
    """
    Retorna o inverso multiplicativo do produto dos parametros informados
    :param n1 int
    :param n2 int
    :return int inverso multiplicativo
    """
    return (n1-1) * (n2-1)


def gerador_chave_publica(inverso_n):
    """
    Retorna 'E', o primeiro elemento da chave publica.
    :param totiente: int
    :return int maior divisor comum entre E e o inverso multiplicativo de N
    """
    while True:
        e = randrange(2, inverso_n)
        if mdc(inverso_n, e) == 1:
            return e


def cifrar(msg, n, e):
    """
    Fazendo uso da chave publica(n, e), é possivel cifrar a mensagem(msg)
    """
    msg_cifrada = ''
    for letra in msg:
        k = ord(letra) ** e % n # ord retorna o unicode do caractere informado como parametro
        msg_cifrada += chr(k) # chr retorna o caractere equivalente ao resultado de K
    return msg_cifrada


def gerador_chave_privada(inverso_n, e):
    """
    Retorna 'D', o primeiro elemento da chave privada. 
    :param inverso_n é o inverso da variavel n
    :param e uma parte do """
    d = 0
    while d*e % inverso_n != 1:
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