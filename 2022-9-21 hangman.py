#Glass Zimny
#21/9/2022
        
while True:
  w = input("Player 1, enter your word: ").replace("  "," ")
  if w.isalpha():
    break
  print("Entry must be alphabetic")
  
while True:
  c = input("How many chances should player 2 be given? ")
  if c.isnumeric():
    if c != "0":
      c=int(c)
      break
    else:
      print("Cannot have 0 guesses")
  print("Entry must be numeric")
for i in range(35):
  print("")

word = []
lword = len(w)
for i in range(lword):
  word.append(w[0])
  w = w[1:]
print("Player 2: ")
guessed = []
found = []
print("*"*lword)
while c != 0:
  while True:
    print("You have "+str(c)+" wrong guesses remaining")
    g = input("Enter a letter: ").replace(" ","")
    if not g in guessed:
      if len(g) == 1:
        if g.isalpha():
          guessed.append(g)
          break
        else:
          print("Your guess must be in the alphabet")
      else:
        print("You can only guess a single character")
    else:
      print("You have already guessed this letter")
  if not g in word:
    c -= 1
  for i in range(lword):
    if word[i] == g:
      found.append(i)
    if i in found:
      print(word[i],end="")
    else:
      print("*",end="")
  print("")
  if len(found) == lword:
    print("Player 2 wins")
    break
if c == 0:
  print("Player 1 wins, the word was \""+"".join(word)+"\"")
  
