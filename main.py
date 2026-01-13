#pgzero
import time
import random

cell = Actor('Pustka')
cell1 = Actor('Ściana')
cell2 = Actor("Podłoga")
cell3 = Actor("Schody")
cell4 = Actor('Schody 1')
cell5 = Actor('Długie Schody')
cell6 = Actor("Długie schody 1")
cell7 = Actor("Boxy")
cell8 = Actor('Drewno')
cell9 = Actor('Ławka')
cell10 = Actor("Okno")
cell11 = Actor("Okno 1")
cell12 = Actor('A')
cell13 = Actor('B')
cell14 = Actor('Van')
bullets = []

size_w = 32 # Szerokość pola w komórkach
size_h = 25 # Wysokość pola w komórkach

WIDTH = cell.width * size_w
HEIGHT = cell.height * size_h

TITLE = "Pixel-Strike 2D"
FPS = 30

mode = 'menu'

my_map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 14, 2, 1, 11, 1, 11, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 2, 2, 2, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 2, 7, 4, 4, 2, 2, 2, 1, 0, 0],
          [0, 1, 2, 2, 9, 2, 2, 13, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0],
          [0, 1, 2, 2, 2, 2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2, 1, 1, 1, 1, 2, 5, 1, 0, 0],
          [0, 0, 1, 1, 1, 2, 1, 2, 1, 1, 2, 7, 1, 1, 7, 2, 1, 0, 0, 0, 1, 5, 5, 1, 0, 0, 1, 2, 5, 1, 0, 0],
          [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 5, 5, 1, 0, 0, 1, 2, 2, 2, 1, 0],
          [0, 0, 0, 0, 1, 2, 1, 1, 1, 11, 1, 1, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 1, 2, 2, 2, 1, 0],
          [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 7, 1, 2, 10, 2, 2, 2, 6, 6, 6, 6, 7, 2, 1, 0, 0, 1, 2, 2, 2, 1, 0],
          [0, 0, 0, 0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 10, 2, 2, 2, 6, 6, 6, 6, 7, 2, 1, 0, 0, 1, 5, 2, 2, 1, 0],
          [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 1, 2, 2, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 2, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1, 5, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 5, 2, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 2, 2, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 1, 2, 2, 2, 2, 2, 3, 1, 7, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 2, 2, 2, 2, 2, 7, 2, 7, 2, 2, 1, 6, 2, 2, 1, 1, 1, 1, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 1, 6, 6, 2, 1, 2, 1, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 1, 0],
          [0, 0, 0, 0, 0, 0, 1, 6, 6, 2, 2, 1, 1, 2, 2, 7, 7, 2, 7, 2, 8, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0, 0, 1, 6, 6, 2, 2, 1, 1, 2, 2, 7, 12, 2, 2, 2, 8, 1, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 7, 2, 1, 2, 1, 2, 2, 1, 2, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 7, 2, 1, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

TT = Actor('Terrorysta.stand', (712.5, 287.5))
TT.health = 100
TT.attack = 18

go = Actor('Go', (400, 100))
win = Actor('Win2', (400, 200))
lose = Actor('Lose2', (400, 200))

# Dodajemy zmienną globalną do przechowywania kierunku gracza
player_direction = 'r' # Domyślny kierunek, np. w prawo

def map_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map[0])):
            if my_map[i][j] == 0:
                cell.left = cell.width*j
                cell.top = cell.height*i
                cell.draw()

            elif my_map[i][j] == 1:
                cell1.left = cell1.width*j
                cell1.top = cell1.height*i
                cell1.draw()

            elif my_map[i][j] == 2:
                cell2.left = cell2.width*j
                cell2.top = cell2.height*i
                cell2.draw()

            elif my_map[i][j] == 3:
                cell3.left = cell3.width*j
                cell3.top = cell3.height*i
                cell3.draw()

            elif my_map[i][j] == 4:
                cell4.left = cell1.width*j
                cell4.top = cell1.height*i
                cell4.draw()

            elif my_map[i][j] == 5:
                cell5.left = cell2.width*j
                cell5.top = cell2.height*i
                cell5.draw()

            elif my_map[i][j] == 6:
                cell6.left = cell3.width*j
                cell6.top = cell3.height*i
                cell6.draw()

            elif my_map[i][j] == 7:
                cell7.left = cell1.width*j
                cell7.top = cell1.height*i
                cell7.draw()

            elif my_map[i][j] == 8:
                cell8.left = cell2.width*j
                cell8.top = cell2.height*i
                cell8.draw()

            elif my_map[i][j] == 9:
                cell9.left = cell3.width*j
                cell9.top = cell3.height*i
                cell9.draw()

            elif my_map[i][j] == 10:
                cell10.left = cell1.width*j
                cell10.top = cell1.height*i
                cell10.draw()

            elif my_map[i][j] == 11:
                cell11.left = cell2.width*j
                cell11.top = cell2.height*i
                cell11.draw()

            elif my_map[i][j] == 12:
                cell12.left = cell3.width*j
                cell12.top = cell3.height*i
                cell12.draw()

            elif my_map[i][j] == 13:
                cell13.left = cell3.width*j
                cell13.top = cell3.height*i
                cell13.draw()

            elif my_map[i][j] == 14:
                cell14.left = cell3.width*j
                cell14.top = cell3.height*i
                cell14.draw()

