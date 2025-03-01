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

#Define color
BLACK = (0,0,0)
GREEN = (0,255,0)

#Set snake properties
snake_size = 20  
snake_x = WIDTH // 2  
snake_y = HEIGHT // 2

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)  

    # Draw a snake
    pygame.draw.rect(screen, GREEN, (snake_x, snake_y, snake_size, snake_size))
    
       
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()       