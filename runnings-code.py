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
level_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/runnings-sprites/level_two.png")
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
#note to add more sounds once i have the time!!! (maybe do during english class bc what else should i do lol)
    
    #setting class sprites for certain images to be changed

girl_sprite = front_face
walk_left_frames = [side_left, walk_left_one, walk_left_two]
walk_right_frames = [side_right, walk_right_one, walk_right_two]
jump_frames = [jump_one, jump_two, jump_three]
crouch_frames = [crouch_one, crouch_two]
flower_frames = [flower_one, flower_two, flower_three, flower_collected]
coin_frames = [coin_one, coin_two, coin_collected]
intro_frames = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8, frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16]
level_frames = [level_one, level_two]
number_frames = [zero, one, two, three, four, five, six, seven, eight, nine]
health_frames = [health_ten, health_nine, health_eight, health_seven, health_six, health_five, health_four, health_three, health_two, health_one, health_zero]


level_sprite = level_frames[0]
flower_sprite = flower_frames[0]
coin_sprite = coin_frames[0]
jump_sprite = jump_frames
health_sprite = health_frames[0]

    #display!

screen_width = 512
screen_height = 128
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

    #initializing main variables

coin = 0
flower = 0
time_remaining = 300
star = False
hourglass = False
health = 10
tens = 0
ones = 0
level = 1
run = True
intro_active = True

