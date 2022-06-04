import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)
    # set background color
    bg_color = (230, 230, 230)
    #main game loop:
    while True:
        # watch for keyboard mouse events
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # make most recently drawn screen visible
        pygame.display.flip()