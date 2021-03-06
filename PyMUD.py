
import itertools
import asyncio
import datetime
import random
import threading
from collections import Counter
import queue
import time
from PyServ import MudServer


map = """
mmmmmmmmmmmmmmmmmmfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgfffffffffffffffffffffffffgfffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggg
mmmmmmmmmmmmfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggfffffffffffffffffffffffgggfffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggg
mmmmmmmmmmmmmfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggffffffffffffffffffffffggggffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggg
mmmmmmmmmmmggggggggggggggggggggggggggggfffffffffffffffffffffffffffffffffffffffggggggggggggggggffffffffffggggggggggggggggffffffffffggggggggggggggggggggggggffffffffffffffffgggggggggggggggggggggggggg
mmmmmmmggggggggggggggggggggggggggggggggggggffffffffffffffffffffgffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggffffffffffffffgggfffggggggggggggggggg
mmmmfffffggggggggggggggggggggggggggggggggggggggffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggffffffffffffffffffgggggggggggggggggg
mmmmmmfffffffgggggggggggggggggggggggggggggggfffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggffffggffffffffffggggggggggggggggggg
mmmmmmfffffgggggggggggggggggggggggggggggggfffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggccccccccccgggggggggggggggggggggggggggggfffgggffffffffffggggggggggggggggggg
mmmmmmmmmmffffffffffdddddddgggggggggggggggfffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggcccccccccccccgggggggggggggggggggggggggggggfffggfffffffffffggggggggggggggggggg
mmmmmmmmmmmmmfffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggffgggggggggggggggggggggggcc0-0-0-0-0ccgggggggggggggggggggggggggggggfffggfffffffffffggggggggggggggggggg
mmmmmmmmmmmmfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggfffggggggggggggggggggggggcc|ccccccc|ccgggggggggggggggggggggggggggggfffggfffffffffffggggggggggggggggggg
mmmmmmmmmmmmmfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggffffgggggggggggggggggggggcc0ccc0ccc0ccggggggggggggggggggggggggggggg0fggfffffffffffffgggggggggggggggggg
mmmmmmmmgggggggggggggggggggggggggggggggfffffffffffffffffffffffffffffffffggggggggggggggggggggggffffgggggggggggggggggggggccc\ccc\ccc\ccgggggggggggggggggggggggggggg|gggggggfgfggffgffggggggggggggggggg
mmmmmggggggggggggggggggggggggggggggggggggggffffffffffffffffffffgffggggggggggggggggggggggggggggggggggggggggggggggggggggggccc0-0-0ccc0ggggggggggggggggggggggggggggg0gggggggggggggggggggggggggggggggggg
mmmmmmfffggggggggggggggggggggggggggggggggggggggffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggcccccccccc\ggggggggggggggggggggggggggg/ggggggggggggggggggggggggggggggggggg
ggggfffffffffgggggggggggggggggggggggggggggggfffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggffffgg0-0-0-0-0-0-0-0-0ggggggggg0gggggggggggggggggggggggggggggggggggg
gggffffffffgggggggggggggggggggggggggggggggfffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggfffffffggggfffffff|ggg|gg\ggggggg/ggggggggggggggggggggggggggggggggggggg
gggfffffffffffffffffddddddddggggggggggggggfffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggffffffffffgfffffff0ggg0ggg0-0-0-0ggggggggggggggggggggggggggggggggggggg
gggfffgggggggggggggggggggggggdddddfffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggfffffffffffffffggg|gg/ggggggggggggggggggggggggggggggggggggggggggggggggg
gggfffgggggggggggggggggggggggggggffffffffffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggf0-0-0-0-0-S-0-0-0-0-0-0gggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggf|ffgggg/gggggggg|ggggg|gggggggggggggggggggggggggggggggggggggggg
gggffggggggggggggggggggggggggggggfffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg0-0-0-0ggggggggg0gggggSgggggggggggggggggggggggggggggggggggggggg
ggggggggggggggggggggggggggggggggffffffffffffffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg/ggg/gg|ggggggggg|ggggg|gggggggggggggggggggggggggggggggggggggggg
ggggggggggggggggggggggggggggggggffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg0ggg0-0-0-0-0-0-0-0-0-0-0gggggggggggggggggggggggggggggggggggggggg
ssssgggggggggggggggggggggggggggggggggggffffffffffffffffgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg|gg/gggg|ggg|gggggggggg\ggggggggggggggggggggggggggggggggggggggggg
ssssggggggggggggggggggggggggggggssssssggggggffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg0-0-0-0-0-0-0ggggggggggg0gggggggggggggggggggggggggggggggggggggggg
sssssgggggggggggggggggggggssssssssssssssssssssssssgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg\ggggggggggggggggggggggggggggggggggggggg
~~sssssssggggggggggggggssssssssssssssssssssssssssssssgggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg0-0-0gggggggggggggggggggggggggggggggggg
~~~~~~~~sssssssggggggssssssssssss~~~~~~ssssssssssssssssssggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~ssssssssssssssssssss~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~ssssssssssssssss~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~~~~gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
~~~ggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg
"""




x = 1
y = 0
be = -1
locnum = -1
mapLines = map.split('\n')
mimelist = []
trueListmap = map.split('\n')
nz = []
nd = []

for i in mapLines:
    mimelist.append(i+'\n')

for i in map:
    x += 1
    if i == "\n":
        y += 1
        x = 1
    j = x, y

    if str(i.encode()) in (str(b'\x0c'),str(b'|'),str(b'/'),str(b'-'),str(b'\\')):
        nd.append([i,j])
    if i == '0' or i == 'S' or i == 'A':
        MP = str(i)
        locnum += 1
        haha = list(mimelist[y])
        haha[x-2] = '*'
        mimelist[y] = ''.join(haha)

        newt = [mimelist[y-7][x-25:x+25]+'\n\r',mimelist[y-6][x-25:x+25]+'\n\r',mimelist[y-5][x-25:x+25]+'\n\r',
                mimelist[y-4][x-25:x+25]+'\n\r',mimelist[y-3][x-25:x+25]+'\n\r',mimelist[y-2][x-25:x+25]+'\n\r',
                mimelist[y-1][x-25:x+25]+'\n\r',mimelist[y][x-25:x+25]+'\n\r',mimelist[y+1][x-25:x+25]+'\n\r',
                mimelist[y+2][x-25:x+25]+'\n\r',mimelist[y+3][x-25:x+25]+'\n\r',mimelist[y+4][x-25:x+25]+'\n\r',
                mimelist[y+5][x-25:x+25]+'\n\r',mimelist[y+6][x-25:x+25]+'\n\r',mimelist[y+7][x-25:x+25]+'\n\r']

        strm = (''.join(newt[0]+newt[1]+newt[2]+newt[3]+newt[4]+newt[5]+newt[6]+newt[7]+newt[8]+newt[9]+newt[10]+newt[11]+newt[12]+newt[13]+newt[14]))
        nz.append(['#'+str(locnum),j,{},strm])
        haha = list(mimelist[y])

        haha[x-2] = MP
        mimelist[y] = ''.join(haha)



