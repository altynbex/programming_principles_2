import pygame, random
from config import W, H, CS, load_settings

class SnakeGame:
    def __init__(self, username, pb):
        self.settings = load_settings()  # load game settings
        self.username = username  # player name
        self.pb = pb  # personal best score
        
        # snake start position (list of body parts)
        self.zmeika = [[15, 10], [14, 10]]
        self.dx, self.dy = 1, 0  # direction of snake (moving right)
        self.ndx, self.ndy = 1, 0  # new direction
        
        self.sc = 0  # score
        self.lvl = 1  # level
        
        self.obstacles = []  # walls / blocks
        self.eda = self.make_eda()  # food
        self.poison = self.make_poison()  # poison
        
        # power-ups (special items)
        self.powerup = None
        self.powerup_spawn_time = 0
        self.active_powerup = None
        self.powerup_end_time = 0
        self.shield_active = False  # shield protection

        self.game_over = False  # game state

    def is_free(self, x, y):
        # check if cell is empty (no snake, no obstacle)
        return [x, y] not in self.zmeika and [x, y] not in self.obstacles

    def make_eda(self):
        # create food in random place
        while True:
            x, y = random.randint(0, W - 1), random.randint(0, H - 1)
            if self.is_free(x, y):
                weight = random.choice([1, 1, 3])  # food value
                timer = 100 if weight == 1 else 50  # food life time
                return [x, y, weight, timer]

    def make_poison(self):
        # create poison (30% chance)
        if random.random() < 0.3:
            while True:
                x, y = random.randint(0, W - 1), random.randint(0, H - 1)
                if self.is_free(x, y) and [x, y] != self.eda[:2]:
                    return [x, y]
        return None

    def make_powerup(self):
        # create power-up item
        while True:
            x, y = random.randint(0, W - 1), random.randint(0, H - 1)
            if self.is_free(x, y) and [x, y] != self.eda[:2] and [x, y] != self.poison:
                type_ = random.choice(["speed", "slow", "shield"])  # type of power
                return [x, y, type_]

    def spawn_obstacles(self):
        # create walls when level is high
        self.obstacles = []
        if self.lvl >= 3:
            for _ in range(self.lvl * 2):
                while True:
                    x, y = random.randint(0, W - 1), random.randint(0, H - 1)
                    if self.is_free(x, y) and [x, y] != self.eda[:2]:
                        self.obstacles.append([x, y])
                        break

    def update(self):
        # game logic update
        if self.game_over: return

        # move snake
        self.dx, self.dy = self.ndx, self.ndy
        nx, ny = self.zmeika[0][0] + self.dx, self.zmeika[0][1] + self.dy

        current_time = pygame.time.get_ticks()

        # check collisions
        hit_wall = nx < 0 or nx >= W or ny < 0 or ny >= H
        hit_self = [nx, ny] in self.zmeika
        hit_obs = [nx, ny] in self.obstacles

        # if hit something
        if hit_wall or hit_self or hit_obs:
            if self.shield_active:
                self.shield_active = False  # shield saves once
                return 
            else:
                self.game_over = True
                return

        self.zmeika.insert(0, [nx, ny])  # move snake head
        ate_something = False

        # food timer decreases
        self.eda[3] -= 1
        if self.eda[3] <= 0:
            self.eda = self.make_eda()

        # eat food
        if nx == self.eda[0] and ny == self.eda[1]:
            self.sc += self.eda[2]
            if self.sc // 4 + 1 > self.lvl:
                self.lvl += 1
                self.spawn_obstacles()
            self.eda = self.make_eda()
            self.poison = self.make_poison()
            ate_something = True

            # spawn power-up (20%)
            if not self.powerup and random.random() < 0.2:
                self.powerup = self.make_powerup()
                self.powerup_spawn_time = current_time

        # eat poison
        elif self.poison and nx == self.poison[0] and ny == self.poison[1]:
            if len(self.zmeika) <= 3:
                self.game_over = True
                return
            self.zmeika.pop()
            self.zmeika.pop()
            self.zmeika.pop()
            self.poison = None
            ate_something = True

        # eat power-up
        elif self.powerup and nx == self.powerup[0] and ny == self.powerup[1]:
            self.active_powerup = self.powerup[2]
            self.powerup_end_time = current_time + 5000  # 5 seconds
            if self.active_powerup == "shield":
                self.shield_active = True
            self.powerup = None
            self.zmeika.pop()
            ate_something = True

        # normal move (no food)
        if not ate_something:
            self.zmeika.pop()

        # remove power-up after 8 seconds
        if self.powerup and current_time - self.powerup_spawn_time > 8000:
            self.powerup = None

        # stop power-up effect after time
        if self.active_powerup in ["speed", "slow"] and current_time > self.powerup_end_time:
            self.active_powerup = None

    def get_speed(self):
        # snake speed depends on level
        base = 8 + (self.lvl * 2)
        if self.active_powerup == "speed": return base + 8
        if self.active_powerup == "slow": return max(4, base - 6)
        return base

    def draw(self, screen):
        # draw game
        screen.fill((0, 0, 0))  # black background
        
        # draw grid
        if self.settings["grid_overlay"]:
            for x in range(0, W * CS, CS):
                pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, H * CS))
            for y in range(0, H * CS, CS):
                pygame.draw.line(screen, (30, 30, 30), (0, y), (W * CS, y))

        # draw food
        eda_color = (255, 0, 0) if self.eda[2] == 1 else (0, 150, 255)
        pygame.draw.rect(screen, eda_color, (self.eda[0] * CS, self.eda[1] * CS, CS, CS))

        # blinking food when time is low
        if self.eda[3] < 20 and self.eda[3] % 2 == 0:
            pygame.draw.rect(screen, (0, 0, 0), (self.eda[0] * CS, self.eda[1] * CS, CS, CS))

        # draw poison
        if self.poison:
            pygame.draw.rect(screen, (139, 0, 0), (self.poison[0] * CS, self.poison[1] * CS, CS, CS))

        # draw power-ups
        if self.powerup:
            colors = {"speed": (0, 255, 255), "slow": (255, 165, 0), "shield": (255, 255, 0)}
            pygame.draw.circle(screen, colors[self.powerup[2]], 
                               (self.powerup[0]*CS + CS//2, self.powerup[1]*CS + CS//2), CS//2)

        # draw obstacles
        for obs in self.obstacles:
            pygame.draw.rect(screen, (100, 100, 100), (obs[0] * CS, obs[1] * CS, CS, CS))

        # draw snake
        for s in self.zmeika:
            col = (255, 255, 0) if self.shield_active else self.settings["snake_color"]
            pygame.draw.rect(screen, col, (s[0] * CS, s[1] * CS, CS, CS))

        # UI text
        font = pygame.font.SysFont("Verdana", 16)
        txt_sc = font.render(f"Score: {self.sc} | PB: {self.pb}", True, (255, 255, 255))
        txt_lvl = font.render(f"Level: {self.lvl}", True, (255, 255, 255))
        screen.blit(txt_sc, (10, 10))
        screen.blit(txt_lvl, ((W * CS) - txt_lvl.get_width() - 10, 10))