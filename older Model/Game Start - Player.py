##10/07/2021
##Pygame Template

##Pygame Libraries

import random
import pygame

##Initialise pygame
pygame.init()
pygame.mixer.init()

##Screen Size and Frame Rate
WIDTH = 1500
HEIGHT = 900
FPS = 60

##Font Initialise
pygame.font.init()
FONT = pygame.font.Font("PixelBase.ttf",28)
SMALLFONT = pygame.font.Font("PixelBase.ttf",24)
TITLEFONT = pygame.font.Font("PixelBase.ttf",60)
ENDFONT = pygame.font.Font("PixelBase.ttf",100)
Typed = False
charactertyped = 0
slowcharactertyped = 0
CharactertypedCheck = False
SlowTypingMessage = str("")


##Font Attributes
typing_speed = 40
TYPING = pygame.USEREVENT+11
slowtyping_speed = 200
SLOWTYPING = pygame.USEREVENT+12

##Animations

##Flipped


##Player Attributes
##Playejumpspeed should be greater than jump height, or else player will fall during jump
Playerjumpspeed = int(35)
Playerjumpspeedvary = Playerjumpspeed
Playerjumpheight = int(25)
Playerjumpcap = int(0)
Playerjumping = False
Playerfalling = False
Playercasting = False
Playeronfloor = False
Playerplatformcorrection = False
Playerup = False
Playerdown = False
Playerleft = True
Playerright = False
Playerfallcap = Playerjumpheight-1
Playerhp = int(100)
PlayerINV = False

##Magicka attributes
Magickagainamount = int(1)
Magickacap = int(100)
Magicka = Magickacap

##Platform attributes
Baseplatformposy = (HEIGHT-200)

##SpellConfig
Firestormspeed = 40
Blizzardspeed = 20
Blizzardrepeats = 150

LaserPrice = 40
TeleportPrice = 10
TimestopPrice = 40
BlizzardPrice = 60

LaserOwned = False
TeleportOwned = False
BlizzardOwned = False
TimestopOwned = False

Lasersfired = 0
Laserfire = False

##Enemy Config
Fodderon = True
Knightbosson = True
Seekeron = True
Pongon = True

##Particle Config
Baseparticleon = False

##Misc
Coins = int(0)
Gamebegun = False
Enemy_init = False
BOSSBATTLE = False
GameSTART = False
textloc = WIDTH//30
Level = 0
CoinsBlitzed = False

##Spell names
def spell_name():
    if Playerspellselection ==1:
        spellname = "Magma pebble"
    elif Playerspellselection == 3:
        spellname = "Orbital Beam"
    elif Playerspellselection == 4:
        spellname = "Time stop"
    elif Playerspellselection == 5:
        spellname = "Flash-freeze"
        
    return spellname


        
            

        
##Player Related Timers
playerjump_time = 15
PLAYERJUMP_EVENT = pygame.USEREVENT+1

laser_rate = 10
LASER_EVENT = pygame.USEREVENT+6
pygame.time.set_timer(LASER_EVENT,laser_rate)
LASER_EVENT = False

Timefreezetimer = int

PLAYERINVFRAMES_EVENT = pygame.USEREVENT+30
playerinv_time = 1000
pygame.time.set_timer(PLAYERINVFRAMES_EVENT, playerinv_time)
PLAYERINVFRAMES = False

##Enemy Timers
knightattack_freq = 1250
KNIGHTATTACK_EVENT = pygame.USEREVENT+4
pygame.time.set_timer(KNIGHTATTACK_EVENT,knightattack_freq)
KNIGHTATTACK_EVENT = False

KNIGHTDROP_FREQ = 50000

SEEKER_FREQ = 25000

PONG_FREQ = 15000

##Misc Timers
magicka_recharge = 300
MAGICKAGAIN = pygame.USEREVENT+2
pygame.time.set_timer(MAGICKAGAIN, magicka_recharge)

PARTICLE_FREQ = 0.1

##Animation Tickers

seekeranim_tickrate = 50
SEEKERANIM_TICK = pygame.USEREVENT+9
pygame.time.set_timer(SEEKERANIM_TICK, seekeranim_tickrate)
SEEKERANIM_TICK = False




##Colour Library
BLACK = (0, 0, 0)
WHITE = (255, 255 , 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 255)
DARKBLUE = (0,100,130)
BROWN = (150, 75, 0)
PURPLE = (216, 191, 216)
VIOLET = (238,130,238)
ORANGE = (255,215,0)
TRANSPARENT = (0,0,0,0)


