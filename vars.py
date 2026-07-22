import pygame

menu_open = False
game_running = True
screen_width = 1600
screen_height = 900
resolution = (screen_width,screen_height)
screen = pygame.display.set_mode((resolution),pygame.SCALED,vsync=1,)
dt = 0
making_obj = False
events = None
keys_pressed = None