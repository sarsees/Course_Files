data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
        ['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
        ['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
        ['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
        ['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
        ['D5', 98], ['D6', 32]]
#How many sites are there
sites = len(data)
#How many birds are at the 7th site
print(data[6][1])
#How many birds are at the last site
print(data[25][1])
#What is the total number of birds counted across all sites
count = 0
for thing in data:
    count += thing[1]
print(count)
#What is the total number of birds counted on sites with codes beginning with C? 
CountForBirdsAtC = 0
for thing in data:
    if thing[0].startswith('C'):
        CountForBirdsAtC += thing[1]
print(CountForBirdsAtC)
    


    
    

