import json



f=open('ChemicalNames.json', 'rb')
ChemicalNames=json.load(f)

ChemicalNamesInverse={}

for k,v in ChemicalNames.iteritems():
	ChemicalNamesInverse[v]=k
g=open('ChemicalNumbers.json', 'wb')
json.dump(ChemicalNamesInverse,g)

