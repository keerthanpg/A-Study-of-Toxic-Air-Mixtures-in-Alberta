from xlrd import open_workbook
import json
import math

a= 6378.137#equitorial radius in km
b= 6356.752#polar radius in km
book = open_workbook('NPRI_GEO.xlsx')
sheet = book.sheet_by_index(0)


# read header values into the list    
keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
f=open('DistancesArray', 'w')
PostalCodes = {}
i=0
for row_index in xrange(1, sheet.nrows):
    d = {keys[col_index]: sheet.cell(row_index, col_index).value 
         for col_index in xrange(sheet.ncols)}
    
    if (d['LATI_DEC']==0) |(d['LATI_DEC']==0 ):
    	i+=1
    else:
    	PostalCodes[d['NPRI_ID']]={}
    	'''
    	lat=math.radians(d['LATI_DEC'])
    	longi=math.radians(d['LONG_DEC'])
    	R=(((((a**2)*math.cos(lat))**2)+(((b**2)*math.sin(lat))**2))/((a*math.cos(lat))**2+(b*math.sin(lat))**2))**0.5
    	PostalCodes[d['NPRI_ID']]['x']=R*math.cos(lat)*math.cos(longi)
    	PostalCodes[d['NPRI_ID']]['y']=R*math.cos(lat)*math.sin(longi)'''
    	PostalCodes[d['NPRI_ID']]['x']=d['LATI_DEC']
    	PostalCodes[d['NPRI_ID']]['y']=d['LONG_DEC']
    	f.write("%s %f %f \n" %(d['NPRI_ID'],PostalCodes[d['NPRI_ID']]['x'], PostalCodes[d['NPRI_ID']]['y'] ))

	
g=open('DistancesDic', 'w')
json.dump(PostalCodes, g)

print i
print len(PostalCodes)
