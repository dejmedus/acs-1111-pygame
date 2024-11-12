import pygame

from helpers.create_objects import create_objects
from helpers.reset_game import reset_game

pygame.init()


def main():
    # Get the clock
    clock = pygame.time.Clock()

    # Configure the screen
    screen = pygame.display.set_mode([500, 500])
    font = pygame.font.Font(pygame.font.get_default_font(), 18)

    # Create a new instance of Surface
    surf = pygame.Surface((150, 150))
    surf.fill((255, 111, 33))

    player, all_sprites, fruit_sprites, bomb = create_objects()

    # Create the game loop
    running = True
    score = 0
    while running:
        # Looks at events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    player.left()
                elif event.key == pygame.K_RIGHT:
                    player.right()
                elif event.key == pygame.K_UP:
                    player.up()
                elif event.key == pygame.K_DOWN:
                    player.down()

        # Clear screen
        screen.fill((255, 255, 255))

        # Move and render Sprites
        for entity in all_sprites:
            if score < 1 and hasattr(entity, 'bomb'):
                continue

            entity.move()
            entity.render(screen)

        text_surface = font.render(
            f'score {score}', True, (0, 0, 0))
        screen.blit(text_surface, dest=(0, 0))

        fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
        if fruit:
            score += 1
            fruit.reset()

            if score == 100:
                reset_game(main, screen, True)

        if pygame.sprite.collide_rect(player, bomb):
            reset_game(main, screen, False)

        # Update the window
        pygame.display.flip()

        # tick the clock!
        clock.tick(25 + score)


main()
