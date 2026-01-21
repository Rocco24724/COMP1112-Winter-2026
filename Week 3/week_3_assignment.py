# Rocco Minetola
# 200647328
# 2025-01-20
# 12:49pm

# This code asks the user for 3 strings. If the string length is 5 or above it prints that string.
# If the length is odd, it adds the length to a combined string and prints it at the end.

print("Please provide your stringOneName:")
string1 = input()

print("Please provide your stringTwoName:")
string2 = input()

print("Please provide your stringThreeName:")
string3 = input()

# Checks for odd lengths and returns the length string if it is odd
def oddNumbersOne(first_string, second_string, third_string):
    oddString = ""

    if len(first_string) % 2 == 1:
        oddString += str(len(first_string))

    if len(second_string) % 2 == 1:
        oddString += str(len(second_string))

    if len(third_string) % 2 == 1:
        oddString += str(len(third_string))

    if oddString == "":
        return "Null"
    return oddString

# Checks for strings with length of 5 or above
def overFiveCheck(first_string, second_string, third_string):
    if len(first_string) >= 5:
        print(first_string)
    if len(second_string) >= 5:
        print(second_string)
    if len(third_string) >= 5:
        print(third_string)

oddResult = oddNumbersOne(string1, string2, string3)
print(oddResult)

overFiveCheck(string1, string2, string3)