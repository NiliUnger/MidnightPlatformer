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
    screen_width = 128
    screen_height = 256
    splash = pygame.Group()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    #setting  sprites

    frame1 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_one.pxm")
    frame2 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_two.pxm")
    frame3 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_three.pxm")
    frame4 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_four.pxm")
    frame5 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_five.pxm")
    frame6 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_six.pxm")
    frame7 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_seven.pxm")
    frame8 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_eight.pxm")
    frame9 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_nine.pxm")
    frame10 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_ten.pxm")
    frame11 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_eleven.pxm")
    frame12 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_twelve.pxm")
    frame13 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_thirteen.pxm")
    frame14 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_fourteen.pxm")
    frame15 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_fifteen.pxm")
    frame16 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/frame_sixteen.pxm")
    front_face = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/FrontFace.png")
    side_left = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/side_left.pxm")
    walk_left_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_left1.pxm")
    walk_left_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_left2.pxm")
    side_right = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/side_right.pxm")
    walk_right_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_right1.pxm")
    walk_right_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/walk_right2.pxm")
    flower_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/Midnight_ flower.pxm")
    flower_collected = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/Midnight_ flower_ collected.pxm")
    level_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/background.png")
    crouch_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/crouch_one.pxm")
    crouch_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/crouch_two.pxm")
    #jump_one
    #jump_two
    #coin_one
    #coin_two
    #coin_collected
    #platforms
    #star_power (makes you jump higher)
    #hourglass_power (speeds you up)
    #timer (like for the corner. i need to research how to do this)(wait i know have a number file than just like apply it to hundreds tens and ones)

# note to fix flower sprite but im lazy rn (rehearsal 11/19)
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

    splash.append(level_sprite)
    splash.append(girl_sprite)

    #add some sounds here!
    #make them myself lol i aint hiring a real composer
    # pygame.mixer.Sound() RESEARCH THIS!!!

    
    #variables
    coin = 0
    flower = 0
    time = 600
    x = girl_sprite.x
    y = girl_sprite.y
    star = False
    hourglass = False
    girl_hitbox = pygame.Rect(x, y, girl_sprite.width, girl_sprite.height)
    flower_hitbox = pygame.Rext(flower_sprite.x, flower_sprite.y, flower_sprite.width, flower_sprite.height)
    #coin_hitbox
    #star_hitbox
    #hourglass_hitbox

    #(intro is defined within the intro function)
    intro()
    # timer for level
    if intro == False:
        for second in clock:
            time -= 1
            if time <= 0:
                #maybe add a losing animation if time? (ofc there's time lol)
                pygame.quit()

    keys = pygame.key.get_pressed()
    if pygame.event(keys[pygame.K_LEFT]) & hourglass == False & intro == False:
        walk_left()
        x -= 1
        
    if pygame.event(keys[pygame.K_RIGHT]) & hourglass == False & intro == False:
       walk_right()
       x += 1
    if pygame.event(keys[pygame.K_LEFT]) & hourglass == True & intro == False:
        walk_left()
        x -= 3
        walk_left()
    if pygame.event(keys[pygame.K_RIGHT]) & hourglass == True & intro == False:
        walk_right()
        x += 3
        walk_right()
    if pygame.event(keys[pygame.K_UP]) & star == False & intro == False:
        y += 5
        pygame.event.wait(.5)
        y -= 5
        #add thing about platforms
    if pygame.event(keys[pygame.K_UP]) & star == True & intro == False:
        y += 10
        pygame.event.wait(.5)
        y -= 10
        # add thing about platforms
    if pygame.event(keys[pygame.K_DOWN]) & intro == False:
        girl_sprite = pygame.image.TileGrid(
            crouch_one,
            pixel_shader = crouch_one.pixel_shader
        )
        pygame.event.wait()(.3)
        girl_sprite = pygame.image.TileGrid(
            crouch_two,
            pixel_shader = crouch_two.pixel_shader
        )
        pygame.event.wait()(.3)
        girl_sprite = pygame.image.TileGrid(
            front_face,
            pixel_shader = front_face.pixel_shader
        )
#walking animation functions for simplicity's sake
    def walk_left():
        girl_sprite = pygame.image.TileGrid(
            walk_left_one,
            pixel_shader = walk_left_one.pixel_shader
        )
        pygame.event.wait()(.2)
        girl_sprite = pygame.image.load(
            walk_left_two,
            pixel_shader = walk_left_two.pixel_shader
        )
        pygame.event.wait()(.2)
        girl_sprite = pygame.image.TileGrid(
            side_left,
            pixel_shader=front_face.pixel_shader
        )
    def walk_right():
        girl_sprite = pygame.image.TileGrid(
            walk_right_one,
            pixel_shader = walk_right_one.pixel_shader
        )
        pygame.event.wait()(.2)
        girl_sprite = pygame.image.load(
            walk_right_two,
            pixel_shader = walk_right_two.pixel_shader
        )
        pygame.event.wait()(.2)
        girl_sprite = pygame.image.TileGrid(
            side_right,
            pixel_shader = side_right.pixel_shader
        )
    def jump():
        #add jump sprites once I make them
        pygame.event.wait()(.2)
        pygame.event.wait()(.2)
        girl_sprite = pygame.image.TileGrid(
            front_face,
            pixel_shader = front_face.pixel_shader
        )
    def intro():
        intro = True
        intro_sprite = pygame.image.TileGrid(
            frame1,
            pixel_shader = frame1.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame2,
            pixel_shader = frame2.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame3,
            pixel_shader = frame3.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame4,
            pixel_shader = frame4.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame5,
            pixel_shader = frame5.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame6,
            pixel_shader = frame6.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame7,
            pixel_shader = frame7.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame8,
            pixel_shader = frame8.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame8,
            pixel_shader = frame8.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame9,
            pixel_shader = frame9.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame10,
            pixel_shader = frame10.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame11,
            pixel_shader = frame11.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame12,
            pixel_shader = frame12.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame13,
            pixel_shader = frame13.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame14,
            pixel_shader = frame14.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame15,
            pixel_shader = frame15.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(.5)
        intro_sprite = pygame.image.TileGrid(
            frame1,
            pixel_shader = frame1.pixel_shader
        )
        splash.append(intro_sprite)
        pygame.event.wait()(3)
        pygame.sprite.remove(intro_sprite)
        intro = False