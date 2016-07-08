import json

f=open('EmissionByFacility.json', 'rb')
Emissions=json.load(f)

f=open('CancerScores', 'rb')
CancerScores=json.load(f)

f=open('NonCancerScores', 'rb')
NonCancerScores=json.load(f)

FacilityEmissionScores={}
for i in xrange(2006,2013):
    FacilityEmissionScores[str(i)]={}
    for facility in Emissions[str(i)]:
        FacilityEmissionScores[str(i)][facility]={}
        FacilityEmissionScores[str(i)][facility]['Cancer_Tonnes']=0.0
        FacilityEmissionScores[str(i)][facility]['NonCancer_Tonnes']=0.0
        for discharge in Emissions[str(i)][facility]:
        	casno=discharge['CAS_Number']
        	tonnes=discharge['Tonnes_Air']
        
        	if casno in CancerScores:
        		FacilityEmissionScores[str(i)][facility]['Cancer_Tonnes']+=tonnes*CancerScores[casno]
    		if casno in NonCancerScores:
    			FacilityEmissionScores[str(i)][facility]['NonCancer_Tonnes']+=tonnes*NonCancerScores[casno]
    			

f=open('FacilityRiskScore', 'wb')
json.dump(FacilityEmissionScores,f)

        


