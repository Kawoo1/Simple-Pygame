import pygame

pygame.init()

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# Sets the screen length and width as the display size for the "game"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Creates the "Player" (A rectangle) // In a more advanced instance, this will utilize actual player sprites and animations
player = pygame.Rect((300, 250, 50, 50))

# Default status to start up the "game"
run = True

# When run, runs the game screen displayed continuously until exit
while run:
    # Screen background will always be black
    screen.fill((0, 0, 0))

    # A nice hue of blue for the rectangle
    pygame.draw.rect(screen, (44, 58, 212), player)

    key = pygame.key.get_pressed()
    # WASD commands to move the player
    if key[pygame.K_a] and player.left > 0:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] and player.right < SCREEN_WIDTH:
        player.move_ip(1, 0)
    elif key[pygame.K_w] and player.top > 0:
        player.move_ip(0, -1)
    elif key[pygame.K_s] and player.bottom < SCREEN_HEIGHT:
        player.move_ip(0, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Crucial for continuing the game, otherwise, it would be a still frame that does not refresh the page
    pygame.display.update()

pygame.quit()
