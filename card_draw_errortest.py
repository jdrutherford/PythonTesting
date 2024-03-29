import random
deck = ["AS","2S","AD","2D","AC","2C","AH","2H",]
hand = []
#Keep track of the number of incorrect submissions
error_count = 0

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

while len(deck) > 0 and error_count < 5:
    draw_count = input("How many cards to draw? ")
    try:
        type(draw_count)
        if int(str(draw_count)) > len(deck) :
            print(f"The deck has less than {draw_count} cards" ) 
        else:
            draw_card(int(float(draw_count)))
    except ValueError or TypeError:
        error_count = error_count + 1
        print(f"That's not a number of cards.\n{error_count}/5 Allowable Errors")
else:
#end the program if more than 5 incorrect entries    
    if error_count >= 5:
        print("Error: Too many incorrect entries")
    else:
        print("The deck is now empty")