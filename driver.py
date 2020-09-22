import pygame as game
from pygame.locals import *
import os
import sys
from bird import Bird
import time

bird = game.image.load('Sprites/bird.png')
background = game.image.load('Sprites/background.jpg')
pipes = game.image.load('Sprites/pipe.png')

FPS = 30
SC_WIDTH = 500
SC_HEIGHT = 750
BLACK = (0,0,0)

background = game.transform.scale(background, (SC_WIDTH,SC_HEIGHT))

def drawWindow(win, flapBird):
    win.blit(background, (0,0))
    win.blit(bird, (100,flapBird.y))

    game.display.update()

def main():

    game.init()
    flapBird = Bird(150, 150, 40, 40)     
    win = game.display.set_mode((SC_WIDTH, SC_HEIGHT))
    clock = game.time.Clock()
    game.display.set_caption("Flappy Bird")

    run = True
    while(run):
        for event in game.event.get():
            if(event.type == QUIT):
                run = False

        keys = game.key.get_pressed()

        if keys[game.K_SPACE]: #and flapBird.isFlapping == False:
            flapBird.flap()

        clock.tick(FPS)
        flapBird.move()
        drawWindow(win, flapBird)

    game.quit()

main()