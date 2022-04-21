import pygame
import random

pygame.init()

# window init
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DVD screensaver")

running = True

# colors
black = pygame.Color((0, 0, 0))
red = pygame.Color((255, 0, 0))
blue = pygame.Color((0, 0, 255))
green = pygame.Color((0, 255, 0))
pink = pygame.Color((255, 0, 255))
cyan = pygame.Color((0, 255, 255))
yellow = pygame.Color((255, 255, 0))
white = pygame.Color((255, 255, 255))

dvd_colors = [red, blue, green, pink, cyan, yellow, white]

# DVD logo
dvd_logo_sprite = pygame.image.load("./dvd_logo.png")
rect = dvd_logo_sprite.get_rect()
rect.center = (300, 300)

dvd_bg_color = random.choice(dvd_colors)
last_bg_color = dvd_bg_color

dvd_logo_bg = pygame.draw.rect(window, dvd_bg_color, rect)

clock = pygame.time.Clock()

dvd_angle = [False, True]

while running:
    pygame.display.flip()
    
    window.fill(black)
    
    if rect.bottomleft[1] == 600:
        dvd_angle[0] = True # up
        
        while dvd_bg_color == last_bg_color:
            dvd_bg_color = random.choice(dvd_colors)
        last_bg_color = dvd_bg_color
    elif rect.topleft[1] == 0:
        dvd_angle[0] = False # down
        
        while dvd_bg_color == last_bg_color:
            dvd_bg_color = random.choice(dvd_colors)
        last_bg_color = dvd_bg_color
    elif rect.left == 0:
        dvd_angle[1] = True # right
        
        while dvd_bg_color == last_bg_color:
            dvd_bg_color = random.choice(dvd_colors)
        last_bg_color = dvd_bg_color
    elif rect.right == 800:
        dvd_angle[1] = False # left
        
        while dvd_bg_color == last_bg_color:
            dvd_bg_color = random.choice(dvd_colors)
        last_bg_color = dvd_bg_color
    
    if dvd_angle[0] == True:
        rect.y -= 1
    else:
        rect.y += 1
    if dvd_angle[1] == True:
        rect.x += 1
    else:
        rect.x -= 1
        
    dvd_logo_bg = pygame.draw.rect(window, dvd_bg_color, rect)
    window.blit(dvd_logo_sprite, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame() # crashes the program, so everything is terminated

    clock.tick(60)