def game():
    
    #hitboxes defined

    girl_hitbox =girl_sprite.get_rect()
    flower_hitbox = flower_sprite.get_rect()
    cloud_hitbox =cloud_platform.get_rect()
    storm_hitbox = storm_platform.get_rect()
    coin_hitbox =  coin_sprite.get_rect()
    box_one_hitbox =box_one.get_rect()
    box_two_hitbox = box_two.get_rect()
    bus_stop_hitbox = bus_stop.get_rect()
    #defining functions that use hitboxes

    def powerup_collect():
        if hourglass == True:
            screen.blit(hourglass_power)
            time.sleep(1)
            screen.remove(hourglass_power)
            time.sleep(10)
            hourglass = False
        if star == True:
            screen.blit(star_power)
            time.sleep(1)
            screen.remove(star_power)
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
                    screen.blit()
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
                    screen.blit(number_frames[1])
                elif ones == 2:
                    screen.blit(number_frames[2])
                elif ones == 3:
                    screen.blit(number_frames[3])
                elif ones == 4:
                    screen.blit(number_frames[4])
                elif ones == 5:
                    screen.blit(number_frames[5])
                elif ones == 6:
                    screen.blit(number_frames[6])
                elif ones == 7:
                    screen.blit(number_frames[7])
                elif ones == 8:
                    screen.blit(number_frames[8])
                elif ones == 9:
                    screen.blit(number_frames[9])
                elif ones == 10:
                    screen.blit(number_frames[0])
                else:
                    ones = 0
                    ones_change()

    #setting the full timer with the previous functions in it

    def countdown():
            for second in time:
                if second >= 300:
                    screen.blit(number_frames[3])
                    tens_change()
                    ones_change()
                elif second >= 200:
                    screen.blit(number_frames[2])
                    tens_change()
                    ones_change()
                elif second >= 100:
                    screen.blit(number_frames[1])
                    tens_change()
                    ones_change()

                else:
                    screen.blit(number_frames[0])
                    tens_change()
                    ones_change()
    
    #function for animating when the main character jumps

    def jumping():
        # JUMP 1
        time.sleep(0.5)
        #JUMP 2

        time.sleep(0.5)
       #JUMP 3

    #makes the flower sprite change on screen

    def flower_change():
        screen.blit(flower_one (0,0)) #fix coords please !!!
        time.sleep(0.5)
        flower_sprite = flower_three
        time.sleep(0.5)
        flower_sprite = flower_one
        time.sleep(0.5)

    #makes the coin sprite change on screen

    def coin_change():
        coin_sprite = coin_two
        time.sleep(0.5)
        coin_sprite = coin_one
        time.sleep(0.5)
    

    
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

    if intro_active == False:
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
    if keys[pygame.K_LEFT] and hourglass == False and intro_active == False:
        walk_left()
        x -= 1     
    if keys[pygame.K_RIGHT] and hourglass == False and intro_active == False:
       walk_right()
       x += 1
    if keys[pygame.K_LEFT] and hourglass == True and intro_active == False:
        walk_left()
        x -= 3
        walk_left()
    if keys[pygame.K_RIGHT] and hourglass == True and intro_active == False:
        walk_right()
        x += 3
        walk_right()
    if keys[pygame.K_UP] and star == False and intro_active == False:
        jumping()
        y += 5
        time.sleep(1)
        y -= 5
    if keys[pygame.K_UP] and star == True and intro_active == False:
        jumping()        
        y += 10
        time.sleep(1)
        y -= 10
    if keys[pygame.K_DOWN] and intro_active == False:
       

        time.sleep(0.3)
        

        time.sleep(0.3)
        

    #walking animation functions

    def walk_left():
        
        time.sleep(0.2)
        

        time.sleep(0.2)
      
    def walk_right():
       
        time.sleep(0.2)

           
        time.sleep(0.2)
       

    #intro animation function


    def intro():
        intro_active = True
        screen.blit(intro_frames[0], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[1], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[2], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[3], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[4], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[5], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[6], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[7], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[8], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[9], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[10], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[11], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[12], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[13], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[14], (0, 0))
        time.sleep(0.5)
        screen.blit(intro_frames[15], (0, 0))
        time.sleep(3)
        intro_active = False  

    #function that updates the level sprite

    def level_update():
        if level == 1:
            level_sprite = level_one
            screen.blit(level_sprite)
        elif level == 2:
            level_sprite = level_two
            screen.blit(level_sprite)
        #add as i add more level background to the game

    #functions that contain all of the info for each level
    
    def level_one():
        night_ambience_sound.play(-1)
        screen.blit(level_sprite, (0, 0))
        screen.blit(girl_sprite, (5, 10))
        screen.blit(coin_sprite, (10, 10))
        screen.blit(flower_sprite, (30, 15))
        screen.blit(coin_sprite, (50, 10))
        screen.blit(cloud_platform, (75, 15))
        screen.blit(storm_platform, (78, 20))
        screen.blit(box_one, (78, 23))
        screen.blit(flower_sprite, (78, 30))
        screen.blit(coin_sprite, (95, 10))
        screen.blit(coin_sprite, (100, 15))
        screen.blit(coin_sprite, (105, 10))
        screen.blit(box_two, (120, 15))
        screen.blit(cloud_platform, (130, 20))
        screen.blit(box_one, (130, 23))
        screen.blit(coin_sprite, (130, 25))
        screen.blit(coin_sprite, (170, 12))
        screen.blit(coin_sprite, (170, 18))
        screen.blit(box_two, (190, 15))
        screen.blit(storm_platform, (200, 20))
        screen.blit(cloud_platform, (190, 30))
        screen.blit(flower_sprite, (190, 35))
        screen.blit(coin_sprite, (220, 10))
        screen.blit(coin_sprite, (225, 12))
        screen.blit(bus_stop, (240, 10))

    #calling functions for the game
    intro()

    while run == True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        # Clear screen
        screen.fill((0, 0, 0))
        
        # Update game logic each frame
        collide()
        flower_collect()
        coin_change()
        flower_change()
        health_change()
        countdown()
        powerup_collect()
        box_hit()
        
        # Render the current level
        if level == 1:
            level_one()
        
        # Always-on-screen UI
        screen.blit(health_sprite, (5, 50))
        screen.blit(number_frames[0], (220, 50))
        screen.blit(number_frames[0], (230, 50))
        screen.blit(number_frames[3], (240, 50))
        screen.blit(coin_one, (15, 50))
        
        # Update display
        pygame.display.flip()

game()
pygame.quit()
