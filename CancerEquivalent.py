from xlrd import open_workbook
import json

book_C = open_workbook('teps.xlsx')
sheet_C = book_C.sheet_by_index(0)


# read header values into the list    
keys = [sheet_C.cell(0, col_index).value for col_index in xrange(sheet_C.ncols)]

cancer_teps = {}
noncancer_teps = {}

for row_index in xrange(1, sheet_C.nrows):
    d = {keys[col_index]: sheet_C.cell(row_index, col_index).value 
         for col_index in xrange(sheet_C.ncols)}
    e= {keys[col_index]: sheet_C.cell(row_index, col_index).value 
         for col_index in xrange(sheet_C.ncols)}
    if d['Cancer_Risk_Score'] !="":
        cancer_teps[d['CAS_Number']]=d['Cancer_Risk_Score']
    
    if e['NonCancer_Risk_Score'] !="":
    	noncancer_teps[d['CAS_Number']]=d['NonCancer_Risk_Score']

f=open("CancerScores", 'wb')
json.dump(cancer_teps,f)
g=open("NonCancerScores", 'wb')
json.dump(noncancer_teps,g)

