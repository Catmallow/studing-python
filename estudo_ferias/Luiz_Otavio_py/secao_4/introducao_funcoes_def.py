'''
Introdução as funções def em python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código
Elas podem recerber valores para parâmetros (argumentos)
E retornar um valor específico
Por padrão funções python retornam None (nada).
'''

'''
1 - Qual seria a diferença de executar algo dentro do def e fora do def ?
A diferença de executar algo dentro e fora de uma função esta relacionado ao escopo das variáveis 
e ao momento em que o código é executado.
'''


# aprendendo a usar uma função
def imprimir(a, b, c):
    print(a, b, c)


imprimir(1, 2, 3)  # argumentos
imprimir(2, 4, 6)  # argumentos
print(100 * '-')


def saudacao(nome='sem nome'):
    print(f'olá {nome}')


saudacao('gabriel')
saudacao()
