import pygame, sys, random
from pygame.math import Vector2

class SNAKE:
    def __init__(self): 
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)] # Create a list of vectors for the snake's body
        self.direction = Vector2(0, 0) # Initial direction to right side
        self.new_block = False # This variable will be used to determine if a new block should be added to the snake's body
        self.crunch_sound = pygame.mixer.Sound('Sound/Crunch.mp3') # Load the sound effect for when the snake eats a fruit

    def draw_snake(self): 
        for block in self.body: # This is the loop that will draw the snake
            x_pos = int(block.x * cell_size) 
            y_pos = int(block.y * cell_size) 
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size) # Create a rectangle for each block of the snake
            pygame.draw.rect(screen, (233, 111, 122), block_rect) # Draw the rectangle on the screen with a color

    def move_snake(self):
        if self.new_block == True: # If a new block should be added to the snake's body
            body_copy = self.body[:] # Create a copy of the snake's body
            body_copy.insert(0, body_copy[0] + self.direction) # This inserts a new block ahead of the snake in its moving direction
            self.body = body_copy[:] # Update the snake's body with the new position
            self.new_block = False # Reset the new_block variable to False after adding a new block
        else:
            body_copy = self.body[:-1] # Create a copy of the snake's body without the last block
            body_copy.insert(0, body_copy[0] + self.direction) # This inserts a new block ahead of the snake in its moving direction
            self.body = body_copy[:] # Update the snake's body with the new position

    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self): # Play the sound effect for when the snake eats a fruit
        self.crunch_sound.play()

    def reset(self): # Reset the snake's position and direction
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)] # Reset the snake's body to its initial position
        self.direction = Vector2(0, 0) # Reset the snake's direction to right side

               
class FRUIT: 
    def __init__(self):
        self.randomize() # Randomize the fruit's position when the game starts 
       
    def draw_fruit(self): # Draw a square which will be the fruit
        fruit_rect = pygame.Rect(int(self.pos.x  * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)  # Create a rectangle for the fruit
        screen.blit(apple, fruit_rect) # Draw the apple image on the screen at the fruit's position

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
        self.check_fail()

    def draw_elements(self): # Draw the snake and fruit on the screen
        self.draw_grass() 
        self.fruit.draw_fruit()
        self.snake.draw_snake() 
        self.draw_scores()

    def check_collision(self): # Check for collision between the snake and the fruit
        if self.fruit.pos == self.snake.body[0]: # Check if the snake's head is at the same position as the fruit
            self.fruit.randomize() # Randomize the fruit's position when the snake eats it 
            self.snake.add_block()
            self.snake.play_crunch_sound() # Play the sound effect for when the snake eats a fruit
        
        for block in self.snake.body[1:]:
            if block == self.fruit.pos: # Check if the fruit's position is at the same position as any part of the snake's body
                self.fruit.randomize() # Randomize the fruit's position if it is on the snake's body

    def check_fail(self): # Check if the snake has collided with itself or the walls
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over() # If the snake's head is out of bounds, end the game
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]: # Check if the snake's head is at the same position as any other part of its body
                self.game_over() # If the snake's head collides with its body, end the game

    def game_over(self): # End the game
        self.snake.reset() # Reset the snake's position and direction

    def draw_grass(self):
        grass_color = (190, 80, 210) # Set the color for the grass
        for row in range(cell_number):
            if row % 2 == 0: # Draw grass only on even rows
                for col in range(cell_number):
                    if col % 2 == 0: # Draw grass only on even columns
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size) # Create a rectangle for each column of grass
                        pygame.draw.rect(screen, grass_color, grass_rect) # Draw the grass rectangle on the screen
            else:
                for col in range(cell_number):
                    if col % 2 != 0: # Draw grass only on odd columns
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect) 

    def draw_scores(self):
        score_text = str(len(self.snake.body) - 3) # Calculate the score based on the length of the snake's body
        score_surface = game_font.render(score_text, True, (56, 74, 12)) # Create a surface for the score text
        score_x = int(cell_number * cell_size - 60) # Calculate the x position for the score text
        score_y = int(cell_number * cell_size - 40) # Calculate the y position
        score_rect = score_surface.get_rect(center=(score_x, score_y)) # Create a rectangle for the score text
        apple_rect = apple.get_rect(midright = (score_rect.left - 10, score_rect.centery - 2)) # Create a rectangle for the apple image next to the score text
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 20, apple_rect.height) # Create a background rectangle for the score and apple
        
        pygame.draw.rect(screen, (180, 75, 200), bg_rect) # Draw the background rectangle on the screen
        screen.blit(score_surface, score_rect) # Draw the score text on the screen
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2) # Draw a border around the background rectangle

pygame.mixer.pre_init(44100, -16, 2, 512) # Pre-initialize the mixer for sound effects
pygame.init() 
cell_size = 30
cell_number = 20
apple_size = cell_size
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple_original = pygame.image.load('Graphics/apple.png').convert_alpha() # Load the apple image for the fruit
apple = pygame.transform.scale(apple_original, (apple_size, apple_size)) # Scale the apple image to fit the cell size
game_font = pygame.font.Font('Font/Eternalo.ttf', 25) # Set the font for the game over message
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
                if main_game.snake.direction.y != 1:  # Prevent the snake from moving in the opposite direction
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:  # Prevent the snake from moving in the opposite direction
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:  # Prevent the snake from moving in the opposite direction
                    main_game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:  # Prevent the snake from moving in the opposite direction
                    main_game.snake.direction = Vector2(1, 0)
        
    screen.fill((180, 75, 200)) # Decide the screen color
    main_game.draw_elements() # Draw the snake and fruit on the screen
    main_game.draw_scores() # Draw the score on the screen
    pygame.display.update()
    clock.tick(60)  # Limit the frame rate to 60 FPS
     