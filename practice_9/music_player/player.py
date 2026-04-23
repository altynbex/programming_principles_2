import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_files = [os.path.join(music_folder, f) for f in os.listdir(music_folder) if f.endswith(('.mp3', '.wav'))]
        self.current_index = 0
        self.playing = False

    def play(self):
        if self.music_files:
            pygame.mixer.music.load(self.music_files[self.current_index])
            pygame.mixer.music.play()
            self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next_track(self):
        if self.music_files:
            self.current_index = (self.current_index + 1) % len(self.music_files)
            self.play()

    def prev_track(self):
        if self.music_files:
            self.current_index = (self.current_index - 1) % len(self.music_files)
            self.play()

    def get_current_track_name(self):
        if self.music_files:
            return os.path.basename(self.music_files[self.current_index])
        return "No tracks found"