from __future__ import division
import pandas
DNAinfo = pandas.read_csv('/Users/sreehl/Documents/Advanced_Computing/Homework/Assignment3/houseelf_earlength_dna_data.csv')

EarSize = []
gc = []
def GC_Percent(DNASequence):
    GC = (DNASequence.count('G')+DNASequence.count('C'))/len(DNASequence)
    return(GC)

for row in DNAinfo.values:
    gc.append(GC_Percent(row[2]))
for row in DNAinfo.values:
    if (row[1] > 10):
        EarSize.append('Large')   
    if (row[1] <= 10):
        EarSize.append('Small')
results = []
results = zip(DNAinfo['id'],EarSize,gc)
#Get the Average GC Counts by ear size
GCBig = []
GCSmall = []            
for elves in results:
    if elves[1] == ('Large'):
        GCBig.append(elves[2]) 
    if elves[1] == ('Small'):
        GCSmall.append(elves[2])
print 'Average GC Percentage for Large Eared Elves:', (sum(GCBig)/len(GCBig))
print 'Average GC Percentage for Small Eared Elves:', (sum(GCSmall)/len(GCSmall))
TheResults = pandas.DataFrame(results)
TheResults.columns=['id','size','GC Percentage']
pandas.DataFrame.to_csv(TheResults,'/Users/sreehl/Documents/Advanced_Computing/Homework/Assignment3/grangers_analysis.csv')

