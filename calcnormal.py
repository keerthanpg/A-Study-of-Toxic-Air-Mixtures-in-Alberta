import numpy as np 
from scipy.stats import multivariate_normal
import json
import geopy
from geopy import distance
from geopy import Point
import math
import datetime
import matplotlib.pyplot as plt

pi=math.pi
e=math.e


mesh=np.load('Points.npy')

f=open('FacilityRiskScore', 'rb')
FacilityRiskScores=json.load(f)

f=open('DistancesDic', 'rb')
FacilityCoordinates=json.load(f)


var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
mesh_years=[mesh, mesh, mesh, mesh, mesh, mesh, mesh, mesh]

X=nlat=1223
Y=nlon=660 #no of divisions in longitude

dellat=(60.0-49.0)/nlat
dellon=(109.0-120.0)/nlon


print datetime.datetime.now()

for facilityID in FacilityRiskScores:
	print facilityID
	try:
		source=Point('%s %s' %(FacilityCoordinates[facilityID]['lat'], FacilityCoordinates[facilityID]['lon']))
		x0,y0=int ((FacilityCoordinates[facilityID]['lat']-49)/dellat),int((FacilityCoordinates[facilityID]['lon']+109)/dellon)#j and k are lower right nodes
		x = y = 0
		dx = 0
		dy = -1
		for i in range(10000):
			if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
				destlat=x+x0
				destlon=y+y0
				for year in FacilityRiskScores[facilityID]:
					try:
						dest=Point('%s %s'%(mesh_years[int(year)-2006][destlat][destlon][0], mesh_years[int(year)-2006][destlat][destlon][1]))
						dist=distance.distance(source,dest).kilometers
						P=1/(2*pi)*(e**(-dist*dist/2))
						try:
							mesh_years[int(year)-2006][destlat][destlon][2]+=P*1000*FacilityRiskScores[facilityID][year]['Cancer_Tonnes']
						except KeyError:
							continue

						try:
							mesh_years[int(year)-2006][destlat][destlon][3]+=P*1000*FacilityRiskScores[facilityID][year]['NonCancer_Tonnes']
						except KeyError:
							continue
					except IndexError:
							continue
					except Exception as e: 
						print(e)
			if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
					dx, dy = -dy, dx
			x, y = x+dx, y+dy
	except KeyError:
		continue
	
print datetime.datetime.now()
np.save("Mesh", mesh_years, allow_pickle=True, fix_imports=True)
