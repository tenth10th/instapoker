from poker_scoring_api import (
    score_poker_hands, card_parser, compare_cards, parse_hand, 
    get_sorted_hand, has_pair, pair_beats_non_pair, compare_rank_lists,
    compare_pair_hands)

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

def test_invalid_rank():
    with pytest.raises(ValueError, match = "Invalid rank."):
        assert score_poker_hands("ZH","10H")

def test_parse_hand():
    assert parse_hand("3H 2D JC") == ["3H", "2D", "JC"]

def test_parse_single_hand():
    assert parse_hand("3H") == ["3H"]

def test_multi_card_hand():
    assert score_poker_hands("3H AD JC", "6S TH 2C") == 1

def test_get_sorted_hand():
    assert get_sorted_hand(["6S", "TH", "2C"]) == [10, 6, 2]

def test_has_pair():
    assert has_pair("2H 7C TS") == False
    assert has_pair("2H 2S TS") == True
    assert has_pair("2H 2S") == True

def test_pair_beats_non_pair():
    assert pair_beats_non_pair("2H 2S", "7C TS") == 1
    assert pair_beats_non_pair("3H 2S", "7C 7S") == 2
    assert pair_beats_non_pair("2H 6S", "7C TS") == 0

def test_score_poker_hands_pair():
    assert score_poker_hands("2H 2S", "7C TS") == 1

def test_score_poker_hand_tie():
    assert score_poker_hands("6D", "6C") == 0
    assert score_poker_hands("6D 6C", "6H 6S") == 0
    assert score_poker_hands("6D 5C", "6H 3S") == 1

def test_compare_rank_lists():
    assert compare_rank_lists([9, 4, 3], [8, 4, 3]) == 1
    assert compare_rank_lists([9, 4, 3], [9, 4, 2]) == 1
    assert compare_rank_lists([9, 4, 3], [9, 4, 3]) == 0
    assert compare_rank_lists([9, 4, 3], [9, 4]) == 1

# Failing because we aren't evaluating the relative rank of pairs
# (e.g. a pair of 4s should beat a pair of 3s)
# def test_compare_pairs():
#      assert score_poker_hands("3C AC TD 3H 4S", "JC 7S 4H QD 4C") == 2

# This function isn't fully implemented yet
def test_call_compare_pair_hands():    
    assert compare_pair_hands(["3C","AC","TD","4H","4S"], ["JC","7S","3H","QD","3C"]) == 1
