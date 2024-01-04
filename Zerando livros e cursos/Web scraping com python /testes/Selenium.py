class Personagem:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel
        self.vida = 100

    def atacar(self):
        print(f"{self.nome} ataca!")

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        print(f"{self.nome} recebeu {quantidade} de dano. Vida restante: {self.vida}")

class Guerreiro(Personagem):
    def __init__(self, nome, nivel, arma):
        super().__init__(nome, nivel)
        self.arma = arma
        self.forca = nivel * 2

    def usar_arma(self):
        print(f"{self.nome} usa {self.arma} para atacar com força {self.forca}!")

class Mago(Personagem):
    def __init__(self, nome, nivel, magia):
        super().__init__(nome, nivel)
        self.magia = magia
        self.magia_poder = nivel * 3

    def lançar_magia(self):
        print(f"{self.nome} lança a magia {self.magia} com poder {self.magia_poder}!")

# Criando instâncias de personagens
heroi_guerreiro = Guerreiro(nome="Conan", nivel=5, arma="Espada")
heroi_mago = Mago(nome="Gandalf", nivel=8, magia="Bola de Fogo")

# Acessando métodos específicos de cada classe
heroi_guerreiro.atacar()
heroi_mago.lançar_magia()

# Acessando métodos da classe base
heroi_guerreiro.receber_dano(10)
heroi_mago.receber_dano(5)
