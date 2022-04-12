from poker_scoring_api import Card
import pytest

def test_instantiate_valid_card():
    c = Card("2H")

INVALID_RANK = "Invalid rank"
INVALID_SUIT = "Invalid suit"

@pytest.mark.parametrize('invalid_card, exception_match', [
    ['CF', INVALID_RANK],
    ['0F', INVALID_RANK],
    ['10F', INVALID_RANK],
    ['2P', INVALID_SUIT],
    ['0C', INVALID_RANK],
])
def test_invalid_card(invalid_card, exception_match):
    with pytest.raises(Exception, match=exception_match):
        c = Card(invalid_card)

@pytest.mark.parametrize('valid_card, expected_rank, expected_suit', [
    ['6C', 6, "C"],
    ['4H', 4, "H"],
    ['QS', 12, "S"],
    ['TD', 10, "D"],
    ['AC', 14, "C"],
])
def test_valid_card(valid_card, expected_rank, expected_suit):
    c = Card(valid_card)
    assert expected_rank == c.rank
    assert expected_suit == c.suit
    assert valid_card == c.name

@pytest.mark.parametrize('card_1, card_2, expected_result', [
    ['6C', '5C', False],
    ['3C', '5C', True]
])
def test_card_rank_compare_less_than(card_1, card_2, expected_result):
    assert (card_1 < card_2) == expected_result
    assert (card_1 > card_2) != expected_result

@pytest.mark.parametrize('card_1, card_2, expected_result', [
    ['6C', '5C', False],
    ['3C', '3C', True]
])
def test_card_rank_compare_equal_to(card_1, card_2, expected_result):
    assert (card_1 == card_2) == expected_result
    assert (card_1 != card_2) != expected_result


def test_are_lists_of_cards_comparable():
    assert [Card("TH"), Card("8S"), Card("4C"),] > [Card("9S"), Card("8D"), Card("5C"),]
    assert [Card("TH"), Card("8S"), Card("5C"),] > [Card("TS"), Card("8D"), Card("4C"),]
    assert [Card("TH"), Card("8S"), Card("4C"),] < [Card("TS"), Card("8D"), Card("5C"),]
    assert [Card("TH"), Card("8S"), Card("4C"),] == [Card("TS"), Card("8D"), Card("4H"),]
