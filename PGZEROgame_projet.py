

###"" === JEUX DE NINJA JUMPER : LE BUT ES DAVOIR LE PLUS DE POINTS POSSIBLE POUR DECOUVRIR D'AUTRE MAP ET TOUT SA SANS TOUCHER LE SOL ===""###
###"" === CECI ES UN PROJET PERSONNEL DONC C'EST UNE SORTE DE DEMO VOILA POURQUOI IL NY A QUE DEUX MAP DANS LE JEUX===""###
##"" === LES MAPS CHANGE A CHAQUE 20 POINTS
###"" === CREATEUR: ange adou 11eme année a franco-cité === ""###

###"" === AMUSEZ VOUS BIEN ===""###


import pgzrun
import time
import pygame
import random
import sys

WIDTH = 1000
HEIGHT = 600
blue = 150
thegroundcolor = 0, 0, 139
floor = Rect((0, 580), (1000, 20))
ninja_x_vel = 0
ninja_y_vel = 0
gravity = 1
points = 0 
died = 0
playing = True
"les diamants et le ninja les actors"
diamond_x = [950, 50, 850, 150, 750, 250, 650, 350, 500]
diamond_y = [70, 70, 170, 170, 270, 270, 370, 370, 470]
d_xy = random.randint(0, 8)
gems = Actor('diamond_s', (diamond_x[d_xy], diamond_y[d_xy]))
mini_ninja = Actor('jumper-1', (500, 250))
all_var = [died,points,mini_ninja]
jumping = False
jumped = False
allow_x = True
timer = []
"les plateforms du jeux et les box pour recommencer le jeux"
platform_1 = Rect((450, 500), (100, 10))
platform_2 = Rect((300, 400), (100, 10))
platform_3 = Rect((600, 400), (100, 10))
platform_4 = Rect((200, 300), (100, 10))
platform_5 = Rect((700, 300), (100, 10))
platform_6 = Rect((100, 200), (100, 10))
plat61_x = 200
plat62_x = 700
platform61 = Rect((plat61_x, 200), (100, 10))
platform62 = Rect((plat62_x, 200), (100, 10))
platform_7 = Rect((800, 200), (100, 10))
platform_8 = Rect((0, 100), (100, 10))
platform_9 = Rect((900, 100), (100, 10))
all_platforms = [floor, platform_1, platform_2, platform_3, platform_4, platform_5, platform_6, platform_7, platform_8,
                 platform_9, platform61, platform62]
plat61_left = True
plat62_left = False
yes_box = Rect(165, 215, 190 ,140)
no_box = Rect(415,215,190,140)

#la musique du jeux

    
def game_loop():
    #la boucle initiale du jeux
    global platform61, patform62, all_platforms,gems,mini_ninja,points, thegroundcolor,points
    for elements in all_var:
        points = 0
        died = 0
        mini_ninja = Actor('jumper-1', (500, 250)) 
    screen.blit('decoration', (0, 0))
    platform61 = Rect((plat61_x, 200), (100, 10))
    platform62 = Rect((plat62_x, 200), (100, 10))
    all_platforms[10] = platform61
    all_platforms[11] = platform62
    for i in all_platforms:
        screen.draw.filled_rect(i, thegroundcolor)
    mini_ninja.draw()
    gems.draw()
    screen.draw.text("score", center=(50, 540), fontsize=40, shadow=(1, 1), color=("red"), scolor="#202020")
    screen.draw.text(str(points), center=(45, 570), fontsize=40, shadow=(1, 1), color=(255, 255, 255), scolor="#202020")

def draw():
    global platform61, patform62, all_platforms,gems,mini_ninja,points, thegroundcolor,points,died,points_2
    screen.blit('decoration', (0, 0))
    platform61 = Rect((plat61_x, 200), (100, 10))
    platform62 = Rect((plat62_x, 200), (100, 10))
    all_platforms[10] = platform61
    all_platforms[11] = platform62
    for i in all_platforms:
        screen.draw.filled_rect(i, thegroundcolor)
    mini_ninja.draw()
    gems.draw()
    screen.draw.text("score", center=(50, 540), fontsize=40, shadow=(1, 1), color=("red"), scolor="#202020")
    screen.draw.text(str(points), center=(45, 570), fontsize=40, shadow=(1, 1), color=(255, 255, 255), scolor="#202020")
    if game_over() and died < 120:
        #ce qui saffiche en premier quand il perds la partie
        game_over_screen()
        sounds.gameover_sound.play()
    elif game_over():
        #ce qui vient en deuxieme pour savoir si on rejoue ou pas
        screen.clear()
        replay_screen()
    elif points >=10:
        # afficher la deuxieme map
        playing = False
        level_2()
        died = 0
        
def update():
    #update pour bouger le ninja et les 2 plateforms bleu
    moving_platform()
    ninja_moves()
    
def level_2():
    #le niveau deux la deuxieme map du jeux
    global platform61, patform62, all_platforms,gems,mini_ninja,points, thegroundcolor
    screen.blit('level2', (0, 0))
    platform61 = Rect((plat61_x, 200), (100, 10))
    platform62 = Rect((plat62_x, 200), (100, 10))
    all_platforms[10] = platform61
    all_platforms[11] = platform62
    for i in all_platforms:
        screen.draw.filled_rect(i, thegroundcolor)
    mini_ninja.draw()
    gems.draw()
    screen.draw.text("score", center=(50, 540), fontsize=40, shadow=(1, 1), color=("red"), scolor="#202020")
    screen.draw.text(str(points), center=(45, 570), fontsize=40, shadow=(1, 1), color=(255, 255, 255), scolor="#202020")    
      
