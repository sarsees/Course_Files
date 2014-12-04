function [ NewAnalyte, NewDilution] = remove_outliers( OldAnalyte,OldDilution, WhichOne)
%knocks is a function that removes data points from a set of data
%   Inputs:
%       OldAnalyte: The unfudged reps of data usually in 8 x 2 format
%       OldDilution: The unfudged first column of data usually in 8 x 1 format
%       WhichOne: Vector of detected outlier from the function
%       detect_outliers

%   Output:
%       NewAnalyte: The new data with removed data point

%Make data a single column
OldAnalyte = OldAnalyte( : );
RepDilution = log(OldDilution)*ones(1,2);   %dilution becomes n x n
OldDilution = RepDilution( : );
%Remove the Selected Rep
%Analyte Point Removal
OldAnalyte(WhichOne) = [];
OldDilution(WhichOne) = [];
NewAnalyte = OldAnalyte;
NewDilution = OldDilution;
    