mean = -1
for i in nz:
    mean +=1
    for j in nd:
        if j[1][0] == i[1][0]-1 and j[1][1] == i[1][1]+1:
            # sloc is the variable for the location of the 'which is' exit.
            sloc = (i[1][0]-2),(i[1][1]+2)
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = str(m[0])
            # print('location',i[0],i[1],'has an exit to the southwest,which is',slic)
            nz[mean][2]['SW']=str(slic)
        if j[1][0] == i[1][0]+1 and j[1][1] == i[1][1]-1:
            sloc = (i[1][0]+2),(i[1][1]-2)
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the northeast,which is',slic)
            nz[mean][2]['NE']=str(slic)
        if j[1][0] == i[1][0]+1 and j[1][1] == i[1][1]+1:
            # sloc is the variable for the 'which is' exit.
            sloc = (i[1][0]+2),(i[1][1]+2)
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the southeast,which is',slic)
            nz[mean][2]['SE']=str(slic)
        if j[1][0] == i[1][0]-1 and j[1][1] == i[1][1]-1:
            # sloc is the variable for the 'which is' exit.
            sloc = (i[1][0]-2),(i[1][1]-2)
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the northwest,which is',slic)
            nz[mean][2]['NW']=str(slic)
        if j[1][0] == i[1][0]-1 and j[1][1] == i[1][1]:
            sloc = (i[1][0]-2),(i[1][1])
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the west,which is',slic)
            nz[mean][2]['W']=str(slic)
        if j[1][0] == i[1][0]+1 and j[1][1] == i[1][1]:
            sloc = (i[1][0]+2),(i[1][1])
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the east, which is',slic)
            nz[mean][2]['E']=str(slic)
        if j[1][1]== i[1][1]-1 and j[1][0] == i[1][0]:
            sloc = (i[1][0]),(i[1][1]-2)
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the north, which is',slic)
            nz[mean][2]['N']=str(slic)
        if j[1][1]== i[1][1]+1 and j[1][0] == i[1][0]:
            sloc = (i[1][0]),(i[1][1]+2)
            slic = 0
            for m in nz:
                if str(sloc) == str(m[1]):
                    slic = m[0]
            # print('location',i[0],i[1],'has an exit to the south, which is',slic)
            nz[mean][2]['S']=str(slic)
    # print('-'*40)


locations = {}

for i in nz:
    locations.update( {i[0]:
        {
        "name": '\n\rA dark forest town',
        "description": '',
        "exits": i[2],
        "interact": [],
        "items": [],
        "maps": i[3],
        "enemies": [],
        "spawn": [],
        "players": []
        }
                })



########################################################################################################################
class classPlayer(object):
    def __init__(self, id = '', vname = '', room='#8', gold = 20, inv = None, playerLevel = 1, currentExp=0, levelNext = 25, teleport = '', balance=3,
                 lwielded=None, wielded = None, maxHealth = 50,
                 health = 50, incap = False, skillPoints = 0, knight = 0, mage=0, canBerserk=0, recur = None, switched = False,hostile = None, loot = None, dead = None):
        self.id = id
        self.vname = vname
        self.room = room
        self.gold = gold
        if inv == None:
            inv = []
        self.inv = inv
        self.playerLevel = playerLevel
        self.currentExp = currentExp
        self.levelNext = levelNext
        self.teleport = teleport
        self.balance = balance
        if lwielded == None:
            lwielded = []
        self.lwielded = lwielded
        if wielded == None:
            wielded = []
        self.wielded = wielded
        self.maxHealth = maxHealth
        self.health = health
        self.incap = incap
        self.skillPoints = skillPoints
        self.knight = knight
        self.mage = mage
        self.canBerserk = canBerserk
        if recur == None:
            recur = []
        self.recur = recur
        self.switched = switched
        self.hostile = hostile
        self.loot = loot
        self.dead = dead

class NPC(object):
    def __init__(self,vname,health,damage,description, xp, hostile, dead, speed,loot,incap,id,status,attacking):
        self.vname = vname
        self.health = health
        self.damage = damage
        self.description = description
        self.xp = xp
        self.hostile = hostile
        self.dead = dead
        self.speed = speed
        self.loot = loot
        self.incap = incap
        self.id = id
        self.status = status
        self.attacking = attacking

class NPCtalker(NPC):
    def __init__(self,vname,health,damage,description, xp, hostile, dead, speed,loot,incap,id,speech):
        self.speech = speech
        self.vname = vname
        self.health = health
        self.damage = damage
        self.description = description
        self.xp = xp
        self.hostile = hostile
        self.dead = dead
        self.speed = speed
        self.loot = loot
        self.incap = incap
        self.id = id

class Shield(object):
    def __init__(self,vname,defense,rarity,value,weight,type):
        self.vname = vname
        self.defense = defense
        self.rarity = rarity
        self.value = value
        self.weight = weight
        self.type = type


class Weapon(object):
    def __init__(self,vname,damage,speed,rarity,value,weight,type):
        self.vname = vname
        self.damage = damage
        self.speed = speed
        self.rarity = rarity
        self.value = value
        self.weight = weight
        self.type = type


class Spoils(object):
    def __init__(self,vname,value,weight,id,type):
        self.vname = vname
        self.value = value
        self.weight = weight
        self.id = id
        self.type = type


class Shop(object):
    def __init__(self,vname,inventory):
        self.vname = vname
        self.inventory = inventory

wshield = Shield('A thick wooden shield',1,'Common',2,10,'shield')

