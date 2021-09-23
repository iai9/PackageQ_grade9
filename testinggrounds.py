###### Data #############################################################################

# considering putting data in external file for prettyness. we'll see. 

regularMin = [3.5, 3.5, 0.007]
regularMax = [4.25, 6, 0.016]

largeMin = [4.25, 6, 0.007]
largeMax = [6, 11.5, 0.015]

envoMin = [3.5, 5, 0.016]
envoMax = [6.125, 11.5, 0.25] 

lenvoMin = [6.125, 11, 0.25]
lenvoMax = [24, 18, 0.5]

fullMin = [regularMin, largeMin, envoMin, lenvoMin]
fullMax = [regularMax, largeMax, envoMax, lenvoMax]

typeList = ['regular', 'large', 'envelope', 'large envelope', "package", "large package", 'unmailable'] # list all package types

zipzones = {
    1:[1, 6999],        # List of zipcodes and their zone. couldve make the key go frm 0th element for iteration. decided not 
    2:[7000, 19999],    # to as its just easier and makes more sense for them to keep OG values. 
    3:[20000, 35999],   # theyre ints, not strings. the sitpulation in the question was that only inputs needed to be strings
    4:[36000, 62999],   # so i kep the zipcode vals as ints to make it easier
    5:[63000, 84999],   #
    6:[85000, 99999]    #
            }           # 

prices = {
    "regular": [20, 3],           # prices. ints in the hundreds, so cents. easier to do this and divide by 100 at the end
    "large": [37, 3],               # than deal with floats. each key is the same as type list so its all accesible. 
    "envelope": [37, 4],            # added the package prices last minute. 
    "large envelope": [295, 5],     # 
    "package": [295, 25],           #
    "large package": [395, 35]      #
        }

#########################################################################################


def findSize(listmin, listmax, item, parType): # finds the type a letter is

    if item[0] > 24 and item[1] > 18 and item[2] > 0.05:
        item.sort()
        item.reverse()
        twine = 2*item[0] + 2*item[1]
        if twine >= 84:
            return "package"
        elif 84 < twine <=134:
            return "large package"
        else:
            return "unmailable"
            
    # the above is last minute stuff before i go to bed. i hate it. just a placeholder. could probbaly be done better
    # if u can crack it, go ahead harry. however, a more pressing concern below:

    else:
        for j in range(0,4):
            counter = 0
            for i in range(0,3):
                if listmin[j][i] < item[i] <= listmax[j][i]:
                    counter += 1
            if counter == 3:
                return parType[j]
            elif counter < 3 and j == 3:
                return parType[6] # Returns a sting with unmailabe if nothing is matched, I wrote this really quickly and have not tested
