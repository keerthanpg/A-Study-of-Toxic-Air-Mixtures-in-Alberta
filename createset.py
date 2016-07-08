import numpy as np
import json


f=open('EmissionByFacility.txt', 'rb')
Emissions=json.load(f)

f=open('EmissionByChemical.txt', 'rb')
EmissionsByChemical=json.load(f)

f=open('CancerScores', 'rb')
CancerScores=json.load(f)

f=open('NonCancerScores', 'rb')
NonCancerScores=json.load(f)

ChemicalDimensions={}

FacilitySamples={}

j=0
k=0
for i in xrange(2006, 2013):
	for facility in Emissions[str(i)]:
		if facility in FacilitySamples:
			continue
		else:
			FacilitySamples[facility]=j
			j=j+1


Set=np.zeros(shape=(len(FacilitySamples), 2))
Sets=[Set, Set, Set, Set, Set, Set, Set, Set]#one for each year and one for average


for i in xrange(2006, 2013):
	for facility in Emissions[str(i)]:
		facdem=FacilitySamples[facility]
		for emission in Emissions[str(i)][facility]:
			if emission['CAS_Number'] in CancerScores:
				Sets[i-2006][facdem][0]+=emission['Tonnes_Air']*CancerScores[emission['CAS_Number']]['Cancer_Risk_Score']
			if emission['CAS_Number'] in NonCancerScores:
				Sets[i-2006][facdem][0]+=emission['Tonnes_Air']*NonCancerScores[emission['CAS_Number']]['NonCancer_Risk_Score']


for i in xrange(np.shape(Set)[0]):
	for j in xrange(np.shape(Set)[1]):
		for k in xrange(7):
			Sets[7][i][j]+=Sets[k][i][j]
		Sets[7][i][j]=Sets[7][i][j]/7

np.save("EmissionFacilityScores", Sets, allow_pickle=True, fix_imports=True)




