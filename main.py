import pygame
from tkinter import simpledialog, messagebox
from ast import literal_eval
from os import remove
from math import sqrt

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
            if len(stars) > 0:
                archive = open("db.txt", "w")
                archive.write(str(stars))
                archive.close()
                messagebox.showinfo("Space Marker", "Points saved in the database")
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if len(stars) > 0:
                archive = open("db.txt", "w")
                archive.write(str(stars))
                archive.close()
                messagebox.showinfo("Space Marker", "Points saved in the database")
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
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F10:
            if len(stars) > 0:
                archive = open("db.txt", "w")
                archive.write(str(stars))
                archive.close()
                messagebox.showinfo("Space Marker", "Points saved in the database")
            else:
                messagebox.showwarning("Space Marker", "There are no points to be saved")
        elif event. type == pygame.KEYDOWN and event.key == pygame.K_F11:
            try:
                archive = open("db.txt", "r")
                stars = literal_eval(archive.read())
                for names, coordinates in stars.items():
                    star_name = font.render(f"{names}", True, white)
                    screen.blit(star_name, coordinates)
                    pygame.draw.circle(screen, white, coordinates, 5)
                archive.close()
                messagebox.showinfo("Space Marker", "Points loaded from the database")
            except:
                messagebox.showwarning("Space Marker", "There are no points to load")
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            remove("db.txt")
            stars = {}
            screen.fill(white)
            screen.blit(background, (0,0))
            screen.blit(f10, (10,10))
            screen.blit(f11, (10,30))
            screen.blit(f12, (10,50))
            messagebox.showinfo("Space Marker", "Points deleted from the database")
    
    if len(stars) > 1:
        key_list = list(stars.keys())

        for i, v in enumerate(key_list):
            try:
                x1, y1 = stars[key_list[i]]
                x2, y2 = stars[key_list[i + 1]]
                distance = round(sqrt((x2 - x1)**2 + (y2 - y1)**2))
                write_distance = font.render(f"{distance}", True, white)
                pygame.draw.line(screen, white, (x1, y1), (x2, y2), 1)
                screen.blit(write_distance, ((x1 + x2)/2, (y1 + y2)/2))
            except:
                break


    pygame.display.update()
pygame.quit()