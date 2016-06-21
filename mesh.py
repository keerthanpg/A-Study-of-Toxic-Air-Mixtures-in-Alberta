import numpy as np
import math
import json

a=49.0+(60.0-49.0)*np.linspace(0, 1, num=1223, endpoint=True, retstep=False, dtype=None)
b=-109.0-(121.0-109.0)*np.linspace(0, 1, num=660, endpoint=True, retstep=False, dtype=None)
c=[]
f=open("Points.txt", 'wb')
f.write('%d, %d \n' %(len(a), len(b)))
for i in xrange(0,len(a)):
	c.append([])
	for j in xrange(0,len(b)):
		c[i].append((a[i],b[j]))
		f.write('%f,%f ' %(a[i],b[j]))
	f.write('\n')
c=np.asarray(c)
np.save("Points", c, allow_pickle=True, fix_imports=True)



