from poker_scoring_api import score_poker_hands, parse_card
import pytest

def test_interface():
    result = score_poker_hands("3D 2H KS 5D 9C", "5H JD 10H AC JS")
    assert isinstance(result, int)

@pytest.mark.parametrize(('hand1', 'hand2', 'expected'), [
    ('2D', '3H', 2),
    ('2D 3H JD 10C KS', '2H 3D 4C 5S 6H', 1),
    ('3H', '2D', 1),
    ('JD', '10D', 1),
    ('10C', '2H', 1),
])
def test_score_poker_hands(hand1, hand2, expected):
    result = score_poker_hands(hand1, hand2)
    assert result == expected

@pytest.mark.parametrize(('hand1', 'hand2'), [
    (None, '3H'),
    ('2D 3H JD 10C KS', None),
])
def test_bad_input_score_poker_hands(hand1, hand2):
    with pytest.raises(ValueError) as ve:
        # in this block, raising ValueError
        # is expected!
        score_poker_hands(hand1, hand2)
    assert 'input' in str(ve)



@pytest.mark.parametrize(('card', 'expected'), [
    ("2S", (2, "S")),
    ("10H", (10, "H")),
    ("JD", (11, "D")),
])
def test_parse_card(card, expected):
    result = parse_card(card)
    assert result == expected

@pytest.mark.parametrize(('card', 'expected_text'), [
    ('KF', 'suit'),
    ('FH', 'rank'),
    ('FF', 'rank'),
    (None, 'card'),
    ('', 'card'),
])
def test_invalid_rank(card, expected_text):
    with pytest.raises(ValueError) as ve:
        # in this block, raising ValueError
        # is expected!
        parse_card(card)
    assert expected_text in str(ve)
