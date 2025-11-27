import pygame
import time
import random
import os
import asyncio

# notes about game lore: a girl is running away from home (don't learn this until end of the game)
# and she's running to her aunt's house. if she runs out of time or takes too much damage play an animation of her parents catching her
# for final level, make coin requirement in order to win as the price to get the final bus ticket to escape

def game():

    #initializing pygame and sounds

    pygame.init()
    pygame.mixer.init()

    #setting  images and sounds

    #images
    
    frame1 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_one.pxm")
    frame2 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_two.pxm")
    frame3 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_three.pxm")
    frame4 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_four.pxm")
    frame5 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_five.pxm")
    frame6 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_six.pxm")
    frame7 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_seven.pxm")
    frame8 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_eight.pxm")
    frame9 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_nine.pxm")
    frame10 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_ten.pxm")
    frame11 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_eleven.pxm")
    frame12 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_twelve.pxm")
    frame13 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_thirteen.pxm")
    frame14 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_fourteen.pxm")
    frame15 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_fifteen.pxm")
    frame16 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/frame_sixteen.pxm")
    front_face = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/FrontFace.png")
    side_left = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/side_left.pxm")
    walk_left_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_left1.pxm")
    walk_left_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_left2.pxm")
    side_right = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/side_right.pxm")
    walk_right_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_right1.pxm")
    walk_right_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/walk_right2.pxm")
    flower_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_one.pxm")
    flower_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_two.pxm")
    flower_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/midnight_flower_three.pxm")
    flower_collected = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/Midnight_ flower_ collected.pxm")
    level_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/background.png")
    crouch_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/crouch_one.pxm")
    crouch_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/crouch_two.pxm")
    jump_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/jump_one.pxm")
    jump_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/jump_two.pxm")
    jump_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/jump_three.pxm")
    coin_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/coin_one.pxm")
    coin_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/coin_two.pxm")
    coin_collected = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/coin_collected.pxm")
    health_ten = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_ten.pxm")
    health_nine = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_nine.pxm")
    health_eight = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_eight.pxm")
    health_seven = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_seven.pxm")
    health_six = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_six.pxm")
    health_five = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_five.pxm")
    health_four = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_four.pxm")
    health_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_three.pxm")
    health_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_two.pxm")
    health_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_one.pxm")
    health_zero = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/health_zero.pxm")
    cloud_platform = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/cloud_platform.pxm")
    storm_platform =  pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/storm_platform.pxm")
    star_power = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/star_power.pxm")
    hourglass_power = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/hourglass_collected.pxm")
    zero = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/zero.pxm")
    one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/one.pxm")
    two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/two.pxm")
    three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/three.pxm")
    four = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/four.pxm")
    five = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/five.pxm")
    six = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/six.pxm")
    seven = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/seven.pxm")
    eight = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/eight.pxm")
    nine = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/nine.pxm")
    box_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/box_one.pxm")
    box_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/box_two.pxm")
    end_frame1 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/end_frame1.pxm")
    end_frame2 = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/end_frame2.pxm")
    bus_stop = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/bus_stop.pxm")

    #sounds

    heartbeat_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/595050__insaind__clean-deep-heartbeat.wav")
    sirens_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/577312__trp__sirens-fire-police-close-pass-distant-urban-calgary-2011.wav")
    whispers_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/182378__elizaeilis__whispers.mp3")
    night_ambience_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/195969__rgbrobot__night-ambience-01-aug-2-2013-back-yard.wav")
    flower_collect_sound = pygame.mixer.Sound("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sounds/413629__djlprojects__video-game-sfx-positive-action-long-tail.wav")
    
    #setting sprites for certain images to be changed

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
    coin_sprite = pygame.image.TileGrid(
        coin_one,
        pixel_shader = coin_one.pixel_shader
    )
    jump_sprite = pygame.image.TileGrid(
        jump_one,
        pixel_shader = jump_one.pixel_shader
    )
    ones_sprite = pygame.image.TileGrid(
        zero,
        pixel_shader = zero.pixel_shader
    )
    tens_sprite = pygame.image.TileGrid(
        zero,
        pixel_shader = zero.pixel_shader
    )
    hundreds_sprite = pygame.image.TileGrid(
        zero,
        pixel_shader = zero.pixel_shader
    )
    health_sprite = pygame.image.TileGrid(
        health_ten,
        pixel_shader = health_ten.pixel_shader
    )

    #display!

    screen_width = 256
    screen_height = 128
    splash = pygame.Group()
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

    #hitboxes defined

    girl_hitbox = pygame.Rect(girl_sprite.x, girl_sprite.y, girl_sprite.width, girl_sprite.height)
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
            splash.append(hourglass_power)
            time.sleep(10)
            hourglass = False
        if star == True:
            splash.append(star_power)
            time.sleep(10)
            star  = False
    def collide():
        if girl_hitbox.colliderect(cloud_hitbox):
            girl_sprite.y = cloud_platform.y
        if girl_hitbox.colliderect(storm_hitbox):
            girl_sprite.y = storm_platform.y
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
                    tens_sprite = pygame.image.TileGrid(
                        zero,
                        pixel_shader = zero.pixel_shader
                    )
                elif tens == 2:
                    tens_sprite = pygame.image.TileGrid(
                        nine,
                        pixel_shader = nine.pixel_shader
                    )
                elif tens == 3:
                    tens_sprite = pygame.image.TileGrid(
                        eight,
                        pixel_shader = eight.pixel_shader
                    )
                elif tens == 4:
                    tens_sprite = pygame.image.TileGrid(
                        seven,
                        pixel_shader = seven.pixel_shader
                    )
                elif tens == 5:
                    tens_sprite = pygame.image.TileGrid(
                        six,
                        pixel_shader = six.pixel_shader
                    )
                elif tens == 6:
                    tens_sprite = pygame.image.TileGrid(
                        five,
                        pixel_shader = five.pixel_shader
                    )
                elif tens == 7:
                    tens_sprite = pygame.image.TileGrid(
                        four,
                        pixel_shader = four.pixel_shader
                    )
                elif tens == 8:
                    tens_sprite = pygame.image.TileGrid(
                        three,
                        pixel_shader = three.pixel_shader
                    )
                elif tens == 9:
                    tens_sprite = pygame.image.TileGrid(
                        two,
                        pixel_shader = two.pixel_shader
                    )
                elif tens == 10:
                    tens_sprite = pygame.image.TileGrid(
                        one,
                        pixel_shader = one.pixel_shader
                    )
                else:
                    tens = 0
                    tens_change()

    #setting the sprite for the one place on the timer

    def ones_change():
            for second in time:
                ones += 1
                if ones == 1:
                    ones_sprite = pygame.image.TileGrid(
                       one,
                       pixel_shader = one.pixel_shader 
                    )
                elif ones == 2:
                    ones_sprite = pygame.image.TileGrid(
                        two,
                        pixel_shader = two.pixel_shader
                    )
                elif ones == 3:
                    ones_sprite = pygame.image.TileGrid(
                        three,
                        pixel_shader = three.pixel_shader
                    )
                elif ones == 4:
                    ones_sprite = pygame.image.TileGrid(
                       four,
                       pixel_shader = four.pixel_shader 
                    )
                elif ones == 5:
                    ones_sprite = pygame.image.TileGrid(
                        five,
                        pixel_shader = five.pixel_shader
                    )
                elif ones == 6:
                    ones_sprite = pygame.image.TileGrid(
                        six,
                        pixel_shader = six.pixel_shader
                    )
                elif ones == 7:
                    ones_sprite = pygame.image.TileGrid(
                        seven,
                        pixel_shader = seven.pixel_shader
                    )
                elif ones == 8:
                    ones_sprite = pygame.image.TileGrid(
                        eight,
                        pixel_shader = eight.pixel_shader
                    )
                elif ones == 9:
                    ones_sprite = pygame.image.TileGrid(
                        nine,
                        pixel_shader = nine.pixel_shader
                    )
                elif ones == 10:
                    ones_sprite = pygame.image.TileGrid(
                        zero,
                        pixel_shader = zero.pixel_shader
                    )
                else:
                    ones = 0
                    ones_change()

    #setting the full timer with the previous functions in it

    def countdown():
            for second in time:
                if second >= 300:
                    hundreds_sprite = pygame.image.TileGrid(
                        three,
                        pixel_shader = three.pixel_shader
                    )
                    tens_change()
                    ones_change()
                elif second >= 200:
                    hundreds_sprite = pygame.image.TileGrid(
                        two,
                        pixel_shader = two.pixel_shader
                    )
                    tens_change()
                    ones_change()
                elif second >= 100:
                    hundreds_sprite = pygame.image.TileGrid(
                        one,
                        pixel_shader = one.pixel_shader
                    )
                    tens_change()
                    ones_change()

                else:
                    hundreds_sprite = pygame.image.TileGrid(
                        zero,
                        pixel_shader = zero.pixel_shader
                    )
                    tens_change()
                    ones_change()
    
    #function for animating when the main character jumps

    def jumping():
        jump_sprite = pygame.image.TileGrid(
            jump_two,
            pixel_shader = jump_two.pixel_shader
        )
        time.sleep(0.5)
        jump_sprite = pygame.image.TileGrid(
            jump_three,
            pixel_shader = jump_three.pixel_shader
        )
        time.sleep(0.5)
        jump_sprite = pygame.image.TileGrid(
            jump_one,
            pixel_shader = jump_one.pixel_shader
        )

    #makes the flower sprite change on screen

    def flower_change():
        flower_sprite = pygame.image.TileGrid(
            flower_two,
            pixel_shader = flower_two.pixel_shader
        )
        time.sleep(0.5)
        flower_sprite = pygame.image.TileGrid(
            flower_three,
            pixel_shader = flower_three.pixel_shader
        )
        time.sleep(0.5)
        flower_sprite = pygame.image.TileGrid(
            flower_one,
            pixel_shader = flower_one.pixel_shader
        )
        time.sleep(0.5)
        flower_change()

    #makes the coin sprite change on screen

    def coin_change():
        coin_sprite = pygame.image.TileGrid(
            coin_two,
            pixel_shader = coin_two.pixel_shader
        )
        time.sleep(0.5)
        coin_sprite = pygame.image.TileGrid(
            coin_one,
            pixel_shader = coin_one.pixel_shader
        )
        time.sleep(0.5)
        coin_change()
    

    
    #collecting flower function, adding it to the flower counter on screen

    def flower_collect():
        if girl_hitbox.colliderect(flower_hitbox) == True:
                flower_collect_sound.play()
                flower += 1
                health += 2
                flower_sprite = pygame.image.TileGrid(
                    flower_collected,
                    pixel_shader= flower_collected.pixel_shader
                )
                time.sleep(0.5)
                splash.remove(flower_sprite)
                flower_sprite = pygame.image.TileGrid(
                    flower_one,
                    pixel_shader = flower_one.pixel_shader
                )
                if flower == 1:
                    splash.append(flower_sprite)
                    flower_sprite.x = 220
                    flower_sprite.y = 120
                if flower == 2:
                    splash.append(flower_sprite)
                    flower_sprite.x = 230
                    flower_sprite.y = 120
                if flower == 3:
                    splash.append(flower_sprite)
                    flower_sprite.x = 240
                    flower_sprite.y = 120

    #collecting coin function, adding to coin counter (tbd)

    def coin_collect():
        if girl_hitbox.colliderect(coin_hitbox) == True:
                coin += 1
                coin_sprite = pygame.image.TileGrid(
                    coin_collected,
                    pixel_shader = coin_collected.pixel_shader
                )
                time.sleep(0.5)
                splash.remove(coin_sprite)
                #update coin counter on screen
    
    #changing health sprite based on health variable

    def health_change():
        if health == 10:
            health_sprite = pygame.image.TileGrid(
                health_ten,
                pixel_shader = health_ten.pixel_shader
            )
        elif health == 9:
            health_sprite = pygame.image.TileGrid(
                health_nine,
                pixel_shader = health_nine.pixel_shader
            )
        elif health == 8:
            health_sprite = pygame.image.TileGrid(
                health_eight,
                pixel_shader = health_eight.pixel_shader
            )
        elif health == 7:
            health_sprite = pygame.image.TileGrid(
                health_seven,
                pixel_shader = health_seven.pixel_shader
            )
        elif health == 6:
            health_sprite = pygame.image.TileGrid(
                health_six,
                pixel_shader = health_six.pixel_shader
            )
        elif health == 5:
            health_sprite = pygame.image.TileGrid(
                health_five,
                pixel_shader = health_five.pixel_shader
            )
        elif health == 4:
            health_sprite = pygame.image.TileGrid(
                health_four,
                pixel_shader = health_four.pixel_shader
            )
        elif health == 3:
            health_sprite = pygame.image.TileGrid(
                health_three,
                pixel_shader = health_three.pixel_shader
            )
        elif health == 2:
            health_sprite = pygame.image.TileGrid(
                health_two,
                pixel_shader = health_two.pixel_shader
            )
        elif health == 1:
            heartbeat_sound.play(-1)
            health_sprite = pygame.image.TileGrid(
                health_one,
                pixel_shader = health_one.pixel_shader
            )
        elif health <= 0:
            
            health_sprite = pygame.image.TileGrid(
                health_zero,
                pixel_shader = health_zero.pixel_shader
            )
            
    #function for ending the game

    def game_end():
        sirens_sound.play(-1)
        whispers_sound.play(-1)
        end_sprite = pygame.image.TileGrid(
            end_frame1,
            pixel_shader = end_frame1.pixel_shader
        )
        splash.append(end_sprite)
        time.sleep(0.2)
        end_sprite = pygame.image.TileGrid(
            end_frame2,
            pixel_shader = end_frame2.pixel_shader
        )
        splash.append(end_sprite)
        time.sleep(0.2)
        end_sprite = pygame.image.TileGrid(
            end_frame1,
            pixel_shader = end_frame1.pixel_shader
        )
        splash.append(end_sprite)
        time.sleep(0.2)
        end_sprite = pygame.image.TileGrid(
            end_frame2,
            pixel_shader = end_frame2.pixel_shader
        )
        splash.append(end_sprite)
        time.sleep(6)

    # timer for level

    if intro == False:
        time_remaining = 300
        time_start = time.time()
        while time_remaining > 0:
            time_remaining = 300 - int(time.time() - time_start)
            if time_remaining <= 0:
                    game_end()
                    pygame.quit()
        if health <= 0:
            game_end()
            pygame.quit()
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
        girl_sprite = pygame.image.TileGrid(
            crouch_one,
            pixel_shader = crouch_one.pixel_shader
        )
        time.sleep(0.3)
        girl_sprite = pygame.image.TileGrid(
            crouch_two,
            pixel_shader = crouch_two.pixel_shader
        )
        time.sleep(0.3)
        girl_sprite = pygame.image.TileGrid(
            front_face,
            pixel_shader = front_face.pixel_shader
        )

    #walking animation functions

    def walk_left():
        girl_sprite = pygame.image.TileGrid(
            walk_left_one,
            pixel_shader = walk_left_one.pixel_shader
        )
        time.sleep(0.2)
        girl_sprite = pygame.image.TileGrid(
            walk_left_two,
            pixel_shader = walk_left_two.pixel_shader
        )
        time.sleep(0.2)
        girl_sprite = pygame.image.TileGrid(
            side_left,
            pixel_shader = side_left.pixel_shader
        )
    def walk_right():
        girl_sprite = pygame.image.TileGrid(
            walk_right_one,
            pixel_shader = walk_right_one.pixel_shader
        )
        time.sleep(0.2)
        girl_sprite = pygame.image.TileGrid(
            walk_right_two,
            pixel_shader = walk_right_two.pixel_shader
        )
        time.sleep(0.2)
        girl_sprite = pygame.image.TileGrid(
            side_right,
            pixel_shader = side_right.pixel_shader
        )

    #intro animation function

    def intro():
        intro = True
        intro_sprite = pygame.image.TileGrid(
            frame1,
            pixel_shader = frame1.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame2,
            pixel_shader = frame2.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame3,
            pixel_shader = frame3.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame4,
            pixel_shader = frame4.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame5,
            pixel_shader = frame5.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame6,
            pixel_shader = frame6.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame7,
            pixel_shader = frame7.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame8,
            pixel_shader = frame8.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame8,
            pixel_shader = frame8.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame9,
            pixel_shader = frame9.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame10,
            pixel_shader = frame10.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame11,
            pixel_shader = frame11.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame12,
            pixel_shader = frame12.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame13,
            pixel_shader = frame13.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame14,
            pixel_shader = frame14.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame15,
            pixel_shader = frame15.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(0.5)
        intro_sprite = pygame.image.TileGrid(
            frame16,
            pixel_shader = frame16.pixel_shader
        )
        splash.append(intro_sprite)
        time.sleep(3)
        splash.remove(intro_sprite)
        intro = False  

    #function that updates the level sprite

    def level_update():
        if level == 1:
            level_sprite = pygame.image.TileGrid(
                level_one,
                pixel_shader = level_one.pixel_shader
            )
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

    #appending things that are always on screen

    splash.append(health_sprite, x= 5, y = 50)
    splash.append(hundreds_sprite, x=220, y=50)
    splash.append(tens_sprite, x=230, y=50)
    splash.append(ones_sprite, x=240, y=50)
    splash.append(coin_one, x= 15, y=50)
    #add numbers for coin counter

    #functions that contain all of the info for each level
    
    def level_one():
        night_ambience_sound.play(-1)
        splash.append(level_sprite)
        splash.append(girl_sprite, x=5, y=10) 
        splash.append(coin_sprite, x=10,y=10)
        splash.append(flower_sprite, x= 30, y = 15)
        splash.append(coin_sprite, x= 50, y = 10)
        splash.append(cloud_platform, x =75, y = 15)
        splash.append(storm_platform, x = 78, y= 20)
        splash.append(box_one, x= 78, y= 23)
        splash.append(flower_sprite, x = 78, y =30)
        splash.append(coin_sprite, x= 95, y = 10)
        splash.append(coin_sprite, x= 100, y = 15)
        splash.append(coin_sprite, x= 105, y = 10)
        splash.append(box_two, x = 120, y = 15)
        splash.append(cloud_platform, x = 130, y = 20)
        splash.append(box_one, x=130, y = 23)
        splash.append(coin_sprite, x=130, y = 25)
        splash.append(coin_sprite, x=170, y=12)
        splash.append(coin_sprite, x=170, y=18)
        splash.append(box_two, x=190, y=15)
        splash.append(storm_platform, x=200,y=20)
        splash.append(cloud_platform, x=190, y=30)
        splash.append(flower_sprite, x=190, y=35)
        splash.append(coin_sprite, x=220, y=10)
        splash.append(coin_sprite, x=225, y=12)
        splash.append(bus_stop, x= 240, y=10)

game()