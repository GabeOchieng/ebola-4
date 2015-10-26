#import glob       #allows use of unix style wildcard filenames
import xlrd        #allows reading of xls
#import xlwt       #allows writing of xls
#from openpyxl import Workbook

file_loc="/Users/elliottkrome/Downloads/templytics/administrative_coverage.xls" # identify xls file
wb=xlrd.open_workbook(file_loc) # open workbook
                                # ~~~ to see names of sheets in wb use
                                # ~~~ wb.sheet_names()
data=wb.sheet_by_index(1)       # pick a sheet to read in
print data.nrows
print data.ncols
max_row=0 # initialize row range                 ~These steps could be simplified
max_col=0 # initialize col range                 ~but this setup will allow for
max_row=max(max_row,data.nrows) # make row range ~reading multiple sheets at once 
max_col=max(max_col,data.ncols) # make col range ~from: http://stackoverflow.com/questions/18630521/loop-excel-sheets-and-rows-in-python
new_array=[[0 for x in range(max_col)] for x in range(max_row)] # init array
for row in range (max_row):     # loop over rows 
    for col in range (max_col): # loop over cols
        new_array[row][col] = data.cell_value(row,col)  # WHERE THE MAGIC HAPPENS


#________________________________________________________________
        print new_array[row][col]
#        ^   ^   ^   ^   ^   ^
#        |   |   |   |   |   |
# delete, only to verify that the thing is read in

        
