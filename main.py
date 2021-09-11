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
<<<<<<< HEAD

typeList = ['regular', 'large', 'envelope', 'large envelope']

parcel = [3.7, 3.7, 0.008]

=======

typeList = ['regular', 'large', 'envelope', 'large envelope']

parcel = [8, 17, 0.3]

>>>>>>> 00788b3ba4ec97218abf4ae3663a46b3054411fa
def findSize(min, max, item, parType):
    counter = 0
    for i in range(3):
        if(item[i]>min[i] and item[i]<max[i]):
            counter += 1
    if counter == 3:
        print(parType)

<<<<<<< HEAD
for i in range(5):
    i -= 1
=======
for i in range(4):
>>>>>>> 00788b3ba4ec97218abf4ae3663a46b3054411fa
    findSize(fullMin[i], fullMax[i], parcel, typeList[i])
