# Ir construindo um jogo de RPG de acordo com o D&D e tendo como base as aulas oline
# Manipulação de clases, funções e Objetos
'''
1° Você tem X pontos para distribuir de acordo com as seguintes atribuições
2° Os personagens evoluem ao atingirem um patamar de pontos
3° Inicialmente pensado para jogar em dois
4° Fazer uma IA de mestre


'''
jogador_1 = input('')
jogador_2 = input('')

class personagem:
    def __int__(self):
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.sabedoria = sabedoria
        self.carisma = carisma
        self.vida = vida
        self.nivel = nivel #retirar

    def atacar(self):
        print(f"{self.nome} ataca!")

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        print(f"{self.nome} recebeu {quantidade} de dano. Vida restante: {self.vida}")

# re avaliar
class elfo(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma
        self.forca = nivel * 2




