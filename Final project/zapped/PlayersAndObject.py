import pygame,sys,random,time,os
from screenMods import *
pygame.init()
Width=600
Height=600
White=(255,255,255)
Black=(0,0,0)
Red=(255, 0,0)
display=pygame.display.set_mode((Width,Height))

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname)
    return image, image.get_rect()

def load_sound(name):
    fullname = os.path.join('data', name)
    sound = pygame.mixer.Sound(fullname)
    return sound
def write_level(file,level):
    savefile=open(file,'w')
    savefile.write(level)
    savefile.close()

class Player(pygame.sprite.Sprite):
    global Stage1
##    playersize=50
    movement_speed=5
    global Red
    global display


    def __init__(self,  x, y,imageloaded,playersize):
        pygame.sprite.Sprite.__init__(self)
        imageloaded="players/"+str(imageloaded)
        self.image, self.rect=load_image(str(imageloaded), colorkey=None)
        self.playersize=playersize
        self.image=pygame.transform.scale(self.image,(self.playersize,self.playersize))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.score=0
        self.health=100
        self.healthFinal=1000
        self.level=1
        self.shield=1
        self.key=False
        
        
            
    def update(self,  X_boundariesR,  X_boundariesL,  Top,  Bottom):
            key = pygame.key.get_pressed()
      
            if  key[pygame.K_LEFT] and  self.rect.x >X_boundariesR:
                self.rect.left -= Player.movement_speed

            if  key[pygame.K_RIGHT] and self.rect.x <= X_boundariesL-self.playersize:
                self.rect.left += Player.movement_speed
            
            if  key[pygame.K_UP] and self.rect.y>Top:
                self.rect.top-=Player.movement_speed
            if  key[pygame.K_DOWN] and self.rect.y<=Bottom-self.playersize:
                self.rect.top+=Player.movement_speed
