import pygame,sys,random,time
from screenMods import *
pygame.init()
Width=600
Height=600
White=(255,255,255)
Black=(0,0,0)
Red=(255, 0,0)
display=pygame.display.set_mode((Width,Height))

class Player(pygame.sprite.Sprite):
    global Stage1
    playersize=50
    movement_speed=5
    global Red
    global display

    def __init__(self,  x, y,imageloaded):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(imageloaded)
        self.image = image
        self.image=pygame.transform.scale(self.image,(Player.playersize,Player.playersize))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
            
    def update(self,  X_boundariesR,  X_boundariesL,  Top,  Bottom):
            key = pygame.key.get_pressed()
      
            if  key[pygame.K_LEFT] and  self.rect.x >X_boundariesR:
                self.rect.left -= Player.movement_speed

            if  key[pygame.K_RIGHT] and self.rect.x <= X_boundariesL-Player.playersize:
                self.rect.left += Player.movement_speed
            
            if  key[pygame.K_UP] and self.rect.y>Top:
                self.rect.top-=Player.movement_speed
            if  key[pygame.K_DOWN] and self.rect.y<=Bottom-Player.playersize:
                self.rect.top+=Player.movement_speed
            


    def collisionHouses(self,playersGroup,Gameobjects_stage1,player,house1,house2,house3,house4,policecar,policecar2, stage1 , stage2):
        for items in pygame.sprite.groupcollide(playersGroup,Gameobjects_stage1,0,0):
            collision1 = pygame.sprite.collide_rect(player,house1)
            collision2= pygame.sprite.collide_rect(player,house2)
            collision3 = pygame.sprite.collide_rect(player,house3)
            collision4 = pygame.sprite.collide_rect(player,house4)
            collision5 = pygame.sprite.collide_rect(player,policecar)
            collision6 = pygame.sprite.collide_rect(player,policecar2)
            if collision1==True:
                house1=GameObjects(0,0,200,200,"house4.png")
                house1.add(Gameobjects_stage1)
                self.rect.left+=Player.movement_speed
                self.rect.top+=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("This is the house of the mafia lord",Red,display,0,250,30)
                houseMessage.messageScreen("You need money inorder to buy REALITY SHIFTER",Red,display,0,300,30)
                
                
            if collision2==True:
                house2=GameObjects(400,0,200,200,"house3.png")
                house2.add(Gameobjects_stage1)
                self.rect.left-=Player.movement_speed
                self.rect.top+=Player.movement_speed
                
                
            if collision3==True:
                house3=GameObjects(0,400,200,200,"house2.png")
                house3.add(Gameobjects_stage1)
                self.rect.left+=Player.movement_speed
                self.rect.top-=Player.movement_speed
            if collision4==True:
                house4=GameObjects(400,400,200,200,"house1.png")
                house4.add(Gameobjects_stage1)
                self.rect.left-=Player.movement_speed
                self.rect.top-=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("Enter Challenge",Red,display,0,250,30)
                houseMessage.messageScreen("to win the Road pass",Red,display,0,300,30)
                #time.sleep(2)
                stage1=False
                stage2=True
                
                            
                
            if collision5==True:
                policecar=GameObjects(230,0,60,60,"policecar.png")
                policecar.add(Gameobjects_stage1)
                self.rect.top+=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("You cannot pass",Red,display,0,250,30)
                houseMessage.messageScreen("You need a special pass to access from the house",Red,display,0,300,30)
            if collision6==True:
                policecar2=GameObjects(320,0,60,60,"policecar.png")
                policecar2.add(Gameobjects_stage1)
                self.rect.top+=Player.movement_speed
                houseMessage=Introscreen()
                houseMessage.messageScreen("You cannot pass",Red,display,0,250,30)
                houseMessage.messageScreen("You need a special pass to access from the house",Red,display,0,300,30)
        return stage1,stage2
    def Stage2_Collisions(self,playersGroup,Gameobjects_stage2,
                                              player,
                                              RoadPass,
                                              shroom1,shroom2,
                                              stage2):
        for items in pygame.sprite.groupcollide(playersGroup,Gameobjects_stage2,0,0):
            collision1 = pygame.sprite.collide_rect(player,RoadPass)
            collision2= pygame.sprite.collide_rect(player,shroom1)
            collision3 = pygame.sprite.collide_rect(player,shroom2)
            if collision1==True:
                RoadPass.rect.x=random.randint(50,550)
                RoadPass.rect.y=random.randint(50,550)
            if collision2==True:
                print("X")
            if collision3==True:
                print("X")
                
class GameObjects(pygame.sprite.Sprite):
    
    def __init__(self,  x, y,width,height,imageloaded,):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(imageloaded)
        self.image = image
        self.image=pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction="bottomleft"
        
    def move(self,MOVESPEED,WINDOWHEIGHT,WINDOWWIDTH):
        if self.direction=="bottomleft":
            self.rect.left-=MOVESPEED
            self.rect.top+=MOVESPEED
        if self.direction == "downleft":
            self.rect.left += MOVESPEED
            self.rect.top += MOVESPEED
        if self.direction == "upleft":
            self.rect.left -= MOVESPEED
            self.rect.top -= MOVESPEED
        if self.direction== "upright":
            self.rect.left += MOVESPEED
            self.rect.top -= MOVESPEED
        if self.rect.top <= 0:
            # The box has moved past the top.
            #this is like action reaction
            #new direction is set and it will loop the for b in boxes again
            if self.direction == "upleft":
                self.direction = "downleft"
            if self.direction == "upright":
                self.direction = "downright"
        if self.rect.bottom >= WINDOWHEIGHT:
            # The box has moved past the bottom.
            if self.direction == "downleft":
                self.direction = "upleft"
            if self.direction == "downright":
                self.direction = "upright"
        if self.rect.left <= 0:
            # The box has moved past the left side.
            if self.direction == "downleft":
                self.direction = "downright"
            if self.direction == "upleft":
                self.direction = "upright"
        if self.rect.right >= WINDOWWIDTH:
            # The box has moved past the right side.
            if self.direction == "downright":
                self.direction = "downleft"
            if self.direction == "upright":
                self.direction = "upleft"
            
            
        
            
    
        
            
            
            
            
            
            
            
        
        
