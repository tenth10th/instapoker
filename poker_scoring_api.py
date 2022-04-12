from dataclasses import dataclass, field
from functools import total_ordering

DRAW = 0
WIN_HAND_1 = 1
WIN_HAND_2 = 2

@total_ordering
@dataclass
class Card:
    """
    Cards have ranks and suits. 
    This is a validated representation. 
    """
    name: str
    rank: int = field(init=False)
    suit: str = field(init=False)

    def __post_init__(self):
        self.validate_card()
        self.parse_rank()
        self.parse_suit()

    def validate_card(self):
        """
        Validate a card, raising an exception if invalid
        """    
        if self.name[0:-1] not in {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}:
            raise InvalidPlayerHandException(f"Invalid rank: {self.name[0:-1]}")

        if self.name[-1] not in 'CHSD':
            print(self.name[-1])
            raise InvalidPlayerHandException(f"Invalid suit: {self.name[-1]}")

    def parse_rank(self):
        face_card_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
        value = self.name[0:-1]

        face_value = face_card_map.get(value.upper())

        if face_value:
            self.rank = face_value
        else:
            self.rank = int(self.name[0:-1])
    
    def parse_suit(self):
        self.suit = self.name[-1]

    def __lt__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError('Not a card')
        return self.rank < other.rank

    def __eq__(self, other):
        if not isinstance(other, Card):
            raise NotImplementedError('Not a card')
        return self.rank == other.rank
       

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

    sorted_hand_1 = get_sorted_hand(card_list_1)
    sorted_hand_2 = get_sorted_hand(card_list_2)

    return compare_rank_lists (sorted_hand_1, sorted_hand_2)

def parse_hand(hand_string):
    """
    Turns hand string into a list of card string(s)
    UPDATE ME to use the new Cards class!
    """
    # Move this into the top of parse_hand (as the first step)
    if not isinstance(hand_string, str):
        raise InvalidPlayerHandException("Not a string.")

    list_of_cards = hand_string.split(" ") # Returns a list of 1 card, if there aren't spaces in hand_string...
    for card in list_of_cards:
        validate_card(card)

    return list_of_cards


def card_parser(card_string):
    """
    (DEPRECATED - Should be replaced with new Card class)
    Given a string representation of a card, like "2H", determine a value
    (Which we can use to compare, and find a "winner")
    """
    face_card_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    value = card_string[0:-1]

    face_value = face_card_map.get(value.upper())

    if face_value:
        return face_value

    # print("card_string: <",repr(card_string),">")
    try:
        return int(card_string[0:-1])
    except Exception:
        print(card_string[0:-1])
        raise


def compare_cards(card_string1, card_string2):
    """
    (DEPRECATED, NO LONGER IN USE - Card does its own parsing, and is comparable)
    Given two cards such as "3H" and "4C", determine which has greater value.
    Given two poker hands, represented by strings, return an integer result:
        1: Hand 1 Wins
        2: Hand 2 Wins
        0: Draw or Tie
    """
    card_one = card_parser(card_string1)
    card_two = card_parser(card_string2)
    
    if card_one < card_two:
        return WIN_HAND_2
    if card_one > card_two:
        return WIN_HAND_1
    return DRAW


class InvalidPlayerHandException(ValueError):
    pass



def validate_card(card):
    """
    DEPRECATED - This behavior is built into new Card class
    Validate a card, raising an exception if invalid
    """    
    if card[-1] not in 'CHSD':
        raise InvalidPlayerHandException("Invalid suit.")
    if card[0:-1] not in {"2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"}:
        raise InvalidPlayerHandException("Invalid rank the card was: " + card)
    

# idea dictionary with result_array[value,card]
def get_sorted_hand(card_list):
    """
    There is still value in sorting lists of Card instances!
    But we no longer need to parse them in the process if we're starting with Cards
    """
    array = list()
    for card in card_list:
        array.append(card_parser(card))
    array.sort(reverse=True)
    return array


def compare_rank_lists(rank_list_1, rank_list_2):
    """
    Return results for two sorted lists
    (should already work for lists of Card classes, since Cards are comparable?)
    """
    if rank_list_1 > rank_list_2:
        return WIN_HAND_1
    elif rank_list_1 < rank_list_2:
        return WIN_HAND_2
    return DRAW


def has_pair(hand):
    """
    Returns True if hand contains a Pair
    (Currently takes a raw string representation of a hand)
    (Should be refactored to use Lists of Cards, or new Hand class TBD?)
    """
    list_of_cards = parse_hand(hand)
    set_of_ranks = set()
    for card in list_of_cards:
        set_of_ranks.add(card[0])
    print("list_of_cards:", list_of_cards)
    print("set_of_ranks:", set_of_ranks)
    print("list length, set length:", len(list_of_cards), len(set_of_ranks))
    return len(list_of_cards) != len(set_of_ranks)


def compare_pair_hands(hand1, hand2):
    """
    THIS FUNCTION IS NOT FULLY IMPLEMENTED YET
    (See commented-out test at the bottom of test_poker_scoring.py)
    Return 0, 1, or 2, to indicate a winning hand (or a draw) based on pairs
    potentially a "better" version of pair_beats_non_pair
    """
    pair_map1 = dict()
    pair_map2 = dict()
    for card in get_sorted_hand(hand1):
        if card in pair_map1:
            pair_map1[card] += 1
        else:
            pair_map1[card] = 1    
    for card in get_sorted_hand(hand2):
        if card in pair_map2:
            pair_map2[card] += 1
        else:
            pair_map2[card] = 1
    print('map1: ', end='')
    print(pair_map1)
    print('map2: ', end='')
    print(pair_map2)

def pair_beats_non_pair(h1, h2):
    pair1 = has_pair(h1)
    pair2 = has_pair(h2)

    if pair1 and not pair2:
        return 1
    if pair2 and not pair1:
        return 2
    return 0
