#comment added, to be deleted
#second comment added, which is to be deleted

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
        "name": 'A dark forest town',
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
    def __init__(self,vname,health,damage,description, xp, hostile, dead, speed,loot,incap,id,status):
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

rat3 = NPC('\x1b[2;31;48m' + 'Rat Matriarch' + '\x1b[0m', 14,10,'\x1b[2;31;48m' + 'A huge rat matriarch wearing a golden, jeweled crown' + '\x1b[0m',50,True,False,3,[ccrown],False,8000,'')
trollking = NPC('\x1b[2;31;48m' + 'The Troll King' + '\x1b[0m',45,20,'The troll king',120,True,False,3,[pearl],True,random.randint(0,9000),'')

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


ratmap = """
dddddddddd
ddddddd0dd
dddddd/ddd
ddd0-*dddd
dddddddddd
dddddddddd
"""

locations.update( {'#100':
        {
        "name": 'Inside a rats nest',
        "description": "You drop down into the dark rats nest. You can't take a single step without crushing the bones of some small unfortunate creature.",
        "exits": {'U':'#61',"E":'#101'},
        "interact": [],
        "items": [],
        "maps": """
dddddddddd\r
ddddddd0dd\r
dddddd/ddd\r
ddd*-0dddd\r
dddddddddd\r
dddddddddd\r
""",
        "enemies": [],
        "spawn": []
        }
                })
locations.update( {'#101':
        {
        "name": 'Inside a rats nest',
        "description": "You are in a dark rats nest.",
        "exits": {"NE":"#102","W":"#100"},
        "interact": [],
        "items": [],
        "maps": """
dddddddddd\r
ddddddd0dd\r
dddddd/ddd\r
ddd0-*dddd\r
dddddddddd\r
dddddddddd\r
""",
        "enemies": [],
        "spawn": []
        }
                })
locations.update( {'#102':
        {
        "name": 'Inside a rats nest',
        "description": "You are in a dark rats nest.",
        "exits": {"SW":"#101"},
        "interact": [],
        "items": [],
        "maps": """
dddddddddd\r
ddddddd*dd\r
dddddd/ddd\r
ddd0-0dddd\r
dddddddddd\r
dddddddddd\r
""",
        "enemies": [rat3],
        "spawn": []
        }
                })
locations["#61"]["exits"]['D'] = '#100'
locations["#61"]["description"]= "There is an entrance to a rats nest here. You can vaguely make out the sounds of deep, labored breathing."


#local location changes


# locations['#']['interact'].append(shop1)
# locations['#']['description'] = 'There is a shop here. Type "shop" to bring up its menu.'
locations['#23']['items'].append(stick)
locations['#26']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',6,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),''))
locations['#21']['interact'].append(helpman)
locations['#35']['interact'].append(shop1)
locations['#47']['interact'].append(shop2)
locations['#70']['items'].append(smallpurse)
# locations['#8']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',25,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),''))
# locations['#13']['enemies'].append(NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',25,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),''))

locations['#7']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),''))
locations['#3']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),''))
locations['#5']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),''))
locations['#9']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),''))
locations['#11']['enemies'].append(NPC('\x1b[2;31;48m' + 'A huge cave troll' + '\x1b[0m',24,15,'A huge cave troll',120,True,False,3,[pearl],False,random.randint(0,9000),''))
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
                        x = NPC('\x1b[2;31;48m' + 'A young rat' + '\x1b[0m',5,3,'\x1b[2;31;48m' + 'A hissing juvenile rat' + '\x1b[0m',20,False,False,3,[rattail],False,random.randint(0,9000),'')
                        locations[i]["enemies"].append(x)
                    if chance >99:
                        y = NPC('\x1b[2;31;48m' + 'An adult rat' + '\x1b[0m', 9,5,'\x1b[2;31;48m' + 'A fully grown adult rat' + '\x1b[0m',30,False,False,3,[rattail],False,random.randint(0,9000),'')
                        locations[i]["enemies"].append(y)


    except Exception as e:
        print(e)


