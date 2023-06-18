import pygame
from tkinter import simpledialog

pygame.init()

size = (1200,728)
white = (255,255,255)
screen = pygame.display.set_mode(size)
space = pygame.image.load('space.png')
background = pygame.image.load('background.jpg')
font = pygame.font.Font(None, 25)
f10 = font.render("Press F10 to save the points", True, white)
f11 = font.render("Press F11 to load the points", True, white)
f12 = font.render("Press F12 to delete the points", True, white)
clock = pygame.time.Clock()
stars = {}
running = True

screen.fill(white)
screen.blit(background, (0,0))
screen.blit(f10, (10,10))
screen.blit(f11, (10,30))
screen.blit(f12, (10,50))

pygame.display.set_caption("Space Marker")
pygame.display.set_icon(space)
pygame.mixer.music.load("track.mp3")
pygame.mixer.music.play(-1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            position = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Star's Name:")
            if item == None or item == '':
                item = "Unknown" + str(position)
            stars[item] = position
            star_name = font.render(f"{item}", True, white)
            screen.blit(star_name, position)
            pygame.draw.circle(screen, white, position, 5)


    pygame.display.update()
pygame.quit()