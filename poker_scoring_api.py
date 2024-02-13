def score_poker_hands(hand1, hand2):

    # Validate
    if((not isinstance(hand1,str)) or (not isinstance(hand2,str))):
        raise ValueError("hand is not a string")
    rank1 = getRank(hand1)
    suit1 = getSuit(hand1)
    rank2 = getRank(hand2)
    suit2 = getSuit(hand2)
    if(rank1 is None):
        raise ValueError("hand1 invalid rank")
    if(rank2 is None):
        raise ValueError("hand2 invalid rank")
    if(suit1 is None):
        raise ValueError("hand1 invalid suit")
    if(suit2 is None):
        raise ValueError("hand2 invalid suit")
    
    #idea1: create a dictionary
    #key (string values): 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
    #values             : 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 
    #idea2: to have "rankSuit"  2H as the key (into integer)
    #create a func getRank()

    if(getRank(hand1) > getRank(hand2) ):
        return 1
    else:
        return 2

def getRank(hand):
    str_rank = hand[:-1]
    
    # Dictionary seems like the simplest way to
    # associate strings with int values (and look up
    # those associations easily)
    rank_dict = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10, 
        "J": 11, "Q": 12, "K": 13, "A": 14
    }
    int_rank = rank_dict.get(str_rank)
    return int_rank

def getSuit(hand):
    str_suit = hand[-1]
    
    # Dictionary seems like the simplest way to
    # associate strings with int values (and look up
    # those associations easily)
    valid_suits = { "H", "S", "C", "D" }
    if(str_suit in valid_suits):
        return str_suit
    else:
        return None

    
