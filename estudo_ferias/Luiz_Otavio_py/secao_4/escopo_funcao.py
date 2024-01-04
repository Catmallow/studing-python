'''
Escopo de funções em Python
Escopo significa local onde aquele código pode atingir
Existe escopo local e global
O escopo global é o local onde todo_ o código é alcançável
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcaçados
'''

x = 1


def escopo():
    x = 10

    def outra_funcao():
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


escopo()