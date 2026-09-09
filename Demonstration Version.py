#01/01/2022
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
FPS = 90 #high Frame Rate is mainly due to the mouse, so movement can remain smooth, it does not affect the game too much.

##Font Initialise
pygame.font.init()
FONT = pygame.font.Font("PixelBase.ttf",28)
SMALLFONT = pygame.font.Font("PixelBase.ttf",24)
TITLEFONT = pygame.font.Font("PixelBase.ttf",60)
INFOFONT = pygame.font.Font("PixelBase.ttf",60)
ENDFONT = pygame.font.Font("PixelBase.ttf",100)
SlowTyped = False
Typed = False
charactertyped = 0
slowcharactertyped = 0
CharactertypedCheck = False
SlowTypingMessage = str("")
TypedCharacterAwaitReset = False

##Font Attributes
typing_speed = 40
TYPING = pygame.USEREVENT+11
slowtyping_speed = 200
SLOWTYPING = pygame.USEREVENT+12

##Animations
Background = [pygame.image.load("level 1.png"),pygame.image.load("level 1.png")]
Playeridle1 = pygame.image.load("Wizardidle1.png")
Playerjumpinganim = pygame.image.load("Wizardjump.png")
Playerfallinganim = pygame.image.load("Wizardfall.png")
Playerwalkinganim = [pygame.image.load("Wizardwalk1.png"),pygame.image.load("Wizardwalk2.png"),pygame.image.load("Wizardwalk3.png"),pygame.image.load("Wizardwalk4.png"),pygame.image.load("Wizardwalk5.png"),pygame.image.load("Wizardwalk6.png")]
Playerupanim = pygame.image.load("Wizardup.png")
Playerwakeupanim = [pygame.image.load("Wizardawakening1.png"),pygame.image.load("Wizardawakening2.png")]
Playerspawnfall = pygame.image.load("Wizardspawnfall.png")

Big_plat = pygame.image.load("Bigplatform.png")
Mousereticle = [pygame.image.load("MagmaReticle.png"),pygame.image.load("TeleportReticle.png"),pygame.image.load("LaserReticle.png"),pygame.image.load("EmptyReticle.png"),pygame.image.load("EmptyReticle.png")]

Laseranim = pygame.image.load("LaserSprite.png")
    
Fireraintome = pygame.image.load("FireRainTome.png")
Portaltome = pygame.image.load("Portaltome.png")
Blizzardtome = pygame.image.load("Blizzardtome.png")
OBtome = pygame.image.load("LaserTome.png")
Timehalttome = pygame.image.load("Timetome.png")
Lockedtome = pygame.image.load("Lockedtome.png")

knightfalling = pygame.image.load("Knightfall2.png")
knightlunge = pygame.image.load("Knightlunge.png")
knightidle = pygame.image.load("Knightidle.png")
knightdeath = pygame.image.load("Knightdeath.png")

FodderAnim = [pygame.image.load("Fodder1.png"),pygame.image.load("Fodder2.png"),pygame.image.load("Fodder3.png"),pygame.image.load("Fodder4.png")]

SeekerAnim = [pygame.image.load("Seeker1.png"),pygame.image.load("Seeker2.png"),pygame.image.load("Seeker3.png")]

PongAnim = pygame.image.load("Pong.png")

Magmapebble = pygame.image.load("Magmapebble.png")

Title = pygame.image.load("Title.png")

Infobar = pygame.image.load("Infobarbar.png")

GOscreen = pygame.image.load("Gameoverscreen.png")

HP = pygame.image.load("HPsign.png")
Mana = pygame.image.load("Mana.png")
ManaNB = pygame.image.load("ManaNoBack.png")
Coin = pygame.image.load("Coin2.png")

Healthdropanim = pygame.image.load("health.png")
magickaPUPanim = pygame.image.load("ManaRegenPowerUp.png")

##Flipped
Playeridle1F= pygame.transform.flip(Playeridle1, True,False)
PlayerjumpinganimF = pygame.transform.flip(Playerjumpinganim, True,False)
PlayerfallinganimF = pygame.transform.flip(Playerfallinganim, True,False)
PlayerupanimF = pygame.transform.flip(Playerupanim, True,False)

