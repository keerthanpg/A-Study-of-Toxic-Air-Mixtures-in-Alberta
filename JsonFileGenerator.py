import json


f=open('EmissionByChemical.json', 'rb')
Emission=json.load(f)

g=open('Graph.txt', 'ab')

h=open("ChemicalNames", 'rb')
ChemicalNames=json.load(h)

for chemical,name in ChemicalNames.iteritems():	
	g.write("\n%s; " %name)
	for i in range(2006,2013):		
		tonnes=0	
		if chemical in Emission[str(i)]:
			for emissions in Emission[str(i)][chemical]:
				tonnes+=emissions['Tonnes_Air']				
		g.write("%f; " %tonnes)

g.close()

