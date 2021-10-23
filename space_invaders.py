from random import random
import pyxel

# note on Pyxel: you can create your own sprites by using pyxeleditor!

SCENE_TITLE=0
SCENE_PLAY=1
SCENE_GAMEOVER=2
STAR_COUNT=100
STAR_COLOR_HIGH=12
STAR_COLOR_LOW=5
PLAYER_WIDTH=8
PLAYER_HEIGHT=8
PLAYER_SPEED=2
BULLET_WIDTH=2
BULLET_HEIGHT=8
BULLET_COLOR=11
BULLET_SPEED=4
ENEMY_WIDTH=8
ENEMY_HEIGHT=8
ENEMY_SPEED=1.5
BLAST_START_RADIUS=1
BLAST_END_RADIUS=8
BLAST_COLOR_IN=7
BLAST_COLOR_OUT=10
enemy_list=[]
bullet_list=[]
blast_list=[]

# rendering, update and delete lists through arrays
def update_list(list):
    for elem in list:
        elem.update()

def draw_list(list):
    for elem in list:
        elem.draw()
def cleanup_list(list):
    i=0
    while i < len(list)
    elem = list[i]
    if not elem.alive:
        list.pop(i)
    else:
        i+=1

# setup game environment
class Background:
    def_init_(self):
        self.star_list=[]
    for i in range(STAR_COUNT):
        self.star_list.append(
            (random()*pyxel.width,random()*pyxel.height,
             random()*1.5 + 1)
        )
    def update(self):
        for i,(x,y,speed) in enumerate(self.star_list):
            y += speed
            if y >= pyxel.height:
                y-=pyxel.height
            self.star_list[i]=(x,y,speed)

    def draw(self):
        for (x,y,speed) in self.star_list:
            pyxel.pset(x,y,STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)

    # To initialize,stars are randomized with a for cicle

# next block will define class player

class Player:
    def_init_self(self, x, y):
    self.x = x
    self.y = y
    self.w = PLAYER_WIDTH
    self.h = PLAYER_HEIGHT
    self.alive = True

def update(self):
    if pyxel.btn(pyxel.KEY_LEFT):
        self.x -= PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_RIGHT):
        self.x += PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_UP):
        self.y -= PLAYER_SPEED

    if pyxel.btn(pyxel.KEY_DOWN):
        self.y += PLAYER_SPEED

    self.x = max(self.x,0)
    self.x = min(self.x,pyxel.width - self.w)
    self.y = max(self.y,0)
    self.y = min(self.y,pyxel.height - self.h)

    if pyxel.btnp(pyxel.KEY_SPACE):
        Bullet(
            self.x + (PLAYER_WIDTH - BULLET_WIDTH)/2,
            self.y - BULLET_HEIGHT/2
        )

        pyxel.play(0,0)

    def draw(self):
        pyxel.blt(self.x,self.y,0,0,0,self.w,self.h,0)

# Now let's define class Bullet
        
    
