import pygame,sys,random
from PlayersAndObject import*
from screenMods import *
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
mainMenu=True#true
Stage1=False#true
Stage2=False#true
Stage3=False#false
Stage4=False#false
Stage5=False
#################
#game groups
playersGroup1= pygame.sprite.Group(())
playersGroup2=pygame.sprite.Group(())
playersGroup3=pygame.sprite.Group(())
playersGroup4=pygame.sprite.Group(())
Gameobjects_stage1=pygame.sprite.Group(())
Gameobjects_stage2=pygame.sprite.Group(())
Gameobjects_stage3=pygame.sprite.Group(())
Gameobjects_stage4=pygame.sprite.Group(())
bulletgroup=pygame.sprite.Group(())
rocks=pygame.sprite.Group(())
superman_laser=pygame.sprite.Group(())

#player object
player1=Player(300,300,"car1.png",50)
player1.add(playersGroup1)
#stage 1 objects
stage1 = pygame.image.load("stage1_fixed.png")
stage1=pygame.transform.scale(stage1,(Width,Height))
house1=GameObjects(0,0,200,200,"house4.png")
house1.add(Gameobjects_stage1)
house2=GameObjects(400,0,200,200,"house3.png")
house2.add(Gameobjects_stage1)
house3=GameObjects(0,400,200,200,"house2.png")
house3.add(Gameobjects_stage1)
house4=GameObjects(400,400,200,200,"house1.png")
house4.add(Gameobjects_stage1)
policecar=GameObjects(230,0,60,60,"policecar.png")
policecar.add(Gameobjects_stage1)
policecar2=GameObjects(320,0,60,60,"policecar.png")
policecar2.add(Gameobjects_stage1)
print("Stage1 Objects")
##########################################
#stage2 Objects
stage2= pygame.image.load("stage2.png")
stage2=pygame.transform.scale(stage2,(Width,Height))
RoadPass=GameObjects(0,0,50,50,"coin.png")
RoadPass.add(Gameobjects_stage2)
Shroom1=GameObjects(250,500,50,50,"shrooms.png")
Shroom1.add(Gameobjects_stage2)
Shroom2=GameObjects(0,100,50,50,"shrooms.png")
Shroom2.add(Gameobjects_stage2)
Shroom3=GameObjects(500,300,50,50,"shrooms.png")
Shroom3.add(Gameobjects_stage2)
positionx=random.randint(0,500)
positiony=random.randint(0,500)
Bomb=GameObjects(positionx,positiony,50,50,"bomb.png")
positionx2=random.randint(0,500)
positiony2=random.randint(0,500)
Bomb2=GameObjects(positionx2,positiony2,50,50,"bomb.png")
positionx_hp=random.randint(0,500)
positiony_hp=random.randint(0,500)
healthpod=GameObjects(positionx_hp,positiony_hp,50,50,"heart_stage2.png")
player2=Player(300,300,"mario.png",50)
player2.add(playersGroup2)
###############################################
#stage3 Objects
counter=0
stage3= pygame.image.load("st3.jpg")
stage3=pygame.transform.scale(stage3,(Width,Height))
Gameobjects_stage3.add(Stage3Cars(200))
Gameobjects_stage3.add(Stage3Cars(300))
Gameobjects_stage3.add(Stage3Cars(400))
player3=Player(300,300,"car1.png",50)
player3.add(playersGroup3)
###############################################
#stage4 Objects
stage4= pygame.image.load("stage4.jpg")
stage4=pygame.transform.scale(stage4,(Width,Height))
player4=Player(300,500,"soldier.png",100)
player4.add(playersGroup4)
player5=Player(300,500,"soldier.png",100)
superman=GameObjects(300,100,100,100,"superman.png")
superman2=GameObjects(300,100,100,100,"superman.png")
superman.add(Gameobjects_stage4)
###############################################
#stage5
stage5= pygame.image.load("gameover.png")
stage5=pygame.transform.scale(stage5,(Width,Height))

def load_sound(name):
    fullname = os.path.join('data', name)
    sound = pygame.mixer.Sound(fullname)
    return sound

