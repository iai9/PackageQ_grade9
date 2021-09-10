#Format [length, height, thick, start zip, end zip]

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

parcel = [8, 17, 0.3]

def findSize(min, max, item, parType):
    counter = 0
    for i in range(3):
        i = i-1
        if(item[i]>min[i] and item[i]<max[i]):
            counter += 1
    if counter == 3:
        print(parType)

for i in range(5):
    i -= 1
    findSize(fullMin[i], fullMax[i], parcel, typeList[i])
