import numpy as np 
from scipy.stats import multivariate_normal
import os
import json
import geopy
from geopy import distance
from geopy import Point
import unicodedata

mesh=np.load('Points.npy')

f=open('EmissionByChemical.txt', 'rb')
Emissions=json.load(f)

f=open('DistancesDic', 'rb')
FacilityCoordinates=json.load(f)

ChemicalDimensions={}
i=2
for j in xrange(2006, 2012):
	for chemical in Emissions[str(j)]:
		if chemical in ChemicalDimensions:
			continue
		else:
			ChemicalDimensions[chemical]=i
			i=i+1
print i
#print ChemicalDimensions



var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
mesh_years=[mesh, mesh, mesh, mesh, mesh, mesh, mesh]

for i in xrange(7):
	for j in xrange(1223):
		for k in xrange(660):
			print np.shape(mesh_years[i][j][k])
			for l in xrange(len(ChemicalDimensions)):
				mesh_years[i][j][k][l+2]=0.0
			for chemical in Emissions[str(i+2006)]:
				l=ChemicalDimensions[chemical]
				print l
				for discharge in Emissions[str(i+2006)][chemical]:
					facilityID=discharge['NPRI_ID']
					try:
						source=Point('%s %s' %(FacilityCoordinates[facilityID]['lat'], FacilityCoordinates[facilityID]['lon']))
					except:
						continue						
					dest=Point('%s %s'%(mesh_years[i][j][k][0], mesh_years[i][j][k][1]))
					sourcelat=FacilityCoordinates[facilityID]['lat']
					sourcelon=FacilityCoordinates[facilityID]['lon']
					destlat=mesh_years[i][j][k][0]
					destlon=mesh_years[i][j][k][1]
					dist=distance.distance(source,dest).kilometers
					if dist>200:
						continue
					x=((dist**2)/2)**0.5
					y=((dist**2)/2)**0.5
					mesh_years[i][j][k][l]+=var.pdf([x,y])*discharge['Tonnes_Air']*1000
					




g=open('ChemicalDimensions', 'wb')
json.dump(ChemicalDimensions, g)


np.save("Mesh", mesh_years, allow_pickle=True, fix_imports=True)
