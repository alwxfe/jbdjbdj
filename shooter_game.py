

from random import randint
from pygame import *
font.init()
font1 = font.Font(None,80)
win = font1.render('YOU WIN!',True,(255,255,255))
lose = font1.render('YOU LOST!',True,(180,0,0))

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')

img_back = "galaxy.jpg"
img_player = "rocket.png"
img_enemy = "ufo.png"
img_bullet = "bullet.png"

score = 0
lost = 0
goal = 10
lost = 0
max_lost = 3

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,size_x,size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80,win_wight - 80)
            self.rect.y = 0
            lost = lost + 1


class Player(GameSprite):
    def update(self):
            keys = key.get_pressed()
            if keys[K_LEFT] and self.rect.x > 5:
                    self.reckt.x -= self.speed
            if keys[K_RIGHT] and self.rect.x < win_wight - 80:
                    self.reckt.x += self.speed
    def fire(self):
        bullets = Bullet(img_bullet,self.rect.centerx,self.rect.top,15,20,-15)
    bullets.add(bullets)

    def fire(self):
       
        pass

window = display.set_mode((700,500))
display.set_cantion("Шутер")
background = transform.scale(image.load("background.png"),(700,500))
clock = time.clock()
FPS = 60
clock.tick(FPS)

fire_sound = mixer.Sound("fire.ogg")

img.bullet = "bullet.png"

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

bullets = sprite.Group()

while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == KEYDOWN:
                if e.key == K_SPACE:
                    fire_sound.play()
                    ship.fire()

ship = Player(img_hero, 5, win_height - 100,80,100,100)

monster = sprite.Group()
for i in range(1,6):
    monster = Enemy(img_enemy, randint(80, win_wight - 80), - 40, 80, 50, randit(1,5))
    monster.add(monster)
finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = false 

        text = font2.render("Счет: " + str(score),1 , (255,255,255))
        window.blit(text, (10,50))
        ship.update()
        monster.update()

        ship.reset
        monster.draw(window)

        display.update

sprites_list = sprite.groupcollide(monsters,bullets,True,True)
for c in collides:
    score = score + 1
    monster = Enemy(img_enemy,randint(80, win_wight - 80),-40, 80, 50,rendit(1,5))
    monster.add(monster)

if sprite.spritecollide(ship,monster,False) or lost >= max_lost:
    finish = True
    window.blit(lose,(200,200))

if score >= goal:

    finis - True
    window.blit(win,(200,200))

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back),(win_width,win_height))


clock = time.clock()
FPS = 60
clock.tick(FPS)
