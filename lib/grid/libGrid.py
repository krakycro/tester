class libCoord:
    def __init__(self, intX = 0, intY = 0):
        self.intX = intX
        self.intY = intY
        
class libChunk:
    def __init__(self):
        self.lstMeeple = []
        self.lstTerra  = []

class libGrid:
    def __init__(self, intSize = 16, intDens = 16):
        self.intX = 0
        self.intY = 0
        self.intH = intSize
        self.intW = intSize
        self.lstChunk = [[ libChunk() for x in range(0, int(intSize / intDens))] for y in range(0, int(intSize / intDens))]
        
    def getChunk(self, x, y):
        return self.lstChunk[y][x]
