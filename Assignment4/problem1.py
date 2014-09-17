import pandas as pd
import numpy as np

def get_data_from_web(url):
    data = pd.read_csv(url,delimiter='\t',names= ["Contintent","Status","Order","Family","Genus","Species","Log_Mass","Combined_Mass","Reference"])
    return data

MammalData = get_data_from_web('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt')
#Find out how many species are in this massive dataset and print the result to the screen

SpeciesArray = np.unique(zip(MammalData['Species'],MammalData['Genus']))
print 'Number of Species:',len(SpeciesArray)

#Find out how many of the species are extinct and how many are extant
ExtinctCount = 0
ExtantCount = 0
for mammal in MammalData.values:
    if mammal[1] == 'extant':
        ExtantCount += 1
    if mammal[1] == 'extinct':
        ExtinctCount += 1
print "Extant Mammals:",ExtantCount
print "Extinct Mammals:",ExtinctCount

#Find out how many genera are present in the dataset
genera = []
for mammal in MammalData.values:
    genera.append(mammal[4])
print "Unique Genera:",len(np.unique(genera))

#Print the names and mass of the largest and smallest species 
size = []
for mammal in MammalData.values:
    if mammal[7] >= 0:
        size.append(mammal[7])
    else:
        size.append(0)
LargestMammal = MammalData.values[size.index(max(size))]  
SmallestMammal = MammalData.values[size.index(min(size))]  
print "Largest Mammal:",LargestMammal[3:6]
print "Has A Mass of:", max(size),"(g)" 
print "Smallest Mammal:",SmallestMammal[3:6]
print "Has A Mass of:", min(size),"(g)" 