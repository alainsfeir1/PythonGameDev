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
################################
Gameloop=True
mainMenu=True
Stage1=True
Stage2=True
#################

class GameObjects(pygame.sprite.Sprite):
    def __init__(self,  x, y,width,height,imageloaded):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load(imageloaded)
        self.image = image
        self.image=pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx=2
        self.dy=2
        
    def update(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        if self.rect.top >550:
            self.dx=2
            self.dy=-2
        if self.rect.top<0:
            self.dx=-2
            self.dy=2
        if self.rect.left<0:
            self.dx=2
            self.dy=2
        if self.rect.left>550:
            self.dx=-2
            self.dy=-2
            
            
#game groups
Gameobjects_stage2=pygame.sprite.Group(())
stage2= pygame.image.load("stage2.png")
stage2=pygame.transform.scale(stage2,(Width,Height))
RoadPass=GameObjects(0,0,50,50,"coin.png")
RoadPass.add(Gameobjects_stage2)
Shroom1=GameObjects(500,500,50,50,"shrooms.bmp")
Shroom1.add(Gameobjects_stage2)
Shroom2=GameObjects(0,400,50,50,"shrooms.bmp")
Shroom2.add(Gameobjects_stage2)

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.blit(stage2,(0,0))
        Gameobjects_stage2.update()
        
        Gameobjects_stage2.draw(display)
       
        Shroom1.update()
        Shroom2.update()
        
        pygame.display.update()
        mainClock.tick(30)
