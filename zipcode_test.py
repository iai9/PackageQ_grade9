## file for testing and validating zipcode functionality. 

## can dict keys be accessed by numbers?

testdict = {1:[1, 6999],
            2:[7000, 19999],
            3:[20000, 35999],
            4:[36000, 62999],
            5:[63000, 84999], 
            6:[85000, 99999]} ### dest dictionary. has the real values though. will likely add to psuedomain

testcodes = ["07245", "89175"] ### String because the problem stipulates that inputed zipcodes must be stings. # appended: tried a bunch, all worked in validation. 

def zonesthrough(testdict, testcodes):
    zones = [0,0] # the two zones we pass through. idc about scalability/adaptivity atm, as the problem has no stipulations
    for j in range (2): # two zipcodes to run through
        for i in range(0,6): # 6 potenial regions to run through
            i += 1 # by def of range func, i is one less than the dict key. "+=" is the quick fix
            if testdict[i][0] <= int(testcodes[j]) <= testdict[i][1]: #simple comparing thezipcode to values for each zone
                zones[j] = i # if zipcode matches with a zone, add zone number to list

    passingthrough = (max(zones) - min(zones)) # finding number of zones passed through. zone numbers themselves irrelevant x-ept for debugging
    return passingthrough # returns number of zones passed to the function

print(zonesthrough(testdict, testcodes)) # print only for debugging :D

#### 