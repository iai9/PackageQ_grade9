## file for testing and validating zipcode functionality. 

## can dict keys be accessed by numbers?

testdict = {1:[1, 6999],
            2:[7000, 19999],
            3:[20000, 35999],
            4:[36000, 62999],
            5:[63000, 84999], 
            6:[85000, 99999]}

testcodes = ["07245", "89175"] ### String because the problem stipulates that inputed zipcodes must be stings

def zonesthrough(testdict, testcodes):
    zones = [0,0]
    for j in range (2):
        for i in range(0,6):
            i += 1
            if testdict[i][0] <= int(testcodes[j]) <= testdict[i][1]:
                zones[j] = i

    passingthrough = (max(zones) - min(zones))
    return passingthrough

print(zonesthrough(testdict, testcodes))

