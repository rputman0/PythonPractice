def fizzBuzz():
    for i in range(1,101):
        if(i%3 == 0):
            print("Fizz")
        if(i%5 == 0):
            print("Buzz")
        if(i%3 != 0 and i%5 != 0):
            print(i)
            
#FizzBuzz with recursion (decreasing)
def fizzBuzzRecursion(number):
    if(number == 0):
        return 0
    else:
       if(number%3 == 0):
            print("Fizz")
       if(number%5 == 0):
            print("Buzz")
       if(number%3 != 0 and number%5 != 0):
            print(number)

    return fizzBuzzRecursion(number-1)
            
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
