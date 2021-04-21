import pygame

def voice_large():
    #
    explosion_large = pygame.mixer.Sound("musics/Explo_Large.wav")
    explosion_large.play()

def voice_small():
    # 
    explosion_small = pygame.mixer.Sound("musics/Explo_Small.wav")
    explosion_small.play()

def bullet_biu():
    # 
    bullet_biu = pygame.mixer.Sound("musics/Bullet_biu.wav")
    bullet_biu.play()

def load_bg_music():
    # background music
    pygame.mixer.music.load("musics/order_music.mp3")