def deadTest():
    def subwait():
        global players
        for i in locations:
            if locations[i]["enemies"] != []:
                for enemy in locations[i]["enemies"]:
                    if enemy.health <= 0:
                        enemy.dead = True
                    if enemy.dead == True:
                        for j in enemy.loot:
                            locations[i]['items'].append(j)
                            mud.send_message(id, enemy.vname + ' drops ' + j.vname)
                        locations[i]['enemies'].remove(enemy)
                        players[id].currentExp += enemy.xp
                        if enemy.status != '':
                            if enemy.status == 'skewer':
                                mud.send_message(id, enemy.vname + ' bleeds to death from their wounds.')
                            if enemy.status == 'pyroblast':
                                mud.send_message(id, enemy.vname + " is incinerated, leaving behind only ash.")
                            if enemy.status == 'fireball':
                                mud.send_message(id, "You burn " +  enemy.vname + " to a crisp.")
                            if enemy.status == 'iceshard':
                                mud.send_message(id, enemy.vname + " falls to the ground with glistening ice sticking out of its wounds.")
                            if enemy.status == "blizzard":
                                mud.send_message(id, enemy.vname +  " turns to solid ice, and falls to the ground with a thud.")

                        else:
                            mud.send_message(id, "You've slain "+enemy.vname)
    for i in range(0,1):
        x = threading.Thread(target=subwait)

        try:
            x.start()
        except RuntimeError:
            x = threading.Thread(target=subwait)
            x.start()


def attackSkewer(target):

    def subWait(): #Needed, if we don't have a sub function with the time.sleep() function inside, it will loop continuosly, not giving the user a prompt.
        while not i.dead:
            mud.send_message(id, i.vname+" bleeds profusely.")
            time.sleep(5)
            i.health -= 5
            deadTest()

    x = threading.Thread(target=subWait)

    for i in locations[players[id].room]["enemies"]:
        if target in str(i.vname).lower():
            if players[id].wielded != []:
                if not i.dead:
                    mud.send_message(id, "You shove your "+str(players[id].wielded[0].vname)+" deep into the gut of "+i.vname)
                    i.status = 'skewer'
                    #print(i.vname,"begins to bleed from his wounds.")
                    i.loot.append(players[id].wielded[0])
                    players[id].wielded.remove(players[id].wielded[0])
                    try:
                        x.start()
                    except RuntimeError:
                        x = threading.Thread(target=subWait)
                        x.start()
            else:
                mud.send_message(id, "You need to wield a weapon first.")



def attackStrike(target):
    for i in locations[players[id].room]["enemies"]:
        if target in str(i.vname).lower():
            # players[id].incap = True
            if not i.dead:
                mud.send_message(id, "You attack "+ i.vname + '! ' + str(i.health))
                i.health -= players[id].wielded[0].damage
                deadTest()
            if players[id].balance - players[id].wielded[0].speed < 0:
                time.sleep(0)
                # players[id].incap = False
            else:
                time.sleep(players[id].balance - players[id].wielded[0].speed)
                # players[id].incap = False
            break
    for i in locations[players[id].room]['players']:
        if target in str(i.vname).lower():
            mud.send_message(id, "You attack "+i.vname+'!')
            i.health -= players[id].wielded[0].damage
            if players[id].balance - players[id].wielded[0].speed < 0:
                time.sleep(0)
            else:
                time.sleep(players[id].balance - players[id].wielded[0].speed)
            break



def npcattack():
    global players
    for npc in locations[players[id].room]["enemies"]:
        if npc in locations[players[id].room]["enemies"]:
            while npc.hostile and not npc.dead:
                if not npc.incap:
                    for i in locations[players[id].room]['enemies']:
                        ubertemp = [(i, players[id].room)]
                        if ubertemp[0][1] == players[id].room and players[id].health > 0 and not i.dead and i.hostile == True:
                            mud.send_message(id, npc.vname + " attacks!")
                            if players[id].lwielded != []:
                                if players[id].lwielded[0].type == 'shield':
                                    players[id].health -= i.damage - players[id].lwielded[0].defense
                            else:
                                players[id].health -= i.damage

                            time.sleep(npc.speed)

