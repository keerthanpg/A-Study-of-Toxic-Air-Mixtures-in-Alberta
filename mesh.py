import numpy as np
import math
import json

a=49.0+(60.0-49.0)*np.linspace(0, 1, num=1223, endpoint=True, retstep=False, dtype=None)
b=-109.0-(121.0-109.0)*np.linspace(0, 1, num=660, endpoint=True, retstep=False, dtype=None)
c=np.zeros((len(a), len(b), 142))
for i in xrange(np.shape(c)[0]):
	for j in xrange(np.shape(c)[1]):
		c[i][j][0]=a[i]
		c[i][j][1]=b[j]
c=np.asarray(c)
np.save("Points", c, allow_pickle=True, fix_imports=True)



