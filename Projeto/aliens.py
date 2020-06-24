import pygame, random
class Alien():
    def __init__(self, janela, Label):
        # Define as barras de vida do personagem
        self.Label = Label
        # Transforma a janela em um rect para usar as coordenadas
        self.janela = janela
        self.janela_rect = self.janela.get_rect()
        # Define a imagem do alien, a posição randomica
        self.alien = pygame.image.load("image/alien_1.png")
        self.alien_rect = self.alien.get_rect()
        X = random.randint(0, 16)
        A = range(50, 900, 50)
        B = range(-425, 0, 25)
        self.alien_rect.x = A[X]
        self.alien_rect.y = B[X]
    def atualiza_alien(self):
        # Regula para que os aliens voltem após passar de y=600, assim podendo ser mortos. E caso sejam mortos, devem ser criados outros
        X = random.randint(0, 16)
        A = range(50, 900, 50)
        B = range(-1700, 0, 100)

        if self.alien_rect.y < 600:
            self.alien_rect.y += 3
        else:
            self.Label.C -= 1
            self.alien_rect.x = A[X]
            self.alien_rect.y = B[X]
    def desenha_alien(self):
        # Desenha os aliens na tela
        self.janela.blit(self.alien, self.alien_rect)


def criar_aliens(Aliens, janela, Label):
    # Controla o número de aliens
    if len(Aliens) < 4:
        novo_alien = Alien(janela, Label)
        novo_alien.desenha_alien()
        Aliens.append(novo_alien)

