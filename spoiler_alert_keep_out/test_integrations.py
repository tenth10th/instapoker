from random import expovariate
import inspect
import pytest

"""
Integration Tests
"""

try:
    import poker_scoring_api
except ImportError:
    poker_scoring_api = None


###########################
### Basic Sanity Checks ###
###########################


@pytest.mark.integration
def test_poker_scoring_api_module_exists():
    """
    poker_scoring_api.py is present
    """
    assert poker_scoring_api is not None, (
        "poker_scoring_api.py module must be present!"
    )


@pytest.mark.integration
def test_score_poker_hands_exists():
    """
    poker_scoring_api.py contains score_poker_hands
    """
    assert hasattr(poker_scoring_api, "score_poker_hands"), (
        "poker_scoring_api.py must contain a \"score_poker_hands\" function"
    )


try:
    from poker_scoring_api import score_poker_hands
except ImportError:
    score_poker_hands = None


@pytest.mark.integration
def test_score_poker_hands_is_a_function():
    """
    poker_scoring_api.score_poker_hands is a function
    """
    assert inspect.isfunction(poker_scoring_api.score_poker_hands), (
        "poker_scoring_api.score_poker_hands must be a function!"
    )


##################################
### Level 0: Poker Scoring API ###
##################################


@pytest.mark.integration(min_level=0)
def test_poker_scoring_api():
    """
    score_poker_hands accepts two strings
    """
    error = ""
    try:
        score_poker_hands("2D", "2H")
    except TypeError as e:
        error = str(e)
    if error:
        pytest.fail(error)


@pytest.mark.integration(min_level=0)
def test_poker_scoring_api_return_type():
    """
    score_poker_hands returns an integer
    """
    result = score_poker_hands("2D", "2H")
    assert isinstance(result, int), "score_poker_hands output must be an integer!"


def hand_error_str(h1, h2, int_result):
    if int_result == 1:
        result_verb = "win"
    elif int_result == 2:
        result_verb = "lose"
    else:
        result_verb = "draw"

    return f"{h1} should {result_verb} against {h2}!"


def validate_hand_result(h1, h2, expected_result):
    __tracebackhide__ = True
    result = score_poker_hands(h1, h2)
    if result != expected_result:
        pytest.fail(hand_error_str(h1, h2, expected_result))


########################################
### Level 1: Basic Single-Card Hands ###
########################################


@pytest.mark.integration(min_level=1)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3H", "2D", 1),
    ("4C", "5S", 2),
    ("7S", "6H", 1),
    ("8D", "9D", 2),
    ("9S", "2H", 1),
    ("4H", "7C", 2),
])
def test_basic_single_card_hands(h1, h2, expected_result):
    """
    Basic single-card hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


#########################################
### Level 2: (Full) Single-Card Hands ###
#########################################


@pytest.mark.integration(min_level=2)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("8D", "QH", 2),
    ("AD", "KC", 1),
    ("JS", "QH", 2),
    ("KD", "QD", 1),
    ("9S", "JS", 2)
])
def test_full_single_card_hands(h1, h2, expected_result):
    """
    Single-card hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


@pytest.mark.integration(min_level=2, max_level=3)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("10H", "9D", 1),
    ("3S", "10C", 2),
    ("JD", "10C", 1),
])
def test_10_single_card_hands(h1, h2, expected_result):
    """
    Single-card rank 10 hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


#################################
### Level 3: Input Validation ###
#################################


@pytest.mark.integration(min_level=3)
@pytest.mark.parametrize("h1, h2", [
    (None, None),
    ("1S", None),
    (None, "1S"),
])
def test_invalid_None_inputs(h1, h2):
    """
    None inputs raise ValueErrors
    """
    NoneValueMessage = "Failed to raise ValueError, given None inputs!"
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(None, None)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(NoneValueMessage)
    else:
        raise AssertionError(NoneValueMessage)


@pytest.mark.integration(min_level=3)
@pytest.mark.parametrize("h1, h2", [
    ("", ""),
    ("1S", ""),
    ("", "1S"),
])
def test_invalid_empty_inputs(h1, h2):
    """
    Empty string inputs raise ValueErrors
    """
    EmptyValueMessage = "Failed to raise ValueError, given empty string inputs!"
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(None, None)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(EmptyValueMessage)
    else:
        raise AssertionError(EmptyValueMessage)


@pytest.mark.integration(min_level=3)
@pytest.mark.parametrize("h1, h2", [
    (1, 2),
    ("1S", 2),
    (3.0, "2D"),
])
def test_invalid_numeric_inputs(h1, h2):
    """
    Numeric inputs raise ValueErrors
    """
    NumericValueMessage = "Failed to raise ValueError, given numeric inputs!"
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(None, None)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(NumericValueMessage)
    else:
        raise AssertionError(NumericValueMessage)


@pytest.mark.integration(min_level=3)
@pytest.mark.parametrize("h1, h2", [
    ("2S", "3X"),
    ("5Z", "2H"),
])
def test_invalid_suit_inputs(h1, h2):
    """
    Hands containing invalid suits raise ValueErrors
    """
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    assertion_error = f"Failed to raise ValueError, given invalid Suit {h2[-1]}"
    try:
        score_poker_hands(h1, h2)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(assertion_error)
    else:
        raise AssertionError(assertion_error)


@pytest.mark.integration(min_level=3)
@pytest.mark.parametrize("h1, h2", [
    ("7D", "0S"),
    ("1H", "3C"),
    ("4S", "-1H"),
])
def test_invalid_rank_inputs(h1, h2):
    """
    Hands containing invalid ranks raise ValueErrors
    """
    assertion_error = f"Failed to raise ValueError, given invalid Rank {h2[0:-1]}"
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(h1, h2)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(assertion_error)
    else:
        raise AssertionError(assertion_error)


@pytest.mark.integration(min_level=3)
@pytest.mark.parametrize("h1, h2", [
    ("11H", "1C"),
    ("DF", "33U"),
    ("TK421", "|-_-|"),
])
def test_invalid_rank_inputs(h1, h2):
    """
    Hands containing completely invalid cards raise ValueErrors
    """
    assertion_error = f"Failed to raise ValueError, given invalid Cards: \"{h1}\", \"{h2}\""
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(h1, h2)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(assertion_error)
    else:
        raise AssertionError(assertion_error)


#################################
### Level 4: Multi-Card Hands ###
#################################


@pytest.mark.integration(min_level=4)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("4D 3H", "2H 3S", 1),
    ("9H 5C", "JD 5C", 2),
    ("9H 5S", "4D 8H", 1),
    ("5D 8C", "4H 9S", 2),
    ("4C QH KC 9C 6H", "3S 7S AD 5D JC", 2),
    ("JH QD AH KD 2H", "6H JC 8H 4D 5D", 1),
])
def test_multi_card_hands(h1, h2, expected_result):
    """
    Multi-card hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


