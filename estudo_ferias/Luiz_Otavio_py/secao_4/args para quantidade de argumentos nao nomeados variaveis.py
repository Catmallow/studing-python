'''
args - argumentos não nomeados
* _ *args (empacotamento e desempacotamento)
'''

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)


# def soma(*args):
#     total = 0
#     for numero in args:
#         total = total + numero
#         print(numero, total)
#         print(total)
#
#
# soma(1, 2, 3, 4, 5, 6)

def minha_funcao(*args):
    for arg in args:
        print(arg)


minha_funcao(1, 2, 3, 4, 5)
