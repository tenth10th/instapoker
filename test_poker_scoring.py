from poker_scoring_api import score_poker_hands
import pytest


def test_first_hand_wins():
    actual = score_poker_hands("10H", "2H")
    assert isinstance(actual, int)
    assert actual == 1


def test_second_hand_wins():
    actual = score_poker_hands("2H", "10H")
    assert isinstance(actual, int)
    assert actual == 2


@pytest.mark.parametrize("first_hand, second_hand", [
    ("4D", "0D"),
    ("0D", "4D"),
    ("14D", "4D"),
    (None, "2D"),
    ("4D", None),
    ("1D", "2D")
])
def test_invalid_ranks(first_hand, second_hand):
    with pytest.raises(ValueError):
        score_poker_hands(first_hand, second_hand)


@pytest.mark.parametrize("first_hand, second_hand", [
    ("4D", "4X"),
    ("4X", "4D"),
    ("10DD", "10D"),
    ("10D", "2DD"),
])
def test_invalid_suits(first_hand, second_hand):
    with pytest.raises(ValueError):
        score_poker_hands(first_hand, second_hand)
