function [ err ] = wMPLE_sub( analyte, parameters, newanalyte, newdilution, reps, WhichOne )

%calculates the error associated with fitting a logistic curve to some data
%data is input as analyte of interest. This particular version uses two
%columns of data to fit (rep1:rep2)

%initialize parameters


d = parameters(1);    %    d, the estimated response at infinite concentration
a = parameters(2);    %    a, the estimated response at zero concentration
b = parameters(3);    %    b, the slope factor
c = parameters(4);    %    c, the mid-range concentration
g = parameters(5);    %    g, asymmetry factor
sigma = parameters(6);%    sigma for negative log
sigma_d = parameters(7);
sigma_a = parameters(8); 
sigma_c = parameters(9);
sigma_b = parameters(10);
sigma_g = parameters(11);
dstar = parameters(12);
astar = parameters(13);
bstar = parameters(14);
cstar = parameters(15);
gstar = parameters(16);
%Input Data
pixint = newanalyte;                               %pixel intensity
weights = ((analyte(:,reps(1))-analyte(:,reps(2))).^2)*ones(1,2);
weights = weights( : );
weights(WhichOne) = [];
constant = 1/sum(weights);

% predicted pixel intensity values for these parameters and dilutions are
pixintpred = d + (a - d)./(((1 + abs(abs(1+(newdilution./c).^b))).^g));

    %err=err+sum((pred-hobs).^2);    %add to previous error this reps error.
[nobs] = length(analyte);
    err = nobs/2*log(2*pi*sigma^2)...
        +sum(constant.*weights.*(pixintpred-pixint).^2)/(2*sigma^2)...
        + 0.5*log(2*pi*sigma_d^2)+(d-dstar)^2/(2*sigma_d^2)+...
        + 0.5*log(2*pi*sigma_a^2)+(a-astar)^2/(2*sigma_a^2)+...
        + 0.5*log(2*pi*sigma_c^2)+(c-cstar)^2/(2*sigma_c^2)+...
        + 0.5*log(2*pi*sigma_g^2)+(g-gstar)^2/(2*sigma_g^2)+...
        + 0.5*log(2*pi*sigma_b^2)+(b-bstar)^2/(2*sigma_b^2);
        
end