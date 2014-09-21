#3 Plotting
import matplotlib.pyplot as plt
#Separate into Extinct and Extant Mammals for AF
AfricanMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AF'])
ExtinctAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extinct']
ExtantAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extant']
#plot the data
plt.subplot(1, 2, 1)
plt.hist(ExtantAfricanMammals['Log_Mass'][ExtantAfricanMammals['Log_Mass'] > 0])#, len(ExtantAfricanMammals))
plt.xlabel('Log Mass (g)', fontsize=20)
plt.ylabel('Individuals', fontsize= 20)
#Extant Mammals will plot without a hitch, but Extinct Mammals spit out several lines of error
plt.hist(ExtinctAfricanMammals['Log_Mass'][ExtinctAfricanMammals['Log_Mass'] > 0])
plt.show()
#I noticed that the indexing is funny for ExtinctAfricanMammals, but I'm not sure why that matters