enemy_type = random.randint(1, 5)

CT_1 = Actor('Anty-terrorysta.r', (8 * cell.width - 12, 20 * cell.height - 12))
CT_2 = Actor('Anty-terrorysta.r', (14 * cell.width - 12, 19 * cell.height - 12))
CT_3 = Actor('Anty-terrorysta.r', (6 * cell.width - 12, 3 * cell.height - 12))
CT_4 = Actor('Anty-terrorysta.r', (4 * cell.width - 12, 7 * cell.height - 12))
CT_5 = Actor('Anty-terrorysta.r', (13 * cell.width - 12, 13 * cell.height - 12))
enemies_1 = [CT_1, CT_2, CT_3, CT_4, CT_5]

CT_6 = Actor('Anty-terrorysta.r', (13 * cell.width - 12, 22 * cell.height - 12))
CT_7 = Actor('Anty-terrorysta.r', (21 * cell.width - 12, 23 * cell.height - 12))
CT_8 = Actor('Anty-terrorysta.r', (16 * cell.width - 12, 11 * cell.height - 12))
CT_9 = Actor('Anty-terrorysta.d', (10 * cell.width - 12, 14 * cell.height - 12))
CT_10 = Actor('Anty-terrorysta.r', (20 * cell.width - 12, 3 * cell.height - 12))
enemies_2 = [CT_6, CT_7, CT_8, CT_9, CT_10]

CT_11 = Actor('Anty-terrorysta.u', (23 * cell.width - 12, 13 * cell.height - 12))
CT_12 = Actor('Anty-terrorysta.l', (12 * cell.width - 12, 10 * cell.height - 12))
CT_13 = Actor('Anty-terrorysta.r', (19 * cell.width - 12, 17 * cell.height - 12))
CT_14 = Actor('Anty-terrorysta.d', (14 * cell.width - 12, 4 * cell.height - 12))
CT_15 = Actor('Anty-terrorysta.r', (12 * cell.width - 12, 18 * cell.height - 12))
enemies_3 = [CT_11, CT_12, CT_13, CT_14, CT_15]

CT_16 = Actor('Anty-terrorysta.r', (21 * cell.width - 12, 7 * cell.height - 12))
CT_17 = Actor('Anty-terrorysta.u', (26 * cell.width - 12, 20 * cell.height - 12))
CT_18 = Actor('Anty-terrorysta.d', (25 * cell.width - 12, 5 * cell.height - 12))
CT_19 = Actor('Anty-terrorysta.l', (9 * cell.width - 12, 8 * cell.height - 12))
CT_20 = Actor('Anty-terrorysta.r', (18 * cell.width - 12, 23 * cell.height - 12))
enemies_4 = [CT_16, CT_17, CT_18, CT_19, CT_20]

CT_21 = Actor('Anty-terrorysta.r', (17 * cell.width - 12, 5 * cell.height - 12))
CT_22 = Actor('Anty-terrorysta.r', (29 * cell.width - 12, 19 * cell.height - 12))
CT_23 = Actor('Anty-terrorysta.l', (30 * cell.width - 12, 7 * cell.height - 12))
CT_24 = Actor('Anty-terrorysta.l', (13 * cell.width - 12, 14 * cell.height - 12))
CT_25 = Actor('Anty-terrorysta.r', (17 * cell.width - 12, 21 * cell.height - 12))
enemies_5 = [CT_21, CT_22, CT_23, CT_24, CT_25]

def draw():
    global mode
    global enemy_type
    if mode == 'menu':
        map_draw()
        go.draw()
        
    if mode == 'game':
        map_draw()
        TT.draw()
        if enemy_type == 1:
            for i in range(len(enemies_1)):
                enemies_1[i].draw()
        if enemy_type == 2:
            for i in range(len(enemies_2)):
                enemies_2[i].draw()
        if enemy_type == 3:
            for i in range(len(enemies_3)):
                enemies_3[i].draw()
        if enemy_type == 4:
           for i in range(len(enemies_4)):
                   enemies_4[i].draw()
        if enemy_type == 5:
            for i in range(len(enemies_5)):
                enemies_5[i].draw()
        
        for bullet in bullets:
            bullet.draw()
    if mode == 'win':
        map_draw()
        win.draw()
    if mode == 'lose':
        map_draw()
        lose.draw()

