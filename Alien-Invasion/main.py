import sys
import pygame

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    # set background color
    bg_color = (230, 230, 230)
    #main game loop:
    while True:
        # watch for keyboard mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        # redraw the screen during each pass through the loop
        screen.fill(bg_color)
        # make most recently drawn screen visible
        pygame.display.flip()