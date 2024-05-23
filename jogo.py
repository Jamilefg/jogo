import random

class Personagem:
    def __init__(self, nome, pontos_de_vida, nivel):
        self.nome = nome
        self.pontos_de_vida = pontos_de_vida
        self.nivel = nivel

    def atacar(self, alvo, nivel_ataque):
        dano = random.randint(nivel_ataque * 5, nivel_ataque * 10)
        alvo.pontos_de_vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano.")

class Heroi(Personagem):
    def __init__(self, nome, pontos_de_vida, nivel):
        super().__init__(nome, pontos_de_vida, nivel)

    def ataque_normal(self, alvo):
        self.atacar(alvo, 1)

    def ataque_especial(self, alvo):
        self.atacar(alvo, 2)

class Inimigo(Personagem):
    def __init__(self, nome, pontos_de_vida, nivel, tipo):
        super().__init__(nome, pontos_de_vida, nivel)
        self.tipo = tipo

def main():
    heroi = Heroi("Herói", 100, 1)
    inimigo = Inimigo("Inimigo", 80, 1, "Normal")

    print("Batalha começou!")
    while heroi.pontos_de_vida > 0 and inimigo.pontos_de_vida > 0:
        print("\nTurno do Herói")
        print("Escolha sua ação:")
        print("1. Ataque Normal")
        print("2. Ataque Especial")
        escolha = input("Escolha o número da ação: ")

        if escolha == "1":
            heroi.ataque_normal(inimigo)
        elif escolha == "2":
            heroi.ataque_especial(inimigo)
        else:
            print("Opção inválida. Tente novamente.")
            continue

        if inimigo.pontos_de_vida <= 0:
            print("Inimigo derrotado!")
            break

        print("\nTurno do Inimigo")
        inimigo.atacar(heroi, 1)

        if heroi.pontos_de_vida <= 0:
            print("Herói derrotado!")
            break

        print(f"\nPontos de vida do Herói: {heroi.pontos_de_vida}")
        print(f"Pontos de vida do Inimigo: {inimigo.pontos_de_vida}")

if __name__ == "__main__":
    main()