kknife = Weapon('\x1b[2;32;48m' + 'A wavy kris knife' + '\x1b[0m',5,1,"Uncommon",15,7,'sharp')
isword = Weapon('An iron sword',4,0,"Common",10,9,'sharp')
sdag = Weapon('A small dagger',3,1,"Common",7,6,'sharp')
stick = Weapon('A small tree branch',2,-1,"Common",0,3,'blunt')
killstick = Weapon("Huge stick for testing",15,0,"Common",0,0,'blunt')
ssword = Weapon('\x1b[2;32;48m' + 'A Steel sword' + '\x1b[0m',6,0,"Uncommon",10,9,'sharp')
scimitar = Weapon('\x1b[1;34;48m' + 'A curved scimitar' + '\x1b[0m',9,0,"Rare",150,8,'sharp')
obsknife = Weapon('\x1b[1;34;48m' + 'An obsidian dagger' + '\x1b[0m',7,2,"Rare",150,7,'sharp')


ccrown = Spoils('\x1b[2;33;48m' + "A Diamond and ruby encrusted crown" + '\x1b[0m',100,7,random.randint(0,9999),'spoils')
rattail = Spoils('\x1b[2;33;48m' + 'The tail of a dead rat' + '\x1b[0m',2,1,random.randint(0,9999),'spoils')
telegem = Spoils('\x1b[2;33;48m' + 'A small glowing gem' + '\x1b[0m',50,1,random.randint(0,9999),'spoils')
pearl = Spoils('\x1b[2;33;48m' + 'A beautiful white pearl' + '\x1b[0m',180,1,random.randint(0,9999),'spoils')
smallpurse = Spoils('\x1b[2;33;48m' + 'A small coinpurse' + '\x1b[0m',30,1,random.randint(0,9999),'spoils')

shop1 = Shop("A small shop in the forest",[{ssword:50,sdag:10,wshield:30,kknife:45,isword:15,scimitar:640,obsknife:580}])
shop2 = Shop("A village mystics shop",[{telegem:100}])

rat3 = NPC('\x1b[2;31;48m' + 'Rat Matriarch' + '\x1b[0m', 14,10,'\x1b[2;31;48m' + 'A huge rat matriarch wearing a golden, jeweled crown' + '\x1b[0m',50,True,False,3,[ccrown],False,8000,'',False)
trollking = NPC('\x1b[2;31;48m' + 'The Troll King' + '\x1b[0m',45,20,'The troll king',120,True,False,3,[pearl],True,random.randint(0,9000),'',False)

helpman = NPCtalker('An elderly man holding a torch',5,3,'An elderly man holding a torch',20,False,False,3,[rattail],False,random.randint(9000,9999),['The old man lifts his torch higher to see your face in the darkness.',
""" "Welcome traveler. My name's Hob, 'n I'm the lookout for Naym, the village t'the south." """,
""" "We've a shop that should help r'plenish yor supplies, if ye want to stock up." """,
""" "As ye might've noticed, our village has quite th' rat problem. They showed up out of nowhere, an' in force, aye." """,
""" "If yo're willin', our shops'll buy every single last rat tail you bring em. Heavens know we need the help." """,
'He glances at the tree branch in your hand.',
""" "Our shop also sells real weapons, if ye get tired of smashin' em in the 'ead with that stick." """,
""" "Oh, and one more thing." """,
""" "Stay far away from the caves in the northwestern part of our forest. Nobody that's ventured in 'as come out." """]
 )


# ratmap = """
# dddddddddd
# ddddddd0dd
# dddddd/ddd
# ddd0-*dddd
# dddddddddd
# dddddddddd
# """
#
# locations.update( {'#100':
#         {
#         "name": 'Inside a rats nest',
#         "description": "You drop down into the dark rats nest. You can't take a single step without crushing the bones of some small unfortunate creature.",
#         "exits": {'U':'#61',"E":'#101'},
#         "interact": [],
#         "items": [],
#         "maps": """
# dddddddddd\r
# ddddddd0dd\r
# dddddd/ddd\r
# ddd*-0dddd\r
# dddddddddd\r
# dddddddddd\r
# """,
#         "enemies": [],
#         "spawn": []
#         }
#                 })
# locations.update( {'#101':
#         {
#         "name": 'Inside a rats nest',
#         "description": "You are in a dark rats nest.",
#         "exits": {"NE":"#102","W":"#100"},
#         "interact": [],
#         "items": [],
#         "maps": """
# dddddddddd\r
# ddddddd0dd\r
# dddddd/ddd\r
# ddd0-*dddd\r
# dddddddddd\r
# dddddddddd\r
# """,
#         "enemies": [],
#         "spawn": []
#         }
#                 })
# locations.update( {'#102':
#         {
#         "name": 'Inside a rats nest',
#         "description": "You are in a dark rats nest.",
#         "exits": {"SW":"#101"},
#         "interact": [],
#         "items": [],
#         "maps": """
# dddddddddd\r
# ddddddd*dd\r
# dddddd/ddd\r
# ddd0-0dddd\r
# dddddddddd\r
# dddddddddd\r
# """,
#         "enemies": [rat3],
#         "spawn": []
#         }
#                 })
# locations["#61"]["exits"]['D'] = '#100'
# locations["#61"]["description"]= "There is an entrance to a rats nest here. You can vaguely make out the sounds of deep, labored breathing."


#local location changes


# locations['#']['interact'].append(shop1)
# locations['#']['description'] = 'There is a shop here. Type "shop" to bring up its menu.'
locations['#23']['items'].append(stick)
locations['#26']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',6,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),'',False))
locations['#21']['interact'].append(helpman)
locations['#35']['interact'].append(shop1)
locations['#47']['interact'].append(shop2)
locations['#70']['items'].append(smallpurse)
locations['#8']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',25,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),'',False))
locations['#8']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',25,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),'',False))

# locations['#13']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',25,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),''))

locations['#7']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),'',False))
locations['#3']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),'',False))
locations['#5']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),'',False))
locations['#9']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),'',False))
locations['#11']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),'',False))
locations['#6']['enemies'].append(trollking)
#def __init__(self,vname,health,damage,description, xp, hostile, dead, speed,loot,incap,id):
#locations['#8']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',5,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),''))


#Locations that can spawn rats:
sprats = ['#36','#60','#56','#34','#33','#32','#31','#43','#44','#45','#46','#53','#54','#55','#51','#52','#68','#67','#66','#65','#64','#63','#62','#50']
for i in sprats:
    locations[i]['spawn'].append('rats')


#functions

