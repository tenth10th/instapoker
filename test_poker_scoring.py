# TODO: Write some tests for score_poker_hands...

from poker_scoring_api import score_poker_hands
import pytest

def test_function_signature():
    """
    score_poker_hands accepts two hands as strings
    (and returns an integer, 1 or 2)
    """
    result = score_poker_hands("2H", "5D")
    assert isinstance(result, int)
    assert result in (1, 2)


def test_simple_comparison():
    assert score_poker_hands("3H", "2D") == 1
    assert score_poker_hands("2H", "3D") == 2


def test_ten_vs_two():
    assert score_poker_hands("TH", "2D") == 1
    assert score_poker_hands("2D", "TH") == 2


def test_j_greater_than_10():
    assert score_poker_hands("JD", "TH") == 1
    assert score_poker_hands("TH", "JD") == 2


def test_invalid_rank():
    with pytest.raises(ValueError):
        score_poker_hands("99H", "1D")


def test_invalid_suit():
    with pytest.raises(ValueError):
        score_poker_hands("2F", "9X")


def test_none_card():
    with pytest.raises(ValueError):
        score_poker_hands(None, None)

def test_multi_card_hands_allowed():
    score_poker_hands("2H 4D 7C 2C 3S", "2D KS 5D 9C JH")

def test_highest_card_wins():
    assert score_poker_hands("2H 4D 7C 2C 3S", "2D KS 5D 9C JH") == 2
    assert score_poker_hands("2D KS 5D 9C JH", "2H 4D 7C 2C 3S") == 1
