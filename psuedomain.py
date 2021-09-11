
# pseudo main with ugly code. will fix when added to "main.py"

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

typeList = ['regular', 'large', 'envelope', 'large envelope']

zipzones = {1:[1, 6999],
            2:[7000, 19999],
            3:[20000, 35999],
            4:[36000, 62999],
            5:[63000, 84999], 
            6:[85000, 99999]}

prices = {"regular": [20, 3],
        "large": [37, 3], 
        "envelope": [37, 4],
        "large envelope": [295, 5]
        }

#########################################################################################

class Letter:
    
    def __init__(self, measurements, zipcode, lettertype, zipsthrough):
        self.dim_list = measurements
        self.zip_list = zipcode
        self.type = lettertype
        self.zones = zipsthrough


def grabdata():
    flag = True
    letter_data = []
    while flag:

        for i in range (0,3):
            letter_data.append(float(input("Measurement: ")))
            pass
        for i in range (0,2):
            letter_data.append(str(input("Zipcode: ")))
            pass

        print(f"Length: {str(letter_data[0])} units, Height: {str(letter_data[1])} units, Thickness: {str(letter_data[2])} Inches, From: {str(letter_data[3])}, To: {str(letter_data[4])}")
        
        if str(input("Would you like to proceed with the above values? (y/n): ")).lower().strip() == "y":
            flag = False

    return letter_data

def findSize(listmin, listmax, item, parType):
    if item[0] > 24 and item[1] > 18 and item[2] > 0.05:
        twine = 2*item[1] + 2*item[2]
        if twine >= 84:
            return "package"
        elif 84 < twine <=134:
            return "large package"
        else:
            raise ValueError

    else:
        for j in range(0,4):
            counter = 0
            for i in range(0,3):
                if listmin[j][i] < item[i] <= listmax[j][i]:
                    counter += 1
            if counter == 3:
            #print(parType[j])
            return parType[j]

def zonesthrough(testdict, testcodes):
    zones = [0,0] # the two zones we pass through. idc about scalability/adaptivity atm, as the problem has no stipulations
    for j in range (2): # two zipcodes to run through
        for i in range(0,6): # 6 potenial regions to run through
            i += 1 # by def of range func, i is one less than the dict key. "+=" is the quick fix
            if testdict[i][0] <= int(testcodes[j]) <= testdict[i][1]: #simple comparing thezipcode to values for each zone
                zones[j] = i # if zipcode matches with a zone, add zone number to list

    passingthrough = (max(zones) - min(zones)) # finding number of zones passed through. zone numbers themselves irrelevant x-ept for debugging
    return passingthrough # returns number of zones passed to the function




letter = Letter(None, None, None, None)
datagrabbed = grabdata()

letter.dim_list = datagrabbed[0:3]
print(letter.dim_list)

letter.zip_list = datagrabbed[3:5]
print(letter.zip_list)

letter.type = str(findSize(fullMin, fullMax, letter.dim_list, typeList))
print(letter.type)

letter.zones = zonesthrough(zipzones, letter.zip_list)
print(letter.zones)
