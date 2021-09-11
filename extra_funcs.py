
####### Data ############################################################################

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

parcel = [3.7, 3.7, 0.008]

#########################################################################################

class Letter:
    
    def __init__(self, measurements, zipcode):
        self.dim_list = measurements
        self.zip_list = zipcode
        pass

    def itemtype(self, type):
        self.type = type

def grabdata():
    flag = True
    letter_data = [4,5,0.01,"0","0"]
    while flag:

        for i in range (0,3):
            # letter_data.append(float(input("Measurement: ")))
            pass
        for i in range (0,2):
            # letter_data.append(str(input("Zipcode: ")))
            pass

        print(f"Length: {str(letter_data[0])} units, Height: {str(letter_data[1])} units, Thickness: {str(letter_data[2])} Inches, From: {str(letter_data[3])}, To: {str(letter_data[4])}")
        
        if str(input("Would you like to proceed with the above values? (y/n): ")).lower().strip() == "y":
            flag = False

    return letter_data

def findSize(listmin, listmax, item, parType):
  for j in range(0,4):
    counter = 0
    for i in range(0,3):
      if listmin[j][i] < item[i] <= listmax[j][i]:
        counter += 1
    if counter == 3:
      #print(parType[j])
      return parType[j]

def zipcodezones():
    pass

letter = Letter(None, None)
datagrabbed = grabdata()
letter.dim_list = datagrabbed[0:3]
print(letter.dim_list)
letter.zip_list = datagrabbed

letter.itemtype(str(findSize(fullMin, fullMax, parcel, typeList)))
print(letter.type)