def rest():
    players[id].incap = True
    mud.send_message(id, "You sit down to rest.")
    while players[id].health < players[id].maxHealth:
        players[id].health += 5
        # if rhealth < playerHealth:
        #     print("You've been awoken out of your trance.")
        #     incap = False
        #     break
        if players[id].health > players[id].maxHealth:
            players[id].health = players[id].maxHealth
        mud.send_message(id, str(players[id].health))
        time.sleep(3)
    mud.send_message(id, "You've fully recovered.>")
    players[id].incap = False

def levelUp():
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

def attackBerserk():
    players[id].balance -= 1
    time.sleep(7)
    players[id].balance += 1
    mud.send_message(id, "You calm down from your rage.")

def attackShieldbash(target):
    def subWait():
        i.incap = True
        time.sleep(7)
        i.incap = False
        if not i.dead:
            mud.send_message(id, i.vname + ' recovers.')

    x = threading.Thread(target=subWait)
    for i in locations[players[id].room]["enemies"]:
        if target in str(i.vname).lower():
            if not i.dead:
                mud.send_message(id, "You bash your shield into " +  i.vname + ", stunning it")
                try:
                    x.start()
                except RuntimeError:
                    x = threading.Thread(target=subWait)
                    x.start()
                i.hostile = True
                i.health -= 3
            deadTest()
            time.sleep(players[id].balance - players[id].wielded[0].speed)
            break



def attackFireball(target):
    for i in locations[players[id].room]["enemies"]:
        if target in str(i.vname).lower():
            if not i.dead:
                mud.send_message(id, "You cast a fireball at "+ i.vname)
                i.status = 'fireball'
                i.health -= 4
                deadTest()
                time.sleep(players[id].balance)
                mud.send_message(id, "You've regained your mental balance.")

def attackIceshard(target):
    def subWait():
        i.status = 'iceshard'
        i.incap = True
        time.sleep(3)
        i.incap = False
        if not i.dead:
            mud.send_message(id, i.vname+' recovers from the ice shards slowing effect.')

    x = threading.Thread(target=subWait)
    for i in locations[players[id].room]["enemies"]:
        if target in str(i.vname).lower():
            if not i.dead:
                mud.send_message(id, "You conjure up and send a shard of razor sharp ice at" + i.vname)
                i.health -= 6
                i.status = 'iceshard'
                deadTest()
                try:
                    x.start()
                except RuntimeError:
                    x = threading.Thread(target=subWait)
                    x.start()
                time.sleep(players[id].balance)
                mud.send_message(id, "You've regained your mental balance.")
        break

def attackBlizzard():
    x = 1
    while x < 6:
        deadTest()
        x += 1
        for i in locations[players[id].room]["enemies"]:
            i.health -= 2
            i.status = 'blizzard'
        mud.send_message(id, "Your blizzard cuts away at your enemies, sapping them of their strength.")
        time.sleep(2)
        deadTest()

def attackFireblast():
    mud.send_message(id, "You conjure a lava orb above the location.")
    time.sleep(4)
    mud.send_message(id, "Your fireblast explodes!")
    for ijm in locations[players[id].room]["enemies"]:
        ijm.hostile = True
        ijm.health -= 6
        deadTest()

def attackPyroblast(target):
    for i in locations[players[id].room]["enemies"]:
        if target in str(i.vname).lower():
            if not i.dead:
                mud.send_message(id, "You charge a huge pyroblast pointed at "+ i.vname)
                time.sleep(players[id].balance + 1)
                mud.send_message(id, "You unleash your pyroblast!")
                i.health -= 10
                i.hostile = True
                i.status = 'pyroblast'
                deadTest()
            break

