from functools import cmp_to_key
def compute(x, z):
     return x - z
def minimuswaps(num):
    Leng = len(num)
    map = {}
    for i in range(Leng):
        map[num[i]] = i
 
    num = sorted(num, key = cmp_to_key(compute))
 

    visited = [False for col in range(Leng)]

    answ = 0
    for i in range(Leng):
 
        if (visited[i] or map[num[i]] == i):
            continue
 
        j,cycle_size = i, 0
        while (visited[j] == False):
            visited[j] = True
            j = map[num[j]]

            cycle_size += 1
 
        if (cycle_size > 0):
            answ += (cycle_size - 1)
 
    return answ

a = [ 0, 5, 4, 3]
print("the minimum swaps are", minimuswaps(a), "times")