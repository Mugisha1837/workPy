def intersection(lst1, lst2):
    
    # this will check values that are in list 1 but not in the list 2
    
    lst3 = [value for value in lst1 if not value in lst2]
    return lst3
num = int(input("Enter N numbers:"))
for n in range(num): 

    lst1 = []

    number = int(input("Enter list 1: "))     
    lst1.append(number)
print("---------------------------")
for i in range(num):
    lst2 = []
     
    number2 = int(input("Enter list 2: ")) 
    lst2.append(number2)  
print("Number belongs in list 1 not in list 2 is/are: ", intersection(lst1, lst2))