def whatsHere():
    enemiesHere = locations[players[id].room]["enemies"]
    availableItems = locations[players[id].room]["items"]
    interactHere = locations[players[id].room]["interact"]
    if locations[players[id].room]['description'] != '':
        mud.send_message(id, locations[players[id].room]['description'])
    if interactHere != []:
        for i in interactHere:
            mud.send_message(id, "There is "+'\x1b[8;30;47m' + i.vname + '\x1b[0m'+" here.")
    if enemiesHere != []:
        if len(enemiesHere) > 1:
            mud.send_message(id, "There are " + str(len(enemiesHere)) + " enemies here:" + ', '.join(
                enemy.vname for enemy in enemiesHere))
        if len(enemiesHere) == 1:
            mud.send_message(id, "There is an enemy here: " + ''.join(enemy.vname for enemy in enemiesHere))
    if availableItems != []:
        mud.send_message(id, "There are items here: " + ', '.join(item.vname for item in availableItems))


#threads

p = threading.Thread(target=attackStrike)
n = threading.Thread(target=npcattack)
dead = threading.Thread(target=deadTest)
r = threading.Thread(target=rest)
fs = threading.Thread(target=attackFireblast)
bliz = threading.Thread(target=attackBlizzard)
ice = threading.Thread(target=attackIceshard)
sb = threading.Thread(target=attackShieldbash)
s = threading.Thread(target=attackSkewer)
f = threading.Thread(target=attackFireball)
py = threading.Thread(target=attackPyroblast)


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


        if not players[id].playerLevel == 0:  # Experience
            if players[id].currentExp >= players[id].levelNext:  # Experience check
                levelUp()  # Experience

            if players[id].skillPoints > 0:
                mud.send_message(id, "You have skillpoints available to spend. Type 'help level' to learn more.")


        # if the player hasn't given their name yet, use this first command as
        # their name
        if players[id].vname is '':
            players[id].vname = command
            # go through all the players in the game
            for pid, pl in players.items():
                # send each player a message to tell them about the new player
                mud.send_message(pid, "{} has entered the game".format(
                    players[id].vname))
            # send the new player a welcome message
            # send the new player a welcome message
            mud.send_message(id, "Your travels bring you to a forest. You mark the setting sun, and make moves to set up"
                                 " camp when you spot dancing lights in the forest to the south. Could they be lights of"
                                 " civilization? \n\rWelcome, {}. \n\r".format(
                                                           players[id].vname)
                             + " ")
            availableExits = ", ".join(locations[players[id].room]["exits"].keys())
            # send the new player the description of their current room
            mud.send_message(id, locations[players[id].room]['name'])
            mud.send_message(id, availableExits)
        for i in locations:
            for enemies in locations[i]["enemies"]:
                if enemies.hostile and not n.is_alive():
                    try:
                        n.start()
                    except RuntimeError:  # occurs if thread is dead
                        n = threading.Thread(target=npcattack)  # create new instance if thread is dead
                        n.start()  # start thread


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
            mud.send_message(id, "Available exits are " + availableExits + " \n".upper())
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
                    picked = "You pick up",i.vname
                    mud.send_message(id, "You pick up "+i.vname)
                    locations[players[id].room]["items"].remove(i)

# Drop
        if command == "drop":
            try:
                target = params
                for i in players[id].inv:
                    if target in i.vname.lower():
                        players[id].inv.remove(i)
                        locations[players[id].room]['items'].append(i)
                        mud.send_message(id, 'You drop '+ i.vname +  ' to the ground.')
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
                        mud.send_message(id, str(items[i])+ ' ' + str(prices[i]))
                mud.send_message(id, '#' * 40)
                mud.send_message(id, 'Your gold: '+ str(players[id].gold))
                mud.send_message(id, "#" * 40)

        if command == "rest":
            r = threading.Thread(target=rest)
            r.start()

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
                                        mud.send_message(id, "You purchase a " +  m.vname + " and slip it into your pack.")
                                        players[id].inv.append(m)
                                        players[id].gold -= int(j[m])
                                    elif players[id].gold < int(j[m]):
                                        mud.send_message(id, "You can't afford that.")
                    else:
                        mud.send_message(id, "You need to be near a shop to do that.")
            except:
                mud.send_message(id, "Buy what?")

# sell
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

            # send player a message containing the list of players in the room
            if len(playershere) > 1:
                mud.send_message(id, "Players here: {}".format(
                                                        ", ".join(playershere)))
            # send player a message containing the list of exits from this room
            mud.send_message(id, "Exits are: {}".format(
                                                    ", ".join(rm["exits"])))
            whatsHere()