def pociski_u():
    global bullets
    new_bullets = []
    for bullet in bullets:
        if bullet.direction == 'u':
            bullet.y -= 10
        elif bullet.direction == 'd':
            bullet.y += 10
        elif bullet.direction == 'l':
            bullet.x -= 10
        elif bullet.direction == 'r':
            bullet.x += 10
        
        if 0 <= bullet.x <= WIDTH and 0 <= bullet.y <= HEIGHT:
            new_bullets.append(bullet)
    bullets = new_bullets

def collisions():
    global mode
    global enemy_type
    if enemy_type == 1:
        for i in range(len(enemies_1) -1, -1, -1):
            if TT.colliderect(enemies_1[i]):
                mode = 'lose'
            for j in range(len(bullets) -1, -1, -1):
                if bullets[j].colliderect(enemies_1[i]):
                    enemies_1.pop(i)
                    bullets.pop(j)
                    break
        if len(enemies_1) == 0:
            mode = 'win'
            
    if enemy_type == 2:
        for i in range(len(enemies_2) -1, -1, -1):
            if TT.colliderect(enemies_2[i]):
                mode = 'lose'
            for j in range(len(bullets) -1, -1, -1):
                if bullets[j].colliderect(enemies_2[i]):
                    enemies_2.pop(i)
                    bullets.pop(j)
                    break
        if len(enemies_2) == 0:
            mode = 'win'
            
    if enemy_type == 3:
        for i in range(len(enemies_3) -1, -1, -1):
            if TT.colliderect(enemies_3[i]):
                mode = 'lose'
            for j in range(len(bullets) -1, -1, -1):
                if bullets[j].colliderect(enemies_3[i]):
                    enemies_3.pop(i)
                    bullets.pop(j)
                    break
        if len(enemies_3) == 0:
            mode = 'win'
            
    if enemy_type == 4:
        for i in range(len(enemies_4) -1, -1, -1):
            if TT.colliderect(enemies_4[i]):
                mode = 'lose'
            for j in range(len(bullets) -1, -1, -1):
                if bullets[j].colliderect(enemies_4[i]):
                    enemies_4.pop(i)
                    bullets.pop(j)
                    break
        if len(enemies_4) == 0:
            mode = 'win'
            
    if enemy_type == 5:
        for i in range(len(enemies_5) -1, -1, -1):
            if TT.colliderect(enemies_5[i]):
                mode = 'lose'
            for j in range(len(bullets) -1, -1, -1):
                if bullets[j].colliderect(enemies_5[i]):
                    enemies_5.pop(i)
                    bullets.pop(j)
                    break
        if len(enemies_5) == 0:
            mode = 'win'

def update(dt):
    global bullets
    pociski_u()
    collisions()
    
    solid_blocks = [1]  

    for p in range(len(bullets) - 1, -1, -1):
        bullet = bullets[p]
        
        bullet_i = int(bullet.y // cell.height)
        bullet_j = int(bullet.x // cell.width)
        if 0 <= bullet_i < len(my_map) and 0 <= bullet_j < len(my_map[0]):
            if my_map[bullet_i][bullet_j] in solid_blocks:
                bullets.pop(p)
        else:
          bullets.pop(p)
        

def on_key_down(key):
    global player_direction 

    old_x = TT.x
    old_y = TT.y
    new_x, new_y = TT.x, TT.y

    if keyboard.a:
        new_x -= cell.width
        TT.image = "Terrorysta.l"
        player_direction = 'l' 
        
    elif keyboard.d:
        new_x += cell.width
        TT.image = "Terrorysta.r"
        player_direction = 'r' 
        
    elif keyboard.w:
        new_y -= cell.width
        TT.image = "Terrorysta.u"
        player_direction = 'u' 
        
    elif keyboard.s:
        new_y += cell.width
        TT.image = "Terrorysta.d"
        player_direction = 'd' 

    TT_j = int(new_x // cell.width)
    TT_i = int(new_y // cell.height)

    if 0 <= TT_i < len(my_map) and 0 <= TT_j < len(my_map[0]):
        if my_map[TT_i][TT_j] != 1:
            TT.x = new_x
            TT.y = new_y

def on_mouse_down(button, pos):
    global mode
    if mouse.left:
        if mode == "menu":
            if go.collidepoint(pos):
                mode = "game"
                
        if mode == "game":
            bullet = Actor("Bullet2")
            bullet.pos = TT.pos
            bullet.direction = player_direction 
            bullets.append(bullet)
            
           
