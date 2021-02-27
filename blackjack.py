import random
dealer = list()
player = list()
all_carts = list()
def ace_value(c):
    if c[0] in ["AceofClubs", "AceofDiamonds", "AceofHearts", "AceofSpades"]:
        ask_ace = int(input("Ace value? 1/11 "))
        if ask_ace == 1:
            value_cart = c[1]
            cart_value.append(value_cart)
        elif ask_ace == 11:
            value_cart = c[2]
            cart_value.append(value_cart)
    else:
        value_cart = c[1]
        cart_value.append(value_cart)
cart_values = [("2ofClubs", 2), ("3ofClubs", 3), ("4ofClubs", 4), ("5ofClubs", 5), ("6ofClubs", 6), ("7ofClubs", 7), ("8ofClubs", 8),
("9ofClubs", 9), ("10ofClubs", 10), ("2ofDiamonds", 2), ("3ofDiamonds", 3), ("4ofDiamonds", 4), ("5ofDiamonds", 5), ("6ofDiamonds", 6),
("7ofDiamonds", 7), ("8ofDiamonds", 8), ("9ofDiamonds", 9), ("10ofDiamonds", 10), ("2ofHearts", 2), ("3ofHearts", 3), ("4ofHearts", 4),
("5ofHearts", 5), ("6ofHearts", 6), ("7ofHearts", 7), ("8ofHearts", 8), ("9ofHearts", 9), ("10ofHearts", 10), ("2ofSpades", 2),
("3ofSpades", 3), ("4ofSpades", 4), ("5ofSpades", 5), ("6ofSpades", 6), ("7ofSpades", 7), ("8ofSpades", 8), ("9ofSpades", 9),
("10ofSpades", 10), ("JackofClubs", 10), ("JackofDiamonds", 10), ("JackofHearts", 10), ("JackofSpades", 10), ("KingofClubs", 10),
("KingofDiamonds", 10), ("KingofHearts", 10), ("KingofSpades", 10), ("QueenofClubs", 10), ("QueenofDiamonds", 10), ("QueenofHearts", 10),
("QueenofSpades", 10), ("AceofClubs", 1, 11), ("AceofDiamonds", 1, 11), ("AceofHearts", 1, 11), ("AceofSpades", 1, 11)]
for i in range(4):
    cart = random.choice(cart_values)
    all_carts.append(cart)
carts = list()
cart_value = list()
for cart in all_carts:
    carts.append(cart[0])
dealer.append(carts[0])
dealer.append(carts[1])
player.append(carts[2])
player.append(carts[3])
bet = int(input("How much do you bet? "))
print("Dealer's hand:")
print("Hidden cart")
print(dealer[1])
print("Player's hand:")
print(player[0])
print(player[1])
for cart in all_carts:
    #player_carts
    if cart[0] in player:
         ace_value(cart)
    #dealer_carts
    elif cart[0] in dealer:
          if cart[0] in ["AceofClubs", "AceofDiamonds", "AceofHearts", "AceofSpades"]:
               for m_cart in cart_values:
                   if m_cart[0] == carts[1]:
                       if m_cart[1] <= 10:
                           value_cart = cart[2]
                           cart_value.append(value_cart)
                       else:
                           value_cart = cart[1]
                           cart_value.append(value_cart)
          elif cart[0] in ["AceofClubs", "AceofDiamonds", "AceofHearts", "AceofSpades"]:
               for m_cart in cart_values:
                   if m_cart[0] == carts[0]:
                       if m_cart[1] <= 10:
                          value_cart = cart[2]
                          cart_value.append(value_cart)
                       else:
                          value_cart = cart[1]
                          cart_value.append(value_cart)
          else:
             value_cart = cart[1]
             cart_value.append(value_cart)
dealer_score = cart_value[1]
player_score = cart_value[2]+cart_value[3]
print("Dealer's score:", dealer_score)
print("Player's score:", player_score)
counter = 0
if player_score == 21:
    print("Black jack! You won!")
elif player_score > 21:
    print("You bust!Dealer wins!")
else:
    while counter == 0:
        hit_stand = input("Do you wanna HIT or STAY? HIT/STAY")
        if hit_stand == "HIT":
            new_cart = random.choice(cart_values)
            player.append(new_cart[0])
            ace_value(new_cart)
            print("Player's hand:")
            for cart in player:
                print(cart)
            player_score = sum(cart_value[2:])
            print("Player's score:", player_score)
            if player_score > 21:
                print("You bust!Dealer wins!")
                counter = 1
            elif player_score == 21:
                print("Black jack! You win!")
        elif hit_stand == "STAY":
            print("Player's hand:")
            for cart in player:
                print(cart)
            player_score = sum(cart_value[2:])
            print("Player's score:", player_score)
            dealer_score = cart_value[0]+cart_value[1]
            if dealer_score <= 16:
                while dealer_score <= 16:
                    new_cart = random.choice(cart_values)
                    dealer.append(new_cart[0])
                    dealer_score += new_cart[1]
                print("Dealer's hand:")
                for cart in dealer:
                    print(cart)
                print("Dealer's score:", dealer_score)
                if player_score > dealer_score and player_score <= 21:
                    print("Player wins!")
                    counter = 1
                elif player_score > dealer_score and player_score == 21:
                    print("Black jack! player wins!")
                    counter = 1
                elif player_score <dealer_score and dealer_score <= 21:
                    print("Dealer wins!")
                    counter = 1
                elif player_score <dealer_score and dealer_score == 21:
                    print("Black jack! dealer wins!")
                    counter = 1
                elif player_score == dealer_score and player_score <= 21:
                    print("push!")
                    counter = 1
                elif dealer_score > 21:
                    print("Dealer bust! you win!")
                    counter = 1
            elif dealer_score >= 17:
                print("Dealer's hand:")
                for cart in dealer:
                    print(cart)
                print("Dealer's score:", dealer_score)
                if player_score > dealer_score and player_score < 21:
                    print("Player wins!")
                    counter = 1
                elif player_score > dealer_score and player_score == 21:
                    print("Black jack! player wins!")
                    counter = 1
                elif player_score <dealer_score and dealer_score < 21:
                    print("Dealer wins!")
                    counter = 1
                elif player_score <dealer_score and dealer_score == 21:
                    print("Black jack! dealer wins!")
                    counter = 1
                elif player_score == dealer_score and player_score <= 21:
                    print("push!")
                    counter = 1
                elif dealer_score > 21:
                    print("Dealer bust! you win!")
                    counter = 1


