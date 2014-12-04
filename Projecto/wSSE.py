function err = wSSE(analyte, parameters,reps)
%
% this function will calculate the error associated with fitting
% a 5PL curve to some data
%
% data has two columns:
% data(:,1) is a vector of times
% data(:,2) is a vector of observations
%
%parameters is a vector of 5PL parameters:

d = parameters(1);    %    d, the estimated response at infinite concentration
a = parameters(2);    %    a, the estimated response at zero concentration
b = parameters(3);    %    b, the slope factor
c = parameters(4);    %    c, the mid-range concentration
g = parameters(5);    %    g, asymmetry factor

dilution = log(analyte(:,1))*ones(1,2);   %dilution becomes n x n
dilution = dilution( : );                 %make one column vector from all columns
an1 = analyte(:,reps);                    %every analyte every rep
an1 = an1( : );                           %make one column vector from all columns
pixint = an1;                             %pixel intensity
weights = ((analyte(:,reps(1))-analyte(:,reps(2))).^2)*ones(1,2);
weights = weights( : );
weights=1+0*weights;
constant = 1/sum(weights);


% predicted pixel intensity values for these parameters and dilutions are
pixintpred = d + (a - d)./(((1 + abs(1+abs( (dilution./c).^b) )).^g));
% calculate the error
err=sum( constant.*weights.*(pixintpred-pixint).^2 );
end