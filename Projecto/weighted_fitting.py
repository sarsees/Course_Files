from openpyxl import load_workbook
import scipy.optimize
import numpy as np
import csv
import matplotlib.pyplot as plt
#Read me: describe the problem and anything you need to run the code
#Conclusion of nested loop


def extract_data(data,start_row,end_row,start_col,end_col):
    data_range_start = []
    data_range_end = []
    usable_data = []
    
    def excel_col(col):
        """col is a column number returns letter. 1=A """
        quot, rem = divmod(col-1,26)
        return excel_col(quot) + chr(rem+ord('A')) if col!=0 else ''    

    for column in range(start_col,end_col):
        data_range_start.append(str(excel_col(column))+start_row)
        data_range_end.append(str(excel_col(column))+end_row)
    
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

def wMPLE(x, rep1, rep2, dilution):   
    """wSSE is a function that returns a weighted Maximum Posterior Likelihood error
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
    nobs = 2*len(rep1);
    err = (nobs/2*np.log(2*np.pi*x[5]**2)
           + nobs*sum(constant*weights*(f(x,dilution) - replicates)**2)/(2*x[5]**2)
           + 0.5*np.log(2*np.pi*x[6]^2)+(x[0]-x[11])**2/(2*x[6]**2)
           + 0.5*np.log(2*np.pi*x[7]^2)+(x[1]-x[12])**2/(2*x[7]**2)
           + 0.5*np.log(2*np.pi*x[8]**2)+(x[3]-x[14])**2/(2*x[8]**2)
           + 0.5*np.log(2*np.pi*x[10]**2)+(x[4]-x[15])**2/(2*x[10]**2)
           + 0.5*np.log(2*np.pi*x[9]**2)+(x[2]-x[13])**2/(2*x[9]**2))
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
    dilution, column of serial dilutions (first column of analyte data)"""
    #Make columns for two replicates for simultaneous fitting
    temp_dilution = np.log(dilution)
    dup_dilution = np.hstack((temp_dilution,temp_dilution))
    
    #calculate response(pixel intensity) for these parameters
    return ( np.array (x[0] + (x[1] - x[0])/( (1 + abs((dup_dilution/x[3])**x[2]) )**x[4] ) ) ) 
        
def predict_values(working_data,method, initial_guess):
    """predict_values is a function that fits a curve to data, minimizing the error
    function specified.
    Inputs:
    working_data, one column of serial dilutions preceding n columns of replicate data
    method, the error function to minimize
    initial_guess, vector of 5 starting parameter values [d, a, b, c, g]
    Output:
    backfit_results_table, a table of predicted/observed ratios for each data point"""
    #First column of any data is dilution scheme
    dilution = np.array(working_data[0]) 
    #Following columns are organized into replicates
    def alternate(i):
        """Pairs columns into corresponding replicates"""
        i = iter(i)
        while True:
            yield(i.next(), i.next())   
            
    columns = range(1,len(working_data))
    col_pairs = list(alternate(columns)) 
    backfit_results_table = []
    for pairs in col_pairs:    
        rep1 = np.array(working_data[pairs[0]])
        rep2 = np.array(working_data[pairs[1]])
        #Optimization
        xopt = scipy.optimize.fmin(func = method, 
                                   x0 = initial_guess,
                                   args = ((rep1,rep2,dilution)),
                                   maxiter=1*10**6, 
                                   maxfun=1*10**6)
        predicted_vals = np.array(f(xopt, dilution))
        backfit = np.hstack((rep1,rep2))/predicted_vals
        backfit_results_table.append(backfit)
    return(backfit_results_table)
    
#Get workable data
wb_template = load_workbook('Data_for_Sarah.xlsx', data_only=True)
data = wb_template[ "Signal" ] 
row_start_stop = [(str(17+20*nums),str(24+20*nums))  for nums in range(0,7)]
wSSE_Results = {}
parameter_results = {}
wMPLE_Results = []

for starts,ends in row_start_stop:
    usable_data = extract_data(data,starts,ends,4,35)
    analyte_results = predict_values(usable_data,wSSE,[18.0, 65000.0, -10.0, 5.0, 0.75])
    wSSE_Results.update({starts:(analyte_results)})



with open("BackfittingResults.txt", 'w') as outfile:
    csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for k,v in wSSE_Results.items():
        csv_writer.writerow([k] + v)