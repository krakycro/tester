from lib.grid.libGrid import *

def runTerrain():
    G = libGrid()
    G.getChunk(0, 0).lstMeeple.append(libMeeple())
    G.getChunk(0, 0).lstTerra.append(libTerra())
    
    print("Terrain OK")
