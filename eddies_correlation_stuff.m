P = [100 87 76 95]; %these are data points. for us its number of diseases in a city per year over 4 years
SP = std(P);        %get standard deviation
AP = mean(P);       %get the mean
N = [300 331 320 295];
SN = std(N);
AN = mean(N);
W = [78 95 83 70];
SW = std(W);
AW = mean(W);
L = [275 240 220 290];
SL = std(L);
AL = mean(L);

ZP = zeros([1,4]);  %create empty array for z values
ZN = zeros([1,4]);
ZW = zeros([1,4]);
ZL = zeros([1,4]);

Z = zeros([4,4]);   %create empty matrix for z values

for m = 1:4
    Z(1,m) = (P(m)-AP)/SP
end

for m = 1:4
    Z(2,m) = (N(m)-AN)/SN
end

for m = 1:4
    Z(3,m) = (W(m)-AW)/SW
end

for m = 1:4
    Z(4,m) = (L(m)-AL)/SL
end

Z

%%
%%to find correlation: example

for i = 1
    corr = (Z(1,i)*Z(2,1+i)+Z(1,i+1)*Z(2,i+2)+Z(1,i+1)*Z(2,i+3))/4
end

%%this is the correlation coefficient of P to N since the N values looked
%%up come after the P values