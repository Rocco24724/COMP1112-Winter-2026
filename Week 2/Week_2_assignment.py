#Rocco Minetola
#200647328
#2025-01-13
#12:53pm
#This code asks the user for a number and checks to see if that number is postive, negative, or zero and then prints the result

print("Please provide any number")
userNumber = input()
if int(userNumber) > 0:
  print(userNumber)
  print("Your number is positive")
elif int(userNumber) < 0:
  print(userNumber)
  print("Your number is negative")
elif int(userNumber) == 0:
  print(userNumber)
  print("Your number is zero")