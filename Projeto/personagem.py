import pygame
class persona():
    def __init__(self, janela):
        """Define onde a nave irá ficar"""
        # Transforma a janela principal em um retângulo, para utilizar suas coordenadas
        self.janela = janela
        self.janela_rect = self.janela.get_rect()
        # Definie a nave  e diz quais são suas coordenadas, além de a transformar em um retângulo
        self.nave = pygame.image.load("image/nave.png")
        self.nave_rect = self.nave.get_rect()
        self.nave_rect.centerx = self.janela_rect.centerx
        self.nave_rect.y = 400
    def desenha_persona(self):
        self.janela.blit(self.nave, self.nave_rect)