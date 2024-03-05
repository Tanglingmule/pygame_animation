import pygame
from pygame.locals import *  # Importing necessary modules

import psutil  # Module for system monitoring


# Class representing the player character
class Player(pygame.sprite.Sprite):
    def __init__(self, aCharacterSpriteSheet, screen_width, screen_height):
        super().__init__()
        # Initialization of player attributes
        self.height = 80
        self.width = 80
        self.speed = 8
        self.frame = 0
        self.state = 0
        self.buffer = 15
        self.spriteSheet = pygame.image.load(aCharacterSpriteSheet)
        self.image = self.spriteSheet.subsurface(Rect(0, 0, self.width, self.height))
        
        # Set initial position to the center of the screen
        self.x = (screen_width - self.width) // 2
        self.y = (screen_height - self.height) // 2

    # Method to update player's position
    def updatePos(self):
        # State management for player movement
        if self.state == 0:
            self.state = 4
        if self.state == 1:
            self.state = 5
        if self.state == 2:
            self.state = 6
        if self.state == 3:
            self.state = 7
        
        # Handling player movement based on pressed keys
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_w]:
            self.y += -self.speed
            self.state = 0
        if pressed_keys[K_s]:
            self.y += self.speed
            self.state = 1
        if pressed_keys[K_d]:
            self.x += self.speed
            self.state = 2
        if pressed_keys[K_a]:
            self.x += -self.speed 
            self.state = 3

    # Method to draw player on the screen
    def draw(self, window):
        # Animation frame update
        self.frame += 1
        if self.frame == 8:
            self.frame = 0
        
        # Extracting appropriate portion of the sprite sheet for animation
        self.image = self.spriteSheet.subsurface(Rect(self.frame * self.width + self.buffer, self.state * self.height + self.buffer, self.width - self.buffer, self.height - self.buffer))
        window.blit(self.image,(self.x, self.y))

# Class representing boundaries of the screen
class Boundary:
    def __init__(self, x, y, width, height):
         self.rect = pygame.Rect(x, y, width, height)
    
    # Method to draw boundaries on the screen
    def draw (self, window):
        pygame.draw.rect(surface=window, color=(255, 0, 0), rect=self.rect)
    
    # Method to check if a point is within the boundary
    def contains_point(self, x, y):
         return self.rect.collidepoint(x, y)

# Function to play background music
def play_music():
    pygame.mixer.music.load('assets/music/soundtrack.mp3')
    pygame.mixer.music.play(-1)

# Function to load background image
def load_background(scene):
    if scene ==1 :
        return pygame.image.load('assets/333121.jpg')
    if scene == 2 :
        return pygame.image.load('assets/spritesheet.png')

# Main function
def main():
    pygame.init()  # Initializing pygame
    scene = 1  # starting scene is 1

    height = 1080  # Screen height
    width = 1920   # Screen width
    FPS = 15       # Frames per second
    clock = pygame.time.Clock()  # Clock object to control frame rate
    screen_boundaries = Boundary(0, 0, width, height)  # Creating screen boundary object

    window = pygame.display.set_mode((width, height))  # Creating game window
    pygame.display.set_caption("Animation Test")  # Setting window title

    # Define the point at which the message will be shown
    message_point_x = 500
    message_point_y = 500
    reached_message = False

    link = Player("assets/spritesheet.png", width, height)  # Creating player object
    play_music()  # Playing background music

    # Font for displaying FPS
    font = pygame.font.Font(None, 24)
    fps_text = ""

    # Game loop
    while True:
        for event in pygame.event.get():  # Event handling loop
            if event.type == QUIT:
                pygame.quit()  # Quit pygame
                exit()        # Exit the program

        link.updatePos()  # Update player position

        # Handling player going out of screen boundaries
        if not screen_boundaries.contains_point(link.x, link.y):
            if link.x < 0:
                link.x = 0
            if link.y < 0:
                link.y = 0
            if link.x > width - link.width:
                link.x = width - link.width
            if link.y > height - link.height:
                link.y = height - link.height
        
        screen_boundaries.draw(window)  # Draw screen boundaries

        # Draw background
        window.blit(load_background(scene), (0, 0))

        # Draw player
        link.draw(window)

        # Check if player is close to the specified point
        distance_threshold = 50
        distance_threshold_squared = distance_threshold ** 2
        distance_squared = (link.x - message_point_x) ** 2 + (link.y - message_point_y) ** 2
        if distance_squared <= distance_threshold_squared:
            reached_message = True
        else:
            reached_message = False

        # Display a message if the player reaches the message point
        if reached_message and pygame.key.get_pressed()[K_SPACE]:
            scene = 2
            reached_font = pygame.font.Font(None, 36)
            text = reached_font.render("You've reached the message point!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(width // 2, height // 2))
            window.blit(text, text_rect)

        # Draw a circle if the player is not near the message point
        if not reached_message:
            pygame.draw.circle(window, (255, 0, 0), (message_point_x, message_point_y), 15)
        
        # Update FPS counter
        fps_text = "FPS: {:.2f}".format(clock.get_fps())
        fps_render = font.render(fps_text, True, (255, 255, 255))
        window.blit(fps_render, (10, 10))

        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=None)
        cpu_text = f"CPU: {cpu_usage:.2f}%"
        cpu_render = font.render(cpu_text, True, (255, 255, 255))
        window.blit(cpu_render, (10, 40))

        # Get GPU usage (assuming you have a dedicated GPU)
        gpu_text = "GPU: N/A"
        gpu_render = font.render(gpu_text, True, (255, 255, 255))
        window.blit(gpu_render, (10, 70))

        pygame.display.update()  # Update the display
        clock.tick(FPS)          # Control the frame rate

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()

