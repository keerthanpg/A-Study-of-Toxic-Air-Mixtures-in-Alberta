import numpy as np 
from scipy.stats import multivariate_normal
import json
import geopy
from geopy import distance
from geopy import Point
import math
import datetime
import matplotlib.pyplot as plt


bigmesh=np.load('Mesh.npy')
mesh=np.load('Points33.npy')
mesh=np.asarray([mesh, mesh, mesh, mesh, mesh, mesh, mesh, mesh])
print bigmesh.shape
print mesh.shape


X=nlat=1223
Y=nlon=660 #no of divisions in longitude

dellat=(60.0-49.0)/nlat
dellon=(109.0-120.0)/nlon

for i in range(bigmesh.shape[1]):
        for j in range(bigmesh.shape[2]):
                bigmesh[7][i][j][1]=(bigmesh[0][i][j][1]+bigmesh[1][i][j][1]+bigmesh[2][i][j][1]+bigmesh[3][i][j][1]+bigmesh[4][i][j][1]+bigmesh[5][i][j][1]+bigmesh[6][i][j][1])/7
                bigmesh[7][i][j][2]=(bigmesh[0][i][j][2]+bigmesh[1][i][j][2]+bigmesh[2][i][j][2]+bigmesh[3][i][j][2]+bigmesh[4][i][j][2]+bigmesh[5][i][j][2]+bigmesh[6][i][j][2])/7

smallmesh=[]
m=-1
n=-1
for i in range(bigmesh.shape[0]):
        smallmesh.append([])
        j=0
        
        for j in range(0, bigmesh.shape[1]):
                if j>=1199:
                        j=0
                        break
                elif j%3==0:
                        
                        smallmesh[i].append([])
                        m+=1
                        for k in range(0, bigmesh.shape[2]):
                                if k>=660:
                                        k=0
                                        break
                                elif k%3==0:
                                        x0=j
                                        y0=k
                                        x = y = 0
                                        dx = 0
                                        dy = -1
                                        a=int(j/3)
                                        b=int(k/3)
                                        for p in range(16):
                                                if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
                                                        destlat=x+x0
                                                        destlon=y+y0
                                                        
                                                        try:
                                                                mesh[i][a][b][2]+=bigmesh[i][destlat][destlon][2]
                                                                mesh[i][a][b][3]+=bigmesh[i][destlat][destlon][3]
                                                        except:
                                                                n+=1
                                                                
                                                if ((x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y)):
                                                        dx, dy = -dy, dx
                                                        x, y = x+dx, y+dy
                                        #print i,j,k
                                        #print mesh[i][a][b]
                                        for c in range(mesh[i][a][b].shape[0]):
                                                mesh[i][a][b][c]/=16
                                        print i, a,b
                                        smallmesh[i][a].append(mesh[i][a][b])
        
	
print datetime.datetime.now()
smallmesh=np.asarray(smallmesh)
print smallmesh.shape

np.save("Smallmesh", smallmesh, allow_pickle=True, fix_imports=True)
np.save("Mesh", bigmesh, allow_pickle=True, fix_imports=True)
