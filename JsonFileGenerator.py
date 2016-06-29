import json

name='ChemicalNames.json'
f=open(name, 'rb')
ChemicalNames=json.load(f)
NamesInverse={}
for k,v in ChemicalNames.iteritems():
	print v
	NamesInverse[v]=k

with open('NamesInverse.json', 'wb') as fp:
    json.dump(NamesInverse, fp)

with open('NamesInverse', 'wb') as fp:
    json.dump(NamesInverse, fp)

with open('ChemicalNames', 'wb') as fp:
	json.dump(ChemicalNames,fp)

