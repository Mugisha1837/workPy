num = int(input("Enter N numbers:"))
#num is N number entred by user
list=[]

for n in range(num):  
    number = int(input("Number:"))
    #for loop to enter N number  
    list.append(number)
    #append entered number in the list
    
print("Maximun is:", max(list))
print("Minimum is:", min(list))
