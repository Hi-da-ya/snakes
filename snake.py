import pygame

#Initialize pygame
pygame.init()

# Set game window size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes!!!")

# Set Frames per second, to manage screen updating
clock = pygame.time.Clock()
FPS = 10




#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))     
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()       