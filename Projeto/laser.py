import pygame
class laser():
    def __init__(self, janela, nave):
        self.janela = janela
        self.janela_rect = self.janela.get_rect()
        self.nave_rect = nave.nave_rect
        self.laser = pygame.Rect(0, 0, 3, 5)
        self.laser.centerx = self.nave_rect.centerx
        self.laser.y = self.nave_rect.top
    def desenha_laser(self):
        pygame.draw.rect(self.janela, (250, 0, 0), self.laser)
    def atualiza_laser(self):
            self.laser.y -= 10
