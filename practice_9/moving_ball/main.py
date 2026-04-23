import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((400, 300))

# Список треков (заполни своими названиями из папки music/)
playlist = ["music/track1.mp3", "music/track2.mp3"]
current_track = 0

def play_music():
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Play
                play_music()
            if event.key == pygame.K_s: # Stop
                pygame.mixer.music.stop()
            if event.key == pygame.K_n: # Next
                current_track = (current_track + 1) % len(playlist)
                play_music()
            if event.key == pygame.K_b: # Back
                current_track = (current_track - 1) % len(playlist)
                play_music()

    screen.fill((50, 50, 50))
    pygame.display.flip()

pygame.quit()