#######################################
### Level 5: Single-Character Ranks ###
#######################################


@pytest.mark.integration(min_level=5)
def test_high_single_card_hands_T():
    """
    T is interpreted to represent Rank 10
    """
    validate_hand_result("TH", "9S", 1)

@pytest.mark.integration(min_level=5)
@pytest.mark.parametrize("h1, h2", [
    ("10D 3H", "2H 3S"),
    ("3C QH KC 9C 6H", "4S 7S AD 5D 10C"),
])
def test_invalid_obsolete_rank_inputs(h1, h2):
    """
    Rank "10" is no longer valid (in favor of rank "T")
    """
    assertion_error = f"Failed to raise ValueError, given invalid Rank \"10\""
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(h1, h2)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(assertion_error)
    else:
        raise AssertionError(assertion_error)


###########################
### Level 6: Pair Hands ###
###########################


@pytest.mark.integration(min_level=6)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C TD 3H 4S", "4S 7S AD 5D JC", 1),
    ("3C 5C TD 3H 4S", "JC 7S 4H AD 4S", 2),
])
def test_pair_hands(h1, h2, expected_result):
    """
    Pair hands are interpreted correctly
    """
    validate_hand_result(h1, h2, expected_result)


##############################
### Level 7: Handling Ties ###
##############################


@pytest.mark.integration(min_level=7)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C AC TD 3H 4S", "JC 7S 4H QD 4S", 2),
    ("3C AC QH 3H 4S", "5C AS 3H QD 3S", 2),
    ("3C AC QH 3H 4S", "4C AS 3H QD 3S", 0),
])
def test_pair_ties_whoops(h1, h2, expected_result):
    """
    Hands with equal value are interpreted as a Draw (Return 0)
    """
    validate_hand_result(h1, h2, expected_result)


########################################
### Level 8: Handling Two Pair Hands ###
########################################


@pytest.mark.integration(min_level=8)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 5S", "4S 7S 4D 5D JC", 1),
    ("3C 5C AD 3H 5S", "JC 6S 4H 6D 4S", 2),
])
def test_two_pair_hands(h1, h2, expected_result):
    """
    Two Pair hands are evaluated correctly, and beat single cards
    """
    validate_hand_result(h1, h2, expected_result)


###############################################
### Level 9: Handling Three Of A Kind Hands ###
###############################################


@pytest.mark.integration(min_level=9)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 3D 3H 4S", "JC 7S 4H 7D 4S", 1),
    ("3C KC 3D 3H 4S", "JC 7S 4H 7D 7H", 2),
])
def test_three_of_a_kind_hands(h1, h2, expected_result):
    """
    Three Of A Kind hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


################################################
### Level 10: Handling "Straight" Hands (v1) ###
################################################


@pytest.mark.integration(min_level=10, max_level=13)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 4H 2S", "JC 7S 4H 7D 7H", 1),
    ("3C 5C 1D 4H 2S", "2C 6S 5H 3D 4S", 2),
])
def test_straight_hands(h1, h2, expected_result):
    """
    Straight hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


######################################
### Level 11: Handling Flush Hands ###
######################################


