import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        pygame.mixer.init()
        self.music_dir = music_dir
        # Сканируем папку и берем только mp3/wav файлы
        self.playlist = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        self.current_track_index = 0
        self.is_playing = False

    def load_track(self):
        if self.playlist:
            track_path = os.path.join(self.music_dir, self.playlist[self.current_track_index])
            pygame.mixer.music.load(track_path)

    def play(self):
        if not self.is_playing:
            if not pygame.mixer.music.get_busy():
                self.load_track()
            pygame.mixer.music.unpause()
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            self.is_playing = True

    def stop(self):
        pygame.mixer.music.pause()
        self.is_playing = False

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.is_playing = False
        self.load_track()
        self.play()

    def prev_track(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.is_playing = False
        self.load_track()
        self.play()

    def get_current_track_name(self):
        if self.playlist:
            return self.playlist[self.current_track_index]
        return "No tracks found"