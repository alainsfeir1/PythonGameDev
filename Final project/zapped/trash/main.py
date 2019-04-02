import pygame,sys,random

pygame.init()
Width=600
Height=600
White=(255,255,255)
Black=(0,0,0)
Red=(255, 0,0)
pygame.display.set_caption("Zapped!!")
display=pygame.display.set_mode((Width,Height))
playersize=50

mainClock = pygame.time.Clock()
#game groups
playersGroup= pygame.sprite.Group(())
Gameobjects_stage1=pygame.sprite.Group(())

class Player(pygame.sprite.Sprite):
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
        
            
    def update(self):
            key = pygame.key.get_pressed()
      
            if  key[pygame.K_LEFT] and  self.rect.x > 0:
                self.rect.left -= Player.movement_speed

            if  key[pygame.K_RIGHT] and self.rect.x <= 600-Player.playersize:
                self.rect.left += Player.movement_speed
            
            if  key[pygame.K_UP] and self.rect.y>0:
                self.rect.top-=Player.movement_speed
            if  key[pygame.K_DOWN] and self.rect.y<=600-Player.playersize:
                self.rect.top+=Player.movement_speed

    def collisionHouses(self,player,house1,house2,house3,house4,policecar,policecar2):
        for items in pygame.sprite.groupcollide(playersGroup,Gameobjects_stage1,0,1):
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
            if collision5==True:
                policecar=GameObjects(550,300,50,50,"policecar.png")
                policecar.add(Gameobjects_stage1)
                self.rect.left-=Player.movement_speed
            if collision6==True:
                policecar2=GameObjects(550,250,50,50,"policecar.png")
                policecar2.add(Gameobjects_stage1)
                self.rect.left-=Player.movement_speed

               
            
        
            
            
class Introscreen():
    def Color_screen(color,display):
        display.fill(color)
    def messageScreen(self,msg,color,screen,x,y,sizefont):#display text on screen
        basicfont = pygame.font.SysFont(None, sizefont)
        text = basicfont.render(msg, True,color)
        screen.blit(text,(x,y))
    
    def backgroundpicture(image,display):
        background=pygame.image.load(image)
        background=pygame.transform.scale(background, (600, 600))
        display.blit(background,[0,0])
    def setScreen(colortext1,colortext2,colorback,display,backgroundpic):
        Introscreen.Color_screen(colorback,display)
        Introscreen.backgroundpicture(backgroundpic,display) 
        Introscreen.messageScreen(0,'Press "S" to Start Game!',colortext1,display,100,200,48)
        Introscreen.messageScreen(0,'Press "Q" to Quit Game!',colortext2,display,100,300,48)
        
    def IntroMenuInput(display,mainmenu,gameloop):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    mainmenu=False
                    gameloop=False
                    pygame.quit()
                    sys.exit()
                if event.key==pygame.K_s:
                    mainmenu=False
        return mainmenu,gameloop
class GameObjects(pygame.sprite.Sprite):
    def __init__(self,  x, y,width,height,imageloaded):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(imageloaded)
        self.image = image
        self.image=pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
            
def main():
    player1=Player(300,300,"car1.png")
    player1.add(playersGroup)
    #stage 1 objects
    stage1 = pygame.image.load("stage1.png")
    stage1=pygame.transform.scale(stage1,(Width,Height))
    house1=GameObjects(0,0,200,200,"house4.png")
    house1.add(Gameobjects_stage1)
    house2=GameObjects(400,0,200,200,"house3.png")
    house2.add(Gameobjects_stage1)
    house3=GameObjects(0,400,200,200,"house2.png")
    house3.add(Gameobjects_stage1)
    house4=GameObjects(400,400,200,200,"house1.png")
    house4.add(Gameobjects_stage1)
    policecar=GameObjects(550,300,50,50,"policecar.png")
    policecar.add(Gameobjects_stage1)
    policecar2=GameObjects(550,250,50,50,"policecar.png")
    policecar2.add(Gameobjects_stage1)
    
    
    Gameloop=True
    mainMenu=True
    Stage1=True
    
    while Gameloop:
        while mainMenu:
            Introscreen.setScreen(Red,Red,White,display,"background.jpg")
            mainMenu,Gameloop=Introscreen.IntroMenuInput(display,mainMenu,Gameloop)
            pygame.display.update()
        while Stage1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            display.blit(stage1,(0,0))
            Gameobjects_stage1.update()
            playersGroup.update()
            Gameobjects_stage1.draw(display)
            playersGroup.draw(display)
            player1.collisionHouses(player1,house1,house2,house3,house4,policecar,policecar2)
            pygame.display.update()
            mainClock.tick(30)
main()
    
            
