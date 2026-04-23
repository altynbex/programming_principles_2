import pygame
import datetime

class MickeyClock:
    def __init__(self, screen):
        self.screen = screen
        self.center = (400, 400) # Центр экрана
        # Загрузка изображений
        self.main_clock = pygame.image.load("mickeys_clock/images/main-clock.png")
        self.right_hand = pygame.image.load("mickeys_clock/images/right-hand.png") # Минуты
        self.left_hand = pygame.image.load("mickeys_clock/images/left-hand.png")   # Секунды

    def rotate_center(self, image, angle):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center=image.get_rect(center=self.center).center)
        return rotated_image, new_rect

    def draw(self):
        self.screen.blit(self.main_clock, (0, 0))
        
        now = datetime.datetime.now()
        
        # Расчет углов (вычитаем из 90, так как 0 градусов в pygame - это 3 часа дня)
        sec_angle = -now.second * 6
        min_angle = -now.minute * 6
        
        # Отрисовка стрелок
        # Секундная (левая рука)
        img_sec, rect_sec = self.rotate_center(self.left_hand, sec_angle)
        self.screen.blit(img_sec, rect_sec)
        
        # Минутная (правая рука)
        img_min, rect_min = self.rotate_center(self.right_hand, min_angle)
        self.screen.blit(img_min, rect_min)