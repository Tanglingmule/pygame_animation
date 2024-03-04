import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, aCharacterSpriteSheet):
        super().__init__()
        self.x = 0
        self.y = 0
        self.height = 80
        self.width = 80
        self.speed = 8
        self.frame = 0
        self.state = 0
        self.buffer = 15
        self.spriteSheet = pygame.image.load(aCharacterSpriteSheet)
        self.image = self.spriteSheet.subsurface(Rect(self.x, self.y, self.width, self.height))

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


def main():
    pygame.init()  # Initialize Pygame

    height = 1080
    width = 1920
    FPS = 15
    clock = pygame.time.Clock()

    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Animation Test")

    link = Player("assets/spritesheet.png")
    play_music()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        link.updatePos()
        window.fill((0, 0, 0))  # Clear screen before drawing
        link.draw(window)

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

