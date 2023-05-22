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