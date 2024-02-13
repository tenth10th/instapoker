from poker_scoring_api import score_poker_hands
from poker_scoring_api import getRank
from poker_scoring_api import getSuit
import pytest

def test_basic_interface():
    result = score_poker_hands("2D","5S")
    assert isinstance(result, int)

# Refactored into the single "parameterized" test below:

# def test_player1_wins():
#     assert score_poker_hands("5H","3D") == 1

# def test_player2_wins():
#     assert score_poker_hands("5H","9D") == 2

# def test_player1_wins_higher_rank():
#     assert score_poker_hands("10C","9S") == 1

@pytest.mark.parametrize(("hand1", "hand2", "result"),  [
    ("5H", "3D", 1),
    ("5H", "9D", 2),
    ("10C", "9S", 1),
    ("AS", "KH", 1),
    ("2C", "JD", 2)
])
def test_score_poker_hands(hand1, hand2, result):
    assert score_poker_hands(hand1, hand2) == result

# Reimplemented using parameters below:

# def test_getRank_func():
#     assert getRank("KD") == 13

@pytest.mark.parametrize(("hand", "rank"), [
    ("2H", 2),
    ("10C", 10),
    ("KD", 13),
    ("XX", None)
])
def test_getRank_func(hand, rank):
    assert getRank(hand) == rank

@pytest.mark.parametrize(("hand", "valid"), [
    ("H", "H"),
    ("X", None)
])
def test_getSuit_func(hand, valid):
    assert getSuit(hand) == valid

@pytest.mark.parametrize(("hand1", "hand2"), [
    ("2H", "22H"),
    ("3F", "10H"),
    (12, "10S"),
    ("AS", None)
])
def test_invalid_input(hand1,hand2):
    with pytest.raises(ValueError):
        score_poker_hands(hand1,hand2)