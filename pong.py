import pygame, random


FPS = 60
WIDTH, HEIGHT = 600, 500
SCR_COL = (0, 0, 0)
OBJ_COL = (255, 255, 255)
PLAYER_SIZE = (10, 80)
BALL_SIZE = (15, 15)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(OBJ_COL)
        self.rect = self.image.get_rect()
        self.rect.center = (30, HEIGHT/2)
        self.speed = 6

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            self.rect.y -= self.speed
        if key[pygame.K_s]:
            self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(PLAYER_SIZE)
        self.image.fill(OBJ_COL)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - 30, HEIGHT/2)
        self.speed = 6

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            self.rect.y -= self.speed
        if key[pygame.K_DOWN]:
            self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(BALL_SIZE)
        self.image.fill(OBJ_COL)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.speedx = random.choice(list(range(-4,-1)) + list(range(2,5)))
        self.speedy = random.choice(list(range(-4,-1)) + list(range(2,5)))

    def update(self, hit1, hit2):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.speedy = self.speedy * -1
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.rect.center = (WIDTH/2, HEIGHT/2)
            self.speedx = random.choice(list(range(-5,-2)) + list(range(3,6)))
            self.speedy = random.choice(list(range(-5,-2)) + list(range(3,6)))
        if hit1:
            self.rect.x -= self.speedx * 2
            self.speedx = random.randrange(4,9)
        if hit2:
            self.rect.x -= self.speedx * 2
            self.speedx = random.randrange(-8,-3)
    

player1 = pygame.sprite.Group()
player1.add(Player1())
player2 = pygame.sprite.Group()
player2.add(Player2())
ball = pygame.sprite.Group()
ball.add(Ball())

hit = False
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    if pygame.sprite.groupcollide(ball, player1, False, False):
        hit1 = True
    else:
        hit1 = False
    if pygame.sprite.groupcollide(ball, player2, False, False):
        hit2 = True
    else:
        hit2 = False
    
    player1.update()
    player2.update()
    ball.update(hit1, hit2)


    screen.fill(SCR_COL)
    player1.draw(screen)
    player2.draw(screen)
    ball.draw(screen)
    pygame.display.update()
