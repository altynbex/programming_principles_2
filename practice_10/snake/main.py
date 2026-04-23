import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Create window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Snake")

# Snake class
class Snake:
    def __init__(self):
        self.size = 20
        self.body = [(300, 200)]  # list of segments
        self.dx = self.size
        self.dy = 0
        self.grow = False  # flag for growth

    def move(self):
        head_x, head_y = self.body[0]

        new_head = (head_x + self.dx, head_y + self.dy)
        self.body.insert(0, new_head)

        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 200, 0), (segment[0], segment[1], self.size, self.size))
    
    def snake_position(self):
        if self.dx > 0 and self.dy == 0: return "right"
        elif self.dx < 0 and self.dy == 0: return "left"
        elif self.dx == 0 and self.dy > 0: return "down"
        elif self.dx == 0 and self.dy < 0: return "up"

    def change_direction(self, dx, dy):
        # prevent reversing
        if (self.dx == -dx and self.dy == -dy):
            return
        self.dx = dx
        self.dy = dy


# Food generation

def generate_food(snake, WIDTH, HEIGHT, size):
    while True:
        x = random.randint(0, (WIDTH // size) - 1) * size
        y = random.randint(0, (HEIGHT // size) - 1) * size

        if (x, y) not in snake.body:
            return (x, y)


# Clock (controls FPS)
clock = pygame.time.Clock()
LEVEL_FPS = {
    1: 20,
    2: 25,
    3: 30
}
snake = Snake()
food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
SCORE = 0

font_big = pygame.font.SysFont(None, 50)
game_over_text = font_big.render("Game Over!", True, (255, 255, 255))

# Levels
LEVEL = 1
LEVEL_COLORS = {
    1: (255, 255, 255),   # white
    2: (255, 215, 0),     # gold
    3: (0, 183, 235)      # light blue
}

# position of element: optional, just to check and adjust manually
# obj_pos = [180, 255]
# Game loop (this makes the program "alive")
running = True
game_over = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction(0, -snake.size)
            elif event.key == pygame.K_DOWN:
                snake.change_direction(0, snake.size)
            elif event.key == pygame.K_LEFT:
                snake.change_direction(-snake.size, 0)
            elif event.key == pygame.K_RIGHT:
                snake.change_direction(snake.size, 0)
            # elif event.key == pygame.K_w:
            #     obj_pos[1] -= 5
            # elif event.key == pygame.K_a:
            #     obj_pos[0] -= 5
            # elif event.key == pygame.K_s:
            #     obj_pos[1] += 5
            # elif event.key == pygame.K_d:
            #     obj_pos[0] += 5
            # print(f"Current object position: {obj_pos}")
    head = snake.body[0]
    head_x, head_y = head[0], head[1]
    if head in snake.body[1:]:
        game_over = True
    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT):
        game_over = True
    if head == food_pos:
        snake.grow = True
        food_pos = generate_food(snake, WIDTH, HEIGHT, snake.size)
        SCORE += 1

    # Fill screen (background)
    if not game_over:
        if SCORE >= 5 and SCORE < 10: LEVEL = 2
        elif SCORE >= 10: LEVEL = 3
        else: LEVEL = 1
        screen.fill(LEVEL_COLORS.get(LEVEL, (255, 255, 255)))
        snake.move()
        snake.draw(screen)
        pygame.draw.rect(screen, (200, 0, 0), (food_pos[0], food_pos[1], snake.size, snake.size))
        font = pygame.font.SysFont("Georgia", 20)
        score_info = font.render(f"Scores: {SCORE}", True, (0, 0, 0))
        level_info = font.render(f"Level: {LEVEL}", True, (0, 0, 0))
        screen.blit(score_info, (5, 0))
        screen.blit(level_info, (5, 25))

    else:
        screen.fill((200, 0, 0))  # red screen = death
        screen.blit(game_over_text, (WIDTH//2 - 120, HEIGHT//2 - 50))
        font = pygame.font.SysFont(None, 50)
        score_display = font.render(f"Score: {SCORE}", True, (255, 255, 255))
        level_display = font.render(f"Level: {LEVEL}", True, (255, 255, 255))
        screen.blit(score_display, (180, 205))
        screen.blit(level_display, (180, 255))

    # Update display
    pygame.display.flip()
    # FPS
    clock.tick(LEVEL_FPS.get(LEVEL, 20))