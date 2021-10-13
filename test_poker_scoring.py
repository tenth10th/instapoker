from poker_scoring_api import (
    score_poker_hands,
    parse_card,
    parse_hand,
    is_pair,
)
import pytest


def test_scoring_api():
    # FIXME: Maybe assert something meaningful about score_poker_hands?
    assert score_poker_hands("2H", "3H") in (0, 1, 2)

def test_simple_scoring():
    assert score_poker_hands("2H", "3H") == 2
    assert score_poker_hands("2H", "2D") == 0
    assert score_poker_hands("3H", "2D") == 1
    assert score_poker_hands("TH", "9S") == 1
    assert score_poker_hands("TH", "JS") == 2

def test_parse_card():
    assert parse_card("TH") == 10
    assert parse_card("9S") == 9
    assert parse_card("JS") == 11
    
@pytest.mark.parametrize("card", [
    ("4"),
    ("XS"),
    ("11H"),
    ("QZ"),
    ("10C"),
])
def test_invalid_cards(card):
    with pytest.raises(ValueError):
        parse_card(card)

@pytest.mark.parametrize("hand", [
    (3),
    (''),
])
def test_invalid_hands(hand):
    with pytest.raises(ValueError):
        parse_hand(hand)

def test_multi_card_hand():
    assert score_poker_hands("2H 7S KC", "5D 5H 5C") == 1

def test_parse_hand():
    assert parse_hand("2H 7S KC") == [13, 7, 2]

def test_pair_hand():
    assert score_poker_hands("2H 2C", "3H 4C") == 1

def test_is_pair():
    assert is_pair("2H 2C") is True
