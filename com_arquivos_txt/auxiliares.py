from sys import exit    # só para interromper o codigo caso necessario


def leia(nome_do_arquivo):
    try: 
        with open(nome_do_arquivo, 'r') as arquivo:
            return arquivo.read()
    except  FileNotFoundError:
        print('\033[31m\n\n\n !!! MENSAGEM NÃO ENCONTRADA !!! \n\n\n\033[m')
        print('\033[33mCrie um arquivo valido, ou informe um existente!\033[m')
        exit(0)



def escreva(nome_do_arquivo, texto):
    with open(nome_do_arquivo, 'a') as arquivo:
        arquivo.write(texto)
        arquivo.close()


