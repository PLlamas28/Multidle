import os
def compareWordsNWrite(answer,guess,fileName):
  subCounter = 0
  rightCounter = 0
  answerListForm = []
  dictOfLetterColors = {
      0:"\033[37m",
      1:"\033[37m",
      2:"\033[37m",
      3:"\033[37m",
      4:"\033[37m"
    }
  for x in answer:
    answerListForm.append(x)
  for guessLetter in guess:
    if guessLetter == answerListForm[subCounter]:
      dictOfLetterColors[subCounter] = "\033[32m"
      rightCounter += 1
      answerListForm[subCounter] = " "
    subCounter += 1

  subCounter = 0

  for guessLetter in guess: 
    if (guessLetter in answerListForm) and (guessLetter != answerListForm[subCounter]):
      if dictOfLetterColors[subCounter] != "\033[32m":
        dictOfLetterColors[subCounter] = "\u001b[33;1m" #"\033[33m"
      answerListForm[answerListForm.index(guessLetter)] = " "
    else:
      if dictOfLetterColors[subCounter] != "\033[32m":
        dictOfLetterColors[subCounter] = "\033[37m"
    subCounter += 1

  
  openFile = open(fileName,"a")
  openFile.write(f"{dictOfLetterColors[0]}{guess[0]}{dictOfLetterColors[1]}{guess[1]}{dictOfLetterColors[2]}{guess[2]}{dictOfLetterColors[3]}{guess[3]}{dictOfLetterColors[4]}{guess[4]}\n")
    
  openFile.close()
  return rightCounter


def clearFile(fileName):
  if os.path.exists(fileName) == True:
    os.remove(fileName)
  openFile = open(fileName,"x")
  openFile.close()

def printWords(fileName):
  openFile = open(fileName,"r")
  for line in openFile:
    print(line.strip("\n"))
  openFile.close()
  print("\n\n\n")
