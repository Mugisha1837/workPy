def intersection(lst, lis):
    lst3 = [value for value in lst if value in lis]
    return lst3

lst = []
lis = []
n = int(input("Enter number of elements FOR fist list: "))
for i in range(0, n):
            element = int(input("Elements for list 1: "))
            lst.append(element) 
print(lst)
p = int(input("Enter number of elements for second list: "))
for i in range(0, p):
            element = int(input("Elements for list 2: "))
            lis.append(element) 
print(lis)
print("intersection of two list: ")
print(intersection(lst, lis))