def check_palin (str):
#defining a functiion named check parendrome
              for i in range (0, int (len (str)/2)):

                             if str [i] != str [len (str) -i-1]:

                                            return False 

                             return True

str_1 = input ('Enter a string.')

ans = check_palin (str_1)

if (ans):

              print ('Yes, it is a palindrome.')

else:

              print ('No, it is not a palindrome.')