##Positions
XMiddle = WIDTH/2
##Objects

def Flipx(image):
    imageF = pygame.transform.flip(image,True,False)

    return imageF
    
def Summon(spell,magickarequired,repeats):
    global Magicka
    if Magicka >= magickarequired:
        for number in range(repeats):
            spell()
    if Magicka-magickarequired>=0:
        Magicka -= magickarequired

def Summonlaser(spell,magickarequired,repeats,posx):
    global Magicka
    if Magicka >= magickarequired:
        for number in range(repeats):
            spell(posx)
    if Magicka-magickarequired>=0:
        Magicka -= magickarequired

def Randomiser(totalrandom):
    outofrandom = random.randint(1,totalrandom)
    
    return outofrandom
    
       
##Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((96,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = (XMiddle)
        self.rect.bottom= (Baseplatformposy-1000)
        self.image.set_colorkey(BLACK)
        self.speedx = 0
        self.speedy = 0
        self.timefreeze = False
        self.timefreezeend = 0
        self.timefreezestart = 0
        self.freezetimetaken = 0
       
    def update(self):
        global Coins
        if Gamebegun == True:
            global Playerfallcap               
            if self.rect.x< mx-126:
                Playerleft = False
                Playerright = True
            elif self.rect.x > mx:
                Playerleft = True
                Playerright = False
            else:
                Playerleft = False
                Playerright = False
                Playerup = True
            ##Player-State checker
            if Playerfalling == True:
                self.image.fill(BLACK)
                try:
                    if Playerleft == False:
                        self.image.blit(PlayerfallinganimF,(0,0))
                    else:
                        self.image.blit(Playerfallinganim,(0,0))
                except UnboundLocalError:
                    Playerleft = True
            elif Playerjumping == True:
                self.image.fill(BLACK)
                if Playerright == True:
                    self.image.blit(PlayerjumpinganimF,(0,0))
                else:
                    self.image.blit(Playerjumpinganim,(0,0))
                    
            elif Playerjumping == False and Playerfalling == False:
                self.image.fill(BLACK)
                if Playerright == True:
                    self.image.blit(Playeridle1F,(0,0))
                elif Playerleft == True:
                    self.image.blit(Playeridle1,(0,0))
                elif Playerup == True:
                    self.image.blit(Playerupanim,(0,0))

            self.speedx=0
            self.speedy=0
            keystate = pygame.key.get_pressed()

            if Playerfalling == True:
                self.speedy = Playerfallcap - Playerjumpheight
                Playerfallcap +=1
            elif Playerfalling == False and Playerjumping == False:
                Playerfallcap = Playerjumpheight-1
                
            if keystate[pygame.K_a]:
                self.speedx = -12
            if keystate[pygame.K_d]:
                self.speedx = 12
                
            self.rect.x += self.speedx
            self.rect.y += self.speedy

    def jump(self):
        self.speedy = -Playerjumpspeedvary
        self.rect.y += self.speedy

    ##Player spells
    def Fireball(self):
        fb = Fireproj(mx-Mousereticle.get_width()//2,0 )
        playerbluntprojectiles.add(fb)
        all_sprites.add(fb)        

    def Flashfreeze(self):
        bl = Blizzardwind(random.randint(-1000,-100) , random.randrange(-350,Baseplatformposy-200))
        playerbluntprojectiles.add(bl)
        all_sprites.add(bl)      
        
    def Teleport(self):
        self.rect.centerx = mx
        self.rect.centery = my

    def Orbital_strike(self,x):
        laser = Laser(x)
        all_sprites.add(laser)
        playerpierceprojectiles.add(laser)

    def Timestop(self):
        if self.timefreeze == False:
            self.timefreeze = True
            self.timefreezestart = pygame.time.get_ticks()           
        elif self.timefreeze == True:
            self.timefreeze = False
            self.timefreezeend = pygame.time.get_ticks()
            self.freezetimetaken = self.timefreezeend - self.timefreezestart            
        
        
##Player Weapons
class Fireproj(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,22))
        self.image.set_colorkey(BLACK)
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 15
        self.rect.centery = y
        self.speedy = Firestormspeed
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.right < 0 or self.rect.left>WIDTH or self.rect.top>HEIGHT:
            self.kill()   

