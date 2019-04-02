#developer:Alain Sfeir
#date:4/132/2018
#file:Tankshooter.py
#description: mods and fixes to the original tank shooter game

import pygame
from pygame.locals import *
import math, random, time, sys

pygame.init()

screen = pygame.display.set_mode((640,480))

font = pygame.font.SysFont("arial",16)

clock = pygame.time.Clock()


end_game = False

ammo = 20
score = 0

ammoDisplay = font.render(str(ammo),1,(0,0,0))
scoreDisplay = font.render(str(score),1,(0,0,0))

screen.blit(scoreDisplay,(10,10))
screen.blit(ammoDisplay, (10,20))

playField = pygame.sprite.Group(())
player = pygame.sprite.Group(())
gun = pygame.sprite.Group(())
enemy = pygame.sprite.Group(())
missile = pygame.sprite.Group(())

#We need a HERO

class Tank(pygame.sprite.Sprite):
    image = pygame.image.load("tank.bmp")
    GunX = 0
    GunY = 0
    GunAngle = 0
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #super(Tank, self).__init__(Tank.image, x = x, y = y)
        self.image = Tank.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect.x = x
        self.rect.y = y
        
        Tank.GunX =  self.rect.x + self.rect.width/2 - 12
        Tank.GunY = self.rect.top + 6
        
        the_gun = Gun(Tank.GunX  , Tank.GunY)
        gun.add(the_gun)
    
        self.missile_wait = 0
   # new code #     
    def stop_message(self):
            
            stop_message = font.render("Not allowed past this point, Please reverse direction",1,(255,0,0))
            screen.blit(stop_message,(screen.get_width()/2,screen.get_height()/2))
               
    def update(self):
        global ammo
        global end_game
        key = pygame.key.get_pressed()
        
        if self.missile_wait > 0:
            self.missile_wait -= 1       
        if key[K_LEFT] and  self.rect.x > 20:
            self.rect.left -= 1
            Tank.GunX -= 1
        if key[K_RIGHT] and self.rect.x <= 346:
            self.rect.left += 1
            Tank.GunX += 1
        if self.rect.x >= 346:
            self.stop_message()
        
        if key[K_SPACE] and self.missile_wait == 0 and self.rect.x <= 346:
            new_missile = Missile(self.rect.x, self.rect.y, Tank.GunAngle )
            missile.add(new_missile)
            self.missile_wait = Tank.MISSILE_DELAY

            ammo -= 1
            #ammo.left = 10
            #new
            if ammo <= 0:
                end_game = True
                
class Missile(pygame.sprite.Sprite):

    image = pygame.image.load("missile.bmp")

    BUFFER = 40
    VELOCITY_FACTOR = 7
    LIFETIME = 25
    TT = 0
    SX = 0
    SY = 0

    def __init__(self, tank_x, tank_y, tank_angle):
        """ Initialize missile sprite. """
        pygame.sprite.Sprite.__init__(self)
        self.image = Missile.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        # convert to radians
        self.angle = (tank_angle + 90) * math.pi / 180  
        self.tank_x = tank_x
        self.tank_y = tank_y
        # calculate missile's starting position 
        self.buffer_x = Missile.BUFFER * math.sin(self.angle)
        self.buffer_y = Missile.BUFFER * -math.cos(self.angle)
        self.rect.x = tank_x + self.buffer_x
        self.rect.y = tank_y + self.buffer_y

        # calculate missile's velocity components
        self.dx = Missile.VELOCITY_FACTOR * math.sin(self.angle)
        self.dy = Missile.VELOCITY_FACTOR * -math.cos(self.angle)


         # calculate missile's velocity components
        self.vx = self.dx
        self.vy = self.dy
        self.lifetime = Missile.LIFETIME

    def collide(self): 
        print ("collide")


    def die(self):
        """ Destroy self and leave explosion behind. """
       
        new_explosion = Explosion(x = self.rect.x, y = self.rect.y)
        playField.add(new_explosion)

        self.kill()
        
             
    def update(self):
        global GRAVITY
        """ Move the missile. """
        #super(Missile, self).update() 
        
        time.sleep(.01)            
        
        # if lifetime is up, start the decent   
        self.lifetime -= 1
        #using the projectiles formula for x and y components
        #y=1/2at^2 +Vot+yo and x=vt+xo where a is gravity
        #self.tt is time dy and dx are vectors of speed and
        #self.rect.x and self.rect.y are xo and yo respectivley
        if self.lifetime <= 0:

            self.SX = self.rect.x
            self.SY = self.rect.y

            self.rect.x = int(self.dx * self.TT + self.rect.x)
            self.rect.y = int ((0.5 * GRAVITY * self.TT * self.TT) + (self.dy * self.TT) + self.rect.y)

            self.TT += .25
        else:
            
            self.SX = self.rect.x
            self.SY = self.rect.y

            self.rect.x = int(self.dx * self.TT + self.rect.x)
            self.rect.y = int ((0.5 * GRAVITY * self.TT * self.TT) + (self.dy * self.TT) + self.rect.y)

            self.TT += 0.25
        self.check_collide()
        
        self.check_kill_enemy()
        
    def check_collide(self):
        if self.rect.y > 344:
            self.die()
            
    def check_kill_enemy(self):
        global score
        
        for e in pygame.sprite.groupcollide(missile,enemy,0,1):
            #enemy.kill()
            self.die()
            #new"Update SCORE"
            score += 10
            #score.right = screen.width - 10
            
            the_enemy = Enemy()
            enemy.add(the_enemy)

