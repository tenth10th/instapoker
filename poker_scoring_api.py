def parse_hand(hand_string):
    """
    Turns hand string into a list of card string(s)
    """
    # Move this into the top of parse_hand (as the first step)
    if not isinstance(hand_string, str):
        raise WhoopsiePoopsie("Not a string.")

    list_of_cards = hand_string.split(" ") # Returns a list of 1 card, if there aren't spaces in hand_string...
    for card in list_of_cards:
        validate(card) #TODO: change to validate_card

    return list_of_cards


def card_parser(card_string):
    """
    Given a string representation of a card, like "2H", determine a value
    (Which we can use to compare, and find a "winner")
    """
    face_card_map = {"J": 11, "Q": 12, "K": 13, "A": 14}
    value = card_string[0:-1]

    face_value = face_card_map.get(value.upper())

    if face_value:
        return face_value

    #raise ValueError("Whoopsie poopsie: Invalid Hand Type (expected String)")
    #raise ValueError("Whoopsie poopsie: Invalid Suit")
    #raise ValueError("Whoopsie poopsie: Invalid Rank")

    print("card_string: <",repr(card_string),">")
    try:
        return int(card_string[:])
    except Exception:
        print(card_string[:])
        raise

def compare_cards(card_string1, card_string2):
    """
    Given two cards such as "3H" and "4C", determine which has greater value.
    Given two poker hands, represented by strings, return an integer result:
        1: Hand 1 Wins
        2: Hand 2 Wins
    """
    card_one = card_parser(card_string1)
    card_two = card_parser(card_string2)
    
    if card_one < card_two:
        return 2
    if card_one > card_two:
        return 1
    return 0

class WhoopsiePoopsie(ValueError):
    pass


def validate(card):
    # Dave's Proposal:

    # Once you have the List of Cards, e.g. ["2H", "4C"], then iterate them,
    # and run both of these checks on each card:
    if card[-1] not in 'CHSD':
        raise WhoopsiePoopsie("Invalid suit.")
    if card[0:-1] not in {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"}:
        raise WhoopsiePoopsie("Invalid rank the card was: " + card)
    # And THEN, if we haven't Exception'ed out, return the card...
    


# idea dictionary with result_array[value,card]
def get_highest_card(hand):
    max_value = 1
    for card in hand:
        print("<",repr(card),">")
        value = card_parser(card)
        max_value = max(max_value, value)
    return max_value


def score_poker_hands(h1, h2):
    """
    Given two poker hands, represented by strings, return an integer result:
        0: Draw (hands have equal value)
        1: Hand 1 Wins
        2: Hand 2 Wins

    Before: "2H"
    After: "3H 1D JC" vs "6S 10H 2A" (first hand wins - highest card Jack)
    """
    card_list_1 = parse_hand(h1)
    card_list_2 = parse_hand(h2)

    # DONE: Are these no longer needed? (now that parse_hand validates?)
    # for card in card_list_1:
    #     validate(card)
        
    # for card in card_list_2:
    #     validate(card)

    result = compare_cards(h1, h2)

    return result
