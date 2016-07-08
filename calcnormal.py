import numpy as np 
from scipy.stats import multivariate_normal
import json
import geopy
from geopy import distance
from geopy import Point
import math
import datetime
print datetime.datetime.now()
import matplotlib.pyplot as plt

pi=math.pi
e=math.e


mesh=np.load('Points.npy')

f=open('FacilityRiskScore', 'rb')
Emissions=json.load(f)

f=open('DistancesDic', 'rb')
FacilityCoordinates=json.load(f)


var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
mesh_years=[mesh, mesh, mesh, mesh, mesh, mesh, mesh, mesh]

nlat=1223
nlon=660 #no of divisions in longitude

dellat=(60-49)/nlat
dellon=(109-120)/nlon

def spiral():
    X=1223
    Y=660    
    x = y = 0
    dx = 0
    dy = -1
    
    for i in range(10000):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            plt.scatter(x,y)
            

            # DO STUFF...
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy



print datetime.datetime.now()
for i in xrange(7):
	for facility in Emissions[str(i)]:
		try:
			source=Point('%s %s' %(FacilityCoordinates[facilityID]['lat'], FacilityCoordinates[facilityID]['lon']))
			j,k=int ((FacilityCoordinates[facilityID]['lat']-49)/dellat),int((FacilityCoordinates[facilityID]['lon']+109)/dellon) #j and k are lower right nodes\

		except:
			continue
	for j in xrange(100):
		for k in xrange(50):
			
			mesh_years[i][j][k][0]=0.0
			mesh_years[i][j][k][1]=0.0
			for chemical in Emissions[str(i+2006)]:	
				try:
					Cancer_risk=CancerScores[chemical]		
				except:
					Cancer_risk=0	
				try:
					NonCancer_risk=NonCancerScores[chemical]		
				except:
					NonCancer_risk=0
				l=0
				for k,v in Emissions[str(i+2006)][chemical].iteritems():
					facilityID=v['NPRI_ID']	

					print l
					l=l+1				
					
					try:
						source=Point('%s %s' %(FacilityCoordinates[facilityID]['lat'], FacilityCoordinates[facilityID]['lon']))
						dest=Point('%s %s'%(mesh_years[i][j][k][0], mesh_years[i][j][k][1]))
						dist=distance.distance(source,dest).kilometers
						P=1/(2*pi)*(e**(-dist*dist/2))						
						mesh_years[i][j][k][0]+=P*v['Tonnes_Air']*1000*Cancer_risk
						mesh_years[i][j][k][1]+=P*v['Tonnes_Air']*1000*NonCancer_risk
					except:
						continue
			print k						
		print j
	print i
					
print datetime.datetime.now()
np.save("Mesh", mesh_years, allow_pickle=True, fix_imports=True)
