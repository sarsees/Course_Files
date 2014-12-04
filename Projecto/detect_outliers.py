function[R1Outlier, R2Outlier, WhichOne] = detect_outliers(reps, prior_reps,sample_size, analyte, threshold)
%detect_outliers is a function that detects outliers in an analyte dataset
%using a family of fits derived from prior information
%Inputs:
%reps: data columns to detect outliers on formatted as a:b for rep a rep b
%prior_reps: columns of good data to use as priors
%sample_size: number of family of fits, 10000 is a good place to start
%analyte: data
%threshold: a cutoff "alpha" for determining outliers between 0.03 and 0.07
%% SSE Cloud
%set a vector to hold SSE based parameters
%set a vector to hold SSE based parameters
%set a vector to hold SSE based parameters
columns = prior_reps;
sse_parms = zeros(length(columns),5);

%iterate through every column of observed pixel intensities
for i = 1:(length(columns)-1)
    [sse_parms(i,:)] = fminsearch(@(x) wSSE(analyte,x,columns(i):columns(i+1)),[500 65000 -10 5 1],optimset('MaxIter', 1*10^6,'MaxFunEvals', 1*10^6)) ;
end

%Family of fits
d = normrnd(mean(sse_parms(:,1)),std(sse_parms(:,1)),[sample_size,1]);
a = normrnd(mean(sse_parms(:,2)),std(sse_parms(:,2)),[sample_size,1]);
b = normrnd(mean(sse_parms(:,3)),std(sse_parms(:,3)),[sample_size,1]);
c = normrnd(mean(sse_parms(:,4)),std(sse_parms(:,4)),[sample_size,1]);
g = normrnd(mean(sse_parms(:,5)),std(sse_parms(:,5)),[sample_size,1]);
intensities = zeros(length(d),8);
for z=1:length(d)
intensities(z,:) = Bayes_FPLerror_tworepsplot(analyte,[d(z), a(z), b(z), c(z), g(z)]);
end
LVal = zeros(8,1);
UVal = zeros(8,1);
R1Outlier = zeros(8,1);
R2Outlier = zeros(8,1);
for p = 1:8
    [N,x] = hist(intensities(:,p),1000);
    CN = cumsum(N)/sum(N);
    LVR = find(CN >= threshold/2 & CN <= (threshold+threshold/2));
    [aL] = linear_regression(x(LVR),CN(LVR));
    UVR = find(CN >= (1-(threshold+threshold/2)) & CN <= ((1-threshold/2)));
    [aU] = linear_regression(x(UVR),CN(UVR));
    LVal(p) = (threshold-aL(2))/aL(1);
    UVal(p) = ((1-threshold)-aU(2))/aU(1);
    if ((analyte(p,reps(1)) < LVal(p)) || (analyte(p,reps(1)) > UVal(p)))
        R1Outlier(p) = analyte(p,reps(1));
    end
    if ((analyte(p,reps(2)) < LVal(p)) || (analyte(p,reps(2)) > UVal(p)))
        R2Outlier(p) = analyte(p,reps(2));
    end   
end
%Get indices of outliers and store in a vector for output
I1 = find(R1Outlier);
I2 = find(R2Outlier)+8;
WhichOne = [I1; I2];

