import numpy as np 
from scipy.stats import multivariate_normal
import os

c=np.load('Points.npy')
for i in xrange(1223):
	for j in xrange(660):
		print c[i][j][0]
		print c[i][j]
		print type(c[i][j])
		print len(c[i][j])
		break
	break


var = multivariate_normal(mean=[0,0], cov=[[1,0],[0,1]])
ChemicalDimensions={}
for i in xrange(2006, 2013):
	path = '%s/'%str(i)
	for filename in os.listdir(path):
		f=open('%s%s'%(path,filename) , 'rb')

print var.pdf([0,0])

print len(c[0])
print len(c)


'''

for i in range(2007, 2013):
	filenames='''
