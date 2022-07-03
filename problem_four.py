n=int(input("Insert number in a list:"))
print("---------------------")
lst=[]
lst1=[]
for i in range(0,n):
    a = int(input("Enter element: "))
    lst.append(a)
    if a % 3 == 0:
      lst1.append(a)
print("Our list is:",lst)
print(len(lst1),"of its elements are multiples of 3")