def spawn():
    try:
        for i in locations:
            if 'rats' in locations[i]["spawn"]:
                chance = random.randint(0,100)
                if len(locations[i]["enemies"]) < 2:
                    if chance >97:
                        x = NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',5,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),'',False)
                        locations[i]["enemies"].append(x)
                    if chance >99:
                        y = NPC('\x1b[2;31;48m' + 'An adult rat' + '\x1b[0m', 9,5,'\x1b[2;31;48m' + 'A fully grown adult rat' + '\x1b[0m',30,False,False,3,[rattail],False,random.randint(0,9000),'',False)
                        locations[i]["enemies"].append(y)


    except Exception as e:
        print(e)

def deadTest():
    global players
    for i in locations:
        xyx = [locations[i]["enemies"], locations[i]['players']]
        for attacked in itertools.chain(*xyx):
            if attacked.health <= 0:
                attacked.dead = True
                try:
                    mud.send_message(attacked.id, """\r
                            Y\r
                            o\r
                            u\r
                \r
                            d\r
                            i\r
                            e\r
                            d\r
                            .""")
                    players[attacked.id].health = 1
                    players[attacked.id].room = '#35'
                    mud.send_message(attacked.id, "You respawn at the village shop.")
                    attacked.dead = False
                    locations[i]["players"].remove(attacked)
                    mud.send_message(attacked.id, '\x1b[6;30;42m' + str(attacked.health) + '/' + str(attacked.maxHealth) + ">" + '\x1b[0m')
                except:
                    pass

            if attacked.dead == True:
                try:
                    for j in attacked.loot:
                        locations[i]['items'].append(j)
                        mud.send_message(id, attacked.vname + ' drops ' + j.vname + '.')
                    locations[i]['enemies'].remove(attacked)
                    players[id].currentExp += attacked.xp
                    levelUp()
                except:
                    print("we excepted at 524")
                mud.send_message(id, "You've slain "+attacked.vname+'!')
                for mm in locations[players[id].room]["players"]:
                    if mm != players[id] and mm != attacked:
                        mud.send_message(mm.id, "{} has slain {}!".format(players[id].vname, attacked.vname))
                        try:
                            mud.send_message(mm.id, str(attacked.vname + ' drops ' + j.vname + '.'))
                        except:
                            print("exception at 532")
                        mud.send_message(mm.id, '\x1b[6;30;42m' + str(mm.health) + '/' + str(mm.maxHealth) + ">" + '\x1b[0m')



async def rest(player):
    player.incap = True
    mud.send_message(player.id, "You sit down to rest.")
    while player.health < players[id].maxHealth:
        await asyncio.sleep(3)
        player.health += 5
        if player.health > player.maxHealth:
            player.health = player.maxHealth
        mud.send_message(player.id, str(player.health))
    mud.send_message(player.id, "You stand up, fully recovered.>")
    mud.send_message(player.id,'\x1b[6;30;42m' + str(player.health) + '/' + str(
        player.maxHealth) + ">" + '\x1b[0m')

    player.incap = False


async def attackKill(target,attacker):
    attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players']]
    for i in itertools.chain(*attackables):
        if target in str(i.vname).lower():
            attacker.incap = True
            if not i.dead:
                mud.send_message(attacker.id, "You touch "+ i.vname + ' softly with your hand.')
                i.health -= 100

                for p in players:
                    if p == i.id:
                        mud.send_message(p,
                                         "\r" + str(attacker.vname) + " touches you softly.\n\r" +
                                         '\x1b[6;30;42m' + str(players[p].health) + '/' + str(
                                             players[p].maxHealth) + ">" + '\x1b[0m')

                        if p != attacker.id and p != i.id:
                            mud.send_message(p, '{} touches {} softly.'.format(attacker.vname, i.vname))
                deadTest()
                await asyncio.sleep(1)
                attacker.incap = False
                mud.send_message(attacker.id, "You regain your balance.")
                mud.send_message(attacker.id, '\x1b[6;30;42m' + str(attacker.health) + '/' + str(
                attacker.maxHealth) + ">" + '\x1b[0m')
            break




async def attackPunch(target,attacker):
    attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players']]
    for i in itertools.chain(*attackables):
        if target in str(i.vname).lower():
            attacker.incap = True
            if not i.dead:
                mud.send_message(attacker.id, "You punch "+ i.vname + ' as hard as you can! ')
                i.health -= 1
                deadTest()
                for p in players:
                    if p == i.id:
                        mud.send_message(p,
                                         "\r" + str(attacker.vname) + " just punched you!\n\r" +
                                         '\x1b[6;30;42m' + str(players[p].health) + '/' + str(
                                             players[p].maxHealth) + ">" + '\x1b[0m')

                        if p != attacker.id and p != i.id:
                            mud.send_message(p, '{} punches {}!'.format(attacker.vname, i.vname))
                await asyncio.sleep(3)
                attacker.incap = False
                mud.send_message(attacker.id, "You regain your balance.")
                mud.send_message(attacker.id, '\x1b[6;30;42m' + str(attacker.health) + '/' + str(
                attacker.maxHealth) + ">" + '\x1b[0m')
            break






async def attackStrike(target,attacker):
    attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players'] ]
    for i in itertools.chain(*attackables):
        if target in str(i.vname).lower():
            attacker.incap = True
            if not i.dead:
                mud.send_message(attacker.id, "You strike "+ i.vname + ' with '+attacker.wielded[0].vname+'!')
                try:
                    i.hostile = True
                except:
                    print("616 i.hostile issues")
                i.health -= attacker.wielded[0].damage
                deadTest()
                for p in players:
                    if p == i.id:
                        mud.send_message(p,
                                         "\r" + str(attacker.vname) + " strikes you with {}!\n\r".format(attacker.wielded[0].vname) +
                                         '\x1b[6;30;42m' + str(players[p].health) + '/' + str(
                                             players[p].maxHealth) + ">" + '\x1b[0m')
                    if players[p].room == players[id].room:
                        if p != id and p != i.id:
                            mud.send_message(p, '{} strikes {} with {}!'.format(attacker.vname, i.vname,attacker.wielded[0].vname))
                if attacker.balance - attacker.wielded[0].speed < 0:
                    await asyncio.sleep(0)
                    attacker.incap = False
                    mud.send_message(attacker.id, "You regain your balance.")
                    mud.send_message(attacker.id, '\x1b[6;30;42m' + str(attacker.health) + '/' + str(
                        attacker.maxHealth) + ">" + '\x1b[0m')
                    break
                else:
                    await asyncio.sleep(attacker.balance - attacker.wielded[0].speed)
                    attacker.incap = False
                    mud.send_message(attacker.id, "You regain your balance.")
                    mud.send_message(attacker.id, '\x1b[6;30;42m' + str(attacker.health) + '/' + str(
                        attacker.maxHealth) + ">" + '\x1b[0m')
                    break


