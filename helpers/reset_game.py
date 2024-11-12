import pygame
import time


def reset_game(main, screen, has_won):
    font = pygame.font.Font(None, 50)
    text_surface = font.render(
        f'Game Over. {"You won!" if has_won else "You lost"}', True, (0, 0, 0), (100, 100, 100))
    screen.blit(text_surface, dest=(75, 200))
    pygame.display.flip()

    time.sleep(2)
    main()
