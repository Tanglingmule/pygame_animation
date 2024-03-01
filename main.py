import pygame
import os

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Sheet Animation")

# Load the sprite sheet image
sprite_sheet = pygame.image.load("assets/spritesheet.png").convert_alpha()

# Function to extract individual frames from the sprite sheet
def get_images(sheet, x, y, width, height, columns, rows):
    images = []
    for j in range(rows):
        for i in range(columns):
            image = sheet.subsurface((x + i * width, y + j * height, width, height))
            images.append(image)
    return images

# Extract frames for walking animations (left and right)
walking_left_frames = get_images(sprite_sheet, 0, 0, 36, 128, 9, 1)
walking_right_frames = get_images(sprite_sheet, 78, 0, 36, 128, 9, 1)

# Extract frames for idle animation
idle_frames = get_images(sprite_sheet, 13, 0, 36, 128, 1, 1)

clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Draw the animation frames
    current_frame = pygame.time.get_ticks() // 100 % 9  # Change the divisor to adjust animation speed
    screen.blit(walking_left_frames[current_frame], (100, 100))
    screen.blit(walking_right_frames[current_frame], (300, 100))
    screen.blit(idle_frames[0], (500, 100))

    pygame.display.flip()
    clock.tick(10)  # Adjust the parameter to control FPS

pygame.quit()
