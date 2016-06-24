import numpy as np
from sklearn.cluster import KMeans
import json
import unicodedata
X = np.load("Sets.npy")


print type(X)
print np.shape(X)

estimators = {'k_means_8': KMeans(n_clusters=5)}
countmembership=[np.zeros(shape=(5))]
''','k_means_bad_init': KMeans(n_clusters=3, n_init=1, init='random')'''



for name, est in estimators.items():
    est.fit(X[7])
    centers = est.cluster_centers_
    print np.shape(centers)
    print est.labels_
    for item in est.labels_:
      countmembership[item]+=1

print countmembership

    
f=open('Centers.txt', 'wb')
g=open('ChemicalDimensions.txt', 'rb')
ChemicalDimensions=json.load(g)
ChemicalDimensionInverse={}
for k,v in ChemicalDimensions.iteritems():
  ChemicalDimensionInverse[v]=k
h=open('ChemicalNames', 'rb')
ChemicalNames=json.load(h)

for i in xrange(np.shape(centers)[0]):
  for j in xrange(np.shape(centers)[1]):
    if centers[i][j]>1000:
      f.write('(%s:%f) '%(ChemicalNames[ChemicalDimensionInverse[j]],centers[i][j]))
  f.write('\n')

