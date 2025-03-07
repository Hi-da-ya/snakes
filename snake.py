import pygame
import random
import math

#Initialize pygame
pygame.init()

# Set game window size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes!!!")

# Set Frames per second, to manage screen updating
clock = pygame.time.Clock()
FPS = 10

#Define colours
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (225,0,0)

#Set snake properties
snake_size = 20  

# Starting point- centre of the screen
snake_x = WIDTH // 2  
snake_y = HEIGHT // 2
snake_body = [(snake_x, snake_y)]

#Initial movement- moves to the right
velocity_x = 5
velocity_y = 0

# Set food properties
food_radius = 7
food_x = random.randint(food_radius, WIDTH - food_radius)
food_y = random.randint(food_radius, HEIGHT - food_radius)


#Game clock
game_clock = pygame.time.Clock()

#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and velocity_x == 0:
                velocity_x = -5
                velocity_y = 0
            elif event.key == pygame.K_RIGHT and velocity_x == 0:
                velocity_x = 5
                velocity_y = 0
            elif event.key == pygame.K_DOWN and velocity_y == 0:
                velocity_x = 0
                velocity_y = 5 
            elif event.key == pygame.K_UP and velocity_y == 0:
                velocity_x = 0
                velocity_y = -5            

    # Update snake position  
    snake_x += velocity_x  
    snake_y += velocity_y 
    snake_body.insert(0, (snake_x, snake_y))

    
    # Check if the snake hits the wall and end the game if it does 
    if snake_x < 0 or snake_x + snake_size > WIDTH or snake_y < 0 or snake_y + snake_size > HEIGHT:  
        running = False        
 

    # **Collision Detection (Using Distance Formula)**
    distance = math.sqrt((snake_x - food_x) ** 2 + (snake_y - food_y) ** 2)
    if distance < food_radius + (snake_size / 2):  # If snake "eats" the food
        food_x = random.randint(food_radius, WIDTH - food_radius)
        food_y = random.randint(food_radius, HEIGHT - food_radius)

    else:
        snake_body.pop()    

    # Check for Self-Collision (Game Over if Snake Hits Itself)
    if (snake_x, snake_y) in snake_body[1:]:
        running = False    

    screen.fill(BLACK) 
    
    # Draw Snake (as multiple squares)
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], snake_size, snake_size))

    pygame.draw.circle(screen, RED, (food_x, food_y), food_radius)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()       