import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self): 
        self.body = [Vector2(5, 10), Vector2(6, 10), Vector2(7, 10)] # Create a list of vectors for the snake's body
        self.direction = Vector2(1, 0) # Initial direction to right side

    def draw_snake(self): 
        for block in self.body: # This is the loop that will draw the snake
            x_pos = int(block.x * cell_size) 
            y_pos = int(block.y * cell_size) 
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size) # Create a rectangle for each block of the snake
            pygame.draw.rect(screen, (233, 111, 122), block_rect) # Draw the rectangle on the screen with a color

    def move_snake(self): 
        body_copy = self.body[:-1] # Create a copy of the snake's body without the last block
        body_copy.insert(0, body_copy[0] + self.direction) # This inserts a new block ahead of the snake in its moving direction
        self.body = body_copy[:] # Update the snake's body with the new position


class FRUIT: 
    def __init__(self): # Create an x and y position
        self.x = random.randint(0, cell_number - 1) # -1 ensures the fruit is within the grid
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)
        
    def draw_fruit(self): # Draw a square which will be the fruit
        fruit_rect = pygame.Rect(int(self.pos.x  * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)  # Create a rectangle for the fruit
        pygame.draw.rect(screen, (126, 166, 113), fruit_rect)

pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

fruit = FRUIT()
snake = SNAKE()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) # Set a timer event to update the screen every 150 milliseconds

# Event loop to keep the game running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            snake.move_snake()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.direction = Vector2(1, 0)
        
    screen.fill((180, 75, 200)) # Decide the screen color
    fruit.draw_fruit()
    snake.draw_snake()
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS
     