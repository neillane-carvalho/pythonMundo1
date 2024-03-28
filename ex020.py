import pygame

pygame.init()
pygame.mixer.music.load("ex020.mp4")  # pygame.error: ModPlug_Load failed
pygame.mixer.music.set_volume(2)
pygame.mixer.music.play()
