# напиши тут код створення та управління карткою
import pickle
class Mapmanager():
    def __init__(self):
        self.model = "block"
        self.texture = "текстура.png"
        self.color =[ (0.5,0.9,0.6,1),
                    (0.5,0.7,0.7,1),
                    (0.6,0.8,0.9,1),
                    (0.6,0.5,0.7,1)]
        self.startNew()
        
    def startNew(self):
        self.land = render.attachNewNode("Land")
    def getColor(self, z):
        if z < len(self.color):
            return self.color[z]
        else:
            return self.color[-1]

    def addBlock(self, position):
        self.block = loader.loadModel(self.model)
        self.block.setTexture(loader.loadTexture(self.texture))
        self.block.setPos(position)
        self.color1 = self.getColor(int(position[2]))
        self.block.setColor(self.color1)
        self.block.setTag('at', str(position))
        self.block.reparentTo(self.land)

    def clear(self):
        self.land.removeNode()
        self.startNew()

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z) + 1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y+=1

    def findBlock(self, pos):
        return self.land.findAllMatches("=at="+str(pos))

    def isEmpty(self,pos):
        blocks = self.findBlock(pos)
        if blocks:
            return False
        else:
            return True

    def findHighestEmpty(self, pos):
        x,y,z=pos
        z=1
        while not self.isEmpty((x,y,z)):
            z+=1
        return(x,y,z)

    def buildBlock(self,pos):
        x,y,z=pos
        new = self.findHighestEmpty(pos)
        if new[2] <= z+1:
            self.addBlock(new)

    def delBlock(self,position):
        blocks = self.findBlock(position)
        for block in blocks:
            block.removeNode()

    def delBlockFrom(self, position):
        x,y,z = self.findHighestEmpty(position)
        pos= x,y,z-1
        for block in self.findBlock(pos):
            block.removeNode()

    def saveMap(self):
        blocks= self.land.getChildren()
        with open('land4.dat','wb') as fout:
            pickle.dump(len(blocks),fout)
            for block in blocks:
                x,y,z= block.getPos()
                pos=(int(x), int(y), int(z))
                pickle.dump(pos,fout)

    def loadMap(self):
        self.clear()
        with open('land4.dat','rb') as fin:
            length=pickle.load(fin)
            for i in range(length):
                pos=pickle.load(fin)
                self.addBlock(pos)