class Blizzardwind(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x + 15
        self.rect.centery = y
        self.speedy = random.randint(8,12)
        self.speedx = random.randint(Blizzardspeed,Blizzardspeed+30)

    def update(self):
        self.rect.y +=self.speedy
        self.rect.x += self.speedx
        if self.rect.right < -1000 or self.rect.left>WIDTH+500:
            self.kill()

class Laser(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((20, 50))
        self.image.blit(Laseranim,(0,0))
        self.rect = self.image.get_rect()
        self.rect.bottom = -20
        self.rect.centerx = x
        self.speedy = random.randint(50,100)

    def update(self):
        self.rect.y +=self.speedy
        if self.rect.top > HEIGHT:
            self.kill()
    
##Platforms    
class LargePlatform(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((WIDTH*2, 250))
        self.rect = self.image.get_rect()
        self.rect.centerx = (XMiddle)
        self.rect.top = (Baseplatformposy)
        self.speedx = 0
        self.speedy = 0
        self.image.blit(Big_plat,(self.rect.centerx,0))

class SmallPlatform(pygame.sprite.Sprite):

    def __init__(self,x,y,width):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, 5))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        
    def update(self):
        if BOSSBATTLE == True:
            self.kill()
            smallplats.add(smallplatform1)
            smallplats.add(smallplatform2)
        else:
            platforms.add(smallplatform1)
            platforms.add(smallplatform2)
            all_sprites.add(platforms)
       
##Basic Enemies
class Fodder(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,64))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x  = random.choice([-100,WIDTH+100])
        self.rect.bottom = random.randrange(100,Baseplatformposy-self.rect.height)
        self.animationtick = random.randint(0,3)
        if self.rect.x ==-100:
            self.speedx = random.randint(3,6)
            self.right = True
        else:
            self.speedx = random.randint(-6,-3)
            self.right = False
        

    def update(self):
        self.animationtick+=1
        if self.animationtick == 4:
            self.animationtick = 0
        self.image.fill(BLACK)
        self.anim = FodderAnim[self.animationtick]
        if self.rect.left> WIDTH +150 or self.rect.right< -150:
            f = Fodder()
            all_sprites.add(f)
            fodders.add(f)
            all_enemies.add(f)
            self.kill()
        if self.right == True:
            self.image.blit(self.anim,(0,0))
        elif self.right == False:
            self.image.blit(Flipx(self.anim),(0,0))
        self.rect.x += self.speedx
        