##Sound objects
JumpSFX = pygame.mixer.Sound("JumpSFX2.WAV")
FodderDeathSFX = pygame.mixer.Sound("FodderDeathSFX.WAV")
FallingSFX = pygame.mixer.Sound("FallingSFX.WAV")
WalkingSFX = pygame.mixer.Sound("WalkingSFX.WAV")
Fanfare = pygame.mixer.Sound("FanfareSFX.WAV")
HitbyknightSFX = pygame.mixer.Sound("PlayerswordhitSFX.WAV")
Playerhit = pygame.mixer.Sound("GeneralDamageSFX.WAV")
KnightlungeSFX = pygame.mixer.Sound("KnightLungeSFX.WAV")
Spellunlock = pygame.mixer.Sound("spellunlockSFX.WAV")
TeleportSFX = pygame.mixer.Sound("TeleportSFX.WAV")
TypeSFX = pygame.mixer.Sound("TypeSFX.WAV")
PongSFX = pygame.mixer.Sound("PongSFX.WAV")
LaserSFX = pygame.mixer.Sound("LaserSFX.WAV")
MagmaSFX = pygame.mixer.Sound("MagmaSFX.WAV")
BlizzardSFX = pygame.mixer.Sound("BlizzardSFX.WAV")
KnightdeathSFX = pygame.mixer.Sound("knightdeathSFX.WAV")
GameoverSFX = pygame.mixer.Sound("GameoverSFX.WAV")
HealSFX = pygame.mixer.Sound("HealSFX.WAV")
EnemyhitSFX = pygame.mixer.Sound("BasicenemyhitSFX.WAV")
SpawnsplatSFX = pygame.mixer.Sound("WizardspawnsplatSFX.WAV")

##OLD COMMENT: To loop the rain, loop was hidden within the 'Pong' enemy, hijacking its timer
RainSFX = pygame.mixer.Sound("RainSFX.WAV")
RainSFX.play()

pygame.mouse.set_visible(False)

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
Playerspellselection = int(1)
Playerteleport = False
Playerhp = int(100)
PlayerINV = False

##Magicka attributes
Magickaagainamount = int(1)
Magickacap = int(100)
Magicka = Magickacap

##Platform attributes
Baseplatformposy = (HEIGHT-200)

##SpellConfig
Firestormspeed = 40
Blizzardspeed = 20
Blizzardrepeats = 300

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
Baseparticleon = True

##Misc
Coins = int(0)
Gamebegun = False
Enemy_init = False
BOSSBATTLE = False
GameSTART = False
textloc = WIDTH//30
Level = 0
CoinsBlitzed = False
Score = int()
SmallplatSFXready = True
Admincommands = False

##Minus Time decreaser for opposite effect
Timedecreaser = [0,1000,2000]

##Gameover
Textinit = False
Gameover = False

##Spell names
def spell_name():
    if Playerspellselection ==1:
        spellname = "Magma pebble"
    elif Playerspellselection ==2:
        spellname = "Teleport"
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

laser_rate = 30
LASER_EVENT = pygame.USEREVENT+6
pygame.time.set_timer(LASER_EVENT,laser_rate)
LASER_EVENT = False

Timefreezetimer = int

##Player invincible frames are to prevent unintended excessive damage from a single enemy attack
##+30 means nothing, i was just being lazy and i knew 30 would be unoccupied instead of making it continous
PLAYERINVFRAMES_EVENT = pygame.USEREVENT+30
playerinv_time = 1500
pygame.time.set_timer(PLAYERINVFRAMES_EVENT, playerinv_time)
PLAYERINVFRAMES = False

##Enemy Timers
knightattack_freq = 1400
KNIGHTATTACK_EVENT = pygame.USEREVENT+4
pygame.time.set_timer(KNIGHTATTACK_EVENT,knightattack_freq)
KNIGHTATTACK_EVENT = False

KNIGHTDROP_FREQ = 35000

SEEKER_FREQ = 9000

PONG_FREQ = 6000

