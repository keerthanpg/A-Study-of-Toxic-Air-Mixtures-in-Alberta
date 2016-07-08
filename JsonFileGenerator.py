import json


f=open('EmissionByChemical.json', 'rb')
Emission=json.load(f)

Emission_dic={}

for i in range(2006,2013):
	Emission_dic[str(i)]={}
	for chemical in Emission[str(i)]:
		Emission_dic[str(i)][chemical]={}
		j=0
		print len(Emission[str(i)][chemical])
		for item in Emission[str(i)][chemical]:
			Emission_dic[str(i)][chemical][j]=item
			j+=1
		print len(Emission_dic[str(i)][chemical])

f=open('EmissionByChemicalDic.json', 'wb')
json.dump(Emission_dic,f)