import pandas as pd

def get_data_from_web(url):
    data = pd.read_csv(url)
    return data

BirdData = get_data_from_web('http://www.esapubs.org/archive/ecol/E091/124/TGPP_pres.csv')
#Make a dictionary with year as key and species by site as value
speciesListByYear = dict()
uniqueYears = set(BirdData['year'])
uniquePlots = set(BirdData['plot'])
plotSpeciesList = []
for years in uniqueYears:
    yearData = BirdData[BirdData['year'] == years]
    for plots in uniquePlots:
        plotYearData = yearData[yearData['plot'] == plots]
        plotYearSpeciesData = set(plotYearData['spcode'])
        plotSpeciesList.append(plotYearSpeciesData)
    speciesListByYear[years] = plotSpeciesList

#a function that calculates the Jaccard similiarity 
#between a pair of sites when passed two sets as arguments
def calculate_Jaccard(speciesA,speciesB):
    J = speciesA.intersection(speciesB) / speciesA.union(speciesB)
    return J

calculate_Jaccard(speciesListByYear[1998],speciesListByYear[1999])