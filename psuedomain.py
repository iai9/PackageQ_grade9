
# pseudo main with ugly code. will fix when added to "main.py"

# commented for your convience harrison. if u need to change something go for it, just indicate what u changed. ty


###### Data #############################################################################

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

zipzones = {1:[1, 6999],        # List of zipcodes and their zone. couldve make the key go frm 0th element for iteration. decided not 
            2:[7000, 19999],    # to as its just easier and makes more sense for them to keep OG values. 
            3:[20000, 35999],   # theyre ints, not strings. the sitpulation in the question was that only inputs needed to be strings
            4:[36000, 62999],   # so i kep the zipcode vals as ints to make it easier
            5:[63000, 84999],   #
            6:[85000, 99999]}   # 

prices = {"regular": [20, 3],           # prices. ints in the hundreds, so cents. easier to do this and divide by 100 at the end
        "large": [37, 3],               # than deal with floats. each key is the same as type list so its all accesible. 
        "envelope": [37, 4],            # added the package prices last minute. 
        "large envelope": [295, 5],     # 
        "package": [295, 25],           #
        "large package": [395, 35]      #
        }

#########################################################################################

### Functions/Classes####################################################################

class Letter: # decided to make a class to store all attributes of the letter easier. just easier to use and manage. 
    
    def __init__(self, measurements, zipcode, lettertype, zipsthrough): # all will be initialized with "None" 
        self.dim_list = measurements # measurements of box (len, height, thick). obtained via user input
        self.zip_list = zipcode # the two zipcode measurements as strings in list. taken from user input. 
        self.type = lettertype # what type of package it is. obtained via dim_list and a function we defined later
        self.zones = zipsthrough #how many zones it passes through. obatained via zip_list and a function well define later


def grabdata():
    flag = True ## Question stipulated input should be able to be reinputed should there be error. flag method easiest. 
    letter_data = [] # blanck list for user input data. expect to have 5 elements.

    while flag:

        for i in range (0,3):
            letter_data.append(float(input("Measurement: ")))
        for i in range (0,2):
            letter_data.append(str(input("Zipcode: "))) 
        # originally did the above iterations as one range(5). but, that is not what is stipulated by the question
        # so easiest way to have to data types was just two iterations

        print(f"Length: {str(letter_data[0])} units, Height: {str(letter_data[1])} units, Thickness: {str(letter_data[2])} Inches, From: {str(letter_data[3])}, To: {str(letter_data[4])}")
        # the above is just user friendlyness. displays the values. probably couldve done something really clever with string
        # manipulation to make this pep8. but whatever. 

        if str(input("Would you like to proceed with the above values? (y/n): ")).lower().strip() == "y":
            flag = False
            # if user is ok with values, flag is set to false and the while loop ends. 

    # returns the list of data
    return letter_data

def findSize(listmin, listmax, item, parType): # finds the type a letter is

    if item[0] > 24 and item[1] > 18 and item[2] > 0.05:
        twine = 2*item[1] + 2*item[2]
        if twine <= 84:
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

    # i like the above. 7 lines, and it works really well. good job with that, harry. 
    # 
    # the biggest problem here is that there is very little error handling and there is not a single condition for 
    # unmailable packages. we need to add something for that. will mull over it b4 i sleep... see what u can do harry

def zonesthrough(testdict, testcodes):
    zones = [0,0] # the two zones we pass through. idc about scalability/adaptivity atm, as the problem has no stipulations
    for j in range (2): # two zipcodes to run through
        for i in range(0,6): # 6 potenial regions to run through
            i += 1 # by def of range func, i is one less than the dict key (see above, key starts at 1, i starts at 0). "+=" is the quick fix
            if testdict[i][0] <= int(testcodes[j]) <= testdict[i][1]: #simple comparing thezipcode to values for each zone
                zones[j] = i # if zipcode matches with a zone, add zone number to list

    passingthrough = (max(zones) - min(zones)) # finding number of zones passed through. zone numbers themselves irrelevant except for debugging
    return passingthrough # returns number of zones passed to the function

    # i generally like this. could maybe be improved. will worry abt that when we port everything over to main.py 
    # biggest worry atm is findSize. 



letter = Letter(None, None, None, None) # created object of the above class

datagrabbed = grabdata() # run grabdata to get list of 3 numbers and 2 zip codes as strings

letter.dim_list = datagrabbed[0:3] # assigns dim_list to the first three elements fo grabdata, the dimesnions
print(letter.dim_list)

letter.zip_list = datagrabbed[3:5] # assigns zip_list to the two zipcodes. 
print(letter.zip_list)

letter.type = str(findSize(fullMin, fullMax, letter.dim_list, typeList)) #findsize func computes the type. takes letter.dim_list
print(letter.type)

letter.zones = zonesthrough(zipzones, letter.zip_list)# finds number of zones passed through. takes letter.zip_list
print(letter.zones)

if letter.type != 'unmailable': # Only shows prices if the package can be mailed
    price = (prices[letter.type][0]  + prices[letter.type][1] * int(letter.zones))/100 ### it works
    print(str(price))
else:
    print('This parcel is not mailable.')
##### IN SUMMARY #####

# I like it so far. obviously we need optimization. this could probably be faster, and generally prettier code, but i think its good
# so far
# Biggest problem right now is the lack of "unmailable" on the findSize function as well as a lack of potential error handling
# so we can work on that