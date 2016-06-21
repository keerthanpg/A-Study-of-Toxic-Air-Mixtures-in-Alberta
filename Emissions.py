from xlrd import open_workbook
import json
import math
import unicodedata
import os

f=open('DistancesDic', 'rb')
Coordinates=json.load(f)

g=open('EmissionByChemical.txt', 'rb')
Emissions=json.load(g)

NoValidCoordinates=[]
'''
filename = "/my/directory/filename.txt"
dir = os.path.dirname(filename)
os.mkdir(dir)

try:
    os.stat(dir)

    newpath = r'\%s'%year
if not os.path.exists(newpath):
    os.makedirs(newpath)'''

i=0
j=0#without valid coordinates

for year in Emissions:
    year=unicodedata.normalize('NFKD', year).encode('ascii','ignore')
    newpath = r'%s/'%year
    os.mkdir(newpath)
    for chemical in Emissions[year]:
        chemical1=chemical
        if chemical=='NA - D/F':
            continue
        if chemical=='NA - P/H':
            chemical1='NA - PH'

        chemical=unicodedata.normalize('NFKD', chemical).encode('ascii','ignore')
        f=open(r'%s/%s'%(year, chemical1), 'wb')
        for entry in Emissions[year][chemical]:
            if entry['NPRI_ID'] in Coordinates:
                f.write('%f, %f, %f \n' %(Coordinates[entry['NPRI_ID']]['x'], Coordinates[entry['NPRI_ID']]['y'], entry['Tonnes_Air']))
            else:
                print ('%s doesnt have valid coordinates' %entry['NPRI_ID'])
                if entry['NPRI_ID'] not in NoValidCoordinates:
                    NoValidCoordinates.append(entry['NPRI_ID'] )
                    j+=1

print j