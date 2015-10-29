#!/usr/bin/python

# analytics challenge ebola correlation first python program

# Library imports
import xlrd
import numpy as np    # np will be alias for numpy when calling numpy functions



dicky = {}
scary = ['tulips','gim']
dicky[scary[1]] = 5
dicky[scary[0]] = {'cats': 1, 'fibby':'no'}

print dicky

dicky['tulips']['cats'] = dicky['tulips']['cats'] + 5

print dicky
