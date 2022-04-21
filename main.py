import pygame
import random

pygame.init()

# window init
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("DVD screensaver")

running = True

# colors
dvd_colors = [pygame.Color("red"), 
              pygame.Color("blue"),
              pygame.Color("green"),
              pygame.Color("magenta"), 
              pygame.Color("cyan"),
              pygame.Color("yellow"), 
              pygame.Color("white"),
              pygame.Color("purple"),
              pygame.Color("orange")]

# DVD logo
dvd_logo_sprite = pygame.image.load("./dvd_logo.png")
rect = dvd_logo_sprite.get_rect()
rect.center = (400, 300)

dvd_bg_color = random.choice(dvd_colors)
last_bg_color = dvd_bg_color

dvd_logo_bg = pygame.draw.rect(window, dvd_bg_color, rect)

clock = pygame.time.Clock()

dvd_angle = [False, True]

while running:
    pygame.display.flip()
    
    window.fill((0, 0, 0))
    
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
    if rect.left == 0:
        dvd_angle[1] = True # right
        
        while dvd_bg_color == last_bg_color:
            dvd_bg_color = random.choice(dvd_colors)
        last_bg_color = dvd_bg_color
    elif rect.right == 800:
        dvd_angle[1] = False # left
        
        while dvd_bg_color == last_bg_color:
            dvd_bg_color = random.choice(dvd_colors)
        last_bg_color = dvd_bg_color
    
    if dvd_angle[0]:
        rect.y -= 1
    else:
        rect.y += 1
    if dvd_angle[1]:
        rect.x += 1
    else:
        rect.x -= 1
        
    dvd_logo_bg = pygame.draw.rect(window, dvd_bg_color, rect)
    window.blit(dvd_logo_sprite, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame() # crashes the program, so everything is terminated

    clock.tick(120)
