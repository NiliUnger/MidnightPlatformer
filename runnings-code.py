import pygame
import time
import random
import os
# notes about game lore: a girl is running away from home (don't learn this until end of the game)
# and she's running to her aunt's house. if she runs out of time or takes too much damage play an animation of her parents catching her

#general notes: add 
# powerups (higher jumps) (maybe a little star!)

def game():
    pygame.init()

    #display!
    screen_width = 256
    screen_height = 256
    splash = pygame.Group()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("the moon has risen... escape as fast as possible")
    clock = pygame.time.Clock()

    #setting  sprites
    front_face = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/FrontFace.png")
    side_left = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/side_left.pxm")
    walk_left_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_left1.pxm")
    walk_left_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_left2.pxm")
    side_right = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/side_right.pxm")
    walk_right_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_right1.pxm")
    walk_right_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_right2.pxm")
    #crouch
    #jump_one
    #jump_two
    #coin_one
    #coin_two
    #coin_collected
    #platform
    #star_power (makes you jump higher)
    #hourglass_power (speeds you up)
    flower_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/Midnight_ flower.pxm")
    flower_collected = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/Midnight_ flower_collected.pxm")
    level_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/background.png")
    girl_sprite = pygame.image.TileGrid(
        front_face,
        pixel_shader = front_face.pixel_shader,
    )
    level_sprite = pygame.image.TileGrid(
        level_one,
        pixel_shader = level_one.pixel_shader
    )
    flower_sprite = pygame.image.TileGrid(
        flower_one,
        pixel_shader = flower_one.pixel_shader
    )
    #add coin sprite, star sprite

    #adding those sprites as file thingies

    splash.append(level_one)
    splash.append(front_face)

    #add some sounds here!

    #walking animation functions for simplicity's sake
    def walk_left():
        girl_sprite = pygame.image.TileGrid(
            walk_left_one,
            pixel_shader = walk_left_one.pixel_shader
        )
        girl_sprite = pygame.image.load(
            walk_left_two,
            pixel_shader = walk_left_two.pixel_shader
        )
        girl_sprite = pygame.image.TileGrid(
            side_left,
            pixel_shader=front_face.pixel_shader
        )
    def walk_right():
        girl_sprite = pygame.image.TileGrid(
            walk_right_one,
            pixel_shader = walk_right_one.pixel_shader
        )
        girl_sprite = pygame.image.load(
            walk_right_two,
            pixel_shader = walk_right_two.pixel_shader
        )
        girl_sprite = pygame.image.TileGrid(
            side_right,
            pixel_shader = side_right.pixel_shader
        )
    def jump():
        #add jump sprites once I make them
        girl_sprite = pygame.image.TileGrid(
            front_face,
            pixel_shader = front_face.pixel_shader
        )
    #variables
    coin = 0
    flower = 0
    time = 600
    x = girl_sprite.x
    y = girl_sprite.y
    star = False
    hourglass = False

    # timer for level
    for second in clock:
        time -= 1
        if time <= 0:
            print("they've caught up... i'm sorry...")
            pygame.quit()

    keys = pygame.key.get_pressed()
    if pygame.event(keys[pygame.K_LEFT]) & hourglass == False:
        walk_left()
        x -= 1
        
    if pygame.event(keys[pygame.K_RIGHT]) & hourglass == False:
       walk_right()
       x += 1
    if pygame.event(keys[pygame.K_LEFT]) & hourglass == True:
        walk_left()
        x -= 3
        walk_left()
    if pygame.event(keys[pygame.K_RIGHT]) & hourglass == True:
        walk_right()
        x += 3
        walk_right()
    if pygame.event(keys[pygame.K_UP]) & star == False:
        y += 5
        pygame.event.wait(.5)
        y -= 5
        #add thing about platforms
    if pygame.event(keys[pygame.K_UP]) & star == True:
        y += 10
        pygame.event.wait(.5)
        y -= 10
        # add thing about platforms
    if pygame.event(keys[pygame.K_DOWN]):
        pass
            #add code to make sprite change and also hitbox
