import string

def score_poker_hands(hand_1, hand_2):
    # TODO: Figure out how Poker hands are scored?   
    # FIXME: Implement Poker scoring here, I guess
    
    h1_value = parse_hand(hand_1)[0]
    h2_value = parse_hand(hand_2)[0]

    # Highest Card Wins
    if h1_value == h2_value:
        return 0

    if h1_value < h2_value: 
        return 2
    
    return 1

face_cards = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10
}

def parse_hand(hand):
    if not isinstance(hand, str):
        raise ValueError("Invalid Hand string")
    if not hand:
        raise ValueError("Invalid empty Hand")
    cards_str = hand.split(' ')
    card_values = [parse_card(card_str) for card_str in cards_str]
    card_values.sort(reverse=True)
    return card_values

def parse_card(card):
    if len(card) != 2:
        raise ValueError("Invalid card")
    rank_str, suit_str = card
    
    if suit_str not in ['H', 'D', 'C', 'S']:
        raise ValueError("Invalid Suit")
    
    try:
        number_value = int(rank_str)
    except Exception:
        pass
    else:
        if number_value > 9 or number_value < 2:
            raise ValueError("Invalid number card")
        return number_value
    
    face_value = face_cards.get(rank_str)
    if face_value is None:
        raise ValueError("Unknown face card")
    return face_value

def is_pair():
    pass