##Misc Timers
HEALTH_FREQ = random.randint(20000,40000)
MAGICKAPUP_FREQ = 40000

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
        self.image = pygame.Surface((94,72))
        self.rect = self.image.get_rect()
        self.rect.centerx = (XMiddle)
        self.rect.bottom= (Baseplatformposy-1000)
        self.image.set_colorkey(WHITE)
        self.speedx = 0
        self.speedy = 0
        self.timefreeze = False
        self.timefreezeend = 0
        self.timefreezestart = 0
        self.freezetimetaken = 0
        self.ATW = 0 ##ATW = Animation Tracker Walking
        self.ATS = 0 ##Spawning
        self.Frametracker = 1 ## Instead of using a timer, to make the players walk anim work i count frames, every 6 frames the anim tracker ticks
        self.SPLAT = True ##This refers to the sound the player first makes when spawning
       
    def update(self):
        global GameSTART
        global Coins
        if GameSTART == True:
            global Playerfallcap               
            if self.rect.centerx <= mx:
                Playerleft = False
                Playerright = True
                
            elif self.rect.centerx > mx:
                Playerleft = True
                Playerright = False
                
            if mx >= self.rect.centerx - 47 and mx <= self.rect.centerx +47:
                Playerup = True

            else:
                Playerup = False
               
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
                if Playerup == True:
                    if Playerleft == True:
                        self.image.blit(Playerupanim,(0,0))
                    else:
                        self.image.blit(PlayerupanimF,(0,0))
                
            self.speedx=0
            self.speedy=0
            keystate = pygame.key.get_pressed()

            if Playerfalling == True:
                self.speedy = Playerfallcap - Playerjumpheight
                Playerfallcap +=1
            elif Playerfalling == False and Playerjumping == False:
                Playerfallcap = Playerjumpheight-1

            ##Bumper
            if self.rect.left < 30:
                self.rect.left = 30
            if self.rect.right > WIDTH - 30:
                self.rect.right= WIDTH - 30

            if keystate[pygame.K_a]:
                self.speedx = -12
                if Playerfalling == False and Playerjumping == False:
                    self.image.blit(Playerwalkinganim[self.ATW],(0,0))
            if keystate[pygame.K_d]:
                self.speedx = 12
                if Playerfalling == False and Playerjumping == False:
                    self.image.blit(Flipx(Playerwalkinganim[self.ATW]),(0,0))
                
            self.Frametracker+=1
            if self.Frametracker == 6:
                if self.ATW != 4:
                    self.ATW +=1
                else:
                    self.ATW = 0
                self.Frametracker = 1
                
            self.rect.x += self.speedx
            self.rect.y += self.speedy
        elif Gamebegun == True and GameSTART == False:
            if self.rect.bottom <= Baseplatformposy:
                self.rect.y += 16
                self.image.blit(Playerspawnfall,(0,0))
            else:
                if self.SPLAT == True:
                    SpawnsplatSFX.play()
                    self.SPLAT = False
                self.image.blit(Playerwakeupanim[self.ATS],(0,0))
                self.Frametracker +=1
            if self.Frametracker == 30:
                if self.ATS == 0:
                    self.ATS += 1
                else:
                    pygame.mouse.set_pos(780,100)
                    GameSTART = True
                self.Frametracker = 1
            
    def jump(self):
        self.speedy = -Playerjumpspeedvary
        self.rect.y += self.speedy

    ##Player spells
    def Fireball(self):
        fb = Fireproj(mx-15,0 )
        playerbluntprojectiles.add(fb)
        all_sprites.add(fb)        
        MagmaSFX.play()

    def Flashfreeze(self):
        bl = Blizzardwind(random.randint(-1000,-100) , random.randrange(-200,Baseplatformposy-200))
        playerbluntprojectiles.add(bl)
        all_sprites.add(bl)      
        
    def Teleport(self):
        TeleportSFX.play()
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
            RainSFX.stop()
        elif self.timefreeze == True:
            self.timefreeze = False
            self.timefreezeend = pygame.time.get_ticks()
            self.freezetimetaken = self.timefreezeend - self.timefreezestart
            RainSFX.play()
        
        
##Player Weapons
class Fireproj(pygame.sprite.Sprite):

    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20,22))
        self.image.set_colorkey(BLACK)
        self.image.blit(Magmapebble,(0,0))
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
        self.speedy = random.randint(4,8)
        self.speedx = random.randint(Blizzardspeed-20,Blizzardspeed+20)

    def update(self):
        self.rect.y +=self.speedy
        self.rect.x += self.speedx
        if self.rect.right < -1000 or self.rect.left>WIDTH+500:
            self.kill()

