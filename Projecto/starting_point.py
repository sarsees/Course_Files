from openpyxl import load_workbook
import scipy.optimize
import numpy as np
import matplotlib.pyplot as plt
#Read me: describe the problem and anything you need to run the code
#Conclusion of nested loop


def extract_data(data):
    data_range_start = []
    data_range_end = []
    usable_data = []
    
    def excel_col(col):
        """col is a column number returns letter. 1=A """
        quot, rem = divmod(col-1,26)
        return excel_col(quot) + chr(rem+ord('A')) if col!=0 else ''    

    for column in range(2,38):
        data_range_start.append(str(excel_col(column))+'17')
        data_range_end.append(str(excel_col(column))+'24')
    
    for i, start_pos in enumerate(data_range_start):
        end_pos = data_range_end[i]
        cell_range = data[start_pos:end_pos]
        col_results = [n[0].value for n in cell_range]
        usable_data.append(col_results)
    return(usable_data)

def wSSE(x, rep1, rep2, dilution): 
    """wSSE is a function that returns a weighted sum of squares error
    value for optimization with fmin.
    Inputs:
    x, a vector of parameters to estimate the model 5 parameter logistic curve f(x,dilution)
    rep1, a vector of observed pixel intensities- first replicate
    rep2, a vector of observed pixel intensities- second replicate
    dilution: column of serial dilutions (first column of analyte data)
    """
    replicates = np.hstack((rep1,rep2))    
    weights = np.hstack( ((rep1-rep2)**2,(rep1-rep2)**2) )
    constant = 1/sum(weights);
    err = sum(constant*weights*( f(x,dilution) - replicates)**2 );  
    return(err)

def f(x,dilution):
    """f is function that evaluates a 5 parameter logistic curve at
    the log of given, replicate, serial dilutions
    Inputs:
    x[0], the estimated response at infinite concentration
    x[1], the estimated response at zero concentration
    x[2], the slope factor
    x[3], the mid-range concentration
    x[4], asymmetry factor
    dilution: column of serial dilutions (first column of analyte data)"""
    #Make columns for two replicates for simultaneous fitting
    temp_dilution = np.log(dilution)
    dup_dilution = np.hstack((temp_dilution,temp_dilution))
    
    #calculate response(pixel intensity) for these parameters
    return ( np.array (x[0] + (x[1] - x[0])/( (1 + abs((dup_dilution/x[3])**x[2]) )**x[4] ) ) ) 

def alternate(i):
    i = iter(i)
    while True:
        yield(i.next(), i.next())
        
#Get workable data
wb_template = load_workbook('Data_for_Sarah.xlsx', data_only=True)
data = wb_template[ "Signal" ]
working_data = extract_data(data)

#First column of any data is dilution scheme
dilution = np.array(working_data[0]) 
#Following columns are organized into replicates
columns = range(1,len(working_data))
col_pairs = list(alternate(columns)) 
backfit_results_table = []

for pairs in col_pairs:    
    rep1 = np.array(working_data[pairs[0]])
    rep2 = np.array(working_data[pairs[1]])
    #Optimization
    xopt = scipy.optimize.fmin(func = wSSE, 
                               x0 = [18.0, 65000.0, -10.0, 5.0, 0.75],
                               args = ((rep1,rep2,dilution)),
                               maxiter=1*10**6, 
                               maxfun=1*10**6)
    predicted_vals = np.array(f(xopt, dilution))
    backfit = np.hstack((rep1,rep2))/predicted_vals
    backfit_results_table.append(backfit)
    
plt.plot( [np.log(dilution)], [rep1],'bo')
plt.plot( [np.log(dilution)],[f(xopt,dilution)],'ro')
plt.show()


     