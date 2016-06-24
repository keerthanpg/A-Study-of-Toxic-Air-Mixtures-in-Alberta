import numpy as np
import json


f=open('EmissionByFacility.txt', 'rb')
Emissions=json.load(f)

f=open('EmissionByChemical.txt', 'rb')
EmissionsByChemical=json.load(f)


ChemicalDimensions={}
ChemicalNames={}
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

	for chemical in EmissionsByChemical[str(i)]:
		if chemical in ChemicalDimensions:
			continue
		elif len(EmissionsByChemical[str(i)][chemical]):
			ChemicalDimensions[chemical]=k
			print len(EmissionsByChemical[str(i)][chemical])
			ChemicalNames[chemical]=EmissionsByChemical[str(i)][chemical][0]['CHEM_E']
			k=k+1

Set=np.zeros(shape=(len(FacilitySamples), len(ChemicalDimensions)))
Sets=[Set, Set, Set, Set, Set, Set, Set, Set]#one for each year and one for average


for i in xrange(2006, 2013):
	for facility in Emissions[str(i)]:
		facdem=FacilitySamples[facility]
		for emission in Emissions[str(i)][facility]:
			if emission['CAS_Number'] in ChemicalDimensions:
				chemdem=ChemicalDimensions[emission['CAS_Number']]
				Sets[i-2006][facdem][chemdem]+=emission['Tonnes_Air']


for i in xrange(np.shape(Set)[0]):
	for j in xrange(np.shape(Set)[1]):
		for k in xrange(7):
			Sets[7][i][j]+=Sets[k][i][j]
		Sets[7][i][j]=Sets[7][i][j]/7

np.save("Sets", Sets, allow_pickle=True, fix_imports=True)



f=open('ChemicalNames', 'wb')
json.dump(ChemicalNames,f)

f=open('ChemicalDimensions.txt', 'wb')
json.dump(ChemicalDimensions,f)


