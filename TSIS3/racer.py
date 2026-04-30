import pygame, sys
from racer import run_game
from persistence import save_score, load_leaderboard
from ui import Button, draw_text, font_lg

# start pygame
pygame.init()

# screen size
SCREEN_W, SCREEN_H = 400, 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("TSIS 3 Racer")

# game clock
clock = pygame.time.Clock()

# MAIN MENU SCREEN
def menu_screen():
    # create buttons
    btn_play = Button(100, 200, 200, 50, "Play")
    btn_leader = Button(100, 270, 200, 50, "Leaderboard")
    btn_quit = Button(100, 340, 200, 50, "Quit")

    # menu loop
    while True:
        screen.fill((255, 255, 255))

        # title text
        draw_text(screen, "MAIN MENU", SCREEN_W//2, 100, font=font_lg, center=True)

        # draw buttons
        btn_play.draw(screen)
        btn_leader.draw(screen)
        btn_quit.draw(screen)

        # events
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "QUIT"

            # button clicks
            if btn_play.is_clicked(e):
                return "PLAY"
            if btn_leader.is_clicked(e):
                return "LEADERBOARD"
            if btn_quit.is_clicked(e):
                return "QUIT"

        pygame.display.update()
        clock.tick(60)

# GAME OVER SCREEN
def game_over_screen(score, distance):
    # back button
    btn_menu = Button(100, 350, 200, 50, "Main Menu")

    # save score to file
    save_score("Player", score, distance)

    # loop
    while True:
        screen.fill((200, 50, 50))

        # show results
        draw_text(screen, "GAME OVER", SCREEN_W//2, 150, font=font_lg, center=True)
        draw_text(screen, f"Score: {score}", SCREEN_W//2, 220, center=True)
        draw_text(screen, f"Distance: {distance}", SCREEN_W//2, 260, center=True)

        btn_menu.draw(screen)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "QUIT"
            if btn_menu.is_clicked(e):
                return "MENU"

        pygame.display.update()
        clock.tick(60)

# LEADERBOARD SCREEN
def leaderboard_screen():
    btn_back = Button(100, 500, 200, 50, "Back")

    # load data from file
    board = load_leaderboard()

    while True:
        screen.fill((255, 255, 255))

        # title
        draw_text(screen, "TOP 10", SCREEN_W//2, 50, font=font_lg, center=True)

        # show leaderboard list
        y = 120
        for i, entry in enumerate(board):
            draw_text(screen, f"{i+1}. {entry['name']} - {entry['score']}", 50, y)
            y += 30

        btn_back.draw(screen)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "QUIT"
            if btn_back.is_clicked(e):
                return "MENU"

        pygame.display.update()
        clock.tick(60)

# MAIN CONTROLLER
def main():
    state = "MENU"

    # main loop
    while True:
        if state == "MENU":
            state = menu_screen()

        elif state == "PLAY":
            # run game logic
            result, score, distance = run_game(screen, clock)

            if result == "QUIT":
                break

            state = "GAME_OVER"

        elif state == "GAME_OVER":
            state = game_over_screen(score, distance)

        elif state == "LEADERBOARD":
            state = leaderboard_screen()

        elif state == "QUIT":
            break

    pygame.quit()
    sys.exit()

# start program
if __name__ == "__main__":
    main()


# -----------------------------
# RACER MODULE (sprites + game)
# -----------------------------
# A1 English comments for defense

import pygame, random
from persistence import load_settings

# screen size
SCREEN_W, SCREEN_H = 400, 600

# PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self, color_name):
        super().__init__()
        # create player rectangle
        self.image = pygame.Surface((40, 60))

        # choose color
        colors = {"blue": (0, 0, 255), "red": (255, 0, 0), "green": (0, 255, 0)}
        self.image.fill(colors.get(color_name, (0, 0, 255)))

        # start position
        self.rect = self.image.get_rect(center=(160, 520))

        # shield state
        self.shield_active = False

    # move player left/right
    def move(self):
        k = pygame.key.get_pressed()

        # move left
        if k[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)

        # move right
        if k[pygame.K_RIGHT] and self.rect.right < SCREEN_W:
            self.rect.move_ip(5, 0)

# ENEMY CLASS
class Enemy(pygame.sprite.Sprite):
    def __init__(self, existing_sprites):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((200, 0, 0))
        self.rect = self.image.get_rect()
        self.safe_spawn(existing_sprites)

    # spawn without overlap
    def safe_spawn(self, existing_sprites):
        while True:
            self.rect.center = (random.randint(40, 360), random.randint(-200, -50))
            if not pygame.sprite.spritecollideany(self, existing_sprites):
                break

    # move down
    def update(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_H:
            self.kill()

# OBSTACLE CLASS
class Obstacle(pygame.sprite.Sprite):
    def __init__(self, existing_sprites):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill((50, 50, 50))
        self.rect = self.image.get_rect()
        self.safe_spawn(existing_sprites)

    def safe_spawn(self, existing_sprites):
        while True:
            self.rect.center = (random.randint(40, 360), random.randint(-200, -50))
            if not pygame.sprite.spritecollideany(self, existing_sprites):
                break

    def update(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_H:
            self.kill()

# POWER UP CLASS
class PowerUp(pygame.sprite.Sprite):
    def __init__(self, existing_sprites):
        super().__init__()
        self.image = pygame.Surface((25, 25))

        # random power type
        self.type = random.choice(["nitro", "shield", "repair"])

        colors = {
            "nitro": (0, 255, 255),
            "shield": (255, 255, 0),
            "repair": (0, 255, 0)
        }

        self.image.fill(colors[self.type])
        self.rect = self.image.get_rect()
        self.safe_spawn(existing_sprites)

    def safe_spawn(self, existing_sprites):
        while True:
            self.rect.center = (random.randint(40, 360), random.randint(-200, -50))
            if not pygame.sprite.spritecollideany(self, existing_sprites):
                break

    def update(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.top > SCREEN_H:
            self.kill()

# MAIN GAME FUNCTION
def run_game(screen, clock):

    # load settings (difficulty, color)
    settings = load_settings()

    # base speed depends on difficulty
    base_spd = 5 if settings["difficulty"] == "normal" else (3 if settings["difficulty"] == "easy" else 7)

    # create player
    player = Player(settings["color"])

    # sprite groups
    all_sprites = pygame.sprite.Group(player)
    enemies = pygame.sprite.Group()
    obstacles = pygame.sprite.Group()
    powerups = pygame.sprite.Group()

    # game variables
    score, distance, coins = 0, 0, 0
    active_power = None
    power_timer = 0

    running = True

    while running:

        # event check
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                return "QUIT", score, distance

        # spawn difficulty increases over time
        enemy_spawn_chance = max(15, 60 - (distance // 100))
        obs_spawn_chance = max(30, 100 - (distance // 100))

        # spawn enemies
        if random.randint(1, enemy_spawn_chance) == 1:
            enemy = Enemy(all_sprites)
            enemies.add(enemy)
            all_sprites.add(enemy)

        # spawn obstacles
        if random.randint(1, obs_spawn_chance) == 1:
            obs = Obstacle(all_sprites)
            obstacles.add(obs)
            all_sprites.add(obs)

        # spawn powerups
        if random.randint(1, 300) == 1:
            pw = PowerUp(all_sprites)
            powerups.add(pw)
            all_sprites.add(pw)

        # game speed
        current_spd = base_spd + (distance // 1000)

        # nitro power effect
        if active_power == "nitro":
            current_spd += 5
            power_timer -= 1
            if power_timer <= 0:
                active_power = None

        # update player
        player.move()

        # update sprites
        enemies.update(current_spd)
        obstacles.update(current_spd)
        powerups.update(current_spd)

        # update score
        distance += current_spd // 2
        score = (distance // 10) + (coins * 10)

        # power collision
        hit_pw = pygame.sprite.spritecollideany(player, powerups)
        if hit_pw:
            active_power = hit_pw.type

            if active_power == "nitro":
                power_timer = 180
            elif active_power == "shield":
                player.shield_active = True
            elif active_power == "repair":
                for obs in obstacles:
                    obs.kill()

            hit_pw.kill()

        # collision with enemies or obstacles
        hit_hazard = pygame.sprite.spritecollideany(player, enemies) or pygame.sprite.spritecollideany(player, obstacles)

        if hit_hazard:
            if player.shield_active:
                player.shield_active = False
                hit_hazard.kill()
            else:
                return "GAME_OVER", score, distance

        # draw background
        screen.fill((100, 100, 100))

        # draw all sprites
        all_sprites.draw(screen)

        # UI text
        from ui import draw_text
        draw_text(screen, f"Score: {score} | Dist: {distance}", 10, 10, (255, 255, 255))

        if active_power:
            draw_text(screen, f"POWER: {active_power.upper()}", 10, 40, (0, 255, 255))

        if player.shield_active:
            pygame.draw.rect(screen, (255, 255, 0), player.rect, 2)

        draw_text(screen, f"Speed: {current_spd}", 10, 70, (255, 255, 255))

        pygame.display.update()
        clock.tick(60)
