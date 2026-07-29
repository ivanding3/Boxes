import pygame

menu_open = False
game_running = True
pygame.display.init()
resolution = (1920,1080)
(screen_width,screen_height) = resolution
screen = pygame.display.set_mode((resolution),pygame.SCALED,vsync=1,)
dt = 0
making_obj = False
events = None
keys_pressed = None