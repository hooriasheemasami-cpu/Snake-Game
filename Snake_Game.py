import pygame, sys, random
from pygame.math import Vector2

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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    screen.fill((180, 75, 200)) # Decide the screen color
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS
     