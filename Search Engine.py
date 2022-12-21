def search(text, word):
   
    for i in text:
        if word in text:
            print("Word found")
            break
        else :
            print("Word not found")
            break
T=input()
w=input()
search(T,w)            