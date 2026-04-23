#Imports
import pygame, sys
from pygame.locals import *
import random, time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COIN_SCORE = 0
COIN_SPEED = 5

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def earn_point(self):
        if (self.rect.bottom <= 600):
            global COIN_SCORE
            COIN_SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)



#Setting up Sprites        
P1 = Player()
E1 = Enemy()
COIN = Coin()
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(COIN)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)


# coin score position, need to be adjusted manually by pressing
# coin_score_coordinate = [40, 325]
#Game Loop
while True:
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         coin_score_coordinate[0] -= 20               
        #     elif event.key == pygame.K_d:
        #         coin_score_coordinate[0] += 20
        #     elif event.key == pygame.K_w:
        #         coin_score_coordinate[1] -= 20
        #     elif event.key == pygame.K_s:
        #         coin_score_coordinate[1] += 20
        #     print(f"coin score coordinate: {coin_score_coordinate}")
    
    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    score_text = font_small.render("Scores", True, BLACK)
    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    coin_text = font_small.render("Coins", True, BLACK)
    DISPLAYSURF.blit(scores, (10,25))
    DISPLAYSURF.blit(score_text, (5, 0))
    DISPLAYSURF.blit(coin_scores, (360, 25))
    DISPLAYSURF.blit(coin_text, (345, 0))
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # If player touched a coin, a point earns        
    if pygame.sprite.spritecollideany(P1, coins):
        COIN.earn_point()
        try:
            pygame.mixer.Sound('coin_take.mp3').play()
        except FileNotFoundError:
            print("[Error]: File 'coin_take.mp3' isn't found. Didn't you delete it?")

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)     
        final_score_text = font.render(f"Scores: {SCORE}", True, BLACK)
        final_coin_score = font.render(f"Coins: {COIN_SCORE}", True, BLACK)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,200))
        DISPLAYSURF.blit(final_score_text, (60, 285))
        DISPLAYSURF.blit(final_coin_score, (60, 365))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
        
    pygame.display.update()
    FramePerSec.tick(FPS)