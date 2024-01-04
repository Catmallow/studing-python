'''
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem como sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
Argumento posicional
'''


def exponeciacao(x, y):
    # definição || quando falo em definição estou me referindo a parametros
    print(f'{x**2 = }, {y**3 = }')
    x = x ** 2
    y = y ** 2


# quando falo em valores me refiro a argumentos
exponeciacao(x=3, y=5)
n