def isAnagram(first,second):
    return assignWordValue(first) == assignWordValue(second)

def assignWordValue(word):
    length = 0
    for i in range(len(word)):
        length += assignLetterValue(word[i])

    return length

def assignLetterValue(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in range(0,26):
        if(letter == alphabet[i]):
            return i+1

    return -1

def main():
    first = input("Enter first word: ")
    second = input("Enter second word: ")

    if(isAnagram(first,second)):
        print("Felicitaciones!",first,"and",second,"are anagrams!")
    else:
        print("Lo Siento!",first,"and",second,"are not anagrams.")

main()
