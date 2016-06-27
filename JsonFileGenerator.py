import json

name='ChemicalNames'
f=open(name, 'rb')
FacilityCoordinates=json.load(f)
with open('ChemicalNames.json', 'wb') as fp:
    json.dump(FacilityCoordinates, fp)