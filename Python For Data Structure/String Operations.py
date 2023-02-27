'''
Problem : Take a string as input and output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string.
'''

str=input()
n=1
for i in str:
   print(i*n)
   n=n+1