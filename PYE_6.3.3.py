w = input("Provide a word to analyse:")
ltr = input("Provide a letter to count in the word:")

def lettercounter(word, ltr) :
    count = 0
    for letter in word :
        if letter == ltr:
            count = count + 1
    print(count)

lettercounter(w, ltr)
