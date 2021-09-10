#Format [length, height, thick, start zip, end zip]

regularMin = [3.5, 3.5, 0.007]
regularMax = [4.25, 6, 0.016]

largeMin = [4.25, 6, 0.007]
largeMax = [6, 11.5, 0.015]

envoMin = [3.5, 5, 0.016]
envoMax = [6.125, 11.5, 0.25] 

lenvoMin = [6.125, 11, 0.25]
lenvoMax = [24, 18, 0.5]

parcel = [3.7, 3.7, 0.008]

def findSize(min, max, item):
    for i in range(3):
        i = i-1
        if(item[i]>min[i] and item[i]<max[i]):
            print("1")

findSize(regularMin, regularMax, parcel)
