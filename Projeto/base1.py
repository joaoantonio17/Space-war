# Importações
import pygame, sys
from personagem import persona
from atualiza import *
from labels import *

def jogo():
    """
    Classe -> Jogo

    """
    pygame.init()

    # Definindo tela, titulo e fundo
    Janela = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("A invasão")
    Janela_fundo = pygame.image.load("image/fundo_galaxia.jpg")
    Janela.blit(Janela_fundo, [0, 0])
    # Definindo personagem, conjunto de lasers e aliens
    P1 = persona(Janela)
    L = []
    Aliens = []
    # Barra de vida
    Barra_vida = Label_vida(Janela)
    while True:
        # Sempre que iniciar o laço, deve-se atualiza a tela e a persona:
        Barra_vida.__Desenha__()
        P1.desenha_persona()
        atualiza(Janela, Janela_fundo, P1, Aliens, L, Barra_vida)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    cria_lasers(L, Janela, P1)
        Movimentos = pygame.key.get_pressed()
        if Movimentos[pygame.K_LEFT] and P1.nave_rect.x > 50:
            P1.nave_rect.x -= 15
        if Movimentos[pygame.K_RIGHT] and P1.nave_rect.x <900:
            P1.nave_rect.x += 15
jogo()