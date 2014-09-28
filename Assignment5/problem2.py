from __future__ import division
import pandas as pd
from itertools import combinations as combinations
import math as math

#Function to calculate the Euclidean Distance of relative species abundance between two locations
#Takes dict(site: species, abundance) as inputs
def calculate_Euclidean_distance(SpeciesSiteA, SpeciesSiteB):
    #Calculate species abundance/ total abundance
    def calculate_relative_abundance(SiteSpeciesDict):
        counts = []
        for key in SiteSpeciesDict:
            counts.append(SiteSpeciesDict.get(key,0))
            totalsum = sum(counts)  
        RelativeAbundanceDict = dict((k, SiteSpeciesDict[k] / totalsum) for k in SiteSpeciesDict)
        return RelativeAbundanceDict
    RelativeSpeciesA = calculate_relative_abundance(SpeciesSiteA)
    RelativeSpeciesB = calculate_relative_abundance(SpeciesSiteB)
    difference = []
    for keyA in RelativeSpeciesA:
        for keyB in RelativeSpeciesB:
            if keyA == keyB:
                difference.append(RelativeSpeciesA[keyA]-RelativeSpeciesB[keyB])
    return math.sqrt(sum(difference)**2)
                
#Import Data    
def get_data_from_web(url):
    data = pd.read_csv(url)
    return data
BirdData = get_data_from_web('http://www.esapubs.org/archive/ecol/E091/124/TGPP_cover.csv')

#Create a dict for each site by species name and cover
#Sort by Site and Species first
groupedBirdData = BirdData.groupby(['plot','spcode'])    
SiteDictOfCoverDict = dict()   
SumGroupBirdData = groupedBirdData.sum()
for site in SumGroupBirdData.index.levels[0]:#get a list of indices from group
    SiteDictOfCoverDict[site] = dict(SumGroupBirdData.loc[site]['cover'])
    
#Combinations of Plots
results = []
CombinationsOfDicts = combinations(SiteDictOfCoverDict.keys(),2)
for plot1, plot2 in CombinationsOfDicts:
    results.append([plot1, plot2, 1-(calculate_Euclidean_distance(SiteDictOfCoverDict[plot1],SiteDictOfCoverDict[plot2]))])
#Write results
resultsData = pd.DataFrame(results)
resultsData.columns = ['ID1','ID2', '1-Euclidean Distance']
pd.DataFrame.to_csv(resultsData,'/Users/sreehl/Documents/Advanced_Computing/Course_Files/Assignment5/Abundance_similarity.csv')
