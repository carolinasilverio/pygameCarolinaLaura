#Importa pacotes
import pygame
import random

#Configurações
largura = 600
altura = 400
window = pygame.display.set_mode((largura, altura))
fundo = pygame.image.load('Pasta/Fundo.png').convert()
fundo = pygame.transform.scale(fundo, (600, 480))
pygame.init()

#Tela 
window = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Jornada da Princesa')

#GAMETRUE
game = True

#Assets
sapato_largura = 50
sapato_altura = 38
font = pygame.font.SysFont(None, 48)
sapato = pygame.image.load('Pasta/Sapato.png').convert_alpha()
sapato_small = pygame.transform.scale(sapato,(sapato_largura, sapato_altura))

#Dados
sapatox = random.randint(0, sapato_largura)
sapatoy = random.randint(-100,sapato_altura)
sapato_vx = random.randint(-3,3)
sapato_vy = random.randint(2,9)
clock = pygame.time.Clock()
FPS = 100

#Loop
while game:
    clock.tick(FPS)
    for event in pygame.event,get():
        #Consequências
        if event.type == pygame.QUIT:
            game = False
    #Atualiza jogo
    sapatox += sapato_vx
    sapatoy += sapato_vy
    #Novas
    if sapatoy > altura or sapatox + sapato_largura < 0 or sapatox > largura:
        sapatox = random.randint(0, sapato_largura)
        sapatoy = random.randint(-100,sapato_altura)
        sapato_vx = random.randint(-3,3)
        sapato_vy = random.randint(2,9)
    #Saídas
    window.fill((255, 255, 255))
    window.blit(fundo, (0,0))
    window.blit(sapato_small, (sapatox, sapatoy))
    #Atualiza jogo
    pygame.display.update()

    #Fim
    pygame.quit()