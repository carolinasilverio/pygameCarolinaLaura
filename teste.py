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