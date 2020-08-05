# python script
import random as rnd

# number of items in list, change this to as huge a list as you want
itemsInList = 5

# specify min and max value bounds for randomly generated values
# change these to play around with different value ranges
minVal = 8
maxVal = 20

# creates a list of random values between minVal and maxVal, and sort them
numList = sorted( [rnd.randint(minVal, maxVal) for x in range(itemsInList)] )
print ('initial list is\n{}\n'.format(numList))

# calculate the normalizer, using: (1 / (sum_of_all_items_in_list))
normalizer = 1 / float( sum(numList) )

# multiply each item by the normalizer
numListNormalized = [x * normalizer for x in numList]
print('Normalized list is\n{}\n'.format(numListNormalized))

print('Sum of all items in numListNormalized is {}'.format(sum(numListNormalized)))