#strike
        if command == 'strike':
            try:
                if not players[id].incap:
                    target = params
                    if players[id].wielded != []:
                        for i in locations[players[id].room]["enemies"]:
                            if str(target).lower() in str(i.vname).lower():
                                i.hostile = True
                                if i.hostile and not n.is_alive():
                                    try:
                                        n.start()
                                    except RuntimeError: #occurs if thread is dead
                                        n = threading.Thread(target=npcattack) #create new instance if thread is dead
                                        n.start() #start thread
                        if not p.is_alive():
                            try:
                                p = threading.Thread(target=attackStrike(target))
                                p.start()
                            except RuntimeError: #occurs if thread is dead
                                p = threading.Thread(target=attackStrike(target)) #create new instance if thread is dead
                                p.start()
                    else:
                        mud.send_message(id, "You're not wielding a weapon!")
            except RuntimeError as e:
                mud.send_message(id, "Strike what?")
                print(e)
                break
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
                    try:
                        players[id].wielded.remove(i)
                    except:
                        pass
                    try:
                        players[id].lwielded.remove(i)
                    except:
                        pass
                    players[id].inv.append(i)


#testing
        if command == "gimme":
            if params == "isword":
                players[id].wielded.append(isword)
                players[id].lwielded.append(wshield)
                mud.send_message(id, "aw ye")
        if command == "levelmyknight":
            players[id].knight = 5
        if command == "levelmymage":
            players[id].mage = 5
#debugging
        if command == "showme":
            print(locations[players[id].room]['enemies'])
        if command == "whoami":
            mud.send_message(id, str(players[id].vname))
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
# Knight skills
        if players[id].knight > 1:
            if command == "shieldbash":
                if not players[id].incap:
                    try:
                        if players[id].lwielded != []:
                            target = params
                            for i in locations[players[id].room]["enemies"]:
                                if target in str(i.vname).lower():
                                    if i.hostile and not n.is_alive():
                                        try:
                                            n.start()
                                        except RuntimeError:
                                            n = threading.Thread(target=npcattack)
                                            n.start()
                                    if not sb.is_alive():
                                        try:
                                            sb = threading.Thread(target=attackShieldbash(target))
                                            sb.start()
                                        except RuntimeError:
                                            sb = threading.Thread(target=attackShieldbash(target))
                                            sb.start()

                                break
                        else:
                            mud.send_message(id, "You don't have a shield equipped.")
                    except:
                        mud.send_message(id, "Shield bash what?")
                else:
                    mud.send_message(id, "You can't do that right now.")

        if players[id].knight > 2:
            # Skewer
            if command == "skewer":
                if not players[id].incap:
                    try:
                        target = params
                        for i in locations[players[id].room]["enemies"]:
                            if str(target).lower() in str(i.vname).lower():
                                i.hostile = True
                                if i.hostile and not n.is_alive():
                                    try:
                                        n.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        n = threading.Thread(target=npcattack)  # create new instance if thread is dead
                                        n.start()  # start thread
                                if not s.is_alive():
                                    try:
                                        s = threading.Thread(target=attackSkewer(target))
                                        s.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        s = threading.Thread(
                                            target=attackSkewer(target))  # create new instance if thread is dead
                                        s.start()
                            break
                    except:
                        mud.send_message(id, "Skewer what?")
        if players[id].knight > 3:
            if command == "switchgrip":
                players[id].switched = True
                mud.send_message(id, "You toss your weapon in the air, snatching it cleanly with an alternate grip.")
        if players[id].knight > 4:
            if command == "berserk":
                mud.send_message(id,
                                 "Your pupils dilate, you clench your teeth and grip your weapon so hard your hand goes numb.")
                xe = threading.Thread(target=attackBerserk)
                xe.start()

# Mage skills
        if players[id].mage >= 1:

            if command == "cast":