while Gameloop:
    menu_sound="sounds/"+"mainmenu.wav"
    menu_sound=load_sound(menu_sound)
    menu_sound.play()
    while mainMenu:
        Introscreen.setScreen(Red,Red,White,display,"background.jpg")
        mainMenu,Gameloop,Stage1,Stage2,Stage3,Stage4=Introscreen.IntroMenuInput(display,mainMenu,Gameloop,Stage1,Stage2,Stage3,Stage4)
        pygame.display.update()
        ###########################################################################
    while Stage1:
        menu_sound.stop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.blit(stage1,(0,0))
        Gameobjects_stage1.update(0,0,0)
        playersGroup1.update(199,401,0,600)
        Gameobjects_stage1.draw(display)
        playersGroup1.draw(display)
        Stage5,Stage4,Stage3,Stage2,Stage1,mainMenu,Gameloop=player1.collisionHouses(Gameobjects_stage1,playersGroup1,player1,
                                                                                                                      house1,house2,house3,house4,
                                                                                                                        policecar,policecar2,
                                                                                                                        Stage5,Stage4,Stage3,Stage2,Stage1,mainMenu,Gameloop)
        if player1.rect.y==0:
            Stage1=False
            Stage2=False
            Stage3=True
            
        
        pygame.display.update()
        mainClock.tick(30)
        
        ####################################################################
    while Stage2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.blit(stage2,(0,0))#draw background
        Gameobjects_stage2.update(0,0,0)
        playersGroup2.update(0,600,0,600)
        
        Gameobjects_stage2.draw(display)
        playersGroup2.draw(display)
        
        Shroom1.move()
        Shroom2.move()
        Shroom3.move()
        
        player2.Stage2_Collisions(playersGroup2,Gameobjects_stage2,
                                              player2,
                                              RoadPass,
                                              Shroom1,Shroom2,Shroom3,
                                              Bomb,Bomb2,healthpod,
                                              Stage2)
        
        score="Score:"+str(player2.score)
        health="Health:"+str(player2.health)
        Introscreen.messageScreen(0,score,Red,display,500,10,32)
        Introscreen.messageScreen(0,health,Red,display,480,40,32)
        Gameloop,mainMenu,Stage1,Stage2=player2.GameOverStage2(Gameloop,mainMenu,Stage1,Stage2)
        if player2.level==2:
            player1.level=2
        
        pygame.display.update()
        mainClock.tick(30)
        
        ########################################################################
    while Stage3:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        display.blit(stage3,(0,0))#draw background
        Gameobjects_stage3.update()
        playersGroup3.update(0,600,0,600)
        Gameobjects_stage3.draw(display)
        playersGroup3.draw(display)
        player3.Stage3_Collisions(playersGroup3,Gameobjects_stage3,
                                              player3,
                                              stage3)
        Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4=player3.GameOverStage3(
                                                                                                                            Gameloop,mainMenu,
                                                                                                                            Stage1,Stage2,Stage3,Stage4,
                                                                                                                            playersGroup3,player3)
        score="Score:"+str(player3.score)
        health="Health:"+str(player3.shield)
        Introscreen.messageScreen(0,score,Red,display,480,10,32)
        Introscreen.messageScreen(0,health,Red,display,480,40,32)
        counter += 1
        player3.score+=10
        if counter >= 100:
          Gameobjects_stage3.add(Stage3Cars(300))
          counter = 0
        
        pygame.display.flip()
        mainClock.tick(30)
        
        ##################################################################
    while Stage4:
        x=0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_o:
                    x=1
                    player5.add(playersGroup4)
                if event.key==pygame.K_k:
                    player5.remove(playersGroup4)
                if event.key==pygame.K_p:
                    superman2.add(Gameobjects_stage4)
                    
            
        display.blit(stage4,(0,0))#draw background
        playersGroup4.update(0,600,540,600)
        playersGroup4.draw(display)
        Gameobjects_stage4.update()
        Gameobjects_stage4.draw(display)
        bulletgroup.update()
        bulletgroup.draw(display)
        player4.Shoot(bulletgroup)
        if x==1:
            player5.Shoot(bulletgroup)
        superman.moveStage4()
        superman2.moveStage4()
        rocks_randomizer=random.randint(0,1000)#random number to spawn rock
        laser_randomizer=random.randint(0,1000)#random number to spawn laser
        if rocks_randomizer<=5:
            rock=Rocks()
            rocks.add(rock)
        if laser_randomizer<=10:
            laser=superlaser(superman.rect.x,superman.rect.y)
            laser.add(superman_laser)
            superlaser_sound="sounds/"+"superlaser.wav"
            superlaser_sound=load_sound(superlaser_sound)
            superlaser_sound.play()
        rocks.draw(display)
        rocks.update()
        superman_laser.draw(display)
        superman_laser.update()
        #collisions with objects
        for hit in pygame.sprite.groupcollide(superman_laser, playersGroup4, 1, 0):
           player4.healthFinal -= 10
        for hit in pygame.sprite.groupcollide(rocks, playersGroup4, 1, 0):
           player4.healthFinal -= 10
        for hit in pygame.sprite.groupcollide(bulletgroup, Gameobjects_stage4, 1, 0):
           superman.BossHealth -= 10
        Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4=player4.GameOverStage4(Gameloop,mainMenu,Stage1,Stage2,Stage3,Stage4,superman,player1)
    
               
        score="Health:"+str(player4.healthFinal)
        enemy="Enemy:"+str(superman.BossHealth)
        Introscreen.messageScreen(0,score,Red,display,460,10,32)
        Introscreen.messageScreen(0,enemy,Red,display,0,10,32)
        pygame.display.flip()
        mainClock.tick(30)
    while Stage5:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         display.blit(stage5,(0,0))
         pygame.display.flip()
         mainClock.tick(30) 
        
            
        
        
        
        
        
        