# i.incap = True
# await
# asyncio.sleep(7)
# i.incap = False
# if not i.dead:
# mud.send_message(attacker.id, i.vname + " recovers.")


async def subwaitSB(target, attacker):
    print("INNN")
    target.hostile = True
    await asyncio.sleep(7)
    target.incap = False
    print(attacker.vname, target.vname)
    print(target.dead)
    if not target.dead:
        print(attacker, target)
        mud.send_message(attacker, target.vname + " recovers.")


async def attackShieldbash(target,attacker):

    attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players'] ]
    for i in itertools.chain(*attackables):
        if target in str(i.vname).lower():
            attacker.incap = True
            if not i.dead:
                mud.send_message(attacker.id, "You bash "+ i.vname + ' with your shield, stunning it!')
                try:
                    i.incap = True
                except:
                    print("616 i.hostile issues")
                i.health -= 1
                deadTest()
                asyncio.run_coroutine_threadsafe(subwaitSB(i, attacker), new_loop)
                for p in players:
                    if p == i.id:
                        mud.send_message(p,
                                         "\r" + str(attacker.vname) + " bashes you with their shield!\n\r" +
                                         '\x1b[6;30;42m' + str(players[p].health) + '/' + str(
                                             players[p].maxHealth) + ">" + '\x1b[0m')
                    if players[p].room == players[id].room:
                        if p != id and p != i.id:
                            mud.send_message(p, '{} bashes {} with their shield!'.format(attacker.vname, i.vname))
                    await asyncio.sleep(2)
                    attacker.incap = False
                    mud.send_message(attacker.id, "You regain your balance.")
                    mud.send_message(attacker.id, '\x1b[6;30;42m' + str(attacker.health) + '/' + str(
                        attacker.maxHealth) + ">" + '\x1b[0m')
                break




def levelUp():
    if int(players[id].currentExp) >= int(players[id].levelNext):  # Experience check
        mud.send_message(id,
            '\x1b[7;36;40m' + "Your experiences in this world make you stronger. You've gained an experience point" + '\x1b[0m')
        mud.send_message(id,
            '\x1b[7;36;40m' + "To level up, type Level class, where class is your class of choice. For a list of classes type 'Help Class.'" + '\x1b[0m')
        players[id].levelNext = players[id].levelNext * 1.8
        players[id].maxHealth += 5
        players[id].health = players[id].maxHealth
        players[id].playerLevel += 1
        players[id].currentExp = 0
        players[id].skillPoints += 1

async def npcattack(target):
    global players
    for enemy in locations[target.room]["enemies"]:
        if enemy in locations[target.room]["enemies"]:
            if enemy.attacking == True:
                break
            if enemy.hostile:
                enemy.attacking = True
                while enemy.hostile and not enemy.dead and target.health >= 0 and enemy in locations[target.room]["enemies"]:
                    if not enemy.incap:
                        mud.send_message(target.id, enemy.vname+" attacks!")
                        target.health -= enemy.damage
                        deadTest()
                        mud.send_message(target.id, '\x1b[6;30;42m' + str(target.health) + '/' + str(target.maxHealth) + ">" + '\x1b[0m')
                        await asyncio.sleep(enemy.speed)





def whatsHere():
    enemiesHere = locations[players[id].room]["enemies"]
    availableItems = locations[players[id].room]["items"]
    interactHere = locations[players[id].room]["interact"]
    playersHere = locations[players[id].room]["players"]
    if locations[players[id].room]['description'] != '':
        mud.send_message(id, locations[players[id].room]['description'])

    if interactHere != []:
        for i in interactHere:
            mud.send_message(id, "There is "+'\x1b[8;30;47m' + i.vname + '\x1b[0m'+" here.")


    if len(playersHere) > 1:
        mud.send_message(id, "Players here: {}".format(", ".join(p.vname for p in playersHere)))


    if enemiesHere != []:
        if len(enemiesHere) > 1:
            mud.send_message(id, "There are enemies here: "+ ', '.join(
                enemy.vname for enemy in enemiesHere))
        if len(enemiesHere) == 1:
            mud.send_message(id, "There is " + ''.join(enemy.vname for enemy in enemiesHere)+' here.')
    if availableItems != []:
        mud.send_message(id, "There are items here: " + ', '.join(item.vname for item in availableItems))


#asyncstart
def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

new_loop = asyncio.new_event_loop()
t = threading.Thread(target=start_loop, args=(new_loop,))
t.start()
#asyncend

#threads


n = threading.Thread(target=npcattack)
dead = threading.Thread(target=deadTest)


knightSkills = ['Shields', 'Shieldbash', 'Skewer', 'Switchgrip', 'Berserk']
mageSkills = ['Fireball','Iceshard', 'Blizzard','Fireblast','Pyroblast']

# stores the players in the game

threads = []
players = {}

# start the server
mud = MudServer()

# main game loop. We loop forever (i.e. until the program is terminated)
while True:
    time.sleep(0.09)
    mud.update()
    # go through any newly connected players
    for id in mud.get_new_players():
        players[id] = classPlayer(id)

        # send the new player a prompt for their name
        mud.send_message(id, "What is your name?")

    # go through any recently disconnected players
    for id in mud.get_disconnected_players():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        if id not in players:
            continue

        # go through all the players in the game
        for pid, pl in players.items():
            # send each player a message to tell them about the diconnected
            # player
            mud.send_message(pid, "{} quit the game".format(
                players[id].vname))



        # remove the player's entry in the player dictionary
        del(players[id])

    # go through any new commands sent from players
    for id, command, params in mud.get_commands():

        # if for any reason the player isn't in the player map, skip them and
        # move on to the next one
        if id not in players:
            continue

        # if the player hasn't given their name yet, use this first command as
        # their name
        if players[id].vname is '':
            players[id].vname = command.title()
            # go through all the players in the game
            for pid, pl in players.items():
                # send each player a message to tell them about the new player
                mud.send_message(pid, "{} has entered the game".format(
                    players[id].vname))
            # send the new player a welcome message
            mud.send_message(id, "Your travels bring you to a forest. You mark the setting sun, and make moves to set up"
                                 " camp when you spot dancing lights in the forest to the south. Could they be lights of"
                                 " civilization? \n\rWelcome, {}. \n\r".format(
                                                           players[id].vname)
                             + " ")