##    def update2(self,  X_boundariesR,  X_boundariesL,  Top,  Bottom):
##            key = pygame.key.get_pressed()
##      
##            if  key[pygame.K_d] and  self.rect.x >X_boundariesR:
##                self.rect.left -= Player.movement_speed
##
##            if  key[pygame.K_a] and self.rect.x <= X_boundariesL-self.playersize:
##                self.rect.left += Player.movement_speed
##            
##            if  key[pygame.K_w] and self.rect.y>Top:
##                self.rect.top-=Player.movement_speed
##            if  key[pygame.K_s] and self.rect.y<=Bottom-self.playersize:
##                self.rect.top+=Player.movement_speed
    def Shoot(self,bulletgroup):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] :
                bulletgroup.add(bullet(self.rect.x,self.rect.y))
                
            


    def collisionHouses(self,playersGroup,Gameobjects_stage1,player,house1,house2,house3,house4,policecar,policecar2,Stage5,Stage4,Stage3,Stage2,Stage1,mainMenu,Gameloop):
        for items in pygame.sprite.groupcollide(playersGroup,Gameobjects_stage1,0,0):
            collision1 = pygame.sprite.collide_rect(player,house1)
            collision2= pygame.sprite.collide_rect(player,house2)
            collision3 = pygame.sprite.collide_rect(player,house3)
            collision4 = pygame.sprite.collide_rect(player,house4)
            collision5 = pygame.sprite.collide_rect(player,policecar)
            collision6 = pygame.sprite.collide_rect(player,policecar2)
            if collision1==True:
                if self.key==False:
                    house1=GameObjects(0,0,200,200,"house4.png")
                    house1.add(Gameobjects_stage1)
                    self.rect.left+=Player.movement_speed
                    self.rect.top+=Player.movement_speed
                    houseMessage=Introscreen()
                    houseMessage.messageScreen("This is the house of the mafia lord",Red,display,0,250,30)
                    houseMessage.messageScreen("You need money inorder to buy REALITY SHIFTER",Red,display,0,300,30)
                else:
                    print("game over")
                    Stage5=True
                    Stage4=False
                    Stage3=False
                    Stage2=False
                    Stage1=False
                    mainMenu=False
                    Gameloop=True
                    
                    
                
                
            if collision2==True:
                house2=GameObjects(400,0,200,200,"house3.png")
                house2.add(Gameobjects_stage1)
                self.rect.left-=Player.movement_speed
                self.rect.top+=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("Future of multiplayer online!!",Red,display,0,250,30)
                
                
                
            if collision3==True:
                house3=GameObjects(0,400,200,200,"house2.png")
                house3.add(Gameobjects_stage1)
                self.rect.left+=Player.movement_speed
                self.rect.top-=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("Access Denied!!",Red,display,0,250,30)
                
            if collision4==True:
                house4=GameObjects(400,400,200,200,"house1.png")
                house4.add(Gameobjects_stage1)
                self.rect.left-=Player.movement_speed
                self.rect.top-=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("Enter Challenge",Red,display,0,250,30)
                houseMessage.messageScreen("to win the Road pass",Red,display,0,300,30)
                pygame.time.wait(5000)
                Stage1=False
                Stage2=True

            if collision6==True or collision5==True:
                if self.level==2:
                    houseMessage=Introscreen()
                    houseMessage.messageScreen("You can pass",Red,display,0,250,30)
                else:
                    policecar=GameObjects(230,0,60,60,"policecar.png")
                    policecar.add(Gameobjects_stage1)
                    
                    policecar2=GameObjects(320,0,60,60,"policecar.png")
                    policecar2.add(Gameobjects_stage1)
                    self.rect.top+=Player.movement_speed
                    houseMessage=Introscreen()
                    houseMessage.messageScreen("You cannot pass",Red,display,0,250,30)
                    houseMessage.messageScreen("You need a special pass to access from the house",Red,display,0,300,30)
        return Stage5,Stage4,Stage3,Stage2,Stage1,mainMenu,Gameloop
    
    def Stage2_Collisions(self,playersGroup,Gameobjects_stage2,
                                              player,
                                              RoadPass,
                                              shroom1,shroom2,shroom3,
                                              bomb,bomb2,healthpod,
                                              stage2):
        write_level("save.txt","2")
        for items in pygame.sprite.groupcollide(playersGroup,Gameobjects_stage2,0,0):
            collision1 = pygame.sprite.collide_rect(player,RoadPass)
            collision2= pygame.sprite.collide_rect(player,shroom1)
            collision3 = pygame.sprite.collide_rect(player,shroom2)
            collision4 = pygame.sprite.collide_rect(player,shroom3)
            collision5=  pygame.sprite.collide_rect(player,bomb)
            collision6=  pygame.sprite.collide_rect(player,healthpod)
            collision7=  pygame.sprite.collide_rect(player,bomb2)
            
            if collision1==True:
                soundloaded="sounds/"+"coin.wav"
                coin=load_sound(str(soundloaded))
                coin.play()
                RoadPass.rect.x=random.randint(50,550)
                RoadPass.rect.y=random.randint(50,550)
                self.score+=1
                bomb.add(Gameobjects_stage2)
                bomb2.add(Gameobjects_stage2)
                healthpod.add(Gameobjects_stage2)
                
                
            if collision2==True:
                self.health-=1
            if collision3==True:
                self.health-=1
            if collision4==True:
                self.health-=1
            if collision5==True:
                self.health-=50
                bomb_sound="sounds/"+"explosion.wav"
                bomb_sound=load_sound(bomb_sound)
                bomb_sound.play()
                bomb.kill()
            if collision6==True:
                self.health+=15
                healthpod.kill()
            if collision7==True:
                bomb_sound="sounds/"+"explosion.wav"
                bomb_sound=load_sound(bomb_sound)
                bomb_sound.play()
                self.health-=50
                bomb2.kill()
    def GameOverStage2(self,Gameloop,mainMenu,Stage1,Stage2):
        if self.health<=0:
            Stage2=True
            Gameloop=True
            mainMenu=True
            Stage1=False
            self.health=100
        if self.score==10:
            Stage2=False
            Gameloop=True
            mainMenu=False
            Stage1=True
            write_level("save.txt","3")
            self.health=100
            self.level=2
            self.score=0
        return Gameloop,mainMenu,Stage1,Stage2
    def Stage3_Collisions(self,playersGroup,Gameobjects_stage3,
                                              player,
                                              stage3):
         for hit in pygame.sprite.groupcollide(playersGroup, Gameobjects_stage3, 0, 1):
            self.shield -= 1
            if self.shield==0:
                accident_sound="sounds/"+"car.wav"
                accident_sound=load_sound(accident_sound)
                accident_sound.play()
                playersGroup.remove(player)
                time.sleep(2)
             
                
    def GameOverStage3(self,Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4,playersGroup,player):
        if self.shield<=0:
            Stage2=False
            Gameloop=True
            mainMenu=True
            Stage1=True
            Stage2=True
            Stage3=False
            self.shield=1
            self.score=0
            playersGroup.add(player)
            
        if self.score>=500 and self.rect.y==0:
            Stage2=False
            Gameloop=True
            mainMenu=False
            Stage1=False
            Stage3=False
            Stage4=True
            write_level("save.txt","4")
            self.shield=1
            self.level=3
        return Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4
    
    def GameOverStage4(self,Gameloop,mainMenu,
                                           Stage1,Stage2,Stage3,Stage4,superman,player1):
        if superman.BossHealth<=0:#check if game ended
                Gameloop=True
                mainMenu=False
                Stage1=True
                Stage2=False
                Stage3=False
                Stage4=False
                superman.BossHealth=1000
                player1.key=True
                player1.rect.x=300
                player1.rect.y=300
        return Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4
        
        
              
            
            
    

            
                
