intro = input("Enter your introduction. ")
print (intro)
characterCount = 0
wordCount = 1

for i in intro:
  characterCount = characterCount + 1
  if i == " ":
    wordCount = wordCount + 1

print ("Number of words: ", wordCount)
print ("Number of characters: ", characterCount)