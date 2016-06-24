import numpy as np
from sklearn.cluster import KMeans
import json
import unicodedata
X = np.load("Sets.npy")


print type(X)
print np.shape(X)
no_clusters=50
estimators = {'k_means_8': KMeans(n_clusters=no_clusters)}

countmembership=[]
for i in xrange(no_clusters):
  countmembership.append(0)
''','k_means_bad_init': KMeans(n_clusters=3, n_init=1, init='random')'''



for name, est in estimators.items():
    est.fit(X[7])
    print est.score(X[7])
    centers = est.cluster_centers_
    for item in est.labels_:
      countmembership[item]+=1

print countmembership
for i in xrange(len(countmembership)):
  if countmembership[i]>50:
    print i+1

    
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
    if centers[i][j]>100:
      f.write('(%s:%f) '%(ChemicalNames[ChemicalDimensionInverse[j]],centers[i][j]))
  f.write('\n')



'''

print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))'''

