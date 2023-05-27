import random

print("Hi! You are in the game of random coins. ")
option = input("What do you choose? Heads or Tails. ")

result = random.randint(1, 2)
if option == 'Heads' and result == 1:
    print("Good! you got heads :D")
elif option == 'Tails' and result == 2:
    print("Good, you got tails :D")        
else:
    print("Oh, you got the opposite result D:")
