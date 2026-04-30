import pygame

# initialize font system
pygame.font.init()

# small font
font_sm = pygame.font.SysFont("Verdana", 20)

# large font
font_lg = pygame.font.SysFont("Verdana", 40)

# draw text function
def draw_text(surface, text, x, y, color=(0, 0, 0), font=font_sm, center=False):
    # create text surface
    txt_surf = font.render(text, True, color)

    # get rectangle
    rect = txt_surf.get_rect()

    # center or top-left position
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    # draw text
    surface.blit(txt_surf, rect)

# BUTTON CLASS
class Button:
    def __init__(self, x, y, w, h, text, color=(200, 200, 200)):
        # button rectangle
        self.rect = pygame.Rect(x, y, w, h)

        # button text
        self.text = text

        # button color
        self.color = color

    # draw button
    def draw(self, surface):
        # draw background
        pygame.draw.rect(surface, self.color, self.rect)

        # draw border
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)

        # draw text in center
        draw_text(surface, self.text, self.rect.centerx, self.rect.centery, center=True)

    # check click
    def is_clicked(self, event):
        # mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            # if mouse inside button
            if self.rect.collidepoint(event.pos):
                return True

        return False