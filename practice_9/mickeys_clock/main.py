import pygame
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

# Загрузи свои картинки тут
# bg = pygame.image.load("images/main-clock.png")
# hand = pygame.image.load("images/mickey_hand.png")

def blit_rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)
    surf.blit(rotated_image, new_rect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.datetime.now()
    # Углы: 1 секунда = 6 градусов. Вычитаем из 90, чтобы 0 был вверху
    # Или просто используем - (секунды * 6)
    sec_angle = -(now.second * 6)
    min_angle = -(now.minute * 6)

    screen.fill((255, 255, 255))
    # Тут отрисовывай фон и стрелки
    # blit_rotate_center(screen, hand, (400, 400), sec_angle)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()