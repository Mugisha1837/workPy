from collections import Counter

list1=[]
w = int(input("enter number of elements: "))
if w > 0:
    print("Enter elements: ")
    for n in range(w):
        elements = input(" ")
        list1.append(elements)
    
counted_elements = Counter(list1)
print(counted_elements)