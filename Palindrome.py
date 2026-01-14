#<...5th program...>

         #Palindrome Checker

print("----<<< Palindrome checker >>>----")


text = input("Enter a word: ")

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

if is_palindrome(text):
    print("It is a Palindrome")
else:
    print("It is Not a Palindrome")
