function err = FPLerror(analyte, parameters, column)
%
% this function will calculate the error associated with fitting
% a 5PL curve to some data
%
% data has two(ish) columns:
% data(:,1) is a vector of serial dilution concentrations
% data(:,column) is a vector of pixel intensity observations
%
%parameters is a vector of 5PL parameters:

d = parameters(1);    %    d, the estimated response at infinite concentration
a = parameters(2);    %    a, the estimated response at zero concentration
b = parameters(3);    %    b, the slope factor
c = parameters(4);    %    c, the mid-range concentration
g = parameters(5);    %    g, asymmetry factor

% %fitting one analyte
% dilution = log(analyte(:,1));               %run dilutions on a log scale
% an1 = analyte(:,column);                    %selected column of data
% pixint = an1;                               %name pixel intensity

%fitting more than one analyte simultaneously
dilution = log(analyte(:,1))*ones(1,2);   %dilution becomes n x n
dilution = dilution( : );                  %make one column vector from all columns
an1 = analyte(:,column:(column+1));                    %every analyte every rep
an1 = an1( : );                            %make one column vector from all columns
pixint = an1;                              %name pixel intensity

% predicted pixel intensity values for these parameters and dilutions are
pixintpred = d + (a - d)./(((1 + abs(abs(1+(dilution./c).^b))).^g));

% calculate the error
err=sum((pixintpred-pixint).^2 );
end