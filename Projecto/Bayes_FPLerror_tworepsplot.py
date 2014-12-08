function [ pixintpred] = Bayes_FPLerror_tworepsplot( analyte, parameters )
%Plotter for a 5 PL curve using input parameters
%initialize parameters

d = parameters(1);    %    d, the estimated response at infinite concentration
a = parameters(2);    %    a, the estimated response at zero concentration
b = parameters(3);    %    b, the slope factor
c = parameters(4);    %    c, the mid-range concentration
g = parameters(5);    %    g, asymmetry factor

 
dilution = log(analyte(:,1))*ones(1,1);   %dilution becomes n x n
dilution = dilution( : );                   %make one column vector from all columns
                     
% predicted pixel intensity values for these parameters and dilutions are
pixintpred = d + (a - d)./(((1 + abs(abs(1+(dilution./c).^b))).^g));


end