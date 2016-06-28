import json

name='EmissionByChemical.txt'
f=open(name, 'rb')
FacilityCoordinates=json.load(f)
Reduced={}
for i in range(2006,2013):
	Reduced[str(i)]=FacilityCoordinates[str(i)]

with open('EmissionByChemical.json', 'wb') as fp:
    json.dump(Reduced, fp)