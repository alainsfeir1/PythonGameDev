import pygame,sys
def write_level(file,level):
    savefile=open(file,'w')
    savefile.write(level)
    savefile.close()
def savefile(file,Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4):
    savefile=open(file,'r')
    level=savefile.readline().replace('/n', '')

    if level=='1':
        Gameloop=True
        mainMenu=False#true
        Stage1=True#true
        Stage2=True#true
        Stage3=False#false
        Stage4=False#false
        
    if level=='2':
        Gameloop=True
        mainMenu=True#true
        Stage1=True#true
        Stage2=True#true
        Stage3=False#false
        Stage4=False#false
    if level=='3':
        Gameloop=True
        mainMenu=False#true
        Stage1=False#true
        Stage2=False#true
        Stage3=True#false
        Stage4=False#false
    if level=='4':
        Gameloop=True
        mainMenu=False#true
        Stage1=False#true
        Stage2=False#true
        Stage3=False#false
        Stage4=True#false
    savefile.close()
    return Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4

pygame.init()
Width=600
Height=600
White=(255,255,255)
Black=(0,0,0)
Red=(255, 0,0)
display=pygame.display.set_mode((Width,Height))
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
        Introscreen.messageScreen(0,'Press "S" to Start Game!',colortext1,display,0,200,48)
        Introscreen.messageScreen(0,'Press "C" to Continue Game!',colortext2,display,0,300,48)
        Introscreen.messageScreen(0,'Press "Q" to Quit Game!',colortext2,display,0,400,48)
        
    def IntroMenuInput(display,mainmenu,gameloop,stage1,stage2,stage3,stage4):
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
                    stage1=True
                    stage2=True
                    write_level("save.txt","1")
                if event.key==pygame.K_c:
                    gameloop,mainmenu,stage1,stage2,stage3,stage4=savefile("save.txt",gameloop,mainmenu,stage1,stage2,stage3,stage4)
                    
        return mainmenu,gameloop,stage1,stage2,stage3,stage4
