import random

# initializing list
test = [1, 4, 5, 6, 3]
 
# Printing original list
print ("The original list is : " + str(test))
 
# using random.shuffle()
# to shuffle a list
random.shuffle(test)
 
# Printing shuffled list
print ("The shuffled list is : " +  str(test))