def fizzBuzz():
    for i in range(1,101):
        if(i%3 == 0):
            print("Fizz")
        if(i%5 == 0):
            print("Buzz")
        if(i%3 != 0 and i%5 != 0):
            print(i)
            
def isPalindrome(word):
    return word == reverse(word)

def reverse(word):
    return word[::-1]

def countVowels(word):
    count = 0
    for i in range(len(word)):
        if(isVowel(word[i])):
            count += 1

    return True

def isVowel(letter):
    vowels = "aeiou"
    for i in range(len(vowels)):
        if(vowels[i] == letter):
            return True

    return False