class Laser(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface ((20, 150))
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
        self.image = pygame.Surface((width, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        
    def update(self):

        ##Secondary collision used in order to detect and correct collisions
        hits = pygame.sprite.spritecollide(self,player_group,False)
        for hit in hits:
            if BOSSBATTLE == False:
                if Playerjumping == False:
                    player.rect.bottom = self.rect.top+1
            
        if BOSSBATTLE == True:
            self.kill()
            smallplats.add(smallplatform1)
            smallplats.add(smallplatform2)
            #smallplats.add(smallplatform3)
        else:
            platforms.add(smallplatform1)
            platforms.add(smallplatform2)
            #platforms.add(smallplatform3)
            all_sprites.add(platforms)

##Power-ups
class HealthPUP(pygame.sprite.Sprite):
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.set_colorkey(BLACK)
        self.image.blit(Healthdropanim,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x  = random.randrange(75, WIDTH-75)
        self.rect.y = random.randrange(-120, -100)
        self.speedy = random.randrange(1,4)
        

    def update(self):
        self.rect.y += self.speedy

class MagickaPUP(pygame.sprite.Sprite):
    

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((80,80))
        self.image.set_colorkey(BLACK)
        self.image.blit(magickaPUPanim,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x  = random.randrange(75, WIDTH-75)
        self.rect.y = random.randrange(-120, -100)
        self.speedy = random.randrange(1,4)
        

    def update(self):
        self.rect.y += self.speedy
        
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
            self.image = pygame.Surface((82,24))
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
                PongSFX.play()
            if self.rect.left <= 0 and self.bounced == 1 or self.rect.right>=WIDTH and self.bounced == 1:
                self.rect.x +=self.speedx*-1
                self.speedx = ((self.speedx+random.choice([-5,-3,-1,1,3,5])))*-1
                PongSFX.play()
            if 0>self.rect.top or self.rect.bottom > (HEIGHT-(HEIGHT-Baseplatformposy-10)):
                self.rect.y += self.speedy*-1
                self.speedy = (self.speedy+random.choice([-5,-3,-1,1,3,5]))*-1
                PongSFX.play()

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
        self.rect.centerx  = WIDTH//2
        ##Spawned at this y-axis in order to let sound effect play out
        ##Falls 900 Pixels per second, 3 is length of sound clip
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
        self.spawnfalling = True
        
        ##This variable has been made so the sound is not repeated while the knight is falling
        self.fallingSFXplayed = False
        
        

    def update(self):
        ##Global coins must be used due to shoddy starting code, it is not ideal but it works
        global Coins
        
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
            if self.dead ==False:
                self.image.blit(knightfalling,(0,0))
            else:
                self.image.blit(knightdeath,(0,0))
            if self.fallingSFXplayed == False and self.dead == False:
                FallingSFX.play()
                self.fallingSFXplayed = True
            
            
        elif self.falling == False:
            self.speedy = 0
            FallingSFX.stop()
            if self.fallingSFXplayed == True:
                if self.spawnfalling == True:
                    Fanfare.play()
                    self.spawnfalling= False
                WalkingSFX.play()
                self.fallingSFXplayed = False

        ##Lunge
        if self.falling == False and self.lungingright == True and self.lungecapvary != self.lungecap and self.rampage == False:
            self.speedx = random.choice([self.lungespeed,self.lungespeed+5])- self.lungecapvary
            self.lungecapvary +=1
        elif self.lungingright == False and self.lungecapvary != self.lungecap and self.rampage == False:
            self.speedx = (random.choice([self.lungespeed,self.lungespeed+5])- self.lungecapvary)*-1
            self.lungecapvary +=1
        ##Rampage
            
        elif self.lungingright == True and self.lungecapvary != self.lungecap and self.rampage == True and self.spawnfalling != True:
            self.speedx = self.lungespeed+35- self.lungecapvary
            self.lungecapvary +=1
        elif self.lungingright == False and self.lungecapvary != self.lungecap and self.rampage == True and self.spawnfalling != True:
            self.speedx = (self.lungespeed+35- self.lungecapvary)*-1
            self.lungecapvary +=1
            
        if self.lungecapvary == self.lungecap:
            self.lungingright = False
            self.lungingleft = False
            self.speedx= 0
            self.rampage = False
        
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.right<10:
            self.rect.left = WIDTH
            if self.rampage == True:
                self.rect.bottom = player.rect.bottom//20*20
        elif self.rect.left>WIDTH+10:
            self.rect.right = 0
            if self.rampage == True:
                self.rect.bottom = player.rect.bottom//20*20

        if self.rect.top>Baseplatformposy:
            self.spawnfalling = True
            Coins+=20
            KnightdeathSFX.play()
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
            KnightlungeSFX.play()
            self.lungecapvary = 0
            if self.rect.centerx<player.rect.centerx:
                selfplayerleft = False
            elif player.rect.centerx<self.rect.centerx:
                selfplayerleft = True
            else:
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
        if player.timefreeze== False and self.spawnfalling == False:
            KnightlungeSFX.play()
            self.rampage = True
            self.lungecapvary = 0
            if self.rect.centerx<player.rect.centerx:
                selfplayerleft = False
            elif player.rect.centerx<self.rect.centerx:
                selfplayerleft = True
            else:
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

class Magmapebbletome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Fireraintome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 250
        self.rect.centery =  HEIGHT
        self.speedy = -5

    def update(self):
        if self.rect.centery > HEIGHT//1.1:
            self.rect.y += self.speedy

            
class Flashfreezetome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 1250
        self.rect.centery =  HEIGHT
        self.speedy = -5

    def update(self):
        if BlizzardOwned == True:
            self.image.set_colorkey(BLACK)
            self.image.blit(Blizzardtome,(0,0))
        if self.rect.centery > HEIGHT//1.1:
            self.rect.y += self.speedy


class Lasertome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 750
        self.rect.centery = HEIGHT
        self.speedy = -5
        
    def update(self):
        if LaserOwned == True:
            self.image.blit(OBtome,(0,0))
        if self.rect.centery > HEIGHT//1.1:
            self.rect.y += self.speedy
        

class Teleporttome(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((128,128))
        self.image.set_colorkey(BLACK)
        self.image.blit(Lockedtome,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = 500
        self.rect.centery = HEIGHT
        self.speedy = -5
        
    def update(self):
        if self.rect.centery > HEIGHT//1.1:
            self.rect.y += self.speedy
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
        self.rect.centery = HEIGHT
        self.speedy = -5
        
    def update(self):
        if TimestopOwned == True:
            self.image.set_colorkey(BLACK)
            self.image.blit(Timehalttome,(0,0))
        if self.rect.centery > HEIGHT//1.1:
            self.rect.y += self.speedy
            
class Infoholder(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1400,175))
        self.image.set_colorkey(BLACK)
        self.image.blit(Infobar,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.top = HEIGHT
        self.speedy = -10
 
    def update(self):
        if self.rect.bottom > HEIGHT//1.007:
            self.rect.y += self.speedy
        else:
            self.rect.bottom = HEIGHT//1.007
            
class Gameoverscreen(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((1500,900))
        self.image.blit(GOscreen,(0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH//2
        self.rect.top= HEIGHT
        self.speedy = -15
        self.Textinit = False

    def update(self):
        if self.rect.y > 0:
            self.rect.y+= self.speedy
        else:
            self.Textinit = True

           


        

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
healthpup = pygame.sprite.Group()
magickapup = pygame.sprite.Group()
gameover = pygame.sprite.Group()
knight_group = pygame.sprite.Group()

##Sprite Declaration
gameoverscreen = Gameoverscreen()
player = Player()
knight = Knight()
largeplatform = LargePlatform()
baseparticle = Baseparticle()
mpt = Magmapebbletome()
fft = Flashfreezetome()
lt = Lasertome()
tp = Teleporttome()
thp = Timestoptome()
infoholder = Infoholder()
HPUP = HealthPUP()
MPUP = MagickaPUP

##Small Platform Delcarations
##smallplatform1 = SmallPlatform(XMiddle,HEIGHT-400 ,300)
##smallplatform2 = SmallPlatform(XMiddle,HEIGHT-650 ,150)

##Sprite Adding
player_group.add(player)

platforms.add(largeplatform)
##platforms.add(smallplatform1)
##platforms.add(smallplatform2)

all_sprites.add(basicenemies)
all_sprites.add(player)
all_sprites.add(platforms)
all_sprites.add(largeplatform)

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

##HealthPUP Timer
health_timer = 0
now6 = pygame.time.get_ticks()

##MagickaPUP Timer
magicka_timer = 0
now7 = pygame.time.get_ticks()

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
        ##Added here so it is when the player finishes falling, not as soon as pygme starts
        smallplatform1 = SmallPlatform(XMiddle,HEIGHT-400 ,300)
        smallplatform2 = SmallPlatform(XMiddle,HEIGHT-650 ,150)
        #smallplatform3 = SmallPlatform(300,HEIGHT-500 ,200)
        smallplats.add(smallplatform1)
        smallplats.add(smallplatform2)
        #smallplats.add(smallplatform3)
        all_sprites.add(smallplats)
        Enemy_init = True

    
    ## 1)Input Process

    Mouseco = []
    Mouseco = pygame.mouse.get_pos()
    mx = int(Mouseco[0])
    my = int(Mouseco[1])
    
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
                    Spellunlock.play()
                if TeleportOwned == True:
                    Playerspellselection = 2
                
            elif event.key == pygame.K_e:
                if TeleportOwned == True:
                    Summon(player.Teleport,5,1)
                    
                
                
            elif event.key == pygame.K_5:
                if Coins >=BlizzardPrice or BlizzardOwned == True:
                    if BlizzardOwned == False:
                        Coins -= BlizzardPrice
                        Spellunlock.play()
                        BlizzardOwned = True
                    Playerspellselection = 5
                    
            elif event.key == pygame.K_3:
                if Coins >=LaserPrice or LaserOwned == True:
                    if LaserOwned == False:
                        Coins -= LaserPrice
                        Spellunlock.play()
                        LaserOwned = True
                    Playerspellselection = 3
                
            elif event.key == pygame.K_4:
                if Coins >=TimestopPrice or TimestopOwned == True:
                    if TimestopOwned == False:
                        Coins -= TimestopPrice
                        TimestopOwned = True
                        Spellunlock.play()
                    Playerspellselection = 4
                    


            if event.key == pygame.K_SPACE or pygame.K_e:
                if Gamebegun == False:
                    Gamebegun = True
                    charactertyped = 0
                    TypingMessage = ""
                    UntilStart = pygame.time.get_ticks()
                    
            if Playerfalling == False and Playerjumping == False:
                if event.key == pygame.K_w:
                    PLAYERJUMP_EVENT = pygame.USEREVENT+1
            
            if event.key == pygame.K_9:
                Admincommands = True

            if Admincommands == True:
                if event.key == pygame.K_UP:
                    Playerhp = 100000
                        
                if event.key == pygame.K_DOWN:
                    Magickacap = 100000
                    Magicka = Magickacap

                if event.key == pygame.K_RIGHT:
                    Coins = 100000

                if event.key == pygame.K_LEFT:
                    mp = MagickaPUP()
                    all_sprites.add(mp)
                    magickapup.add(mp)

                if event.key == pygame.K_k:
                    Playerhp = 0

                if event.key == pygame.K_p:
                    print("Spawn")
                    BOSSBATTLE = True
                    now2 = pygame.time.get_ticks()
                    knight.dead = False
                    knight.hp = 40
                    print(BOSSBATTLE)
                    ##Spawned at this y-axis in order to let sound effect play out
                    ##Falls 900 Pixels per second, 3 is length of sound clip
                    ##I just guessed it in the end, it works.
                    knight.rect.bottom = ((600*2)*-1)#- (Baseplatformposy) )*-1
                    knight.rect.centerx = WIDTH//2
                    all_sprites.add(knight)
                    complexenemies.add(knight)
                    knight_group.add(knight)
                    KNIGHTATTACK_EVENT = pygame.USEREVENT+4

                if event.key == pygame.K_o:
                    f = Fodder()
                    all_sprites.add(f)

                    fodders.add(f)

                if event.key == pygame.K_i:
                    d = Seeker()
                    all_sprites.add(d)
                    basicenemies.add(d)

                if event.key == pygame.K_u:
                    u = Pong()
                    all_sprites.add(u)
                    basicenemies.add(u)
                            
        if event.type == pygame.MOUSEBUTTONUP:
            if Gamebegun == True and Gameover == False:
                if Playerspellselection == 1:
                    Summon(player.Fireball,3,1)
                elif Playerspellselection == 5:
                    if Magicka >= 65:
                        BlizzardSFX.play()
                    Summon(player.Flashfreeze,65,Blizzardrepeats)
                elif Playerspellselection == 2:
                    Summon(player.Teleport,5,1)
                elif Playerspellselection == 3:
                    LASER_EVENT = pygame.USEREVENT+6
                elif Playerspellselection == 4:
                    if player.timefreeze == False:
                        Summon(player.Timestop,40,1)
                    else:
                        Summon(player.Timestop,0,1)

    
                

                 
        elif event.type == PLAYERJUMP_EVENT:
            if Playerjumpcap != Playerjumpheight:
                Playerjumping = True
                if Playerjumpcap == 0:
                    JumpSFX.play()
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
                Magicka+=Magickaagainamount

        elif event.type == KNIGHTATTACK_EVENT:
            if Gameover == False:
                knight.rampage = False
                if Randomiser(100)<65:
                    knight.lunge()
                elif Randomiser(100)>=65 and Randomiser(100)<90:
                    knight.charge()

        elif event.type == LASER_EVENT:
            if Lasersfired == 0:
                ogposx = mx
            if Laserfire == False:    
                if Magicka>60:
                    LaserSFX.play()
                    Magicka-=60
                    Laserfire = True
                
            if Laserfire == True:
                Summonlaser(player.Orbital_strike,0,5,ogposx)
                Lasersfired+=1
                if Lasersfired>=30:
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
            ##Look in pygame Tests for in depth view of inner workings of typing
            if charactertyped!=len(TypingMessage):
                Typed = False
                TypeSFX.play()
                charactertyped += 1

        if event.type == SLOWTYPING:
            if slowcharactertyped!=len(SlowTypingMessage):
                SlowTyped = False
                TypeSFX.play()
                slowcharactertyped += 1
                
        if event.type == PLAYERINVFRAMES_EVENT:
            PlayerINV = False
            
    ##Timers
                
    ## Knight Spawn Timer
##    if Knightbosson == True and GameSTART == True and knight.dead == True and player.timefreeze == False:
##        try:
##            try:
##                knight_timer = pygame.time.get_ticks() - UntilStart - now2 - (knight.deadtime-knightalive) - player.freezetimetaken
##            except AttributeError:
##                knight_timer = pygame.time.get_ticks() - UntilStart - now2 - (knight.deadtime-knightalive)
##        except AttributeError:
##            knight_timer = pygame.time.get_ticks() - UntilStart - now2
##        if knight_timer >= KNIGHTDROP_FREQ + random.choice([3000,2000,1000,500]) and BOSSBATTLE == False:
##            knightalive = pygame.time.get_ticks()

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
##        if Seekeron == True and player.timefreeze == False:
##            seeker_timer = pygame.time.get_ticks() - now4 - player.freezetimetaken - UntilStart  + random.choice(Timedecreaser)
##            if seeker_timer >= SEEKER_FREQ:
##                now4 = pygame.time.get_ticks()
##                s = Seeker()
##                basicenemies.add(s)
##                all_sprites.add(s)
##                if SEEKERANIM_TICK == False:
##                    SEEKERANIM_TICK = pygame.USEREVENT+9
##
        ##Pong Spawn Timer
##        if Pongon == True and player.timefreeze == False:
##            pong_timer = pygame.time.get_ticks() - now5 - player.freezetimetaken - UntilStart + random.choice(Timedecreaser)
##            if pong_timer >= PONG_FREQ:
##                now5 = pygame.time.get_ticks()
##                p = Pong()
##                basicenemies.add(p)
##                all_sprites.add(p)

        ##HealthPUP Spawn Timer
        if player.timefreeze == False:
            health_timer = pygame.time.get_ticks() - now6 - player.freezetimetaken - UntilStart - random.choice(Timedecreaser)
            if health_timer >= HEALTH_FREQ:
                now6 = pygame.time.get_ticks()
                hp = HealthPUP()
                all_sprites.add(hp)
                healthpup.add(hp)

        ##MagickaPUP Spawn Timer
##        if player.timefreeze == False:
##            magicka_timer = pygame.time.get_ticks() - now7 - player.freezetimetaken - UntilStart - random.choice(Timedecreaser)
##            if magicka_timer >= MAGICKAPUP_FREQ:
##                now7 = pygame.time.get_ticks()
##                mp = MagickaPUP()
##                all_sprites.add(mp)
##                magickapup.add(mp)

    ##Collisions
            
    hits = pygame.sprite.spritecollide(largeplatform,player_group,False)

    if hits:
        Playerfalling  = False
        if Playerjumping == False:
            Playerplatformcorrection = True
            
            if player.rect.bottom >Baseplatformposy + 2:
                WalkingSFX.play()
            player.rect.bottom = Baseplatformposy+1
        
    else:
        if Playerjumping == False:
            Playerfalling = True
        Playerplatformcorrection =  False

    ##Primary collision to stop falling, correction within the class itself on line 480
    hits = pygame.sprite.spritecollide(player, smallplats, False)

    if hits:
        if BOSSBATTLE == False:
            if SmallplatSFXready == True:
                if Playerjumping == False:
                    WalkingSFX.play()
                    SmallplatSFXready = False
            Playerfalling  = False

    else:
        SmallplatSFXready = True
        ##Why no Else?
        ##Becuase if there was else delcaring the player falling they fell through the base platform, however, the player doesnt float becuase the fall delcaration on the base plat covers it 


    ##Power Ups

    hits = pygame.sprite.groupcollide(healthpup, player_group,True,False)

    if hits:
        HealSFX.play()
        
        Playerhp +=30
        HPscore = Playerhp - 100
        if HPscore>0:
            Score+=HPscore
        if Playerhp>100:
            Playerhp = 100
            
    hits = pygame.sprite.groupcollide(magickapup, player_group,True,False)

    if hits:
        HealSFX.play()               
        Magickacap +=100
        Magicka = Magickacap
        Magickaagainamount +=1
        if PONG_FREQ>5000:
            KNIGHTDROP_FREQ -= 5000
            PONG_FREQ -= 1250
            SEEKER_FREQ -=1500
        else:
            s.speedx *=2
            KNIGHTDROP_FREQ = 500
            PONG_FREQ = 2000
            SEEKER_FREQ = 3000
              
        
    ##Fodder have their own specific collision due to a prevous error, when any previous enemy was shot, a fodder would spawn, exceeding the limit of 6
    hits = pygame.sprite.groupcollide(playerbluntprojectiles, fodders, True,True)

    for hit in hits:
##        f = Fodder()
##        all_sprites.add(f)
##        all_enemies.add(f)
##        fodders.add(f)
        Score+=1
        Coins+=1
        FodderDeathSFX.play()

    hits = pygame.sprite.groupcollide(playerpierceprojectiles, fodders, False,True)

    for hit in hits:
##        f = Fodder()
##        all_sprites.add(f)
##        all_enemies.add(f)
##        fodders.add(f)
        Score+=1
        Coins+=1
        FodderDeathSFX.play()
        
    hits = pygame.sprite.groupcollide(player_group, fodders, False,True)

    for hit in hits:
##        f = Fodder()
##        all_sprites.add(f)
##        all_enemies.add(f)
##        fodders.add(f)
        Playerhit.play()
        Playerhp -=5
        
    hits = pygame.sprite.groupcollide(playerbluntprojectiles, basicenemies, True,True)

    for hit in hits:
        Coins+=5
        Score += 5
        EnemyhitSFX.play()

    hits = pygame.sprite.groupcollide(playerpierceprojectiles, basicenemies, False,True)

    for hit in hits:
        Coins+=5
        Score+=5
        EnemyhitSFX.play()
        
    hits = pygame.sprite.groupcollide(player_group, basicenemies, False,True)

    for hit in hits:
        Playerhp -=10
        Playerhit.play()
            
    hits = pygame.sprite.groupcollide(knight_group,playerpierceprojectiles,False,False)
    for hit in  hits:
        knight.hp -=3
        
    hits = pygame.sprite.groupcollide(knight_group,playerbluntprojectiles,False,True)
    for hit in hits:
        knight.hp -=2

    hits = pygame.sprite.spritecollide(knight,player_group,False)
    
    if hits and PlayerINV == False:
        if knight.lungingleft==True or knight.lungingright==True:
            HitbyknightSFX.play()
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
        
    ## 2)Update
    if Magicka>Magickacap:
        Magicka = Magickacap
        
    if Playerhp <= 0 and Gameover == False:
        gameover.add(gameoverscreen)
        player.kill()
        pygame.mouse.set_visible(True)
        print("GAMEOVER")
        GameoverSFX.play()
        Gameover=True
        TypingMessage  = "Thank You For Playing!"
        TypedCharacterAwaitReset = True
        RainSFX.stop()

    if Gameover == True:
        gameover.update()
        
    if player.timefreeze == True:
        player_group.update()
    else:
        if Gameover == False:
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
        Message5 = ":60"
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
    BlizzardPriceMessage = FONT.render(Message7, False, WHITE)

    Message8 = ":3"
    PebbleManaMessage = FONT.render(Message8, False, WHITE)

    Message9 = "HP:"+str(Playerhp)
    HPMessage = FONT.render(Message9, False, WHITE)
    
    TitleMessage = "Press Any Key To Start"

    Message10 = "SCORE: "+str(Score*10)
    ScoreMessage = FONT.render(Message10,False,WHITE)

    
    ## 4)Render
    screen.blit(Background[Level+1],(0,0))

    if Gameover == True:
        gameover.draw(screen)
        if gameoverscreen.Textinit == True:
            if SlowTyped == False:
                SlowTypingMessage  = Message10
                slowcharacters = str(SlowTypingMessage[:slowcharactertyped])
                SlowTyped = True
                TypedScoreMessage = ENDFONT.render(slowcharacters, False, WHITE)

            screen.blit(TypedScoreMessage,((WIDTH//2)+100-((len(Message10)//2)*100),HEIGHT//1.3))
        
    if Gamebegun == False:
        screen.blit(Title,(WIDTH//2-Title.get_width()/2+8,HEIGHT//4))
        particles.draw(screen)
        
    if Gamebegun == False and Gameover == False:
        TypingMessage  = TitleMessage
        
    if Typed == False:   
        characters = str(TypingMessage[:charactertyped])
        Typed = True

    if gameoverscreen.Textinit == True:
        if TypedCharacterAwaitReset == True:
            charactertyped = 0
            TypedCharacterAwaitReset = False
        AuthorMessageTyped = FONT.render(characters,False,WHITE)
        screen.blit(AuthorMessageTyped,(WIDTH//2 - 11*20,HEIGHT//1.1))

    TitleMessageTyped= TITLEFONT.render(characters,False,WHITE)

    
    if Gamebegun == True and Gameover == False:
        all_sprites.draw(screen)
        particles.draw(screen)
        platforms.draw(screen)
        infos.draw(screen)
        if GameSTART == True:
            Mouseanim = Mousereticle[Playerspellselection-1]
            screen.blit(Mouseanim,(mx-15,my - 15))

    


    if GameSTART == True and Gameover == False:

        ##Key Rendering
        for Number in range(5):
            MessageNumber = str(Number+1)
            MessageKey = TITLEFONT.render(MessageNumber, False, WHITE)
            textxpos = (250*(Number+1))+40
            screen.blit(MessageKey,(textxpos,HEIGHT//1.225))
            
        ##Infobar Coin rendering  
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
        screen.blit(ScoreMessage,(WIDTH-250,30))
            
    if Gamebegun == False:
        AuthorMessage = FONT.render("By Tyler Lynch",False,(WHITE))
        screen.blit(TitleMessageTyped,(WIDTH//2-(420),HEIGHT//2))
        screen.blit(AuthorMessage,(WIDTH//2-(113),HEIGHT//1.2))
    ##after render flip display
    pygame.display.flip()
    
pygame.quit()
        
