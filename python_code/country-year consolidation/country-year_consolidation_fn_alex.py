#max_row is the number of rows in the original datasheet and the array arr that only has 3 cols of the data

#make countries dictionary
ctrs = {}

# loop through arr[][0] column ie. countries in arr
for arrctr in range(max_row):
   #check if current country is already in countries dict
    # if no, add to countries dict as dictionary within
    if arr[arrctr][0] not in ctrs:
        ctrs[arr[arrctr][0]] = {}   #verified method of setting array element contents as dictionary name or key name
        #and add year with case value to the dict of the country
        ctrs[arr[arrctr][0]][arr[arrctr][1]] = arr[arrctr][2]      
    # if yes, check if year is already in the dict of the country
    else:
        # if no, add year key with case value
        if arr[arrctr][1] not in ctrs[arr[arrctr][0]]:
            ctrs[arr[arrctr][0]][arr[arrctr][1]] = arr[arrctr][2]
        # if yes, add case value to exisitng year key value
        else:
            ctrs[arr[arrctr][0]][arr[arrctr][1]] = ctrs[arr[arrctr][0]][arr[arrctr][1]] + arr[arrctr][2]     #verified method of changing dict key value to sum of old and new values



#	if arr[arrctr][0] != ctrs[ce][0][0]:         
 #           x = arr[arrctr][0]
  #          exec("%s = %f" % (x,[][])
   #         ctrs.append(arr[arrctr][0])
            

    #    ctrs[ce][0][0] = 
