import pygame, sys
class Label_vida():
    def __init__(self, janela):
        self.C = 3 # Número de vidas
        self.janela = janela
        self.janela_rect = self.janela.get_rect()
        self.label_vida = pygame.image.load("image/barravidas3.png")
        self.label_vida_rect = self.label_vida.get_rect()
        self.label_vida_rect.left = self.janela_rect.left
        self.label_vida_rect.top = self.janela_rect.top
    def atualiza(self):
        if self.C == 3:
            pass
        elif self.C == 2:
            self.label_vida = pygame.image.load("image/barravidas2.png")
        elif self.C == 1:
            self.label_vida = pygame.image.load("image/barravidas1.png")
        elif self.C == 0:
            self.label_vida = pygame.image.load("image/barravidas0.png")
        else:
            sys.exit()
    def __Desenha__(self):
        self.janela.blit(self.label_vida, self.label_vida_rect)


