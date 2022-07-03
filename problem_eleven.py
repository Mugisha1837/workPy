def count(s, c) : 
    # Count variable
    res = 0
    for i in range(len(s)) :
         
        # Checking character in string
        if (s[i] == c):
            res = res + 1
    return res
 
text = str(input("Enter any string: "))
c = str(input("Enter character to find: "))
print("The character you entered comes", count(text, c) , "times")