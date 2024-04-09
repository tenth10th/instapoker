# TODO: Write some tests for score_poker_hands...
# from poker_scoring_api import score_poker_hands
from poker_scoring_api import Card, Hand, score_poker_hands
import pytest


def test_example():
    # Example of a PyTest test case:
    # a function whose name start with "test"
    # (that ideally asserts some stuff...)
    assert True


@pytest.mark.parametrize("card, rank, suit", [
    ("2H", 2, "H"),
    ("JD", 11, "D"),
    ("TS", 10, "S")
])
def test_card_parsing(card, rank, suit):
    c = Card(card)
    assert c.rank == rank
    assert c.suit == suit


def test_hand():
    h = Hand("2H")
    assert h.highest_card() == 2


@pytest.mark.parametrize("h1, h2, expected", [
    ("TH", "2D", 1),
    ("2D", "TH", 2),
])
def test_score_poker_hands(h1, h2, expected):
    result = score_poker_hands(h1, h2)
    assert result == expected


@pytest.mark.parametrize("h1, h2, expected, except_message", [
    ("GH", "2D", ValueError, "That is not a valid rank"),
    ("99H", "2D", ValueError, "The card rank must be between 2 and 9"),
    ("2F", "6F", ValueError, "That is not a valid suit"),
    ("10H", "6D", ValueError, "The card rank must be between 2 and 9"),
    (None, None, ValueError, "Please check hand types or be fired"),
    ("", "", ValueError, "Cards must be at least two characters"),
    (1, False, ValueError, ""),
])
def test_score_poker_hands_error(h1, h2, expected, except_message):
    with pytest.raises(expected) as ex:
        _ = score_poker_hands(h1, h2)
    if except_message:
        assert except_message in str(ex)


@pytest.mark.parametrize("h1, h2, expected", [
    ("2H 3D", "4C 6S", 2),
    ("2H 8D", "4C 6S", 1),
])
def test_score_poker_hands_multiple_cards(h1, h2, expected):
    result = score_poker_hands(h1, h2)
    assert result == expected


@pytest.mark.parametrize(("hand_str", "best_pair"), [
    ("2H 3D 2C", 2),
    ("2H 3D 2C 3S", 3),
    ("2H 3D", None),
    ("2H 3C 2D 2S", 2),
])
def test_hand_has_pair(hand_str, best_pair):
    h = Hand(hand_str)
    assert h.has_pair() == best_pair



@pytest.mark.parametrize("h1, h2, expected", [
    ("2H 3D 2S", "4C 6S", 1),
    ("2H 8D", "4C 6S 4D", 2),
])
def test_score_poker_hands_pairs(h1, h2, expected):
    result = score_poker_hands(h1, h2)
    assert result == expected


def test_hand_highest_card():
    h = Hand("2H 3D 2S")
    print(h.highest_card())
