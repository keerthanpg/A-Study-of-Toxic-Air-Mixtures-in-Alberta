import json

name='FacilityCoordinates.json'
f=open(name, 'rb')
FacilityCoordinates=json.load(f)
Reduced={}
for k,v in FacilityCoordinates.iteritems():
	new_v={}
	new_v['lat']=v['lat']
	new_v['lng']=v['lon']
	Reduced[k]=new_v

with open(name, 'wb') as fp:
    json.dump(Reduced, fp)