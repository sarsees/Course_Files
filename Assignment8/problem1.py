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
        
perry = Platypus("perry", [3, 2, 4, 1, 2])
print perry.total_fecundity()
print perry.breeding_seasons()
