#Importa pacotes
import pygame
import random

pygame.init()

#Configurações
largura = 920
altura = 640
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jornada da Princesa')

#Assets
sapato_largura = 50
sapato_altura = 38
princesa_altura = 200
princesa_largura = 152
coco_largura = 50
coco_altura = 48
fundo = pygame.image.load('Pasta/Fundo.png').convert()
font = pygame.font.SysFont(None, 48)
sapato = pygame.image.load('Pasta/Sapato.png').convert_alpha()
sapato = pygame.transform.scale(sapato, (sapato_largura, sapato_altura))
princesa = pygame.image.load('Pasta/Princesa.png')
princesa = pygame.transform.scale(princesa, (princesa_largura, princesa_altura))
scorefont = pygame.font.SysFont('impact', 48)
coco=pygame.image.load('Pasta/Cocô.png').convert_alpha()
coco = pygame.transform.scale(coco, (coco_largura, coco_altura))

#Novos 

class princesaclasse(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = largura/2
        self.rect.bottom = altura-10
        self.vx = 0
        #self.vy = random.randint(2,9)

    def update(self):
        self.rect.x += self.vx
        if self.rect.right > largura:
            self.rect.right = largura
        if self.rect.left < 0:
            self.rect.left = 0

class cococlasse(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura-coco_largura)
        self.rect.y = random.randint(-100,-coco_altura)
        self.vx = random.randint(-3,3)
        self.vy = random.randint(2,9)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > altura or self.rect.right  < 0 or self.rect.left > largura:
            self.rect.x=random.randint(0, largura-coco_largura)
            self.rect.y=random.randint(-100,-coco_altura)
            self.vx=random.randint(-3,3)
            self.vy=random.randint(2,9)



class sapatoclasse(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, largura-sapato_largura)
        self.rect.y = random.randint(-100,-sapato_altura)
        self.vx = random.randint(-3,3)
        self.vy = random.randint(2,9)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.top > altura or self.rect.right  < 0 or self.rect.left > largura:
            self.rect.x=random.randint(0, largura-sapato_largura)
            self.rect.y=random.randint(-100,-sapato_altura)
            self.vx=random.randint(-3,3)
            self.vy=random.randint(2,9)

#GAMETRUE 
game = True

#Dados
clock = pygame.time.Clock()
FPS = 30

all_sprites = pygame.sprite.Group()
all_sapatos = pygame.sprite.Group()
all_cocos=pygame.sprite.Group()
player = princesaclasse(princesa)
all_sprites.add(player)


DONE = 0
PLAYING = 1
state = PLAYING

for i in range(8):
    sapatos = sapatoclasse(sapato)
    all_sprites.add(sapatos)
    all_sapatos.add(sapatos)

for i in range(8):
    cocos= cococlasse(coco)
    all_sprites.add(cocos)
    all_cocos.add(cocos)

score = 0

#Loop
while game:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if state == PLAYING:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.vx -= 8
                if event.key == pygame.K_RIGHT:
                    player.vx += 8
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.vx += 8
                if event.key == pygame.K_RIGHT:
                    player.vx -= 8

    all_sprites.update()

    #Colisão

    hits = pygame.sprite.spritecollide(player, all_sapatos, True)
    for hit in hits:
        score += 100

    hits_c = pygame.sprite.spritecollide(player, all_cocos, True)
    for hit_c in hits_c:
        score -= 50

    if score < 0:
        game = False


    #Saídas
    window.fill((0, 0, 0)) 
    window.blit(fundo, (0,0))
    all_sprites.draw(window)

    #Score

    text_surface = scorefont.render('{:08d}'.format(score), True, (255, 0, 132))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (largura/2, 10)
    window.blit(text_surface, text_rect)

    #Atualiza jogo
    pygame.display.update()

#Fim
pygame.quit()