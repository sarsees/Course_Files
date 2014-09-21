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
ExtinctMammal = []
ExtantMammal = []
for mammal in MammalData.values:
    if mammal[1] == 'extant':
        ExtantMammal.append([mammal[4],mammal[5],mammal[7]])
    if mammal[1] == 'extinct':
        ExtinctMammal.append([mammal[4],mammal[5],mammal[7]])
#Gather Mean information
ExtantMammal = pd.DataFrame(ExtantMammal)
ExtantMean = ExtantMammal.mean().values[0]
ExtinctMammal = pd.DataFrame(ExtinctMammal)
ExtinctMean = ExtinctMammal.mean().values[0]
print "The average mass of extant species is:", ExtantMean, '(g)'
print "and the average mass of extinct species is:", ExtinctMean, '(g)'

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

#3 Plotting: Interested in AF, AUS, Insular, SA
#Yes, this is cheap and a result of broken for loops
AfricanMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AF'])
ExtinctAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extinct']
ExtantAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extant']

AustralianMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AUS'])
ExtinctAustralienMammals = AustralianMammals[AustralianMammals['Status'] == 'extinct']
ExtantAustralienMammals = AustralianMammals[AustralianMammals['Status'] == 'extant']

AustralianMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AUS'])
ExtinctAustralienMammals = AustralianMammals[AustralianMammals['Status'] == 'extinct']
ExtantAustralienMammals = AustralianMammals[AustralianMammals['Status'] == 'extant']

InsularMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'Insular'])
ExtinctInsularMammals = InsularMammals[InsularMammals['Status'] == 'extinct']
ExtantInsularMammals = InsularMammals[InsularMammals['Status'] == 'extant']

SAMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'SA'])
ExtinctSAMammals = SAMammals[SAMammals['Status'] == 'extinct']
ExtantSAMammals = SAMammals[SAMammals['Status'] == 'extant']
#plot the data
import matplotlib.pyplot as plt
#AF
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(8, 6.5))
plt.suptitle('AF Mammals',fontsize=20)
ax0.hist(ExtantAfricanMammals['Log_Mass'][ExtantAfricanMammals['Log_Mass'] > 0])
ax0.set_title('Extant Mammals')
ax1.hist(ExtinctAfricanMammals['Log_Mass'][ExtinctAfricanMammals['Log_Mass'] > 0].values,histtype='bar', facecolor='g')
ax1.set_title('Extinct Mammals')
ax1.axis([0, 7, 0, 3])
fig.text(0.5, 0.04, 'Log Mass (g)', ha='center', va='center',fontsize=14)
fig.text(0.06, 0.5, 'Individuals', ha='center', va='center', rotation='vertical', fontsize=14)
plt.show()

#AUS
fig, (ax2, ax3) = plt.subplots(ncols=2, figsize=(8, 6.5))
plt.suptitle('AUS Mammals',fontsize=20)
ax2.hist(ExtantAustralienMammals['Log_Mass'][ExtantAustralienMammals['Log_Mass'] > 0].values)
ax2.set_title('Extant Mammals')
ax3.hist(ExtinctAustralienMammals['Log_Mass'][ExtinctAustralienMammals['Log_Mass'] > 0].values,histtype='bar', facecolor='g')
ax3.set_title('Extinct Mammals')
ax3.axis([0, 7, 0, 16])
fig.text(0.5, 0.04, 'Log Mass (g)', ha='center', va='center',fontsize=14)
fig.text(0.06, 0.5, 'Individuals', ha='center', va='center', rotation='vertical', fontsize=14)
plt.show()

#Insular

fig, (ax4, ax5) = plt.subplots(ncols=2, figsize=(8, 6.5))
plt.suptitle('Insular Mammals',fontsize=20)
ax4.hist(ExtantInsularMammals['Log_Mass'][ExtantInsularMammals['Log_Mass'] > 0].values)
ax4.set_title('Extant Mammals')
ax5.hist(ExtinctInsularMammals['Log_Mass'][ExtinctInsularMammals['Log_Mass'] > 0].values,histtype='bar', facecolor='g')
ax5.set_title('Extinct Mammals')
ax5.axis([0, 7, 0, 8])
fig.text(0.5, 0.04, 'Log Mass (g)', ha='center', va='center',fontsize=14)
fig.text(0.06, 0.5, 'Individuals', ha='center', va='center', rotation='vertical', fontsize=14)
plt.show()

#SA

fig, (ax6, ax7) = plt.subplots(ncols=2, figsize=(8, 6.5))
plt.suptitle('SA Mammals',fontsize=20)
ax6.hist(ExtantSAMammals['Log_Mass'][ExtantSAMammals['Log_Mass'] > 0].values)
ax6.set_title('Extant Mammals')
ax7.hist(ExtinctSAMammals['Log_Mass'][ExtinctSAMammals['Log_Mass'] > 0].values,histtype='bar', facecolor='g')
ax7.set_title('Extinct Mammals')
ax7.axis([0, 7, 0, 20])
fig.text(0.5, 0.04, 'Log Mass (g)', ha='center', va='center',fontsize=14)
fig.text(0.06, 0.5, 'Individuals', ha='center', va='center', rotation='vertical', fontsize=14)
plt.show()
