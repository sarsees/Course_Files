from __future__ import division
import pandas as pd
from itertools import combinations as combinations

def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

BirdData = get_data_from_web('http://www.esapubs.org/archive/ecol/E091/124/TGPP_pres.csv')
#Make a dictionary with year as key and species by site as value
speciesListByYear = dict()
uniqueYears = set(BirdData['year'])
uniquePlots = set(BirdData['plot'])
plotSpeciesList = dict()
for years in uniqueYears:
    yearData = BirdData[BirdData['year'] == years]
    for plot in uniquePlots:
        plotYearData = yearData[yearData['plot'] == plot]
        plotYearSpeciesData = set(plotYearData['spcode'])
        plotSpeciesList[plots] = plotYearSpeciesData
    speciesListByYear[years] = plotSpeciesList

#a function that calculates the Jaccard similiarity 
#between a pair of sites when passed two sets as arguments
def calculate_Jaccard(speciesA,speciesB):
    J = len(speciesA.intersection(speciesB)) / len(speciesA.union(speciesB))
    return J

results = []
plotNumber = []
combinationsOfPlots = []
for year in speciesListByYear:
    combinationsOfPlots = combinations(speciesListByYear[year].keys(),2)
    for plot1, plot2 in combinationsOfPlots:
        results.append([year,plot1,plot2,calculate_Jaccard(speciesListByYear[year][plot1],speciesListByYear[year][plot2])])
resultsData = pd.DataFrame(results)
resultsData.columns = ['Year','ID1','ID2', 'Jaccard Similarity']
pd.DataFrame.to_csv(resultsData,'/Users/sreehl/Documents/Advanced_Computing/Course_Files/Assignment5/Jaccard_similarity.csv')