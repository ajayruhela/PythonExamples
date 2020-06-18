# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)
p1= []
p2= []
# draw 3 cards for each
i = 0
while i < 6:
    print(i)
    p1.append(''.join([str(deck[i][0]), " of ", deck[i][1]]))
    print(deck.pop(i))
    i= i+1
    p2.append(''.join([str(deck[i][0]), " of ", deck[i][1]]))
    print(deck.pop(i))
    i= i+1
print("Player1 You got:")
print(p1)
print("Player2 You got:")
print(p2)
