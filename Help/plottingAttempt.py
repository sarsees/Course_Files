import pandas as pd
import numpy as np

def get_data_from_web(url):
    data = pd.read_csv(url,delimiter='\t',names= ["Contintent","Status","Order","Family","Genus","Species","Log_Mass","Combined_Mass","Reference"])
    return data

MammalData = get_data_from_web('http://www.esapubs.org/archive/ecol/E084/094/MOMv3.3.txt')

import matplotlib.pyplot as plt
AfricanMammals = pd.DataFrame(MammalData[MammalData['Contintent'] == 'AF'])
ExtinctAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extinct']
ExtantAfricanMammals = AfricanMammals[AfricanMammals['Status'] == 'extant']
#plot the data
plt.subplot(1, 2, 1)
plt.hist(ExtantAfricanMammals['Log_Mass'][ExtantAfricanMammals['Log_Mass'] > 0])#, len(ExtantAfricanMammals))
plt.xlabel('Log Mass (g)', fontsize=20)
plt.ylabel('Individuals', fontsize= 20)
plt.hist(ExtinctAfricanMammals['Log_Mass'][ExtinctAfricanMammals['Log_Mass'] > 0])
plt.show()