######################################################################
######################### game loop ##################################
######################################################################



            asyncio.run_coroutine_threadsafe(npcattack(players[id]), new_loop)
            playersprompt = '\x1b[6;30;42m' + str(players[id].health) + '/' + str(
                players[id].maxHealth) + ">" + '\x1b[0m'
            availableExits = ", ".join(locations[players[id].room]["exits"].keys())
            # send the new player the description of their current room
            mud.send_message(id, locations[players[id].room]['name'])
            mud.send_message(id, availableExits)
            locations[players[id].room]['players'].append(players[id])

            # Experience

        if players[id].skillPoints > 0:
            mud.send_message(id, "You have skillpoints available to spend. Type 'help level' to learn more.")
        players[id].recur.append(command + ' ' + params)
        if len(players[id].recur) > 3:  # keeps recur list from growing too big
            del players[id].recur[0]
#checking for buffs
        if players[id].switched == True:
            players[id].balance = 0
            players[id].switched = False
        else:
            players[id].balance = 3
#Movement
        if command.upper() in locations[players[id].room]["exits"]:
#this is for the arrival/departure piece, it stores the direction and opposite direction for arriving/leaving
            ex = command.upper()
            ub = ''
            nb = ''
            if ex == "S":
                ub = 'south.'
                nb = 'north.'
            elif ex == 'N':
                ub = 'north.'
                nb = 'south.'
            elif ex == 'NE':
                ub = 'northeast.'
                nb = 'southwest.'
            elif ex == 'NW':
                ub = 'northwest.'
                nb = 'southeast'
            elif ex == 'SE':
                ub = 'southeast.'
                nb = 'northwest.'
            elif ex == 'SW':
                ub = 'southwest.'
                nb = 'northeast.'
            elif ex == 'E':
                ub = 'east.'
                nb = 'west.'
            elif ex == 'W':
                ub = 'west.'
                nb = 'east.'
#departure, using 'ub' variable:
            for pid, pl in players.items():
                # if player is in the same room and isn't the player
                # sending the command
                if players[pid].room == players[id].room \
                        and pid != id:
                    # send them a message telling them that the player
                    # left the room
                    mud.send_message(pid, "{} leaves to the {}".format(
                                                  players[id].vname, ub))
# Movement Actual
            try:
                locations[players[id].room]['players'].remove(players[id])
            except:
                print('cant remove')
            players[id].room = locations[players[id].room]["exits"][command.upper()]  # This line moves us
            try:
                locations[players[id].room]['players'].append(players[id])
            except RuntimeError as e:
                print(e)
            # locations[players[id].room]['players'].append(players[id])
            mud.send_message(id, "{}".format(locations[players[id].room]["name"]))
            # send player his location #
            mud.send_message(id, players[id].room)
            availableExits = ", ".join(locations[players[id].room]["exits"].keys())
            mud.send_message(id, "Available exits are " + availableExits + " ".upper())
            whatsHere()
#arrival, using 'nb' variable
            rm = locations[players[id].room]
            # go through all the players in the game
            for pid, pl in players.items():
                # if player is in the same (new) room and isn't the player
                # sending the command
                if players[pid].room == players[id].room \
                        and pid != id:
                    # send them a message telling them that the player
                    # entered the room
                    mud.send_message(pid,
                                     "{} arrives from the {}".format(
                                         players[id].vname, nb))
# If it's not in the exits of the room, but still a direction:
        elif command.upper() in ("N","NE","E","SE","S","SW","W","NW","N"):
            mud.send_message(id, "You can't go that way.")

#Level
        if command == 'level':
            try:
                category = params
                if players[id].skillPoints >0:
                    if category == 'knight':
                        players[id].skillPoints -= 1
                        players[id].knight += 1
                        mud.send_message(id, "Your expertise with blades and shields grows.")
                        if players[id].knight == 1:
                            mud.send_message(id, "You've gained the ability to wield shields.")
                        if players[id].knight ==2:
                            mud.send_message(id, "You've gained a new ability: 'Shieldbash': \n\rBash your target with your shield, stunning him.\n\rShieldbash $target")
                        if players[id].knight == 3:
                            mud.send_message(id,
                                             "You've learned a new ability: 'Skewer': \n\rImpale your target, leaving your weapon in them while they bleed.\n\rSkewer $target")
                        if players[id].knight == 4:
                            mud.send_message(id,
                                             "You've learned a new ability: 'Switchgrip'\n\rChange grips on your weapon, allowing you a much quicker successive strike.")
                        if players[id].knight == 5:
                            mud.send_message(id,
                                             "You've learned a new ability: 'Berserk'\n\rChannel your rage, reducing time between attacks.")

                    if category == 'mage':
                        players[id].skillPoints -= 1
                        players[id].mage += 1
                        mud.send_message(id, "Your ability to harness the elements grows.")
                        if players[id].mage ==1:
                            mud.send_message(id,
                                             "You've learned a new spell: 'Fireball': \n\rHurl a ball of fire at your enemy.\n\rCast Fireball $target")
                        if players[id].mage == 2:
                            mud.send_message(id,
                                             "You've learned a new spell: 'Iceshard': \n\rConjure a spear of ice, and send it flying towards your foes.\n\rCast Iceshard $target")
                        if players[id].mage == 3:
                            mud.send_message(id,
                                             "You've learned a new spell: 'Blizzard': \n\rYour abilities with the elements all you to control the weather itself. Summon a \n\rblizzard, hurting every enemy in the location.\n\rCast Blizzard")
                        if players[id].mage == 4:
                            mud.send_message(id,
                                             "You've learned a new spell: 'Fireblast': \n\rSummon a ball of lava, exploding after a short time causing massive damage to all enemies.\n\rCast Fireblast")
                        if players[id].mage == 5:
                            mud.send_message(id,
                                             "You've learned a new spell: 'Pyroblast': \n\rAfter casting for a short time, cast a huge ball of fire to an enemy,\n\rdoing massive damage.\n\rCast Pyroblast $target")
                    # else:
                    #     mud.send_message(id, "You don't have any skillpoints available.")
            except:
                mud.send_message(id, "Level what?")
#Skills
        if command == 'skills':
            mud.send_message(id, "Your current level of experience is: "+str(players[id].playerLevel))
            if players[id].knight > 0:
                mud.send_message(id, 'Knight level '+ str(players[id].knight))
                mud.send_message(id, str(knightSkills[:int(players[id].knight)]))
            if players[id].mage > 0:
                mud.send_message(id, 'Mage level ' + str(players[id].mage))
                mud.send_message(id, str(mageSkills[:int(players[id].mage)]))
