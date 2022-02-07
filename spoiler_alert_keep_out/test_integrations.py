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


@pytest.mark.integration(min_level=1)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3H", "2D", 1),
    ("4C", "5S", 2),
    ("AD", "KC", 1),
    ("JS", "QH", 2),
    ("8D", "7D", 1),
])
def test_single_card_hands(h1, h2, expected_result):
    """
    Single-card hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


@pytest.mark.integration(min_level=1, max_level=3)
def test_high_single_card_hands_10():
    """
    Single-card rank 10 hands are evaluated correctly
    """
    validate_hand_result("10H", "9S", 1)


@pytest.mark.integration(min_level=2)
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


@pytest.mark.integration(min_level=2)
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


@pytest.mark.integration(min_level=2)
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


@pytest.mark.integration(min_level=2)
@pytest.mark.parametrize("h1, h2", [
    ("1S", "3X"),
    ("5H", "2Z"),
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


@pytest.mark.integration(min_level=2)
@pytest.mark.parametrize("h1, h2", [
    ("7D", "0S"),
    ("4H", "-1C"),
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
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("4D 3H", "2H 3S", 1),
    ("4C QH KC 9C 6H", "3S 7S AD 5D JC", 2),
])
def test_multi_card_hands(h1, h2, expected_result):
    """
    Multi-card hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=4)
def test_high_single_card_hands_T():
    """
    T is interpreted to represent Rank 10
    """
    validate_hand_result("TH", "9S", 1)

@pytest.mark.integration(min_level=4)
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

@pytest.mark.integration(min_level=5)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 4S", "4S 7S AD 5D JC", 1),
    ("3C 5C 1D 3H 4S", "JC 7S 4H AD 4S", 2),
])
def test_pair_hands(h1, h2, expected_result):
    """
    Pair hands are interpreted correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=6)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C AC 1D 3H 4S", "JC 7S 4H QD 4S", 2),
    ("3C AC QH 3H 4S", "5C AS 3H QD 3S", 2),
    ("3C AC QH 3H 4S", "4C AS 3H QD 3S", 0),
])
def test_pair_ties_whoops(h1, h2, expected_result):
    """
    Hands with equal values are interpreted as a Draw
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=7)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 5S", "4S 7S 4D 5D JC", 1),
    ("3C 5C AD 3H 5S", "JC 6S 4H 6D 4S", 2),
])
def test_two_pair_hands(h1, h2, expected_result):
    """
    Two Pair hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=8)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 3D 3H 4S", "JC 7S 4H 7D 4S", 1),
    ("3C KC 3D 3H 4S", "JC 7S 4H 7D 7H", 2),
])
def test_three_of_a_kind_hands(h1, h2, expected_result):
    """
    Three Of A Kind hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=9, max_level=12)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 4H 2S", "JC 7S 4H 7D 7H", 1),
    ("3C 5C 1D 4H 2S", "2C 6S 5H 3D 4S", 2),
])
def test_straight_hands(h1, h2, expected_result):
    """
    Straight hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=10)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("7C 5C 1C 3C 4C", "4C 8S 7H 5D 6S", 1),
    ("7C 5C 1C 3C 4C", "4S 8S 7S 5S 6S", 2),
])
def test_flush_hands(h1, h2, expected_result):
    """
    Flush hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=11)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3D 3S 4C 3H 4D", "2C 5C 1C 3C 4C", 1),
    ("3D 3S 4C 3H 4D", "4H 4S 5C 4B 5H", 2),
])
def test_full_house_hands(h1, h2, expected_result):
    """
    Full House hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=12)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 3D 3H 3S", "4H 4S 5C 4B 5H", 1),
    ("3C KC 3D 3H 3S", "4H 4S 4C 5H 4B", 2),
])
def test_four_of_a_kind_hands(h1, h2, expected_result):
    """
    Four Of A Kind hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=13)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 4S", "4S 7S AD 5D JC", 1),
    ("3C 5C 1D 3H 4S", "JC 7S 4H AD 4S", 2),
])
def test_straight_hands_whoops(h1, h2, expected_result):
    """
    Straight hands (updated definition!) are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)

@pytest.mark.integration(min_level=14)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("2C 5C 1C 3C 4C", "JC 7S 4H AD 4S", 1),
    ("2C 5C 1C 3C 4C", "2S 5S 3S 6S 4S", 2),
])
def test_straight_flush_hands(h1, h2, expected_result):
    """
    Straight Flush hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


@pytest.mark.integration(min_level=15)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("JC AC TC QC KC", "2S 5S 3S 6S 4S", 1),
    ("JC AC TC QC KC", "JS AS TS QS KS", 0),
])
def test_royal_flush_hands(h1, h2, expected_result):
    """
    Royal Flush hands are evaluated correctly
    """
    validate_hand_result(h1, h2, expected_result)


@pytest.mark.integration(min_level=16)
@pytest.mark.parametrize("h1, h2", [
    ("JC AC AC 1C 8D", "2S 5D 3S 6H 4S"),
    ("JC AC TC 1C 8D", "JS AC TS 6H 4S"),
])
def test_duplicate_cards(h1, h2):
    """
    Duplicate cards within/across hands raise ValueErrors
    """
    assertion_error = f"Failed to raise ValueError, given duplicate card AC!"
    # Less idiomatic than pytest.raises, but clearer assertion errors!
    try:
        score_poker_hands(h1, h2)
    except Exception as e:
        if not isinstance(e, ValueError):
            raise AssertionError(assertion_error)
    else:
        raise AssertionError(assertion_error)