class Gun(pygame.sprite.Sprite):
    image = pygame.image.load("gun.bmp")
 
    #Create a surface over the sprite and then rotate that surface with the
    #pygame.transform.rotate method 
    def __init__(self,  tank_x, tank_y):
        pygame.sprite.Sprite.__init__(self)
        self.imageOrigninal = Gun.image
        self.imageOrigninal = self.imageOrigninal.convert()#converts to surface.
        self.image=self.imageOrigninal
        self.rect = self.image.get_rect()
        self.rect.center = (Tank.GunX+24, Tank.GunY-5)
        self.gunAngle=0#angle by with surface will rotate
        



##        self.rect = self.image.get_rect()
##        self.image.set_colorkey(self.image.get_at((0,0)))
##        self.rect.x = tank_x
##        self.rect.y = tank_y
        self.angle = 90
        
    def update(self):
        
        key = pygame.key.get_pressed()
        
        if key[K_UP]:
            self.angle -= 1
            Tank.GunAngle -= 1
            self.gunAngle+=1
                
        if key[K_DOWN]:
            self.angle += 1
            Tank.GunAngle += 1
            self.gunAngle-=1
        #conditionals for the surface gun image angles
        if self.gunAngle>90:
            self.gunAngle-=1
        if self.gunAngle==0:
            self.gunAngle+=1
            

        if Tank.GunAngle < -90:
                self.angle += 1
                Tank.GunAngle += 1
             
        if Tank.GunAngle > 0:
            self.angle -= 1
            Tank.GunAngle -= 1
        #pygame function for rotation which requires
        #a  surface=self.imageOrigninal and a angle=self.gunAngle
        self.image = pygame.transform.rotate(self.imageOrigninal, self.gunAngle)
        self.rect = self.image.get_rect()
        #adding some values to x and y so it looks like
        #it is on the tip of the tank like barrel
        self.rect.left = Tank.GunX+13
        self.rect.bottom = Tank.GunY-2

class Explosion(pygame.sprite.Sprite):
    """ Explosion animation. """
    #sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("explosion2.bmp")
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        #self.rect.x = x
        #self.rect.y = y
        self.rect.center = (x,y)
        self.repeat = 5
        # self.repeat_interval = 4
        # self.repeat_interval = 4
        self.is_collideable = False
        
    def update(self):
        pygame.sprite.Sprite.update(self)
        self.repeat -= 1
        if self.repeat == 0:
            self.kill()
        

class Enemy(pygame.sprite.Sprite):
    
    image = pygame.image.load("enemy.bmp")

   
    def __init__(self, speed = 1, odds_change = 200):
        pygame.sprite.Sprite.__init__(self)
        self.image = Enemy.image
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect.x = 600
        self.rect.y = 344
        self.dx = speed
        
        # super(Enemy, self).__init__(image = Enemy.image,
                                   # x = 600,
                                   # y = 344,
                                   # dx = speed)
        
        self.odds_change = odds_change



    def update(self):
        """ Determine if direction needs to be reversed. """
        if self.rect.left < 400 or self.rect.right > screen.get_width():
           self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
           self.dx = -self.dx
        
        self.rect.x += self.dx


class Church(pygame.sprite.Sprite):
    image = pygame.image.load("church.bmp")
    def __init__(self,  x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Church.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_collidable = False

        # super(Church, self).__init__(image = Church.image,
                                      # x = x, y = y,
                                     # is_collideable = False)


# def end_game():
    
    # end_message = font.render("Game Over",1,(255,0,0))
    # screen.blit(end_message,(screen.get_width()/2,screen.get_height()/2))
    # pygame.display.flip()
    # wait(1000)
    # pygame.event.post(pygame.event.Event(QUIT))
    # #input()
    
                                     
def main():
    
    
    global GRAVITY
    GRAVITY =2.5
    
    # establish background
    background_image = pygame.image.load("background.jpg")
    #game.screen.background = background_image
    
    
    
##    #load tank
    the_tank = Tank( x = 100, y = 344)
    player.add(the_tank)
## 
    the_enemy = Enemy()
    enemy.add(the_enemy)
##    
    the_church = Church( x = 380, y = 333)
    playField.add(the_church)
    
    #game.screen.mainloop()
    loop = True
    while loop:
        clock.tick(30)
        #if ammo <= 0:
            #end_game()
            #loop = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               
                loop = False
        #screen.fill((0,0,0))
        screen.blit(background_image,(0,0))
        ammoDisplay = font.render("Ammo: " + str(ammo),1,(0,0,0))
        scoreDisplay = font.render("Score" + str(score),1,(0,0,0))

        screen.blit(scoreDisplay,(10,10))
        screen.blit(ammoDisplay, (10,25))
        
        if end_game:
            end_message = font.render("Game Over",1,(255,0,0))
            screen.blit(end_message,(screen.get_width()/2,screen.get_height()/2))
            loop = False
        
        player.update()
        gun.update()
        enemy.update()
        missile.update()
        playField.update()
        player.draw(screen)
        gun.draw(screen)
        enemy.draw(screen)
        missile.draw(screen)
        playField.draw(screen)
        pygame.display.flip()
    if end_game:
        pygame.time.wait(2000)
# kick it off!
main()


