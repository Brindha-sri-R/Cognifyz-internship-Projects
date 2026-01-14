#<...2nd program...>
       #Temperature conversion


print("----- <<< Temperature Conversion Program >>> -----")

print("Enter unit as C for Celsius or F for Fahrenheit : ")

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9


temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C/F): ").upper()

if unit == 'C':
    converted = celsius_to_fahrenheit(temp)
    print("Temperature in Fahrenheit:", converted)

elif unit == 'F':
    converted = fahrenheit_to_celsius(temp)
    print("Temperature in Celsius:", converted)

else:
    print("Invalid unit! Please enter C or F only.")
