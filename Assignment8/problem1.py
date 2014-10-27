class Platypus:
    def __init__(self,name,eggCount):
        self.name = name
        self.eggCount = eggCount
        
    def total_fecundity(self):
        return(sum(self.eggCount))
perry = Platypus("perry", [3, 2, 4, 1, 2])
print perry.total_fecundity()
