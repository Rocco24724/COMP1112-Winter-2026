# Rocco Minetola
# 200647328
# 2025-01-27
# 12:43pm
#This code asks the user for a string and checks if there is a duplicate word 

#Function for checking for duplicate words
def duplicateCheck(string):
  words = string.split()

  #For loop to check if the same word appears in a string with spaces
  for i in range(len(words) - 1):
    if words[i].lower() == words[i+1].lower():
      #print(f) lets me insert variable into string to show which word was the issue
      print(f"Duplicated word found: '{words[i]}'")
      return
    
  #For loop to check if a word is doubled in a string (ex.testtest)
  for word in words:
    #Checks to see if a word is even to use to check to see if it is a duplicate (ex.testtest)
    half = len(word) // 2
    if len(word) % 2 == 0:
      #Splits the word in 2 puts them into 2 variables first_word and second_word and then checks if they are the same
      first_word = word[:half].lower()
      second_word = word[half:].lower()
      if first_word == second_word:
        #print(f) lets me insert variable into string to show which word was the issue
        print(f"Duplicated word found (no space): '{first_word}'")
        return
  
  #Prints to the user their are no duplicated words if there is none
  print("No duplicated words found.")

print("Please provide a string")
userString = input()
duplicateCheck(userString)