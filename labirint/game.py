# напиши тут код основного вікна гри
from direct.showbase.ShowBase import ShowBase
from mapmanager import Mapmanager
from hero import Hero

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        self.land.loadLand("land4.txt")
        self.hero = Hero((3,1,1),self.land)
        base.camLens.setFov(90)
        self.modell = loader.loadModel("whale.obj")
        self.modell.reparentTo(render)
        self.modell.setScale(0.004)
        self.modell.setPos(15,2,1)
        self.modell4 = loader.loadModel("whale.obj")
        self.modell4.reparentTo(render)
        self.modell4.setScale(0.004)
        self.modell4.setPos(7,30,2)
        self.modell3 = loader.loadModel("wooden watch tower2.obj")
        self.modell3.setTexture(loader.loadTexture("Wood_Tower_Col.jpg"))
        self.modell3.reparentTo(render)
        self.modell3.setScale(0.4)
        self.modell3.setP(90)
        self.modell3.setPos(17,4,0)
        self.modell2 = loader.loadModel("grass.obj")
        self.modell2.reparentTo(render)
        self.modell2.setScale(0.008)
        self.modell2.setPos(9,28,0.5)
        self.modell6 = loader.loadModel("whale.obj")
        self.modell6.reparentTo(render)
        self.modell6.setScale(0.004)
        self.modell6.setPos(15,13,2)
        self.modell7 = loader.loadModel("grass.obj")
        self.modell7.reparentTo(render)
        self.modell7.setScale(0.008)
        self.modell7.setPos(6,41,0.5)
        self.modell8 = loader.loadModel("grass.obj")
        self.modell8.reparentTo(render)
        self.modell8.setScale(0.008)
        self.modell8.setPos(3,18,0.5)
        self.modell9 = loader.loadModel("fish.obj")
        self.modell9.setTexture(loader.loadTexture("fish.png"))
        self.modell9.reparentTo(render)
        self.modell9.setScale(0.1)
        self.modell9.setPos(3,15,1)
        self.modell10 = loader.loadModel("fish.obj")
        self.modell10.setTexture(loader.loadTexture("fish.png"))
        self.modell10.reparentTo(render)
        self.modell10.setScale(0.1)
        self.modell10.setP(90)
        self.modell10.setPos(15,35,1)
        self.modell11 = loader.loadModel("fish.obj")
        self.modell11.setTexture(loader.loadTexture("fish.png"))
        self.modell11.reparentTo(render)
        self.modell11.setScale(0.1)
        self.modell11.setP(90)
        self.modell11.setPos(1,43,2)
        self.modell12 = loader.loadModel("fish.obj")
        self.modell12.setTexture(loader.loadTexture("fish.png"))
        self.modell12.reparentTo(render)
        self.modell12.setScale(0.2)
        self.modell12.setP(90)
        self.modell12.setPos(18,18,2)
        self.modell13 = loader.loadModel("SHARK.obj")
        self.modell13.setTexture(loader.loadTexture("12960_Shark_diff_v2.jpg"))
        self.modell13.reparentTo(render)
        self.modell13.setScale(0.4)
        self.modell13.setPos(4,18,2)
        self.modell14 = loader.loadModel("SHARK.obj")
        self.modell14.setTexture(loader.loadTexture("12960_Shark_diff_v2.jpg"))
        self.modell14.reparentTo(render)
        self.modell14.setScale(0.5)
        self.modell14.setPos(3,11,2)
        self.modell15 = loader.loadModel("SHARK.obj")
        self.modell15.setTexture(loader.loadTexture("12960_Shark_diff_v2.jpg"))
        self.modell15.reparentTo(render)
        self.modell15.setScale(0.5)
        self.modell15.setPos(15,28,1)
        self.modell16 = loader.loadModel("fishh.obj")
        self.modell16.setTexture(loader.loadTexture("fish_texture.png"))
        self.modell16.reparentTo(render)
        self.modell16.setScale(0.5)
        self.modell16.setP(90)
        self.modell16.setPos(2,28,1)
        self.modell17 = loader.loadModel("WoodHouse.obj")
        self.modell17.setTexture(loader.loadTexture("Diffuse.png"))
        self.modell17.reparentTo(render)
        self.modell17.setScale(0.4)
        self.modell17.setP(90)
        self.modell17.setPos(10,20,1)
        self.modell18 = loader.loadModel("grass.obj")
        self.modell18.reparentTo(render)
        self.modell18.setScale(0.008)
        self.modell18.setPos(8,8,0.5)

        

game = Game()
game.run()