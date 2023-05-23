import pygame
import random
from os import path

FPS = 35

def init_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    comeco = pygame.image.load(path.join('Pasta/Começo.png')).convert()
    comeco_rect = comeco.get_rect()
    nome = pygame.font.SysFont('impact', 48)
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = False
                running = False

            if event.type == pygame.KEYUP:
                state = True
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.blit(comeco, comeco_rect)
        text_surface = nome.render(format('Jornada da Princesa'), True, (255, 0, 132))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (460, 560)
        screen.blit(text_surface, text_rect)
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state