# Fireball
                if params.split(' ')[0] == 'fireball':
                    if not players[id].incap:
                        ##########################################################################
                        target = params.split(' ')[1]
                        for i in locations[players[id].room]["enemies"]:
                            if str(target).lower() in str(i.vname).lower():
                                i.hostile = True
                                if i.hostile and not n.is_alive():
                                    try:
                                        n.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        n = threading.Thread(
                                            target=npcattack)  # create new instance if thread is dead
                                        n.start()  # start thread
                            if not f.is_alive():
                                try:
                                    f = threading.Thread(target=attackFireball(target))
                                    f.start()
                                except RuntimeError:  # occurs if thread is dead
                                    f = threading.Thread(
                                        target=attackFireball(target))  # create new instance if thread is dead
                                    f.start()
                            # break
                            # iceshard
                if players[id].mage >= 2:
                    if params.split(' ')[0] == 'iceshard':
                        if not players[id].incap:
                            target = params.split(' ')[1]
                            for i in locations[players[id].room]["enemies"]:
                                if str(target).lower() in str(i.vname).lower():
                                    i.hostile = True
                                    if i.hostile and not n.is_alive():
                                        try:
                                            n.start()
                                        except RuntimeError:  # occurs if thread is dead
                                            n = threading.Thread(
                                                target=npcattack)  # create new instance if thread is dead
                                            n.start()  # start thread
                                if not ice.is_alive():
                                    try:
                                        ice = threading.Thread(target=attackIceshard(target))
                                        ice.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        ice = threading.Thread(target=attackIceshard(
                                            target))  # create new instance if thread is dead
                                        ice.start()
                                break
                if players[id].mage >= 3:
                    if params.split(' ')[0] == 'blizzard':
                        if not players[id].incap:
                            for i in locations[players[id].room]['enemies']:
                                i.hostile = True
                                if i.hostile and not n.is_alive():
                                    try:
                                        n.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        n = threading.Thread(
                                            target=npcattack)  # create new instance if thread is dead
                                        n.start()  # start thread
                        if not bliz.is_alive():
                            try:
                                bliz = threading.Thread(target=attackBlizzard)
                                bliz.start()
                            except RuntimeError:  # occurs if thread is dead
                                bliz = threading.Thread(
                                    target=attackBlizzard)  # create new instance if thread is dead
                                bliz.start()
                if players[id].mage >= 4:
                    if params.split(' ')[0] == 'fireblast':
                        if not players[id].incap:
                            for i in locations[players[id].room]['enemies']:
                                if i.hostile and not n.is_alive():
                                    try:
                                        n.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        n = threading.Thread(
                                            target=npcattack)  # create new instance if thread is dead
                                        n.start()  # start thread
                            if not fs.is_alive():
                                try:
                                    fs = threading.Thread(target=attackFireblast)
                                    fs.start()
                                except RuntimeError:  # occurs if thread is dead
                                    fs = threading.Thread(
                                        target=attackFireblast)  # create new instance if thread is dead
                                    fs.start()
                if players[id].mage >= 5:
                    if params.split(' ')[0] == 'pyroblast':
                        if not players[id].incap:
                            target = params.split(' ')[1]
                            for i in locations[players[id].room]["enemies"]:
                                if str(target).lower() in str(i.vname).lower():
                                    if i.hostile and not n.is_alive():
                                        try:
                                            n.start()
                                        except RuntimeError:  # occurs if thread is dead
                                            n = threading.Thread(
                                                target=npcattack)  # create new instance if thread is dead
                                            n.start()  # start thread
                                if not py.is_alive():
                                    try:
                                        py = threading.Thread(target=attackPyroblast(target))
                                        py.start()
                                    except RuntimeError:  # occurs if thread is dead
                                        py = threading.Thread(target=attackPyroblast(
                                            target))  # create new instance if thread is dead
                                        py.start()
                                break



#comment added to test GIT commit


        if players[id].health <= 0:
            mud.send_message(id, """\r
            Y\r
            o\r
            u\r
\r
            d\r
            i\r
            e\r
            d\r
            .""")
            players[id].health = 1
            players[id].room = '#35'
            mud.send_message(id, "You respawn at the village shop.")
