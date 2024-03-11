from poker_scoring_api import score_poker_hands
from poker_scoring_api import get_rank
from poker_scoring_api import get_suit
import pytest


def test_basic_interface():
    result = score_poker_hands("2D", "5S")
    assert isinstance(result, int)


# Refactored into the single "parameterized" test below:

# def test_player1_wins():
#     assert score_poker_hands("5H","3D") == 1

# def test_player2_wins():
#     assert score_poker_hands("5H","9D") == 2

# def test_player1_wins_higher_rank():
#     assert score_poker_hands("10C","9S") == 1


@pytest.mark.parametrize(
    ("hand1", "hand2", "result"),
    [
        # fmt: off
        ("5H", "3D", 1),
        ("5H", "9D", 2),
        ("10C", "9S", 1),
        ("AS", "KH", 1),
        ("2C", "JD", 2),
        # fmt: on
    ],
)
def test_score_poker_hands(hand1, hand2, result):
    assert score_poker_hands(hand1, hand2) == result


# Reimplemented using parameters below:

# def test_get_rank_func():
#     assert getRank("KD") == 13


@pytest.mark.parametrize(
    ("hand", "rank"),
    [
        # fmt: off
        ("2H", 2),
        ("10C", 10),
        ("KD", 13),
        ("XX", None),
        # fmt: on
    ],
)
def test_get_rank_func(hand, rank):
    assert get_rank(hand) == rank


@pytest.mark.parametrize(
    ("hand", "valid"),
    [
        # fmt: off
        ("H", "H"),
        ("X", None),
        # fmt: on
    ],
)
def test_get_suit_func(hand, valid):
    assert get_suit(hand) == valid


@pytest.mark.parametrize(
    ("hand1", "hand2"),
    [
        # fmt: off
        ("2H", "22H"),
        ("3F", "10H"),
        (12, "10S"),
        ("AS", None),
        # fmt: on
    ],
)
def test_invalid_input(hand1, hand2):
    with pytest.raises(ValueError):
        score_poker_hands(hand1, hand2)
