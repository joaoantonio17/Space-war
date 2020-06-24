import pygame, sys
from aliens import criar_aliens
from laser import laser

# Atualiza a tela e todos os seus elementos
def atualiza(janela, janela_fundo, persona, aliens, L, Label):
    janela.blit(janela_fundo, [0, 0]) # Primeiro redesenha a tela
    persona.desenha_persona()
    Label.__Desenha__()
    # Pondo e atualizando os lasers
    try:
        for i in L:
            i.atualiza_laser()
            i.desenha_laser()
            if i.laser.y < 0:
                del L[0]
    except:
        pass
    # Criando a lista de aliens
    criar_aliens(aliens, janela, Label)
    # Detectando colisões
    CA = -1
    CL = -1
    for i in aliens:
        CA += 1
        for b in L:
            CL += 1
            if i.alien_rect.colliderect(b.laser) == 1:
                del aliens[CA]
                del L[CL]
        CL = -1
    # Atualizando aliens
    for i in aliens:
        i.atualiza_alien()
        i.desenha_alien()
    # Atualizando barra da vida
    Label.atualiza()
    # Por último atualiza todos os rectângulos
    pygame.display.update()
    pygame.display.flip()


def cria_lasers(L, janela, nave):
    if len(L) < 4:
        novo_laser = laser(janela, nave)
        L.append(novo_laser)

