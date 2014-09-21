import pandas as pd
import numpy as np

def get_data_from_web(url):
    data = pd.read_csv(url,delimiter='\t',names= ["Contintent","Status","Order","Family","Genus","Species","Log_Mass","Combined_Mass","Reference"])
    return data

MammalData = get_data_from_web('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt')
#Find out how many species are in this massive dataset and print the result to the screen

SpeciesArray = np.unique(zip(MammalData['Species'],MammalData['Genus']),return_index=True)
print 'Number of Species:',len(SpeciesArray)

#Find out how many of the species are extinct and how many are extant
ExtinctMammal = []
ExtantMammal = []
for mammal in MammalData.values:
    if mammal[1] == 'extant':
        ExtantMammal.append([mammal[4],mammal[5],mammal[7]])
    if mammal[1] == 'extinct':
        ExtinctMammal.append([mammal[4],mammal[5],mammal[7]])
#Make numpy arrays so we can identify unique species    
ExtantMammal = np.array(ExtantMammal)
ExtinctMammal = np.array(ExtinctMammal)
print "Extant Mammals:",len(np.unique(ExtantMammal))
print "Extinct Mammals:",len(np.unique(ExtinctMammal))

#Find out how many genera are present in the dataset
print "Unique Families:",len(np.unique(MammalData['Family']))

#Print the names and mass of the largest and smallest species 
size = MammalData['Combined_Mass']
m = max(size)
n = min(size)
MaxIndex =[i for i, j in enumerate(size) if j == m]#thank you StackOverflow 'SilentGhost'
MaxIndex = MaxIndex[0]
MinIndex = [i for i, j in enumerate(size) if j == n]
#Lots of small mammals in a list
SmallestMammals = []
for animal in MinIndex:
    SmallestMammals.append(MammalData.values[animal][3:6])
#Output
print "Largest Mammal:",MammalData.values[MaxIndex][3:6]
print "Has A Mass of:", max(size),"(g)" 
print "First Smallest Mammal:",SmallestMammals[0]
print "Has A Mass of:", min(size),"(g)" 

#Calculate the average (i.e., mean) mass of extinct species and the average mass of extant species.
ExtantMammal = pd.DataFrame(ExtantMammal)
ExtantMean = pd.DataFrame.mean(ExtantMammal)
ExtinctMammal = pd.DataFrame(ExtinctMammal)
ExtinctMean = pd.DataFrame.mean(ExtinctMammal)
print "The average mass of extant species is:", ExtantMean
print "and the average mass of extinct species is:", ExtinctMean

#2
#compare the mean masses within each of the different continents
byContinent = MammalData.groupby(['Contintent','Status'])
#summary = byContinent['Combined_Mass'].mean() maybe this would work in the future
gonersByCont= []
stillHereByCont = []
for continent, continent_data in byContinent:
    if continent[1] == 'extinct':
        gonersByCont.append([continent[0], continent_data['Combined_Mass'].mean()])
    if continent[1] == 'extant':
        stillHereByCont.append([continent[0],continent_data['Combined_Mass'].mean()])
Gone = pd.DataFrame(gonersByCont)
Here = pd.DataFrame(stillHereByCont)
matches = []
for idx, a in enumerate(Here[0]):
    for gidx, b in enumerate(Gone[0]):
        if a == b:
            matches.append([a,Gone[1][gidx]-Here[1][idx]])
Summary = pd.concat([Gone, Here,pd.DataFrame(matches)],axis=1)
Summary.columns = ['Extinct Location','Average Mass','Extant Location',
                   'Average Mass','Comparison Location','Mean Extinct Mass - Mean Extant Mass']
pd.DataFrame.to_csv(Summary,'/Users/sreehl/Documents/Advanced_Computing/Course_Files/Assignment4/continent_mass_differences.csv')

#3 Plotting
import matplotlib.pyplot as plt
AfricanMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AF'])
ExtinctAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extinct']
ExtantAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extant']
#plot the data
plt.subplot(1, 2, 1)
plt.hist(ExtantAfricanMammals['Log_Mass'][ExtantAfricanMammals['Log_Mass'] > 0])#, len(ExtantAfricanMammals))
plt.xlabel('Log Mass (g)', fontsize=20)
plt.ylabel('Individuals', fontsize= 20)
plt.hist(ExtinctAfricanMammals['Log_Mass'][ExtinctAfricanMammals['Log_Mass'] > 0])
plt.show()