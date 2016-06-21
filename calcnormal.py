import numpy as np 
from scipy.stats import multivariate_normal
import os
import json

c=np.load('Points.npy')
for i in xrange(1223):
	for j in xrange(660):
		print c[i][j][0]
		print c[i][j]
		print type(c[i][j])
		print len(c[i][j])
		break
	break
f=open('EmissionByChemical.txt', 'rb')
Emissions=json.load(f)

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
print ChemicalDimensions

g=open('ChemicalDimensions', 'wb')
json.dump(ChemicalDimensions, g)
'''
var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])

for i in xrange(2006, 2013):
	path = '%s/'%str(i)
	for filename in os.listdir(path):
		f=open('%s%s'%(path,filename) , 'rb')

print var.pdf([0,0])

print len(c[0])
print len(c)'''


'''

for i in range(2007, 2013):
	filenames='''
