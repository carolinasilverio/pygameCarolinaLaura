#Importa pacotes
import pygame
import random

pygame.init()

#Tela 
window = pygame.display.set_mode((600, 480))
pygame.display.set_caption('Jornada da Princesa')

#Configurações
largura = 600
altura = 400
#window = pygame.display.set_mode((largura, altura))
fundo = pygame.image.load('Pasta/Fundo.png').convert()
fundo = pygame.transform.scale(fundo, (600, 480))

#GAMETRUE
game = True

#Assets
sapato_largura = 50
sapato_altura = 38
font = pygame.font.SysFont(None, 48)
sapato = pygame.image.load('Pasta/Sapato.png').convert_alpha()
sapato_small = pygame.transform.scale(sapato,(sapato_largura, sapato_altura))

#Novos 
class sapato(pygame.sprite.Sprite):
    def init(self,img):
        pygame.sprite.Sprite.init(self)
        self.image=img
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0, sapato_largura)
        self.rect.y=random.randint(-100,sapato_altura)
        self.vx=random.randint(-3,3)
        self.vy=random.randint(2,9)

    def update(self):
        self.rect.x+=self.vx
        self.rect.y+=self.vy
        if self.rect.top > altura or self.rect.right  < 0 or self.rect.left > largura:
            self.rect.x=random.randint(0, sapato_largura)
            self.rect.y=random.randint(-100,sapato_altura)
            self.vx=random.randint(-3,3)
            self.vy=random.randint(2,9)
#GAMETRUE 
game = True

#Dados

clock = pygame.time.Clock()
FPS = 100

sapato1 = sapato(sapato)
sapato2 = sapato(sapato)

#Loop
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        #Consequências
        if event.type == pygame.QUIT:
            game = False
    #Atualiza jogo
    sapato1.update()
    sapato2.update()
    
    #Saídas
    window.fill((255, 255, 255))
    window.blit(fundo, (0,0))
    window.blit(sapato1.image, sapato1.rect)
    window.blit(sapato2.image, sapato2.rect)

    #Atualiza jogo
    pygame.display.update()

#Fim
pygame.quit()