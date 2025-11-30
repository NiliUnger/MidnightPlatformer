import pygame
import time
import random
import os
import asyncio

# notes about game lore: a girl is running away from home (don't learn this until end of the game)
# and she's running to her aunt's house. if she runs out of time or takes too much damage play an animation of her parents catching her
# for final level, make coin requirement in order to win as the price to get the final bus ticket to escape
#initializing pygame and sounds

pygame.init()
pygame.mixer.init()

#setting  images and sounds

#images
    
frame1 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_one.png")
frame2 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_two.png")
frame3 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_three.png")
frame4 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_four.png")
frame5 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_five.png")
frame6 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_six.png")
frame7 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_seven.png")
frame8 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_eight.png")
frame9 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_nine.png")
frame10 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_ten.png")
frame11 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_eleven.png")
frame12 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_twelve.png")
frame13 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_thirteen.png")
frame14 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_fourteen.png")
frame15 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_fifteen.png")
frame16 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_sixteen.png")
front_face = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/FrontFace.png")
side_left = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/side_left.png")
walk_left_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_left1.png")
walk_left_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_left2.png")
side_right = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/side_right.png")
walk_right_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_right1.png")
walk_right_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_right2.png")
flower_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_one.png")
flower_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_two.png")
flower_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_three.png")
flower_collected = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_collected.png")
level_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/background.png")
crouch_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/crouch_one.png")
crouch_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/crouch_two.png")
jump_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/jump_one.png")
jump_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/jump_two.png")
jump_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/jump_three.png")
coin_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/coin_one.png")
coin_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/coin_two.png")
coin_collected = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/coin_collected.png")
health_ten = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_ten.png")
health_nine = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_nine.png")
health_eight = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_eight.png")
health_seven = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_seven.png")
health_six = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_six.png")
health_five = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_five.png")
health_four = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_four.png")
health_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_three.png")
health_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_two.png")
health_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_one.png")
health_zero = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_zero.png")
cloud_platform = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/cloud_platform.png")
storm_platform =  pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/storm_platform.png")
star_power = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/star_power.png")
hourglass_power = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/hourglass_power.png")
zero = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/zero.png")
one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/one.png")
two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/two.png")
three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/three.png")
four = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/four.png")
five = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/five.png")
six = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/six.png")
seven = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/seven.png")
eight = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/eight.png")
nine = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/nine.png")
box_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/box_one.png")
box_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/box_two.png")
end_frame1 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/end_frame1.png")
end_frame2 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/end_frame2.png")
bus_stop = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/bus_stop.png")

    #sounds

heartbeat_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/595050__insaind__clean-deep-heartbeat.wav")
sirens_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/577312__trp__sirens-fire-police-close-pass-distant-urban-calgary-2011.wav")
whispers_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/182378__elizaeilis__whispers.mp3")
night_ambience_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/195969__rgbrobot__night-ambience-01-aug-2-2013-back-yard.wav")
flower_collect_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/413629__djlprojects__video-game-sfx-positive-action-long-tail.wav")
    
    #setting class sprites for certain images to be changed

class Player():
    def __init__(self, x, y, width, height):
        front_face,
        self.x = x
        self.y = y
        self.width = width
        self.height = height

class Level():
    def __init__(self, width, height):
        level_one,
        self.width=width
        self.height=height

class flower():
    def __init__ (self, width, height):
        flower_one,
        self.width=width
        self.height=height


level_sprite = level_one
flower_sprite = flower_one
coin_sprite = coin_one
jump_sprite = jump_one
ones_sprite = zero
tens_sprite = zero
hundreds_sprite = zero
health_sprite = health_ten

    #display!

screen_width = 256
screen_height = 128
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

    #initializing main variables

coin = 0
flower = 0
time = 300
star = False
hourglass = False
health = 10
tens = 0
ones = 0
level = 1
run = True