class Seeker(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((100,40))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.x  = random.choice([-100,WIDTH+100])
            self.rect.bottom = random.randrange(100,Baseplatformposy-100)
            self.animationtick = 1
        

        def update(self):
            self.alive = True
            if self.animationtick == 3:
                self.animationtick = 0
            self.image.fill(BLACK)
            try:
                self.anim = SeekerAnim[self.animationtick]
            except IndexError:
                self.anim = SeekerAnim[1]
            if self.rect.x <= -100:
                self.speedx = random.randint(20,30)
                self.right = True
                self.rect.x += self.speedx
                self.rect.centery = player.rect.centery
                
            elif self.rect.x>= WIDTH+100:
                self.speedx = random.randint(-30,-20)
                self.right = False
                self.rect.x += self.speedx
                self.rect.centery = player.rect.centery
                
            if self.right == True:
                self.image.blit(self.anim,(0,0))
                
            elif self.right == False:
                self.image.blit(Flipx(self.anim),(0,0))
            self.rect.x += self.speedx

class Pong(pygame.sprite.Sprite):
    
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface((64,64))
            self.rect = self.image.get_rect()
            self.image.set_colorkey(BLACK)
            self.image.blit(PongAnim,(0,0))
            self.rect.x  = -50
            self.rect.centery = random.randrange(100,Baseplatformposy-100)
            self.speedy = random.randint(10,15)
            self.speedx = random.randint(10,15)
            self.bounced = 0

        def update(self):
            if self.rect.right >= WIDTH and self.bounced == 0:
                self.bounced = 1
            if self.rect.left <= 0 and self.bounced == 1 or self.rect.right>=WIDTH and self.bounced == 1:
                self.speedx = ((self.speedx+random.choice([-5,-3,-1,1,3,5])))*-1
            if 0>self.rect.top or self.rect.bottom > (HEIGHT-(HEIGHT-Baseplatformposy-10)):
                self.speedy = (self.speedy+random.choice([-5,-3,-1,1,3,5]))*-1

            if self.speedx >= 25:
                self.speedx = 25
            if self.speedy>= 25:
                self.speedy = 25
            self.rect.x +=self.speedx
            self.rect.y += self.speedy
            
    
        

##Complex enemies
class Knight(pygame.sprite.Sprite):
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((148,90))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()      
        self.rect.centerx  = random.randint(+50,WIDTH-50)        
        self.rect.bottom = 0
        self.speedx = 4
        self.speedy = 0
        self.falling = True
        self.walkright = False
        self.walkleft = False
        self.lungingright = False
        self.lungingleft = False
        self.lungespeed = int(35)
        self.lungecap = int(30)
        self.lungecapvary = self.lungecap
        self.rampage = False
        self.dead = True
        self.hp = int(30)
        
        

    def update(self):
        if self.hp <= 0:
            self.dead = True
            BOSSBATTLE = False
            self.deadtime = pygame.time.get_ticks()
        if self.rect.centerx<player.rect.centerx:
            selfplayerleft = False
        elif player.rect.centerx<self.rect.centerx:
            selfplayerleft = True
        else:
            selfplayerleft = True
        self.image.set_colorkey(WHITE)
        
        if self.falling == True and self.rampage == False and player.timefreeze ==False:
            self.speedy = 15
            self.speedx = 0
            self.image.fill(WHITE)
            self.image.blit(knightfalling,(0,0))
            
        elif self.falling == False:
            self.speedy = 0

        ##Lunge
        if self.falling == False and self.lungingright == True and self.lungecapvary != self.lungecap and self.rampage == False:
            self.speedx = random.choice([self.lungespeed,self.lungespeed+5])- self.lungecapvary
            self.lungecapvary +=1
        elif self.lungingright == False and self.lungecapvary != self.lungecap and self.rampage == False:
            self.speedx = (random.choice([self.lungespeed,self.lungespeed+5])- self.lungecapvary)*-1
            self.lungecapvary +=1
        ##Rampage
        elif self.lungingright == True and self.lungecapvary != self.lungecap and self.rampage == True:
            self.speedx = self.lungespeed+35- self.lungecapvary
            self.lungecapvary +=1
        elif self.lungingright == False and self.lungecapvary != self.lungecap and self.rampage == True:
            self.speedx = (self.lungespeed+35- self.lungecapvary)*-1
            self.lungecapvary +=1
            
        if self.lungecapvary == self.lungecap:
            self.lungingright = False
            self.lungingleft = False
            self.speedx= 0
            self.rampage = False
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right<-50:
            self.rect.left = WIDTH
            if self.rampage == True:
                self.rect.bottom = player.rect.bottom//20*20
        elif self.rect.left>WIDTH+50:
            self.rect.right = 0
            if self.rampage == True:
                self.rect.bottom = player.rect.bottom//20*20

        if self.rect.top>HEIGHT:
            self.kill()
                
        if self.falling == False and self.lungingright == False and self.lungingleft == False and player.timefreeze == False:
            self.image.fill(WHITE)
            if selfplayerleft == False:
                self.image.blit(knightidle,(0,0))
            else:
                knightidleF = pygame.transform.flip(knightidle,True,False)
                self.image.blit(knightidleF,(0,0))

    def lunge(self):
        if self.falling == False and player.timefreeze== False:
            self.lungecapvary = 0
            if self.rect.centerx<player.rect.centerx:
                selfplayerleft = False
            elif player.rect.centerx<self.rect.centerx:
                selfplayerleft = True
            self.image.set_colorkey(WHITE)
        
            if selfplayerleft == True:
                self.lungingright = False
                self.lungingleft = True
                knightlungeF = pygame.transform.flip(knightlunge,True,False)
                self.image.blit(knightlungeF,(0,0))
                
            elif selfplayerleft == False:
                self.lungingright = True
                self.lungingleft = False
                self.image.blit(knightlunge,(0,0))

    def charge(self):
        if player.timefreeze== False:
            self.rampage = True
            self.lungecapvary = 0
            if self.rect.centerx<player.rect.centerx:
                selfplayerleft = False
            elif player.rect.centerx<self.rect.centerx:
                selfplayerleft = True
            self.image.set_colorkey(WHITE)
            if selfplayerleft == True:
                self.lungingright = False
                self.lungingleft = True
                knightlungeF = pygame.transform.flip(knightlunge,True,False)
                self.image.blit(knightlungeF,(0,0))
                
            elif selfplayerleft == False:
                self.lungingright = True
                self.lungingleft = False
                self.image.blit(knightlunge,(0,0))

        
            

##Particle Effects
class Baseparticle(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((4,random.randint(6,8)))
        self.image.fill(DARKBLUE)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(-70, WIDTH)
        self.rect.y = random.randint(-100,-60)
        self.speedx = random.randint(3,10)
        self.speedy = random.randint(20,30)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x +=self.speedx
        if self.rect.top >HEIGHT or self.rect.left>WIDTH:
            self.kill()

##Infobar
##class Portrait(pygame.sprite.Sprite):
##    
##    def __init__(self):
##        pygame.sprite.Sprite.__init__(self)
##        self.image = pygame.Surface((128,128))
##        self.image.set_colorkey(WHITE)
##        self.image.blit(Wizport,(0,0))
##        self.rect = self.image.get_rect()
##        self.rect.centerx = 100
##        self.rect.centery = 100

class Magmapebbletome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Fireraintome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery =  HEIGHT//1.1


class Flashfreezetome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1250
        self.rect.centery =  HEIGHT//1.1

    def update(self):
        if BlizzardOwned == True:
            self.image.set_colorkey(BLACK)
            self.image.blit(Blizzardtome,(0,0))

class Lasertome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 750
        self.rect.centery =  HEIGHT//1.1

    def update(self):
        if LaserOwned == True:
            self.image.blit(OBtome,(0,0))

        

class Teleporttome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = HEIGHT//1.1

    def update(self):
        if TeleportOwned == True:
            self.image.blit(Portaltome,(0,0))

class Timestoptome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1000
        self.rect.centery = HEIGHT//1.1

    def update(self):
        if TimestopOwned == True:
            self.image.set_colorkey(BLACK)
            self.image.blit(Timehalttome,(0,0))

class Infoholder(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1400,175))
        self.image.set_colorkey(BLACK)
        self.image.blit(Infobar,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.bottom = HEIGHT//1.007
        
        


           


        

##Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Success!")
clock = pygame.time.Clock()

##Group Declaration
all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
playerbluntprojectiles = pygame.sprite.Group()
playerpierceprojectiles = pygame.sprite.Group()
basicenemies = pygame.sprite.Group()
complexenemies = pygame.sprite.Group()
all_enemies = pygame.sprite.Group()
player_group = pygame.sprite.Group()
infos = pygame.sprite.Group()
smallplats = pygame.sprite.Group()
opening = pygame.sprite.Group()
particles = pygame.sprite.Group()
fodders = pygame.sprite.Group()

##Sprite Declaration
player = Player()
knight = Knight()
largeplatform = LargePlatform()
##portrait = Portrait()
baseparticle = Baseparticle()
mpt = Magmapebbletome()
fft = Flashfreezetome()
lt = Lasertome()
tp = Teleporttome()
thp = Timestoptome()
infoholder = Infoholder()

##Small Platform Delcarations
smallplatform1 = SmallPlatform(XMiddle,HEIGHT-400 ,300)
smallplatform2 = SmallPlatform(XMiddle,HEIGHT-650 ,150)

##Sprite Adding
player_group.add(player)

platforms.add(largeplatform)
platforms.add(smallplatform1)
platforms.add(smallplatform2)
smallplats.add(smallplatform1)
smallplats.add(smallplatform2)

all_sprites.add(basicenemies)
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(largeplatform)

##infos.add(portrait)
infos.add(infoholder)
infos.add(mpt)
infos.add(fft)
infos.add(lt)
infos.add(tp)
infos.add(thp)




##Setting timers

knight_timer = 0
now2 = pygame.time.get_ticks()

##Particle Timer
particle_timer = 0
now3 = pygame.time.get_ticks()

##Seeker Timer
seeker_timer = 0
now4= pygame.time.get_ticks()

##Pong Timer
pong_timer = 0
now5= pygame.time.get_ticks()


##Setting Timers w/ USEREVENTS
pygame.time.set_timer(PLAYERJUMP_EVENT, playerjump_time)
PLAYERJUMP_EVENT = False
pygame.time.set_timer(TYPING, typing_speed)
pygame.time.set_timer(SLOWTYPING, slowtyping_speed)



## Game Loop ##

running = True
while running:
    if Magicka<0:
        Magicka =0
    clock.tick(FPS)
    if GameSTART == True and Enemy_init == False:
        for number in range(6):
            f = Fodder()
            all_sprites.add(f)
            fodders.add(f)
            all_enemies.add(f)


        Enemy_init = True


    Mouseco = []
    Mouseco = pygame.mouse.get_pos()
    mx = int(Mouseco[0])
    my = int(Mouseco[1])
    ## 1)Input Process
    for event in pygame.event.get():
        if knight.dead == True:
            BOSSBATTLE = False
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            ##Spell selection
            if event.key == pygame.K_1:
                Playerspellselection = 1
                
            elif event.key == pygame.K_2:
                if Coins >= TeleportPrice and TeleportOwned == False:
                    Coins-=TeleportPrice
                    TeleportOwned = True
                if TeleportOwned == True:
                    Summon(player.Teleport,5,1)
                
            elif event.key == pygame.K_5:
                if Coins >=BlizzardPrice or BlizzardOwned == True:
                    if BlizzardOwned == False:
                        Coins -= BlizzardPrice
                        BlizzardOwned = True
                    Playerspellselection = 5
                    
            elif event.key == pygame.K_3:
                if Coins >=LaserPrice or LaserOwned == True:
                    if LaserOwned == False:
                        Coins -= LaserPrice
                        LaserOwned = True
                    Playerspellselection = 3
                
            elif event.key == pygame.K_4:
                if Coins >=TimestopPrice or TimestopOwned == True:
                    if TimestopOwned == False:
                        Coins -= TimestopPrice
                        TimestopOwned = True
                    Playerspellselection = 4
                    


            elif event.key == pygame.K_SPACE:
                if Gamebegun == False:
                    Gamebegun = True
                    UntilStart = pygame.time.get_ticks()
                    
            if Playerfalling == False and Playerjumping == False:
                if event.key == pygame.K_w:
                    PLAYERJUMP_EVENT = pygame.USEREVENT+1
            

                
            if event.key == pygame.K_UP:
                if BOSSBATTLE == False:
                    all_sprites.add(knight)
                    complexenemies.add(knight)
                    KNIGHTATTACK_EVENT = pygame.USEREVENT+4


                
        if event.type == pygame.MOUSEBUTTONUP:
            if Playerspellselection == 1:
                Summon(player.Fireball,2,1)
            elif Playerspellselection == 5:
                Summon(player.Flashfreeze,65,Blizzardrepeats)
            elif Playerspellselection == 3:
                LASER_EVENT = pygame.USEREVENT+6
            elif Playerspellselection == 4:
                if player.timefreeze == False:
                    Summon(player.Timestop,40,1)
                else:
                    Summon(player.Timestop,0,1)
                print(player.timefreeze)

    
                

                 
        elif event.type == PLAYERJUMP_EVENT:
            if Playerjumpcap != Playerjumpheight:
                Playerjumping = True
                player.jump()                
                Playerjumpcap+= 1
                Playerjumpspeedvary = Playerjumpheight-Playerjumpcap
                
            else:
               PLAYERJUMP_EVENT = False
               Playerjumpcap = 0
               Playerjumpspeedvary = Playerjumpspeed
               Playerjumping = False
               
        elif event.type == MAGICKAGAIN:
            if Magicka != Magickacap and Magicka<Magickacap and player.timefreeze == False:
                Magicka+=Magickagainamount

        elif event.type == KNIGHTATTACK_EVENT:
            knight.rampage = False
            if Randomiser(100)<65:
                knight.lunge()
            elif Randomiser(100)>=65 and Randomiser(100)<90:
                knight.charge()

        elif event.type == LASER_EVENT:
            if Lasersfired == 0:
                ogposx = mx
            if Laserfire == False:    
                if Magicka>40:
                    Magicka-=40
                    Laserfire = True
                
            if Laserfire == True:
                Summonlaser(player.Orbital_strike,0,5,ogposx)
                Lasersfired+=1
                if Lasersfired>=50:
                    Lasersfired = 0
                    Laserfire = False
                    LASER_EVENT = False
            else:
                LASER_EVENT = False
                Lasersfired = 0
                
        elif event.type == SEEKERANIM_TICK:
            if player.timefreeze == False:
                s.animationtick +=1
                
        if event.type == TYPING:
            if charactertyped!=len(TypingMessage):
                Typed = False
                charactertyped += 1

        if event.type == PLAYERINVFRAMES_EVENT:
            PlayerINV = False
            
    ##Timers
                
    ## Knight Spawn Timer
    if Knightbosson == True and GameSTART == True and knight.dead == True and player.timefreeze == False:
        try:
            try:
                knight_timer = pygame.time.get_ticks() - UntilStart - now2 - (knight.deadtime-knightalive) - player.freezetimetaken
            except AttributeError:
                knight_timer = pygame.time.get_ticks() - UntilStart - now2 - (knight.deadtime-knightalive)
        except AttributeError:
            knight_timer = pygame.time.get_ticks() - UntilStart - now2
        if knight_timer >= KNIGHTDROP_FREQ + random.choice([3000,2000,1000,500]) and BOSSBATTLE == False:
            knightalive = pygame.time.get_ticks()
            print("Spawn")
            BOSSBATTLE = True
            now2 = pygame.time.get_ticks()
            knight.dead = False
            knight.hp = 40
            print(BOSSBATTLE)
            knight.rect.bottom = 0
            all_sprites.add(knight)
            complexenemies.add(knight)
            KNIGHTATTACK_EVENT = pygame.USEREVENT+4

    ##Baseparticle Spawn Timer
    if Baseparticleon == True and player.timefreeze == False:
        particlesize = random.randint(2,20)
        particle_timer = pygame.time.get_ticks() - now3
        if particle_timer >= PARTICLE_FREQ:
            now3 = pygame.time.get_ticks()
            for number in range(particlesize):
                bp = Baseparticle()
                particles.add(bp)
                all_sprites.add(bp)
                
    if GameSTART == True:
        ##Seeker Spawn Timer
        if Seekeron == True and player.timefreeze == False:
            seeker_timer = pygame.time.get_ticks() - now4 - player.freezetimetaken - UntilStart
            if seeker_timer >= SEEKER_FREQ:
                now4 = pygame.time.get_ticks()
                s = Seeker()
                basicenemies.add(s)
                all_sprites.add(s)
                if SEEKERANIM_TICK == False:
                    SEEKERANIM_TICK = pygame.USEREVENT+9

        ##Pong Spawn Timer
        if Pongon == True and player.timefreeze == False:
            pong_timer = pygame.time.get_ticks() - now5 - player.freezetimetaken - UntilStart
            if pong_timer >= PONG_FREQ:
                now5 = pygame.time.get_ticks()
                p = Pong()
                basicenemies.add(p)
                all_sprites.add(p)

    ##Collisions
            
    hits = pygame.sprite.spritecollide(player, platforms, False)

    if hits:
        GameSTART = True
        Playerfalling  = False
        if Playerjumping == False:
            Playerplatformcorrection = True
    else:
        if Playerjumping == False:
            Playerfalling = True
        Playerplatformcorrection =  False
        
    hits = pygame.sprite.spritecollide(largeplatform,player_group,False)
    for hit in hits:
        player.rect.bottom = Baseplatformposy+1


    ##Fodder have their own specific collision due to a prevous error, when any previous enemy was shot, a fodder would spawn, exceeding the limit of 6
    hits = pygame.sprite.groupcollide(playerbluntprojectiles, fodders, True,True)

    for hit in hits:
        f = Fodder()
        all_sprites.add(f)
        all_enemies.add(f)
        fodders.add(f)
        
        Coins+=1

    hits = pygame.sprite.groupcollide(playerpierceprojectiles, fodders, False,True)

    for hit in hits:
        f = Fodder()
        all_sprites.add(f)
        all_enemies.add(f)
        fodders.add(f)
        Coins+=1

        
    hits = pygame.sprite.groupcollide(player_group, fodders, False,True)

    for hit in hits:
        Playerhp -=5
        
    hits = pygame.sprite.groupcollide(playerbluntprojectiles, basicenemies, True,True)

    for hit in hits:
        Coins+=1

    hits = pygame.sprite.groupcollide(playerpierceprojectiles, basicenemies, False,True)

    for hit in hits:
        Coins+=1
        
    hits = pygame.sprite.groupcollide(player_group, basicenemies, False,True)

    for hit in hits:
        Playerhp -=5
           
        
    hits = pygame.sprite.spritecollide(knight,playerpierceprojectiles,False)
    for hit in hits:
        knight.hp -=1
    hits = pygame.sprite.spritecollide(knight,playerbluntprojectiles,False)
    for hit in hits:
        knight.hp -=1

    hits = pygame.sprite.spritecollide(knight,player_group,False)
    
    if hits and PlayerINV == False:
        if knight.lungingleft==True or knight.lungingright==True:
            Playerhp -=20
            PlayerINV = True
            PLAYERINVFRAMES_EVENT = pygame.USEREVENT+30
        
    hits = pygame.sprite.spritecollide(knight,platforms,False)
    if hits and knight.dead == False:
        knight.rect.bottom = Baseplatformposy+1
        knight.falling = False
    else:
        knight.falling = True


    hits = pygame.sprite.groupcollide(playerbluntprojectiles, platforms, True,False)

##    hits = pygame.sprite.spritecollide(knight,platforms,False)
##
##    if hits:
##        Knightfalling = False
##    else:
##        Knightfalling = True
        
    ## 2)Update
    if player.timefreeze == True:
        player_group.update()
    else:
        all_sprites.update()
    if Gamebegun == True:
        platforms.update()
        infos.update()
        smallplats.update()
        opening.update()

    ## 3)Text sorting
    Message1 = "Magicka: "+str(Magicka)
    CurrentMagickaMessage = FONT.render(Message1, False, WHITE)

    Message2 = "Coins: "+str(Coins)
    CurrentCoinsMessage = FONT.render(Message2, False, WHITE)

    Message3 = "Spell: "+str(spell_name())
    CurrentSpellMessage = FONT.render(Message3, False, WHITE)

    ##Infobar prices and Magicka cost
    if TeleportOwned == False:       
        Message4 = ":"+str(TeleportPrice)
    else:
        Message4 = ":5"
    TeleportPriceMessage =FONT.render(Message4, False, WHITE)

    
    if LaserOwned == False:       
        Message5 = ":"+str(LaserPrice)
    else:
        Message5 = ":40"
    LaserPriceMessage = FONT.render(Message5, False, WHITE)


    if TimestopOwned == False:       
        Message6= ":"+str(TimestopPrice)
    else:
        Message6 = ":40"
    TmestopPriceMessage = FONT.render(Message6, False, WHITE)


    if BlizzardOwned== False:       
        Message7= ":"+str(BlizzardPrice)
    else:
        Message7 = ":65"
    Message7 = ":"+str(BlizzardPrice)
    BlizzardPriceMessage = FONT.render(Message7, False, WHITE)

    Message8 = ":2"
    PebbleManaMessage = FONT.render(Message8, False, WHITE)

    Message9 = "HP:"+str(Playerhp)
    HPMessage = FONT.render(Message9, False, WHITE)
    
    TitleMessage = "Press Space To Start"

    ## 4)Render
    screen.blit(Background[Level+1],(0,0))
    
    if Gamebegun == False:
        screen.blit(Title,(WIDTH//2-Title.get_width()//2+8,HEIGHT//4))
        particles.draw(screen)
        
    if Typed == False and Gamebegun == False:
        TypingMessage  = TitleMessage
        characters = str(TitleMessage[:charactertyped])
        Typed = True

    TitleMessageTyped= TITLEFONT.render(characters,False,WHITE)
    
    if Gamebegun == True:
        all_sprites.draw(screen)
        particles.draw(screen)
        platforms.draw(screen)
        infos.draw(screen)

    
        screen.blit(Mousereticle,(mx-Mousereticle.get_width()//2,my - Mousereticle.get_height()//2))
        ##Key Rendering
        for Number in range(5):
            MessageNumber = str(Number+1)
            MessageKey = TITLEFONT.render(MessageNumber, False, WHITE)
            textxpos = (250*(Number+1))+40
            screen.blit(MessageKey,(textxpos,HEIGHT//1.225))

        ##Infobar Coing rendering  
        for number in range(4):
            coinxpos = (250*(number+2))+30
            Coin.set_colorkey(WHITE)
            screen.blit(Coin,(coinxpos,HEIGHT//1.116))
        screen.blit(Mana,(280,HEIGHT//1.116))
        if TeleportOwned == True:
            screen.blit(Mana,(530,HEIGHT//1.116))
        if LaserOwned == True:
            screen.blit(Mana,(780,HEIGHT//1.116))
        if TimestopOwned == True:
            screen.blit(Mana,(1030,HEIGHT//1.116))
        if BlizzardOwned == True:
            screen.blit(Mana,(1280,HEIGHT//1.116))
        YC = 45
        screen.blit(CurrentMagickaMessage,(textloc+60,200 - YC))
        screen.blit(CurrentCoinsMessage,(textloc+65,140- YC))
        screen.blit(CurrentSpellMessage,(textloc,260- YC))
        screen.blit(Coin,(textloc-5,128- YC))
        screen.blit(HP,(textloc-5,70 - YC))
        screen.blit(HPMessage,(textloc+65,80- YC))
        screen.blit(ManaNB,(textloc-23,180- YC))
        
        screen.blit(TeleportPriceMessage,(600,HEIGHT//1.1))
        screen.blit(LaserPriceMessage,(850,HEIGHT//1.1))
        screen.blit(TmestopPriceMessage,(1100,HEIGHT//1.1))
        screen.blit(BlizzardPriceMessage,(1350,HEIGHT//1.1))
        screen.blit(PebbleManaMessage,(350,HEIGHT//1.1))

    if Gamebegun == False:
        AuthorMessage = FONT.render("By Tyler Lynch",False,(WHITE))
        screen.blit(TitleMessageTyped,(WIDTH//2-(390),HEIGHT//2))
        screen.blit(AuthorMessage,(WIDTH//2-(120),HEIGHT//1.2))
    ##after render flip display
    pygame.display.flip()
    
pygame.quit()
        
