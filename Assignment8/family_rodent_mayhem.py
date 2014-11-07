import re
import pandas as pd
import sqlite3 as dbapi
#bring data in one line at a time and store any output you need to

inputfile = open('rodents.php', 'r')

results = []
familyresults = []
speciesresults=[]
nomatch = []

def get_family(inputline):
    """Find the rodent family name from text file"""
    family_re = "(Family ?(..[A-Z][a-z]+..))"
    for family in family_re:
        family_search = re.search(family_re, inputline)
        if family_search:
            return family_search.group(1)
        
        
def get_species(inputline):
    """Find the rodent genus and species name from text file"""
    species_re = "([A-Z][a-z]+ [a-z]+)" #parens makes a group for matching items
    species_search = re.search(species_re, inputline)
    if species_search:
        return species_search.group(1)
                                                                                   
con = dbapi.connect("rodent_names")
cur = con.cursor()  

for line in inputfile:
    family = get_family(line)
    species = get_species(line)
    if family:
        results.append(family)
        cur.execute("INSERT INTO Rodents VALUES (?)", (family,))
    if species:
        results.append(species)
        cur.execute("INSERT INTO Rodents VALUES (?)", (species,))
    else:
        nomatch.append(line)
con.commit()       