def game():

    
    #hitboxes defined

    girl_hitbox = pygame.Rect(Player.x, Player.y, Player.width, Player.height)
    flower_hitbox = pygame.Rect(flower_sprite.x, flower_sprite.y, flower_sprite.width, flower_sprite.height)
    cloud_hitbox = pygame.Rect(cloud_platform.x, cloud_platform.y, cloud_platform.width, cloud_platform.height)
    storm_hitbox = pygame.Rect(storm_platform.x, storm_platform.y, storm_platform.width, storm_platform.height)
    coin_hitbox =  pygame.Rect(coin_sprite.x, coin_sprite.y, coin_sprite.width, coin_sprite.height)
    box_one_hitbox = pygame.Rect(box_one.x, box_one.y, box_one.width, box_one.height)
    box_two_hitbox = pygame.Rect(box_two.x, box_two.y, box_two.width, box_two.height)
    bus_stop_hitbox = pygame.Rect(bus_stop.x, bus_stop.y, bus_stop.width, bus_stop.height)

    #defining functions that use hitboxes

    def powerup_collect():
        if hourglass == True:
            screen.blit(hourglass_power)
            time.sleep(10)
            hourglass = False
        if star == True:
            screen.blit(star_power)
            time.sleep(10)
            star  = False
    def collide():
        if girl_hitbox.colliderect(cloud_hitbox):
            Player.y = cloud_platform.y
        if girl_hitbox.colliderect(storm_hitbox):
            Player.y = storm_platform.y
            health -= 1
    def box_hit():
        if girl_hitbox.colliderect(box_one_hitbox) or girl_hitbox.colliderect(box_two_hitbox):
            if random.randint(1, 3) > 1:
                coin += 1
            else:
                if random.randint(1,2) ==1:
                    star = True
                else:
                    hourglass = True
    
    #timer functions to make the timer count down on screen

    #setting the sprite for the tens place in the timer

    def tens_change():
        for second in time:    
            if second % 10:
                tens += 1
                if tens == 1:
                    tens_sprite = zero
                elif tens == 2:
                    tens_sprite = nine
                elif tens == 3:
                    tens_sprite = eight
                elif tens == 4:
                    tens_sprite = seven
                elif tens == 5:
                    tens_sprite = six
                elif tens == 6:
                    tens_sprite = five
                elif tens == 7:
                    tens_sprite = four
                elif tens == 8:
                    tens_sprite = three
                elif tens == 9:
                    tens_sprite = two
                elif tens == 10:
                    tens_sprite = one
                else:
                    tens = 0
                    tens_change()

    #setting the sprite for the one place on the timer

    def ones_change():
            for second in time:
                ones += 1
                if ones == 1:
                    ones_sprite = one
                elif ones == 2:
                    ones_sprite = two
                elif ones == 3:
                    ones_sprite = three
                elif ones == 4:
                    ones_sprite = four
                elif ones == 5:
                    ones_sprite = five
                elif ones == 6:
                    ones_sprite = six
                elif ones == 7:
                    ones_sprite = seven
                elif ones == 8:
                    ones_sprite = eight
                elif ones == 9:
                    ones_sprite = nine
                elif ones == 10:
                    ones_sprite = zero
                else:
                    ones = 0
                    ones_change()

    #setting the full timer with the previous functions in it

    def countdown():
            for second in time:
                if second >= 300:
                    hundreds_sprite = three
                    tens_change()
                    ones_change()
                elif second >= 200:
                    hundreds_sprite = two
                    tens_change()
                    ones_change()
                elif second >= 100:
                    hundreds_sprite = one
                    tens_change()
                    ones_change()

                else:
                    hundreds_sprite = zero
                    tens_change()
                    ones_change()
    
    #function for animating when the main character jumps

    def jumping():
        class Player():
            def __init__(self, x, y, width, height):
                jump_one,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.5)
        class Player():
            def __init__(self, x, y, width, height):
                jump_two,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.5)
        class Player():
            def __init__(self, x, y, width, height):
                jump_three,
                self.x = x
                self.y = y
                self.width = width
                self.height = height


    #makes the flower sprite change on screen

    def flower_change():
        flower_sprite = flower_two
        time.sleep(0.5)
        flower_sprite = flower_three
        time.sleep(0.5)
        flower_sprite = flower_one
        time.sleep(0.5)
        flower_change()

    #makes the coin sprite change on screen

    def coin_change():
        coin_sprite = coin_two
        time.sleep(0.5)
        coin_sprite = coin_one
        time.sleep(0.5)
        coin_change()
    

    
    #collecting flower function, adding it to the flower counter on screen

    def flower_collect():
        if girl_hitbox.colliderect(flower_hitbox) == True:
                flower_collect_sound.play()
                flower += 1
                health += 2
                flower_sprite = flower_collected
                time.sleep(0.5)
                screen.remove(flower_sprite)
                flower_sprite = flower_one
                if flower == 1:
                    screen.blit(flower_sprite)
                    flower_sprite.x = 220
                    flower_sprite.y = 120
                if flower == 2:
                    screen.blit(flower_sprite)
                    flower_sprite.x = 230
                    flower_sprite.y = 120
                if flower == 3:
                    screen.blit(flower_sprite)
                    flower_sprite.x = 240
                    flower_sprite.y = 120

    #collecting coin function, adding to coin counter (tbd)

    def coin_collect():
        if girl_hitbox.colliderect(coin_hitbox) == True:
                coin += 1
                coin_sprite = coin_collected
                time.sleep(0.5)
                screen.remove(coin_sprite)
                #update coin counter on screen
    
    #changing health sprite based on health variable

    def health_change():
        if health == 10:
            health_sprite = health_ten
        elif health == 9:
            health_sprite = health_nine
        elif health == 8:
            health_sprite = health_eight
        elif health == 7:
            health_sprite = health_seven
        elif health == 6:
            health_sprite = health_six
        elif health == 5:
            health_sprite =health_five
        elif health == 4:
            health_sprite = health_four
        elif health == 3:
            health_sprite = health_three
        elif health == 2:
            health_sprite = health_two
        elif health == 1:
            heartbeat_sound.play(-1)
            health_sprite = health_one
        elif health <= 0:
            
            health_sprite = health_zero
            
    #function for ending the game

    def game_end():
        sirens_sound.play(-1)
        whispers_sound.play(-1)
        end_sprite = end_frame1
        screen.blit(end_sprite)
        time.sleep(0.2)
        end_sprite = end_frame2
        screen.blit(end_sprite)
        time.sleep(0.2)
        end_sprite = end_frame1
        screen.blit(end_sprite)
        time.sleep(0.2)
        end_sprite = end_frame2
        screen.blit(end_sprite)
        time.sleep(6)

    # timer for level

    if intro == False:
        time_remaining = 300
        time_start = time.time()
        while time_remaining > 0:
            time_remaining = 300 - int(time.time() - time_start)
            if time_remaining <= 0:
                    game_end()
                    pygame.QUIT()
        if health <= 0:
            game_end()
            pygame.QUIT()
    if girl_hitbox.colliderect(bus_stop_hitbox) and flower == 3:
        level += 1
        #play short animation of girl getting on bus to next level and start the actual next level!!!

    #doing key detection and action for key presses

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hourglass == False and intro == False:
        walk_left()
        x -= 1     
    if keys[pygame.K_RIGHT] and hourglass == False and intro == False:
       walk_right()
       x += 1
    if keys[pygame.K_LEFT] and hourglass == True and intro == False:
        walk_left()
        x -= 3
        walk_left()
    if keys[pygame.K_RIGHT] and hourglass == True and intro == False:
        walk_right()
        x += 3
        walk_right()
    if keys[pygame.K_UP] and star == False and intro == False:
        jumping()
        y += 5
        time.sleep(1)
        y -= 5
    if keys[pygame.K_UP] and star == True and intro == False:
        jumping()        
        y += 10
        time.sleep(1)
        y -= 10
    if keys[pygame.K_DOWN] and intro == False:
        class Player():
            def __init__(self, x, y, width, height):
                crouch_one,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.3)
        class Player():
            def __init__(self, x, y, width, height):
                crouch_two,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.3)
        class Player():
            def __init__(self, x, y, width, height):
                front_face,
                self.x = x
                self.y = y
                self.width = width
                self.height = height


    #walking animation functions

    def walk_left():
        class Player():
            def __init__(self, x, y, width, height):
                walk_left_one,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.2)
        class Player():
            def __init__(self, x, y, width, height):
                walk_left_two,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.2)
        class Player():
            def __init__(self, x, y, width, height):
                side_left,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

    def walk_right():
        class Player():
            def __init__(self, x, y, width, height):
                walk_right_one,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.2)
        class Player():
            def __init__(self, x, y, width, height):
                walk_right_two,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

        time.sleep(0.2)
        class Player():
            def __init__(self, x, y, width, height):
                side_right,
                self.x = x
                self.y = y
                self.width = width
                self.height = height

    #intro animation function

    def intro():
        intro = True
        intro_sprite = frame1
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame2
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite =frame3
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame4
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame5
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame6
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame7
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame8
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame9
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame10
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame11
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame12
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame13
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame14
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite =frame15
        screen.blit(intro_sprite)
        time.sleep(0.5)
        intro_sprite = frame16
        screen.blit(intro_sprite)
        time.sleep(3)
        screen.remove(intro_sprite)
        intro = False  

    #function that updates the level sprite

    def level_update():
        if level == 1:
            level_sprite = level_one
            screen.blit(level_sprite)
        #add as i add more level background to the game

    #calling functions for the game
    intro()
    collide()
    flower_collect()
    coin_change()
    flower_change()
    health_change()
    countdown()
    powerup_collect()
    box_hit()
    level_update()

    #bliting things that are always on screen

    screen.blit(health_sprite, x= 5, y = 50)
    screen.blit(hundreds_sprite, x=220, y=50)
    screen.blit(tens_sprite, x=230, y=50)
    screen.blit(ones_sprite, x=240, y=50)
    screen.blit(coin_one, x= 15, y=50)
    #add numbers for coin counter

    #functions that contain all of the info for each level
    
    def level_one():
        night_ambience_sound.play(-1)
        screen.blit(level_sprite)
        screen.blit(Player, x=5, y=10) 
        screen.blit(coin_sprite, x=10,y=10)
        screen.blit(flower_sprite, x= 30, y = 15)
        screen.blit(coin_sprite, x= 50, y = 10)
        screen.blit(cloud_platform, x =75, y = 15)
        screen.blit(storm_platform, x = 78, y= 20)
        screen.blit(box_one, x= 78, y= 23)
        screen.blit(flower_sprite, x = 78, y =30)
        screen.blit(coin_sprite, x= 95, y = 10)
        screen.blit(coin_sprite, x= 100, y = 15)
        screen.blit(coin_sprite, x= 105, y = 10)
        screen.blit(box_two, x = 120, y = 15)
        screen.blit(cloud_platform, x = 130, y = 20)
        screen.blit(box_one, x=130, y = 23)
        screen.blit(coin_sprite, x=130, y = 25)
        screen.blit(coin_sprite, x=170, y=12)
        screen.blit(coin_sprite, x=170, y=18)
        screen.blit(box_two, x=190, y=15)
        screen.blit(storm_platform, x=200,y=20)
        screen.blit(cloud_platform, x=190, y=30)
        screen.blit(flower_sprite, x=190, y=35)
        screen.blit(coin_sprite, x=220, y=10)
        screen.blit(coin_sprite, x=225, y=12)
        screen.blit(bus_stop, x= 240, y=10)
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    game()  