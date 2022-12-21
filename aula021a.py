def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    :return: não tem retorno
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2)
somar(b=2, c=9)
somar()
