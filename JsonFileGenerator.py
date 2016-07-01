import json

name='EmissionByChemical.json'

ChemicalNames={}
f=open(name, 'rb')
Emission=json.load(f)

for i in xrange(2006,2013):
	for chemicals in Emission[str(i)]:
		if chemicals in ChemicalNames:
			continue
		elif len(Emission[str(i)][chemicals])==0:
			continue
		else:
			ChemicalNames[chemicals]=Emission[str(i)][chemicals][0]['CHEM_E']
			print Emission[str(i)][chemicals][0]['CHEM_E']
			
		
print len(ChemicalNames)
g=open('ChemicalNames.json', 'wb')
json.dump(ChemicalNames,g)