class GameObjects(pygame.sprite.Sprite):
    
    def __init__(self,  x, y,width,height,imageloaded):
        pygame.sprite.Sprite.__init__(self)
        imageloaded="objects/"+str(imageloaded)
        self.image, self.rect=load_image(str(imageloaded), colorkey=None)
        self.image=pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx=8
        self.dy=8
        self.BossHealth=5000
        
    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top >550:
            self.dx=8
            self.dy=-8
        if self.rect.top<0:
            self.dx=-8
            self.dy=8
        if self.rect.left<0:
            self.dx=8
            self.dy=8
        if self.rect.left>550:
            self.dx=-8
            self.dy=-8
    def moveStage4(self):
        self.rect.centerx += self.dx
        if self.rect.left<0:
            self.dx=8
        if self.rect.left>500:
            self.dx=-8
            self.dy=-8
        


class Stage3Cars(pygame.sprite.Sprite):
    def __init__(self, centerx):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("objects/stage3Car.png", -1)
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.dy = 8
        self.reset()
        
    def update(self):

        self.rect.centery += self.dy
        if self.rect.top > 600:
            self.reset()
           
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(100, 550)
        self.dy = random.randrange(5, 10)
class bullet(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("objects/bullet.png", -1)
        self.image=pygame.transform.scale(self.image,(50,50))
        self.rect.x = x
        self.rect.y=y

    
    def update(self):
        if self.rect.top < 0:
            self.kill()
        else:    
            self.rect.move_ip(0, -15)
class Rocks(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("objects/rock.png", -1)
        self.image=pygame.transform.scale(self.image,(80,80))
        self.rect.x = random.randint(50,550)
        self.rect.y=0
        self.dy = 8
        self.reset()
        
    def update(self):
        self.rect.centery += self.dy
##        self.rect.centerx-=self.dy
        if self.rect.top > 600:
            self.kill()
            self.reset()
           
    def reset(self):
        self.rect.bottom = 0
        self.rect.centerx = random.randrange(100, 550)
        self.dy = random.randrange(5, 10)
class superlaser(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("objects/laser.png", -1)
        self.image=pygame.transform.scale(self.image,(25,25))
        self.rect.x = x
        self.rect.y=y

    
    def update(self):
        if self.rect.top > 600:
            self.kill()
        else:    
            self.rect.move_ip(0, 15)
        
        
        
        
        
       
            
        
            
    
        
            
            
            
            
            
            
            
        
        
