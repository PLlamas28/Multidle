import FuncFile, os, MultiAnsFile

def checkIsNum():
  while True:
    inputN = input("How many words would you like to guess?\nThis number must be between 1 and 64, inclusive.\n\t")
    if inputN.isdigit() == True:
      if int(inputN) > 64 or int(inputN) < 1:
        print("That number is not from 1-64!")
      else:
        break
    else:
      print("That is not a number")
  return int(inputN)
    

def revampedMultidle():
  amountOfWords = checkIsNum()
  wordList = []
  
  dictOfWordsNFiles = {}
  
  for x in range(amountOfWords):
    newWord = FuncFile.generateWord()
    wordList.append(newWord)
    dictOfWordsNFiles[newWord] = x
    MultiAnsFile.clearFile(f"Guesses{x}.txt")
    
  ogWordList = wordList.copy()
  attempts = 0
  
  while attempts < amountOfWords+5:
    guessWord = FuncFile.useableWord(attempts)
    
    removeList = []
    os.system("clear")
    
    for word in wordList: #compare the guess to each answer
      #print(f"\033[35m{word}")
      if MultiAnsFile.compareWordsNWrite(word, guessWord,f"Guesses{dictOfWordsNFiles[word]}.txt") == 5:
        removeList.append(word)
        
    for x in removeList:
      wordList.remove(x)
        
    for z in range(amountOfWords):
      MultiAnsFile.printWords(f"Guesses{z}.txt")
      
    if len(wordList) == 0:
      print("\033[37mYou have guessed all the words!")
      break 
    attempts += 1

  #sdfgasdf
  for w in range(len(ogWordList)):
    print(f"\033[37mAnswer {w+1}: {ogWordList[w]}")
    os.remove(f"Guesses{dictOfWordsNFiles[ogWordList[w]]}.txt")