def ninja_moves():
    global ninja_x_vel, ninja_y_vel, jumping, gravity, jumped, allow_x, jumped, timer, points, d_xy

    # he is facing the front
    if ninja_y_vel == 0 and not jumped:
        mini_ninja.image = 'jumper-1'

    # thegravity
    if collision_check():
        gravity = 1
        mini_ninja.y -= 1
        allow_x = True
        timer = []
    if not collision_check():
        mini_ninja.y += gravity
        if gravity <= 20:
            gravity += 0.5
        timer.append(pygame.time.get_ticks())
        if len(timer) > 5 and not jumped:
            allow_x = False
            mini_ninja.image = 'jumper-up'
            if len(timer) > 20:
                mini_ninja.image = 'jumper-fall'
                if len(timer) > 20:
                    mini_ninja.image = 'jumper-fall'

    # mouvement gauche et droite
    if (keyboard.left) and allow_x:
        if (mini_ninja.x > 40) and (ninja_x_vel > -8):
            ninja_x_vel -= 2
            mini_ninja.image = "jumper-left"
            if (keyboard.left) and jumped:
                mini_ninja.image = "jumper-jleft"
    if (keyboard.right) and allow_x:
        if (mini_ninja.x < 960) and (ninja_x_vel < 8):
            ninja_x_vel += 2
            mini_ninja.image = "jumper-right"
            if (keyboard.right) and jumped:
                mini_ninja.image = "jumper-jright"
    mini_ninja.x += ninja_x_vel
    # velocité
    if ninja_x_vel > 0:
        ninja_x_vel -= 1
    if ninja_x_vel < 0:
        ninja_x_vel += 1
    if mini_ninja.x < 50 or mini_ninja.x > 950:
        ninja_x_vel = 0
    # mouvement de saut
    if  not game_over():
        if (keyboard.up) and collision_check() and not jumped:
            sounds.jump.play()
            jumping = True
            jumped = True
            clock.schedule_unique(jumpedrecently, 0.4)
            mini_ninja.image = "jumper-up"
            ninja_y_vel = 95
        if jumping and ninja_y_vel > 25:
            ninja_y_vel = ninja_y_vel - ((100 - ninja_y_vel) / 2)
            mini_ninja.y -= ninja_y_vel / 3
        else:
            ninja_y_vel = 0
            jumping = False

    #quand il touche les diamants, collecter les diamants"

    if mini_ninja.colliderect(gems):
        points += 2
        sounds.gem.play()
        old_d_xy = d_xy
        d_xy = random.randint(0, 8)
        while old_d_xy == d_xy:
            d_xy = random.randint(0, 8)
        gems.x = diamond_x[d_xy]
        gems.y = diamond_y[d_xy]


def moving_platform():
    #les  deux platforms qui bouge
    global plat61_x, plat62_x, plat61_left, plat62_left
    #===la platform gauche===
    if plat61_left:
        plat61_x += 2
        if plat61_x == 400:
            plat61_left = False
        if mini_ninja.colliderect(platform61):
            mini_ninja.x += 2
    else:
        plat61_x -= 2
        if plat61_x == 200:
            plat61_left = True
        if mini_ninja.colliderect(platform61):
            mini_ninja.x -= 2
    #==la plarform droite==
    if plat62_left:
        plat62_x += 2
        if plat62_x == 700:
            plat62_left = False
        if mini_ninja.colliderect(platform62):
            mini_ninja.x += 2
    else:
        plat62_x -= 2
        if plat62_x == 500:
            plat62_left = True
        if mini_ninja.colliderect(platform62):
            mini_ninja.x -= 2

def collision_check():
    #quand il collecte les diamants
    collide = False
    for i in all_platforms:
        if mini_ninja.colliderect(i):
            collide = True
    return collide
    
def jumpedrecently():
    global jumped
    jumped = False
    
def game_over():
    # ici on verifie si le joueur a perdu la partie
    gameover = False
    for elements in all_platforms:
        if mini_ninja.colliderect(floor):
            gameover = True
    return gameover

def game_over_screen():
    #ecran qui saffiche quand le joueur perds
    global died  
    screen.blit('g_o_s',(0,0))
    died += 1

def replay_screen():
    #ecran pour verifier si on recommence la partie ou non
    global no_box, yes_box, died
    screen.draw.text("DO YOU WANT TO PLAY AGAIN", (yes_box.x, yes_box.y - 50))
    screen.draw.filled_rect(yes_box, "green")
    screen.draw.textbox("YES", yes_box, color = "black")
    screen.draw.filled_rect(no_box, "red")
    screen.draw.textbox("NO", no_box, color = "black")

def on_mouse_down(pos):
    #verifier si on doit recommencer le jeu ou si on doit quitter le jeux en fonction du choix de joueur
    if yes_box.collidepoint(pos):
        #si le joueur clique sur la boite YES la viriable died revient a zero et on recommence le jeux
        died = 0
        game_loop()
    elif no_box.collidepoint(pos):
        #si le joueur clique sur la boite non on quitte directement le jeux
        sys.exit()
pgzrun.go()