import random
class Platypus:
    def __init__(self,name,eggCount):
        self.name = name
        self.eggCount = eggCount
        
    def total_fecundity(self):
        return(sum(self.eggCount))
    
    def breeding_seasons(self):
        count = 0
        for eggs in self.eggCount:
            if(eggs > 0):
                count += 1
        return(count)
    
    def lay_eggs(self,numEggs):
        return self.eggCount.append(numEggs)
    
    def platypus_details(self):
        print "%s laid a total of %s eggs in %s successful breeding seasons." % (
            self.name, self.total_fecundity(), self.breeding_seasons())

    
#Problem3    
perry = Platypus("Perry",[0])                                          
winny = Platypus("Winny", [0])
steve = Platypus("Steve", [0])

for seasons in range(1,11):
    for platypus in [perry, winny, steve]:
        platypus.lay_eggs(random.sample(range(1,4),1)[0])
        
perry.platypus_details()
winny.platypus_details()
steve.platypus_details()
    
undergrad_data = [Platypus("perry", [3,2,4,1,2]),
Platypus("quacker", [100,1,3,1,2]),
Platypus("fishface", [0,1,3,1,2,1]),
Platypus("duckhead", [3,1,3,6,3]),
Platypus("waddles", [3,1,2,0,8,3]),
Platypus("professor quackington", [2,1,4,5,7]),
Platypus("bartholomew beavertail", [0,1,3,1,0,0,2]),
Platypus("syd", [3,1,3,1,3,5,5,2,1,3]),
Platypus("ovide", [2,0,10,0,0,0,0,0,0]),
Platypus("hexley", [3,1,2,3,1,0,0,1,1]),
Platypus("supafly", [19,1,2,1,0,0,0,1])]

unlikely_platyped = [platyped.name for platyped in undergrad_data if platyped.total_fecundity()/platyped.breeding_seasons() > 3]



