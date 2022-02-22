from poker_scoring_api import (
    score_poker_hands, card_parser, compare_cards, parse_hand, 
    get_highest_card)

import pytest


def test_card_parser():
    assert card_parser("2H") == 2

def test_compare_cards_less():
    assert compare_cards("4H", "3C") == 1

def test_compare_cards_equal():
    assert compare_cards("5H", "5S") == 0

def test_compare_cards_greater():
    assert compare_cards("5H", "6S") == 2

def test_card_parse_face_cards_jack():
    assert card_parser("JH") == 11
    assert card_parser("jH") == 11

def test_card_parse_face_cards_queen():
    assert card_parser("QH") == 12
    assert card_parser("qH") == 12

def test_card_parse_face_cards_king():
    assert card_parser("KH") == 13
    assert card_parser("kH") == 13

def test_card_parse_face_cards_ace():
    assert card_parser("AH") == 14
    assert card_parser("aH") == 14

def test_card_JS_should_lose_against_QH():
    assert score_poker_hands("JS", "QH") == 2

def test_invalid_card_not_string():
    with pytest.raises(ValueError):
        assert score_poker_hands(0, 0)

def test_invalid_suit():
    with pytest.raises(ValueError, match = "Invalid suit."):
        assert score_poker_hands("2Z","2Z")

def test_invalid_rank():
    with pytest.raises(ValueError, match = "Invalid rank."):
        assert score_poker_hands("ZH","14H")

def test_parse_hand():
    assert parse_hand("3H 2D JC") == ["3H", "2D", "JC"]

def test_parse_single_hand():
    assert parse_hand("3H") == ["3H"]

def test_multi_card_hand():
    assert score_poker_hands("3H AD JC", "6S 10H 2C") == 1

def test_get_highest_card():
    assert get_highest_card(["6S", "10H", "2C"]) == "10H"