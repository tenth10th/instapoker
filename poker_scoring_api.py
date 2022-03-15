def parse_hand(hand_string):
    """
    Turns hand string into a list of card string(s)
    """
    # Move this into the top of parse_hand (as the first step)
    if not isinstance(hand_string, str):
        raise WhoopsiePoopsie("Not a string.")

    list_of_cards = hand_string.split(" ") # Returns a list of 1 card, if there aren't spaces in hand_string...
    for card in list_of_cards:
        validate_card(card)

    return list_of_cards


def card_parser(card_string):
    """
    Given a string representation of a card, like "2H", determine a value
    (Which we can use to compare, and find a "winner")
    """
    face_card_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value = card_string[0:-1]

    face_value = face_card_map.get(value.upper())

    if face_value:
        return face_value

    print("card_string: <",repr(card_string),">")
    try:
        return int(card_string[0:-1])
    except Exception:
        print(card_string[0:-1])
        raise

def compare_cards(card_string1, card_string2):
    """
    Given two cards such as "3H" and "4C", determine which has greater value.
    Given two poker hands, represented by strings, return an integer result:
        1: Hand 1 Wins
        2: Hand 2 Wins
        0: Draw or Tie
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


def validate_card(card):
    """
    (This is a docstring, a multi-line comment that can be queried)
    Validate a card, raising an exception if invalid
    """    
    if card[-1] not in 'CHSD':
        raise WhoopsiePoopsie("Invalid suit.")
    if card[0:-1] not in {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}:
        raise WhoopsiePoopsie("Invalid rank the card was: " + card)
    


# idea dictionary with result_array[value,card]
def get_highest_card(card_list):
    max_value = 1
    highest_card = None
    for card in card_list:
        print("<",repr(card),">")
        rank_value = card_parser(card)
        if rank_value > max_value:
            max_value = rank_value
            highest_card = card
    return highest_card


def score_poker_hands(h1, h2):
    """
    Given two poker hands, represented by strings, return an integer result:
        0: Draw (hands have equal value)
        1: Hand 1 Wins
        2: Hand 2 Wins

    Before: "2H"
    After: "3H 1D JC" vs "6S TH 2A" (first hand wins - highest card Jack)
    """
    pair_results = pair_beats_non_pair(h1, h2)
    
    if pair_results:
        return pair_results

    card_list_1 = parse_hand(h1)
    card_list_2 = parse_hand(h2)

    high_card_1 = get_highest_card(card_list_1)
    high_card_2 = get_highest_card(card_list_2)

    result = compare_cards(high_card_1, high_card_2)

    return result

def has_pair(hand):
    list_of_cards = parse_hand(hand)
    set_of_ranks = set()
    for card in list_of_cards:
        set_of_ranks.add(card[0])
    print("list_of_cards:", list_of_cards)
    print("set_of_ranks:", set_of_ranks)
    print("list length, set length:", len(list_of_cards), len(set_of_ranks))
    return len(list_of_cards) != len(set_of_ranks)

def pair_beats_non_pair(h1, h2):
    pair1 = has_pair(h1)
    pair2 = has_pair(h2)

    if pair1 and not pair2:
        return 1
    if pair2 and not pair1:
        return 2
    return 0
