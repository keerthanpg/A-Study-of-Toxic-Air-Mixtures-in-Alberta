import json
import os
os.chdir('C:\Users\David\Desktop\Alberta\A-Study-of-Toxic-Air-Mixtures-in-Alberta')
f=open('EmissionByFacility.json', 'rb')
Emissions=json.load(f)

f=open('CancerScores', 'rb')
CancerScores=json.load(f)

f=open('NonCancerScores', 'rb')
NonCancerScores=json.load(f)

FacilityEmissionScores={}
for i in xrange(2006,2013):
    for facility in Emissions[str(i)]:
    	for discharge in Emissions[str(i)][facility]:
            casno=discharge['CAS_Number']
            tonnes=discharge['Tonnes_Air']
            if casno in CancerScores:
                if facility in FacilityEmissionScores:
                    if str(i) in FacilityEmissionScores[facility]:
                        if 'Cancer_Tonnes' in  FacilityEmissionScores[facility][str(i)]:
                            FacilityEmissionScores[facility][str(i)]['Cancer_Tonnes']+=tonnes*CancerScores[casno]
                        else:
                            FacilityEmissionScores[facility][str(i)]['Cancer_Tonnes']=tonnes*CancerScores[casno]
                    else:
                        FacilityEmissionScores[facility][str(i)]={}
                        FacilityEmissionScores[facility][str(i)]['Cancer_Tonnes']=tonnes*CancerScores[casno]
                else:
                    FacilityEmissionScores[facility]={}
                    FacilityEmissionScores[facility][str(i)]={}
                    FacilityEmissionScores[facility][str(i)]['Cancer_Tonnes']=tonnes*CancerScores[casno]

            if casno in NonCancerScores:
                if facility in FacilityEmissionScores:
                    if str(i) in FacilityEmissionScores[facility]:
                        if 'NonCancer_Tonnes' in  FacilityEmissionScores[facility][str(i)]:
                                FacilityEmissionScores[facility][str(i)]['NonCancer_Tonnes']+=tonnes*NonCancerScores[casno]
                        else:
                                FacilityEmissionScores[facility][str(i)]['NonCancer_Tonnes']=tonnes*NonCancerScores[casno]
                    else:
                            FacilityEmissionScores[facility][str(i)]={}
                            FacilityEmissionScores[facility][str(i)]['NonCancer_Tonnes']=tonnes*NonCancerScores[casno]
                else:
                        FacilityEmissionScores[facility]={}
                        FacilityEmissionScores[facility][str(i)]={}
                        FacilityEmissionScores[facility][str(i)]['NonCancer_Tonnes']=tonnes*NonCancerScores[casno]
   			

f=open('FacilityRiskScore', 'wb')
json.dump(FacilityEmissionScores,f)

        