#recur
        if command == '':
            try:
                command = players[id].recur[-2].split(' ')[0]
                params = (' '.join(players[id].recur[-2].split(' ')[1:]))
                del players[id].recur[-1]
            except RuntimeError as e:
                print("problem Recur!!!")
                print(e)
#Greet
        if command == 'greet':
            target = params
            for i in locations[players[id].room]['interact']:
                if target in i.vname:
                    if i.speech:
                        for pid, pl in players.items():
                            if players[pid]["room"] == players[id].room:
                                for j in i.speech:
                                    mud.send_message(pid, j)
#Get
        if command == "get":
            target = params
            for i in locations[players[id].room]["items"]:
                if target in i.vname:
                    players[id].inv.append(i)
                    # picked = "You pick up",i.vname
                    mud.send_message(id, "You pick up "+i.vname+".")
                    locations[players[id].room]["items"].remove(i)
                    break
#Drop
        if command == "drop":
            try:
                target = params
                for i in players[id].inv:
                    if target in i.vname.lower():
                        players[id].inv.remove(i)
                        locations[players[id].room]['items'].append(i)
                        mud.send_message(id, 'You drop '+ i.vname +  ' to the ground.')
                        if len(locations[players[id].room]["players"]) > 1:
                            for j in locations[players[id].room]["players"]:
                                if j.id != players[id]:
                                    mud.send_message(j.id,
                                                     str(players[id].vname) + " lets " + i.vname + " fall to the ground.")
            except:
                mud.send_message(id, "Drop what?")
