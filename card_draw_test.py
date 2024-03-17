import random
deck = ["AS","2S","AD","2D","AC","2C","AH","2H",]
hand = []

def draw_card(num):
    for i in range(int(float(num))) :
        hand.append(deck.pop(0))
    print_cards()

def print_cards():
    print()
    print(f"Deck: {deck}")
    print(f"Hand: {hand}")


print(f"Deck: {deck}")
print("Shuffling...")
random.shuffle(deck)
print(f"Shuffled Deck: {deck}")
print()

while len(deck) > 0:
    draw_count = input("How many cards to draw? ")
    if draw_count == "" :
        print("That's not a number of cards.")
    elif int(str(draw_count)) > len(deck) :
        print(f"The deck has less than {draw_count} cards" ) 
    else:
        draw_card(int(float(draw_count)))
else:
    print("The deck is now empty")

