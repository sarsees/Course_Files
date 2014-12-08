close all
clear all
clc

Analytes
for w = 2
analyte =eval(['analyte' num2str(w)]);
%% SSE Cloud and Nominal Case
%set a vector to hold SSE based parameters
columns = 20:25;
sse_parms = zeros(length(columns),5);

%iterate through every column of observed pixel intensities
%[17 61964 -10 35000 2]
for i = 1:(length(columns)-1)
    [sse_parms(i,:),fval,flag] = fminsearch(@(x) wSSE(analyte,x,columns(i):columns(i+1)),[17 61964 -10 35000 1],optimset('MaxIter', 1*10^6,'MaxFunEvals', 1*10^6)) ;
end
%Take means/ Nominal SSE Fit
dstar=mean(sse_parms(:,1));
astar=mean(sse_parms(:,2));
bstar=mean(sse_parms(:,3));
cstar=mean(sse_parms(:,4));
gstar=mean(sse_parms(:,5));

%%% Loop Through Reps
    for r = 11
        reps = r:r+1;
    %Nominal SSE Fit
        [SSEparms,sfval, sflag] = fminsearch(@(x) wSSE(analyte,x,reps),...
                                            [dstar astar bstar cstar gstar],...
                                            optimset('MaxIter', 1*10^5,'MaxFunEvals', 1*10^5)) ;
    %plot predicted curve using Bayes_FPLerror_tworepsplot
    % figure(7)
    SSEPredicted = Bayes_FPLerror_tworepsplot(analyte,SSEparms);
    % plot(log(analyte(:,1)),SSEPredicted,'b','LineWidth',1.2)
    % title('Nominal SSE Fit')
    % %plot actual data
    % hold on
    % plot(log(analyte(:,1)),analyte(:,reps),'r*')
    % hold off
    %Nominal BSE Fit
     [BSEparms, fval, flag] = fminsearch(@(x) wMPLE(analyte,x,reps),...
                                        [dstar astar bstar cstar gstar 2000 std(sse_parms(:,1)) std(sse_parms(:,2))...
                                        std(sse_parms(:,4)) std(sse_parms(:,3)) std(sse_parms(:,5)) mean(sse_parms(:,1))...
                                        mean(sse_parms(:,2)) mean(sse_parms(:,3)) mean(sse_parms(:,4)) mean(sse_parms(:,5))],...
                                        optimset('MaxIter', 1*10^5,'MaxFunEvals', 1*10^5)) ;

    %plot predicted curve using Bayes_FPLerror_tworepsplot
    figure(8)
    BSEPredicted = Bayes_FPLerror_tworepsplot(analyte,BSEparms);
    plot(log(analyte(:,1)),BSEPredicted,'b','LineWidth',1.2)
    title('Nominal MPLE Fit')
    %plot actual data
    hold on
    plot(log(analyte(:,1)),analyte(:,reps),'r*')
    hold off
    analyte(:,reps(1))./BSEPredicted
    analyte(:,reps(2))./BSEPredicted
    end
end
%% Detect and Remove Outliers
%Detect
[R1, R2, WhichOne] = detect_outliers(reps,20:25,10000,analyte, 0.005);
%Remove
[NewAnalyte, NewDilution] = remove_outliers(analyte(:,reps),analyte(:,1),WhichOne);
%Identify new parameters
[bseparms, fval, flag] = fminsearch(@(x) wMPLE_sub(analyte,x,NewAnalyte(:,1),NewDilution(:,1),reps,WhichOne),...
                                   [dstar astar bstar cstar gstar 1050 std(sse_parms(:,1)) std(sse_parms(:,2))...
                                   std(sse_parms(:,4)) std(sse_parms(:,3)) std(sse_parms(:,5)) mean(sse_parms(:,1))...
                                   mean(sse_parms(:,2)) mean(sse_parms(:,3)) mean(sse_parms(:,4)) mean(sse_parms(:,5))],...
                                   optimset('MaxIter', 1*10^6,'MaxFunEvals', 1*10^6)) ;
%Evaluate new parameters    
NewBayesFit = Bayes_FPLerror_tworepsplot(analyte,bseparms);

figure()
box on
hold on
title('Removed MPLE Fit')
plot(log(analyte(:,1)),analyte(:,reps),'b*');
plot(NewDilution(:,1),NewAnalyte(:,1),'k*');
plot(log(analyte(:,1)),NewBayesFit,'b','LineWidth',1.2);
legend( 'Removed Outliers','Location','Best')
hold off