#Importa pacotes
import pygame
import random
pygame.init()

#Configurações
largura = 920
altura = 640
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jornada da Princesa')

sapato_largura = 50
sapato_altura = 38
fundo = pygame.image.load('Pasta/Fundo.png').convert()
font = pygame.font.SysFont(None, 48)
sapato = pygame.image.load('Pasta/Sapato.png').convert_alpha()
sapato = pygame.transform.scale(sapato, (sapato_largura, sapato_altura))

#Novos 
class sapatoclasse(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, sapato_largura)
        self.rect.y = random.randint(-100,-sapato_altura)
        self.vx = random.randint(-3,3)
        self.vy = random.randint(2,9)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > altura or self.rect.right  < 0 or self.rect.left > largura:
            self.rect.x=random.randint(0, sapato_largura)
            self.rect.y=random.randint(-100,-sapato_altura)
            self.vx=random.randint(-3,3)
            self.vy=random.randint(2,9)

#GAMETRUE 
game = True

#Dados
clock = pygame.time.Clock()
FPS = 30

sapato1 = sapatoclasse(sapato)
sapato2 = sapatoclasse(sapato)

#Loop
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    #Atualiza jogo
    sapato1.update()
    sapato2.update()
    
    #Saídas
    window.fill((0, 0, 0)) 
    window.blit(fundo, (0,0))
    window.blit(sapato1.image, sapato1.rect)
    window.blit(sapato2.image, sapato2.rect)

    #Atualiza jogo
    pygame.display.update()

#Fim
pygame.quit()