@pytest.mark.integration(min_level=11)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("7C 5C 1C 3C 4C", "4C 8S 7H 5D 6S", 1),
    ("7C 5C 1C 3C 4C", "4S 8S 7S 5S 6S", 2),
])
def test_flush_hands(h1, h2, expected_result):
    """
    Flush hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


###########################################
### Level 12: Handling Full House Hands ###
###########################################


@pytest.mark.integration(min_level=12)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3D 3S 4C 3H 4D", "2C 5C 1C 3C 4C", 1),
    ("3D 3S 4C 3H 4D", "4H 4S 5C 4B 5H", 2),
])
def test_full_house_hands(h1, h2, expected_result):
    """
    Full House hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


###############################################
### Level 13: Handling Four Of A Kind Hands ###
###############################################


@pytest.mark.integration(min_level=13)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 3D 3H 3S", "4H 4S 5C 4B 5H", 1),
    ("3C KC 3D 3H 3S", "4H 4S 4C 5H 4B", 2),
])
def test_four_of_a_kind_hands(h1, h2, expected_result):
    """
    Four Of A Kind hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


##############################################
### Level 14: Handling Straight Hands (v2) ###
##############################################


@pytest.mark.integration(min_level=14)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 4S", "4S 7S AD 5D JC", 1),
    ("3C 5C 1D 3H 4S", "JC 7S 4H AD 4S", 2),
])
def test_straight_hands_whoops(h1, h2, expected_result):
    """
    (Corrected!) Straight hands are evaluated, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


###############################################
### Level 15: Handling Straight Flush Hands ###
###############################################


@pytest.mark.integration(min_level=15)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("2C 5C 1C 3C 4C", "JC 7S 4H AD 4S", 1),
    ("2C 5C 1C 3C 4C", "2S 5S 3S 6S 4S", 2),
    ("3C 6C 4C 7C 5C", "2S 5S 3S 6S 4S", 1),
    ("3C 6C 4C 7C 5C", "3S 6S 4S 7S 5S", 0),
])
def test_straight_flush_hands(h1, h2, expected_result):
    """
    Straight Flush hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


"""
@pytest.mark.integration(min_level=16)
@pytest.mark.parametrize("hands, expected_result", [
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'] ],
        2),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'] ],
        2),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'] ],
        2),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'],  ['QC', '2H', '7H', '4D', '5H'] ],
        2),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'],  ['QC', '2H', '7H', '4D', '5H'],  ['4S', '3D', 'AS', '7S', '4H'] ],
        6),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'],  ['QC', '2H', '7H', '4D', '5H'],  ['4S', '3D', 'AS', '7S', '4H'],  ['5S', 'JC', '9C', '5C', 'KD'] ],
        7),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'],  ['QC', '2H', '7H', '4D', '5H'],  ['4S', '3D', 'AS', '7S', '4H'],  ['5S', 'JC', '9C', '5C', 'KD'],  ['TH', '2C', 'JD', '6S', 'TD'] ],
        8),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'],  ['QC', '2H', '7H', '4D', '5H'],  ['4S', '3D', 'AS', '7S', '4H'],  ['5S', 'JC', '9C', '5C', 'KD'],  ['TH', '2C', 'JD', '6S', 'TD'],  ['AH', '7D', 'KS', 'AC', '3H'] ],
        9),
    ( [ ['6H', 'JS', '2D', '3S', '9D'], ['QD', 'KH', '8S', '2S', 'AD'],  ['QH', 'TS', '8C', '3C', 'JH'],  ['QS', 'TC', '9H', 'KC', '5D'],  ['QC', '2H', '7H', '4D', '5H'],  ['4S', '3D', 'AS', '7S', '4H'],  ['5S', 'JC', '9C', '5C', 'KD'],  ['TH', '2C', 'JD', '6S', 'TD'],  ['AH', '7D', 'KS', 'AC', '3H'], ['8H', '6C', '6D', '9S', '7C'] ],
        9),
])
def test_multi_hand_api(hands, expected_result):
    result = score_poker_hands(*hands)
    assert result == expected_result, f"Given multiple Hands: {hands} - Expected Hand #{expected_result} to win."
"""


############################################
### Level 16: Handling Royal Flush Hands ###
############################################


@pytest.mark.integration(min_level=16)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("JC AC TC QC KC", "2S 5S 3S 6S 4S", 1),
    ("JC AC TC QC KC", "JS AS TS QS KS", 0),
])
def test_royal_flush_hands(h1, h2, expected_result):
    """
    Royal Flush hands are evaluated correctly, beating lesser Hands
    """
    validate_hand_result(h1, h2, expected_result)


##########################################
### Level 17: Duplicate Card Detection ###
##########################################


@pytest.mark.integration(min_level=17)
@pytest.mark.parametrize("h1, h2, duplication", [
    ("JC AC AC 1C 8D", "2S 5D 3S 6H 4S", "AC twice in one hand"),
    ("JC AC TC 1C 8D", "JS KC TC 6H 4S", "TC in both hands"),
])
def test_duplicate_cards(h1, h2, duplication):
    """
    Duplicate cards within/across hands raise ValueErrors
    """
    assertion_error = f"Failed to raise ValueError, given {duplication}!"
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(h1, h2)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(assertion_error)
    else:
        raise AssertionError(assertion_error)