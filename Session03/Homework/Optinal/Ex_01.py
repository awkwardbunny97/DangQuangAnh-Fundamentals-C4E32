import random
WORDS = ("meticulous", "champion", "hexagon")
word = random.choice(WORDS)
correct = word

jumble =""
 
while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]

print ("The jumble is:", jumble)
guess = input("Your guess: ")
guess = guess.lower()
lst = range(len(jumble))
hint_str = '_'*len(jumble)
while True:
 
     
 if guess == correct:
      print ("huray")
      input("\n\nPress the enter key to exit.")
      break
      guess = input("Guess or '?' or 'X': ").lower()

 else:
       guess = input(": (").lower()