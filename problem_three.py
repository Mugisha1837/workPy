a = 2000
b = 3200

nl=[]

for i in range(a,b):
      #it like i=a and i <=b 
    if i % 7 ==0 and not i % 5 == 0:
               
        nl.append(str(i))
print(",".join(nl))
