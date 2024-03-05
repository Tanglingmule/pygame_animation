import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, aCharacterSpriteSheet, screen_width, screen_height):
        super().__init__()
        # Other initialization code...
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

    def updatePos(self):
        if self.state == 0:
            self.state = 4

        if self.state == 1:
            self.state = 5

        if self.state == 2:
            self.state = 6

        if self.state == 3:
            self.state = 7

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

    def draw(self, window):
        self.frame +=1
        if self.frame == 8:
            self.frame = 0

        self.image = self.spriteSheet.subsurface(Rect(self.frame * self.width + self.buffer, self.state * self.height + self.buffer, self.width - self.buffer, self.height - self.buffer))
        window.blit(self.image,(self.x, self.y))

def play_music():
    pygame.mixer.music.load('assets/music/soundtrack.mp3')
    pygame.mixer.music.play(-1)


def load_background():
    return pygame.image.load('assets/333121.jpg')

def main():
    pygame.init()

    height = 1080
    width = 1920
    FPS = 15
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Animation Test")


    # Define the point at which the message will be shown
    message_point_x = 500
    message_point_y = 500
    reached_message = False

    link = Player("assets/spritesheet.png", width, height)
    play_music()

    # FPS counter variables
    font = pygame.font.Font(None, 24)  # Define the font
    fps_text = ""
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        link.updatePos()

        # Draw background
        window.blit(load_background(), (0, 0))

        # Draw player
        link.draw(window)

        # Check if the player is close to the specified point
        distance_threshold = 50  # smaller area
        distance_threshold_squared = distance_threshold ** 2
        distance_squared = (link.x - message_point_x) ** 2 + (link.y - message_point_y) ** 2
        if distance_squared <= distance_threshold_squared:
            reached_message = True
        else:
            reached_message = False

        # Display a message if the player reaches the message point
        if reached_message:
            font = pygame.font.Font(None, 36)
            # black text
            text = font.render("You've reached the message point!", True, (0, 0, 0))
            text_rect = text.get_rect(center=(width // 2, height // 2))  # Center the text
            window.blit(text, text_rect)


        # Draw a circle if the player is not near the message point
        if not reached_message:
            pygame.draw.circle(window, (255, 0, 0), (message_point_x, message_point_y), 15)  # smaller dot
        
        # Update FPS counter
        fps_text = "FPS: {:.2f}".format(clock.get_fps())
        fps_render = font.render(fps_text, True, (255, 255, 255))
        window.blit(fps_render, (10, 10))


        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
