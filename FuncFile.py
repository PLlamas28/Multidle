import random
def generateWord():

  BWL = open("BonWordList.txt","r")
  wordCounter = 0

  for line in BWL:
    wordList = line.split(",")
    for word in wordList:
      wordCounter += 1
    answer = wordList[random.randrange(0,len(wordList))].strip("\"")
  #print(f"Word counter: {wordCounter}")
  #print(f"Answer: {answer}")
  BWL.close()
  return answer

  #modified on 12/29/2023, changed file var from FWL to BWL


def useableWord(attempts):
  wordExists = False
  while wordExists == False:
    guess = input(f"\033[37mPlease guess the word here (guess {attempts+1}): ")
    if len(guess) != 5:
      print("That is not acceptable! This word is not 5 letters long!")
    else:
      
      FWL = open("FullWordList.txt","r")
  
      for line in FWL:
        wordList = line.split(",")
        for word in wordList:
          word = word.strip("\"")
          if word.lower() == guess.lower():
            wordExists = True
            break
      FWL.close()
  
      if wordExists == False:
        print("That is not a word in this dictionary!")
  return guess
