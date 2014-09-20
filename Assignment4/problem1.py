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
        ExtantMammal.append([mammal[4],mammal[5]])
    if mammal[1] == 'extinct':
        ExtinctMammal.append([mammal[4],mammal[5]])
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
byStatus = MammalData.groupby(['Status'])
#2
#compare the mean masses within each of the different continents
byContinent = MammalData.groupby(['Contintent','Status'])
summary = byContinent['Combined_Mass'].mean()
conts = ['AF','AUS','Af','EA','Insular','Oceanic','SA']
summary.loc[conts,'extant']-summary.loc[conts,'extinct']



summary.loc['AUS','extant']-summary.loc['AUS','extinct']
summary.loc['EA','extant']-summary.loc['EA','extinct']
summary.loc['Insular','extant']-summary.loc['Insular','extinct']
summary.loc['Oceanic','extant']-summary.loc['Oceanic','extinct']
summary.loc['SA','extant']-summary.loc['SA','extinct']

Summary = pd.DataFrame(summary)
pd.DataFrame.to_csv(Summary,'/Users/sreehl/Documents/Advanced_Computing/Course_Files/Assignment4/continent_mass_differences.csv')
#How do I access these elements to subtract means?

#3 Plotting
import matplotlib.pyplot as plt
AfricanMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AF'])
ExtinctAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extinct']
ExtantAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extant']
#plot the data
plt.hist(ExtantAfricanMammals['Log_Mass'][ExtantAfricanMammals['Log_Mass'] > 0])#, len(ExtantAfricanMammals))
plt.show()