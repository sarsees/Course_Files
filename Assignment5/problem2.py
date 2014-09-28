from __future__ import division
import pandas as pd
from itertools import combinations as combinations

def calculate_Euclidean_distance(SpeciesSiteA, SpeciesSiteB):
    def calculate_relative_abundance(SiteSpeciesDict):
        counts = []
        for key in SiteSpeciesDict:
            counts.append(SiteSpeciesDict.get(key,0))
            totalsum = sum(counts)  
        RelativeAbundanceDict = dict((k, float(SiteSpeciesDict[k]) / totalsum) for k in SiteSpeciesDict)
        return RelativeAbundanceDict
    


    

 
 
     
def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

BirdData = get_data_from_web('http://www.esapubs.org/archive/ecol/E091/124/TGPP_cover.csv')
#Create a dict for each site by species name and cover
#Sort by Site
groupedBirdData = BirdData.groupby(['plot','spcode'])    
SiteDictOfCoverDict = dict()   
SumGroupBirdData = groupedBirdData.sum()
for site in SumGroupBirdData.index.levels[0]:#get a list of indices from group
    SiteDictOfCoverDict[site] = dict(SumGroupBirdData.loc[site]['cover'])
#Combinations of Plots
results = []
plotNumber = []
CombinationsOfDicts = []
for plot in SiteDictOfCoverDict:
    CombinationsOfDicts = combinations(SiteDictOfCoverDict[plot].keys(),2)
    for plot1, plot2 in CombinationsOfDicts:
        results.append([plot1,plot2,calculate_Euclidean_distance(speciesListByYear[year][plot1],speciesListByYear[year][plot2])])
resultsData = pd.DataFrame(results)
resultsData.columns = ['ID1','ID2', 'Euclidean Distance']

counts = []
RealtiveAbundanceA = []
for key in SiteDictOfCoverDict[226]:
    counts.append(SiteDictOfCoverDict[226].get(key,0))
    totalsumA = sum(counts)  
RealtiveAbundanceA.append(SiteDictOfCoverDict[226].values()/totalsumA)
SiteDictOfCoverDict[226] = RealtiveAbundanceA

SpeciesAcounts = []
SpeciesBcounts = []
for key in SpeciesSiteA, SpeciesSiteB:
    SpeciesAcounts.append(SpeciesSiteA.get(key,0))
    SpeciesBcounts.append(SpeciesSiteB.get(key,0))
    totalsumA = sum(SpeciesAcounts)  
    totalsumB = sum(SpeciesBcounts)
RealtiveAbundanceA = SpeciesSiteA.append(SpeciesSiteA.values()/totalsumA)
RealtiveAbundanceB = SpeciesSiteB.append(SpeciesSiteB.values()/totalsumB)


counts = []
RealtiveAbundanceA = {}
for key in SiteDictOfCoverDict[226]:
    counts.append(SiteDictOfCoverDict[226].get(key,0))
    totalsumA = sum(counts)  
    RealtiveAbundanceA[key] = (SiteDictOfCoverDict[226].values()/totalsumA)    

