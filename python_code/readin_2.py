#!/usr/bin/python

# analytics challenge ebola correlation first python program

# Library imports
import xlrd
import numpy as np    # np will be alias for numpy when calling numpy functions
import re


file_loc="/home/ed/bin/StochData/anal_challenge/disease_map_data.xlsx" # identify xls file

wb=xlrd.open_workbook(file_loc) # open workbook
                                # ~~~ to see names of sheets in wb use
                                # ~~~ wb.sheet_names()
data=wb.sheet_by_index(0)       # pick a sheet to read in
print data.nrows
print data.ncols

max_row=0                                #how manr rows in excel file to loop through
max_row=max(max_row,data.nrows)


#how many rows will our matrix be (determined by number of measles occurence)
meas_row=0
o=0
for o in range(max_row):
    if str(data.cell_value(o,0))=="Measles":   
        meas_row=meas_row+1

#make measles matrix
arr=[[0 for x in range(4)] for x in range(meas_row)]
#Col(2) is location                Col(7) is year                Col(8) is number of cases
meas_num=0
a="Measles"
for row in range(max_row):
    if str(data.cell_value(row,0))=="Measles":
        arr[meas_num][0] = data.cell_value(row,2)
        arr[meas_num][1] = data.cell_value(row,7)
        arr[meas_num][2] = data.cell_value(row,8)
        meas_num=meas_num+1

#print out new matrix
for wrow in range(meas_num):
    print arr[wrow][0],"        ", arr[wrow][1],"        ", arr[wrow][2]


#create new empty matrix
arr_measles=[[0 for x in range(4)] for x in range(meas_num)]  

for qrow in range(meas_num):
    #print arr[296][0]	#just for debugging
    if qrow!=14 and qrow!=296 and qrow!=491 and qrow!=537 and qrow!=576 and qrow!=588:		#handles countries whose names doesnt work for unknown reasons
        country = str(arr[qrow][0])
        co = country.split()
        print co[0]
        #print qrow	#just for debugging



#        
#name_list=[0 for x in range(max_row)]
#for name in range (max_row):
#    name_list[name]=arr[name][0]
#name_list.sort()
#for name in range(max_row):
#    print name_list[name]
                   





#these are data points. for us its number of diseases in a city per year over 4 years
#P = [100, 87, 76, 95]
#get standard deviation
#stdP = np.std(P)
#get the mean
#avgP = np.mean(P)
#N = [300, 331, 320, 295]
#stdN = np.std(N)
#avgN = np.mean(N)
#W = [78, 95, 83, 70]
#stdW = np.std(W)
#avgW = np.mean(W)
#L = [275, 240, 220, 290]
#stdL = np.std(L)
#avgL = np.mean(L)

##create 1x4  empty array for z values
##wait, why do we have these variables? they aren't used
#zP=np.zeros((1,4),dtype=int)
#zN=np.zeros((1,4),dtype=int)
#zW=np.zeros((1,4),dtype=int)
#zL=np.zeros((1,4),dtype=int)

##create empty matrix for z values
#z=np.zeros((4,4),dtype=float)

#for m in range(0, 4):
#    z[0][m] = (P[m]-avgP)/stdP

#for m in range(0, 4):
#    z[1][m] = (N[m]-avgN)/stdN

#for m in range(0, 4):
#    z[2][m] = (W[m]-avgW)/stdW

#for m in range(0, 4):
#    z[3][m] = (L[m]-avgL)/stdL

#print z


##to find correlation: example
##this is the correlation coefficient of P to N since the N values looked 
##    up come after the P values

#for i in range(0, 4):
#    corr = ( z[0][i]*Z[1][i+1] + z[0][i+1]*z[1][i+2] + z[0][i+1]*z[1][i+3] ) / 4

