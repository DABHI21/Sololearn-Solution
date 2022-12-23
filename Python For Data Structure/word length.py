"""
Given a sentence as input, calculate and output the average word length of that sentence .
In the sentence whitespace not included.

"""
text=input()
words=text.split()
text=text.replace(" ","")
letters=len(text)
word=len(words)

print(letters/word)
