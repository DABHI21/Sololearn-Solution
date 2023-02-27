"""
Problem : You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.

"""

str = input()
count =0
for L in str :

  if L=='a'or L=='e'or L=='i'or L=='o'or L=='u' :
     count = count+1
print (count )
