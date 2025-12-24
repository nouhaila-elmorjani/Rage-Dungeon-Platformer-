import pygame, sys
from pygame import mixer

# Initialising pygame
pygame.init()
print("Pygame initialized")

# Defining size of game window
screen = pygame.display.set_mode((1280, 640))
print("Screen created")

# Creating clock - to set max frame rate to 60
Clock = pygame.time.Clock()

# Test basic display
font = pygame.font.SysFont(None, 36)
text = font.render("Testing game display - Press any key", True, (255, 255, 255))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            running = False
    
    screen.fill((0, 0, 0))
    screen.blit(text, (400, 300))
    pygame.display.update()
    Clock.tick(60)

print("Test completed successfully")
pygame.quit()
