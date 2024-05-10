# Poker Spades
# cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
# These correspond to the cards 2 of Spades, 3 of Spades, and so on through Jack, Queen, King, and Ace of Spaced.
# S2 has numerical value 2. S3 has numerical value 3, and so on. SJ has numerical value 11, SQ has value 12, SK has value 13, and SA has value 14.
Cards = {'S2': 2, 'S3':  3, 'S4': 4, 'S5': 5, 'S6': 6, 'S7': 7, 'S8': 8,'S9': 9, 'S10': 10, 'SJ': 11,'SQ': 12, 'SK': 13, 'SA': 14}


# If the cards passed in are three cards in a sequence, this function returns the greatest value.
# Otherwise it returns 0. For example, check_straight('S5','S6','S7') would return 7. check_straight('S6', 'S5', 'S7') 
# would also return 7.  check_straight('S3','SQ','SK') would return 0. Come up with several tests.
def check_straight(card1, card2, card3):
    arr = sorted([Cards[card1], Cards[card2], Cards[card3]])
    if arr[0] == arr[1]-1 == arr[2]-2:
        return arr[2]
    return 0


# If the three cards passed in are all the same, return the value. Otherwise return 0. 
# For example, check_3ofa_kind('S9', 'S9', 'S9') would return 9. check_3ofa_kind('S2', 'S4', 'S2') would return 0.
def check_3ofa_kind(card1, card2, card3):
    if Cards[card1] == Cards[card2] == Cards[card3]:
        return Cards[card1]
    return 0


# (The code in this function will make use of the check_straight function from earlier, 
# and will assume it’s been tested already and is functioning correctly.) If the cards passed 
# in are a straight with the value of 14, then this function returns 14. Otherwise it returns 0. For this one, you only need maybe three tests.
def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    return 0


# This method takes three cards for the left player (left1, left2, left3) 
# and three cards for the right player (right1, right2, right3) and determines who wins.
# If left wins, it returns -1.
# If neither win (a draw), it returns 0.
# If right wins, it returns 1.
def play_cards(left1, left2, left3, right1, right2, right3):
    royal_left = check_royal_flush(left1, left2, left3)
    royal_right = check_royal_flush(right1, right2, right3)

    # check for royal flush
    if royal_left > 0 or royal_right > 0:
        if royal_left == royal_right:
            return 0
        elif royal_right > royal_left:
            return 1
        elif royal_left > royal_right:
            return -1
        
    # check for straight
    else:
        straight_left = check_straight(left1, left2, left3)
        straight_right = check_straight(right1, right2, right3)

        if straight_left > 0 or straight_right > 0:
            if straight_left == straight_right:
                return 0
            elif straight_right > straight_left:
                return 1
            elif straight_left > straight_right:
                return -1
        
        # check for 3 of a kind
        else:
            kind_left = check_3ofa_kind(left1, left2, left3)
            kind_right = check_3ofa_kind(right1, right2, right3)

            if kind_left > 0 or kind_right > 0:
                if kind_left == kind_right:
                    return 0
                elif kind_right > kind_left:
                    return 1
                elif kind_left > kind_right:
                    return -1
            
            # all other cases a draw
            else:
                return 0




