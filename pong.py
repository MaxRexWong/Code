import pygame
import random

FPS = 60
WIDTH = 600
HEIGHT = 500
SCREEN_COL = (0, 0 ,0)
PLAYER_COL = (255, 255, 255)
PLAYER_SIZE = (10, 80)
BALL_COL = (255, 255, 255)
BALL_SIZE = (15, 15)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong game")
clock = pygame.time.Clock()

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COL)
        self.rect = self.image.get_rect()
        self.rect.left = 30
        self.rect.centery = (HEIGHT/2)
        self.speedy = 6

    def update(self):
         key = pygame.key.get_pressed()
         if key[pygame.K_w]:
             self.rect.y -= self.speedy
         if key[pygame.K_s]:
             self.rect.y += self.speedy
         
         if self.rect.bottom > HEIGHT:
             self.rect.bottom = HEIGHT
         if self.rect.top < 0:
             self.rect.top = 0

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(PLAYER_COL)
        self.rect = self.image.get_rect()
        self.rect.right = WIDTH - 30
        self.rect.centery = (HEIGHT/2)
        self.speedy = 6

    def update(self):
         key = pygame.key.get_pressed()
         if key[pygame.K_UP]:
             self.rect.y -= self.speedy
         if key[pygame.K_DOWN]:
             self.rect.y += self.speedy
         
         if self.rect.bottom > HEIGHT:
             self.rect.bottom = HEIGHT
         if self.rect.top < 0:
             self.rect.top = 0

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BALL_SIZE)
        self.image.fill(BALL_COL)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.rect.x = random.randrange(260, 340)
        self.rect.y = random.randrange(170, 330)
        self.speedx = random.choice(list(range(-4, -1)) + list(range(1, 5)))
        self.speedy = random.choice(list(range(-4, -1)) + list(range(1, 5)))

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speedy = self.speedy * -1
            self.rect.y += self.speedy
        if self.rect.left < 0:
            self.rect.x = random.randrange(260, 340)
            self.rect.y = random.randrange(170, 330)
            self.speedx = random.choice(list(range(-4, -1)) + list(range(1, 5)))
            self.speedy = random.choice(list(range(-4, -1)) + list(range(1, 5)))
        if self.rect.right > WIDTH:
            self.rect.x = random.randrange(260, 340)
            self.rect.y = random.randrange(170, 330)
            self.speedx = random.choice(list(range(-4, -1)) + list(range(1, 5)))
            self.speedy = random.choice(list(range(-4, -1)) + list(range(1, 5)))

    def hit(self, players):
        if self.rect.left == players:
            self.speedx = self.speedx * -1
            self.rect.x += self.speedx


all_sprite = pygame.sprite.Group()
all_sprite.add(Player1(), Player2(), Ball())

players = pygame.sprite.Group()
players.add(Player1(), Player2())

ball = Ball()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    all_sprite.update()
    hit = pygame.sprite.spritecollide(ball, all_sprite, False)
    if hit:
        Ball.hit(ball, players)

    screen.fill(SCREEN_COL)
    all_sprite.draw(screen)
    pygame.display.update()
    
