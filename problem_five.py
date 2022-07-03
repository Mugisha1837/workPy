intlist=[2, 3, 3, 6, 4, 5]
print(intlist)
print("----------")

maximum=max(intlist)
max_index=intlist.index(maximum)
intlist.pop(max_index)
runner_up=max(intlist)

print("The maximum in the list is " +str(maximum)+  " and the runner-up is " +str(runner_up))