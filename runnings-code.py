import pygame
import time
import random
import os

#WHAT TO CODE AFTER SHABBAT!
# PUT IN COIN SPRITE, ADDING COINS, DOING A COUNT, ADDING THE ANIMATION, ETC
#FIX THE FLOWER SPRITE. ADD A TIMER, ETC
#MAKE BLOCKS TO GET POWERUPS OUT OF AND ADD THE FILES FOR IT (ONCE I DRAW THEM)

# notes about game lore: a girl is running away from home (don't learn this until end of the game)
# and she's running to her aunt's house. if she runs out of time or takes too much damage play an animation of her parents catching her

# powerups (higher jumps) (maybe a little star!)

def game():
    pygame.init()

    #display!
    screen_width = 256
    screen_height = 128
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
    jump_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/jump_one.pxm")
    jump_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/jump_two.pxm")
    jump_three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/jump_three.pxm")
    coin_one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/coin_one.pxm")
    coin_two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/coin_two.pxm")
    #health_bar
    cloud_platform = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/cloud_platform.pxm")
    storm_platform =  pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/storm_platform.pxm")
    star_power = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/star_power.pxm")
    hourglass_power = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/hourglass_collected.pxm")
    zero = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/zero.pxm")
    one = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/one.pxm")
    two = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/two.pxm")
    three = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/three.pxm")
    four = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/four.pxm")
    five = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/five.pxm")
    six = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/six.pxm")
    seven = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/seven.pxm")
    eight = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/eight.pxm")
    nine = pygame.image.load("C:/Users/nilib/OneDrive/HackClub/MilkyWayProjects/MidnightPlatformer/nine.pxm")
    #make some sort of box for powerups to be in
    #something signifying the end of the level

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
    def countdown():
        for second in time:
            if second == 600:
                hundreds_sprite = pygame.image.TileGrid(
                    six,
                    pixel_shader = six.pixel_shader
                )
            elif second >= 500:
                hundreds_sprite = pygame.image.TileGrid(
                    five,
                    pixel_shader = five.pixel_shader
                )
            elif second >= 400:
                hundreds_sprite = pygame.image.TileGrid(
                    four,
                    pixel_shader = four.pixel_shader
                )
            elif second >= 300:
                 hundreds_sprite = pygame.image.TileGrid(
                    three,
                    pixel_shader = three.pixel_shader
                )
            elif second >= 200:
                hundreds_sprite = pygame.image.TileGrid(
                    two,
                    pixel_shader = two.pixel_shader
                )
            elif second >= 100:
                hundreds_sprite = pygame.image.TileGrid(
                    one,
                    pixel_shader = one.pixel_shader
                )
        #add tens here
        #add ones here
    def jumping():
        jump_sprite = pygame.image.TileGrid(
            jump_two,
            pixel_shader = jump_two.pixel_shader
        )
        pygame.event.wait()(.5)
        jump_sprite = pygame.image.TileGrid(
            jump_three,
            pixel_shader = jump_three.pixel_shader
        )
        pygame.event.wait()(.5)
        jump_sprite = pygame.image.TileGrid(
            jump_one,
            pixel_shader = jump_one.pixel_shader
        )


    def coin_change():
        for second in clock:
            coin_sprite = pygame.image.TileGrid(
                coin_two,
                pixel_shader = coin_two.pixel_shader
            )
            pygame.event.wait()(.5)
            coin_sprite = pygame.image.TileGrid(
                coin_one,
                pixel_shader = coin_one.pixel_shader
            )
    #adding those sprites as file thingies

    splash.append(level_sprite)
    splash.append(girl_sprite, x=10, y=20)
    splash.append(cloud_platform, x=50, y=80)
    splash.append(storm_platform, x=200, y=65)
    splash.append(flower_sprite, x= 200, y = 70)
    #add platforms and flowers and coins to splash once i decide where they go (DESIGN THE LEVEL)
    #it's agreed by me that there are 3 flowers per level


    #add some sounds here!
    #make them myself lol i aint hiring a real composer
    # pygame.mixer.Sound() RESEARCH THIS!!!

    
    #variables defined (for beginning)
    coin = 0
    flower = 0
    time = 300
    star = False
    hourglass = False
    health = 10

    #hitboxes defined

    girl_hitbox = pygame.Rect(girl_sprite.x, girl_sprite.y, girl_sprite.width, girl_sprite.height)
    flower_hitbox = pygame.Rect(flower_sprite.x, flower_sprite.y, flower_sprite.width, flower_sprite.height)
    cloud_hitbox = pygame.Rect(cloud_platform.x, cloud_platform.y, cloud_platform.width, cloud_platform.height)
    storm_hitbox = pygame.Rect(storm_platform.x, storm_platform.y, storm_platform.width, storm_platform.height)
    coin_hitbox =  pygame.Rect(coin_sprite.x, coin_sprite.y, coin_sprite.width, coin_sprite.height)
    star_hitbox = pygame.Rect(star_power.x, star_power.y, star_power.width, star_power.height)
    hourglass_hitbox = pygame.Rect(hourglass_power.x, hourglass_power.y, hourglass_power.width, hourglass_power.height)

    #functions for hitboxes
    def powerup_collect():
        if girl_hitbox.collideobjects(hourglass_hitbox) == True:
            hourglass = True
            pygame.event.wait()(10)
            hourglass = False
        if girl_hitbox.collideobjects(star_hitbox) == True:
            star = True
            pygame.event.wait()(10)
            star  = False
    def collide():
        if girl_hitbox.collideobjects(cloud_hitbox):
            girl_sprite.y == cloud_platform.y
        if girl_hitbox.collideobjects(storm_hitbox):
            girl_sprite.y == storm_platform.y
            for second in clock:
                health -= .5
    #collecting flower function, changing sprite and appending to screen
    def flower_collect():
        if girl_sprite.collideobjects(flower_hitbox) == True:
                flower += 1
                health += 2
                flower_sprite = pygame.image.TileGrid(
                    flower_collected,
                    pixel_shader= flower_collected.pixel_shader
                )
                pygame.event.wait()(.5)
                splash.remove(flower_sprite)
                flower_sprite = pygame.image.TileGrid(
                    flower_one,
                    pixel_shader = flower_one.pixel_shader
                )
                if flower == 1:
                    splash.append(flower_sprite, x=220, y=120)
                if flower == 2:
                    splash.append(flower_sprite, x = 230, y=120) and splash.append(flower_sprite, x=220, y=120)
                if flower == 3 :
                    splash.append(flower_sprite, x = 240, y=120) and splash.append(flower_sprite, x = 230, y=120) and splash.append(flower_sprite, x=220, y=120)
    def coin_collect():
        if girl_sprite.collideobjects(coin_hitbox) == True:
                coin += 1
                #add coin collecting sound and sprite here
                pygame.event.wait()(.5)
                splash.remove(coin_sprite)
                #update coin counter on screen
    #(intro is defined within the intro function)
    intro()
    collide()
    flower_collect()
    coin_change()
    # timer for level
    if intro == False:
        for second in clock:
            time -= 1
            if time <= 0:
                #maybe add a losing animation if time? (ofc there's time lol)
                pygame.quit()
        if health <= 0:
            #add losing animation with girl falling to the ground
            #blare out screen with sirens
            pygame.quit()
    keys = pygame.key.get_pressed()
    if pygame.event(keys[pygame.K_LEFT]) and hourglass == False and intro == False:
        walk_left()
        x -= 1     
    if pygame.event(keys[pygame.K_RIGHT]) and hourglass == False and intro == False:
       walk_right()
       x += 1
    if pygame.event(keys[pygame.K_LEFT]) and hourglass == True and intro == False:
        walk_left()
        x -= 3
        walk_left()
    if pygame.event(keys[pygame.K_RIGHT]) and hourglass == True and intro == False:
        walk_right()
        x += 3
        walk_right()
    if pygame.event(keys[pygame.K_UP]) and star == False and intro == False:
        jumping()
        y += 5
        pygame.event.wait(1)
        y -= 5
    if pygame.event(keys[pygame.K_UP]) and star == True and intro == False:
        jumping()        
        y += 10
        pygame.event.wait(1)
        y -= 10
    if pygame.event(keys[pygame.K_DOWN]) and intro == False:
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
    game()