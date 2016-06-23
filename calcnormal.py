import numpy as np 
from scipy.stats import multivariate_normal
import os
import json
import geopy

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

print np.shape(mesh_years)

for i in xrange(np.shape(mesh_years)[0]):
	for j in xrange(np.shape(mesh_years)[1]):
		for k in xrange(np.shape(mesh_years)[2]):
			mesh_years[i][j][k]=np.asarray(mesh_years[i][j][k])
			print np.shape(mesh_years[i][j][k])
			for l in xrange(140):
				np.append((mesh_years[i][j][k], 0), axis=1)
			print np.shape(mesh_years[i][j][k])
			print mesh_years[i][j][k]
			print len(mesh_years[i][j][k])
			print mesh_years[i][j][k][2]

			break
		break
	break


	


	
print var.pdf([0,0])

g=open('ChemicalDimensions', 'wb')
json.dump(ChemicalDimensions, g)

'''

for i in range(2007, 2013):
	filenames='''
