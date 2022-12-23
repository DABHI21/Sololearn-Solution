"""
You are making a program to analyse text .
Take the text as the first input and a letter as the second input and output the frequency of that letter in the text as a whole percentage .
The letter L appeares 2 times in the text Hello . which has 5 letter so the frequency would be 40.

"""

text =input()
letter =input()

c=text.count(letter)
k=len(text)
frequency = int((c/k)*100)
print(frequency)