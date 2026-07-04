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
    def __init__(self):
        self.randomize() # Randomize the fruit's position when the game starts 
       
    def draw_fruit(self): # Draw a square which will be the fruit
        fruit_rect = pygame.Rect(int(self.pos.x  * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)  # Create a rectangle for the fruit
        pygame.draw.rect(screen, (126, 166, 113), fruit_rect)

    def randomize(self): # Randomize the fruit's position
        self.x = random.randint(0, cell_number - 1) 
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)

class MAIN: 
    def __init__(self): # Initialize the main game class
        self.snake = SNAKE() 
        self.fruit = FRUIT()

    def update(self): # Update the game state
        self.snake.move_snake() # Move the snake in its current direction
        self.check_collision() 

    def draw_elements(self): # Draw the snake and fruit on the screen
        self.fruit.draw_fruit()
        self.snake.draw_snake() 

    def check_collision(self): # Check for collision between the snake and the fruit
        if self.fruit.pos == self.snake.body[0]: # Check if the snake's head is at the same position as the fruit
            self.fruit.randomize() # Randomize the fruit's position when the snake eats it   

pygame.init()
cell_size = 30
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

main_game = MAIN()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150) # Set a timer event to update the screen every 150 milliseconds

# Event loop to keep the game running
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                main_game.snake.direction = Vector2(1, 0)
        
    screen.fill((180, 75, 200)) # Decide the screen color
    main_game.draw_elements() # Draw the snake and fruit on the screen
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS
     