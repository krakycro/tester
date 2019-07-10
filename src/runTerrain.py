from lib.grid.libGrid import *
from lib.node.libMeeple import *
from lib.node.libTerra import *

def runTerrain():
    G = libGrid()
    G.getChunk(0, 0).lstMeeple.extend([libMeeple("M1"),libMeeple("M2")])
    G.getChunk(0, 0).lstTerra.extend([libTerra("T1"),libTerra("T2")])
    print(G.getChunk(0, 0).lstMeeple[0].strName)
    print("Terrain OK")
