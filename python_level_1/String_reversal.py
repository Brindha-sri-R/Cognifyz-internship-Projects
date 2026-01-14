#<...1st program...>

#Method 1 :

       #<...SLICING...>

print("-----<<< String Reversal Program >>>-----")

def reverse_string(text):
    return text[::-1]

user_input = input("Enter a string to reverse: ")
reversed_output = reverse_string(user_input)

print("Original String :", user_input)
print("Reversed String :", reversed_output)

#Method 2 :

        #<...USING LOOP(without slicing)...>


def reverse_string(text):
    reversed_str = ""
    for i in range(len(text) - 1, -1, -1):
        reversed_str += text[i]
    return reversed_str

print(reverse_string("s'ahdnirB"))


#Method 3 :

        #<...USINF REVERSED FN...>

def reverse_string(text):
    return "".join(reversed(text))

print(reverse_string("zyfingoC"))


#Method 4 :

        #<...RECURSION METHOD...>

def reverse_string(text):
    if text == "":
        return text
    return reverse_string(text[1:]) + text[0]

print(reverse_string("tcejorp tsriF"))


#Method 5 :

         #<...WHILE LOOP...>

def reverse_string(text):
    i = len(text) - 1
    reversed_str = ""
    while i >= 0:
        reversed_str += text[i]
        i -= 1
    return reversed_str

print(reverse_string("!!!enod si"))