#Shop
        if command == "shop":
            templist = []
            for i in locations[players[id].room]['interact']:
                if 'shop' in i.vname:
                    mud.send_message(id, str(i.vname) + ': ')
                    mud.send_message(id, '#' * 40)
                    for j in i.inventory[0]:
                        templist.append(j.vname)
                    for x in i.inventory:
                        for y in x.values():
                            templist.append(y)
                    items = templist[:len(templist) // 2]
                    prices = templist[len(templist) // 2:]

                    for i in range(0, len(items)):
                        mud.send_message(id, str(items[i]) + ' ' + str(prices[i]))
                mud.send_message(id, '#' * 40)
                mud.send_message(id, 'Your gold: ' + str(players[id].gold))
                mud.send_message(id, "#" * 40)
#buy
        if command == 'buy':
            try:
                templist = []
                target = params
                for i in locations[players[id].room]['interact']:
                    if 'shop' in i.vname:
                        for j in i.inventory:
                            for m in j.keys():
                                if target in m.vname.lower():
                                    if players[id].gold >= int(j[m]):
                                        mud.send_message(id,
                                                         "You purchase a " + m.vname + " and slip it into your pack.")
                                        players[id].inv.append(m)
                                        players[id].gold -= int(j[m])
                                    elif players[id].gold < int(j[m]):
                                        mud.send_message(id, "You can't afford that.")
                    else:
                        mud.send_message(id, "You need to be near a shop to do that.")
            except:
                mud.send_message(id, "Buy what?")
#sell
        if command == 'sell':
            try:
                for i in locations[players[id].room]['interact']:
                    if 'shop' in i.vname:
                        target = params
                        for i in players[id].inv:
                            if target in i.vname:
                                players[id].gold += i.value
                                players[id].inv.remove(i)
                                mud.send_message(id, "You sell " + i.vname + ' for ' + str(i.value) + ' gold.')
                                if len(locations[players[id].room]["players"]) > 1:
                                    for j in locations[players[id].room]["players"]:
                                        if j.id != players[id]:
                                            mud.send_message(j.id, str(players[id].vname) + " sells " +i.vname + " to the shop.")
                                break
                    else:
                        mud.send_message(id, "You can only sell your items at a shop.")
            except:
                mud.send_message(id, "Sell what?")
#'say' command
        if command == "say":
            # go through every player in the game
            for pid, pl in players.items():
                # if they're in the same room as the player
                if players[pid].room == players[id].room:
                    # send them a message telling them what the player said
                    mud.send_message(pid, '{} says: "{}"'.format(
                                                players[id].vname, params))
#inv
        if command == "inv":
            if players[id].wielded == []:
                mud.send_message(id,"You aren't wielding any weapons.")
            if players[id].wielded != []:
                mud.send_message(id, "You're currently wielding: "+', '.join(i.vname for i in players[id].wielded)+' in your RIGHT hand.')
            if players[id].lwielded != []:
                mud.send_message(id, "You're currently wielding: " + ', '.join(i.vname for i in players[id].lwielded)+' in your LEFT hand.')
            if players[id].inv == []:
                mud.send_message(id, "You have nothing in your pack.")
            tempinv = []
            for i in players[id].inv:
                tempinv.append(i.vname)
            jj = dict(Counter(tempinv))
            mud.send_message(id, ', '.join((i+"(x"+str(jj[i])+")") for i in jj))
            mud.send_message(id, "You have "+str(players[id].gold)+" gold in your coinpurse.")

# 'look' command
        if command == "look":

            # store the player's current room
            rm = locations[players[id].room]
            # send the player back the description of their current room
            mud.send_message(id, rm["description"])

            playershere = []
            # go through every player in the game
            for pid, pl in players.items():
                # if they're in the same room as the player
                if players[pid].room == players[id].room:
                    # add their name to the list
                    playershere.append(players[pid].vname)


            # send player a message containing the list of exits from this room
            mud.send_message(id, "Exits are: {}".format(
                                                    ", ".join(rm["exits"])))
            whatsHere()
#punch
        if command == 'punch':
            if not players[id].incap:
                target = params
                attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players']]
                for i in itertools.chain(*attackables):
                    if str(target).lower() in str(i.vname).lower():
                        asyncio.run_coroutine_threadsafe(attackPunch(target,players[id]), new_loop)
                        break
            elif players[id].incap:
                mud.send_message(id, "You can't do that right now.")
        if command == "rest":
            asyncio.run_coroutine_threadsafe(rest(players[id]), new_loop)

#strike
        if command == 'strike':
            if not players[id].incap:
                target = params
                if players[id].wielded != []:
                    attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players']]
                    for i in itertools.chain(*attackables):
                        if str(target).lower() in str(i.vname).lower():
                            asyncio.run_coroutine_threadsafe(attackStrike(target, players[id]), new_loop)
                            break
                elif players[id].wielded == []:
                    mud.send_message(id, "You're not wielding a weapon!")
            elif players[id].incap:
                mud.send_message(id, "You can't do that right now.")

#who
        if command == "who":
            for i in players:
                mud.send_message(id, players[i].vname)
#wield
        if command == "wield":
            try:
                for i in players[id].inv:
                    if params in str(i.vname.lower()):
                        if i.type == 'sharp' or i.type == 'blunt':
                            if len(players[id].wielded)<1:
                            # while len(wielded)<1:
                                players[id].wielded.append(i)
                                mud.send_message(id, "You wield "+i.vname+" in your right hand.")
                                if len(locations[players[id].room]["players"]) > 1:
                                    for j in locations[players[id].room]["players"]:
                                        if j.id != players[id].id:
                                            print(j.id, players[id])
                                            mud.send_message(j.id,
                                                             str(players[
                                                                     id].vname) + " wields " + i.vname + " in their right hand.")
                                players[id].inv.remove(i)
                                break
                            else:
                                mud.send_message(id, "You already have " + players[id].wielded.vname + " in your hand.")
                                break
                        if i.type == 'shield':
                            if players[id].knight >0:
                                if len(players[id].lwielded)<1:
                                    players[id].lwielded.append(i)
                                    mud.send_message(id, 'You wield ' + i.vname + " in your left hand.")
                                    if len(locations[players[id].room]["players"]) > 1:
                                        for j in locations[players[id].room]["players"]:
                                            if j.id != players[id]:
                                                mud.send_message(j.id,
                                                                 str(players[id].vname) + " wields " + i.vname + " in their left hand.")
                                    players[id].inv.remove(i)
                                    break
                                else:
                                    mud.send_message("You already have " + players[id].lwielded.vname + " in your hand.")
                                    break
                            else:
                                mud.send_message(id, "You don't have the required Knight proficiency to use that item.")
            except:
                mud.send_message(id, "Wield what?")
#unwield
        if command == "unwield":
            newlist = players[id].wielded+players[id].lwielded
            for i in newlist:
                if params in i.vname.lower():
                    mud.send_message(id, "You put " + i.vname + " back into your pack.")
                    if len(locations[players[id].room]["players"]) > 1:
                        for j in locations[players[id].room]["players"]:
                            if j.id != players[id].id:
                                mud.send_message(j.id,
                                                 str(players[id].vname) + " unwields " + i.vname + " and slips it into his pack.")
                    try:
                        players[id].wielded.remove(i)
                    except:
                        pass
                    try:
                        players[id].lwielded.remove(i)
                    except:
                        pass
                    players[id].inv.append(i)
        if command == "help":
            if params == "level":
                mud.send_message(id, "The currently supported classes are Knight and Mage. To gain expertise in the Knight skill set, type Level Knight. To gain expertise in the Mage skillset, type Level Mage.")
#testing
        if command == "gimme":
            if params == "isword":
                players[id].wielded.append(isword)
                players[id].lwielded.append(wshield)
                mud.send_message(id, "aw ye")
        if command == "healme":
            players[id].health = 999
        if command == "levelmyknight":
            players[id].knight = 5

        if command == "shieldbash":
            if not players[id].incap:
                target = params
                if players[id].lwielded != []:
                    attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players']]
                    for i in itertools.chain(*attackables):
                        if str(target).lower() in str(i.vname).lower():
                            asyncio.run_coroutine_threadsafe(attackShieldbash(target, players[id]), new_loop)
                            break
                elif players[id].wielded == []:
                    mud.send_message(id, "You're not wielding a shield!")
            elif players[id].incap:
                mud.send_message(id, "You can't do that right now.")


#debugging
        if command == "experience":
            print(players[id].currentExp, players[id].levelNext)
        if command == "whoami":
            mud.send_message(id, str(players[id].vname))
        if command == "sendid":
            mud.send_message(id, str(id))
            for i in players:
                mud.send_message(id, str(i))
                mud.send_message(i, str("worky?"))
        if command == "reset":
            for i in players:
                players[id].incap = False
        if command == "health":
            players[id].health = int(params)
        if command == "dead":
            print(players[id].dead)
        if command == 'touchx':
            if not players[id].incap:
                target = params
                attackables = [locations[players[id].room]["enemies"], locations[players[id].room]['players']]
                for i in itertools.chain(*attackables):
                    if str(target).lower() in str(i.vname).lower():
                        asyncio.run_coroutine_threadsafe(attackKill(target,players[id]), new_loop)
                        break
            elif players[id].incap:
                mud.send_message(id, "You can't do that right now.")

# Map
        if command == "map":
            minilist = list(locations[players[id].room]["maps"])
            for i in range(len(minilist)):
                if minilist[i] == 'g':
                    minilist[i] = '\x1b[0;30;42m' + 'g' + '\x1b[0m'
                if minilist[i] == 'f':
                    minilist[i] = '\x1b[3;32;42m' + 'f' + '\x1b[0m'
                if minilist[i] == 'c':
                    minilist[i] = '\x1b[3;30;47m' + 'c' + '\x1b[0m'
            mud.send_message(id, ''.join(minilist))
# inspect
        if command == 'inspect':
            try:
                item = params
                for i in players[id].inv or players[id].wielded or players[id].lwielded:
                    if item in i.vname.lower():
                        if i.type == 'sharp' or i.type == 'blunt':
                            mud.send_message(id, i.vname + ':'+ '\n\rDamage: '+ str(i.damage) + "\n\rSpeed: "+ str(i.speed)+ "\n\rRarity: "+ i.rarity+
                                  "\n\rWeight: "+ str(i.weight)+ "\n\rValue: "+ str(i.value)+ '\n\rType: '+ i.type)
                            break
                        if i.type == 'spoils':
                            mud.send_message(id, i.vname + ':' + '\n\rValue: ' +  str(i.value) + "\n\rWeight: " + str(i.weight))
                            break
                        if i.type == 'shield':
                            mud.send_message(id, i.vname + ':' + '\n\rDefense: ' + str(i.defense) + "\n\rRarity: " + i.rarity)
                            mud.send_message(id, "we got here")
                        else:
                            mud.send_message(id, "You don't have that in your inventory.")
            except:
                mud.send_message(id, "Inspect what?")

# player prompt, sent as a message
        j = '\x1b[6;30;42m' + str(players[id].health) + '/' + str(players[id].maxHealth) + ">" + '\x1b[0m'
        mud.send_prompt(id, j)
        scribed = False
        spawn()
        asyncio.run_coroutine_threadsafe(npcattack(players[id]), new_loop)

# Knight skills

# Mage skills

# Fireball


