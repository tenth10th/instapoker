import pytest
from poker_scoring_api import score_poker_hands


@pytest.mark.level(0)
def test_poker_scoring_api():
    """
    score_poker_hands accepts two strings, and returns an integer
    """
    result = score_poker_hands("2D", "2H")
    assert isinstance(result, int)


@pytest.mark.level(1)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3H", "2D", 1),
    ("4C", "5S", 2),
    ("AD", "KC", 1),
    ("JS", "QH", 2),
    ("8D", "7D", 1),
])
def test_single_card_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(1)
@pytest.mark.max_level(3)
def test_high_single_card_hands_10():
    assert score_poker_hands("10H", "9S") == 1


@pytest.mark.level(2)
def test_invalid_None_inputs():
    with pytest.raises(ValueError):
        score_poker_hands(None, None)


@pytest.mark.level(2)
def test_invalid_empty_inputs():
    with pytest.raises(ValueError):
        score_poker_hands("", "")


@pytest.mark.level(2)
def test_invalid_integer_inputs():
    with pytest.raises(ValueError):
        score_poker_hands(1, 2)


@pytest.mark.level(2)
def test_invalid_suit_inputs():
    with pytest.raises(ValueError):
        score_poker_hands("1Z", "2X")


@pytest.mark.level(2)
def test_invalid_rank_inputs():
    with pytest.raises(ValueError):
        score_poker_hands("0H", "-1C")


@pytest.mark.level(3)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("4D 3H", "2H 3S", 1),
    ("3C QH KC 9C 6H", "4S 7S AD 5D JC", 2),
])
def test_multi_card_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(4)
def test_high_single_card_hands_T():
    assert score_poker_hands("TH", "9S") == 1


@pytest.mark.level(5)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 4S", "4S 7S AD 5D JC", 1),
    ("3C 5C 1D 3H 4S", "JC 7S 4H AD 4S", 2),
])
def test_pair_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(6)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C AC 1D 3H 4S", "JC 7S 4H QD 4S", 2),
    ("3C AC QH 3H 4S", "5C AS 3H QD 3S", 2),
    ("3C AC QH 3H 4S", "4C AS 3H QD 3S", 0),
])
def test_pair_ties_whoops(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(7)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 5S", "4S 7S 4D 5D JC", 1),
    ("3C 5C AD 3H 5S", "JC 6S 4H 6D 4S", 2),
])
def test_two_pair_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(8)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 3D 3H 4S", "JC 7S 4H 7D 4S", 1),
    ("3C KC 3D 3H 4S", "JC 7S 4H 7D 7H", 2),
])
def test_three_of_a_kind_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(9)
@pytest.mark.max_level(12)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 4H 2S", "JC 7S 4H 7D 7H", 1),
    ("3C 5C 1D 4H 2S", "2C 6S 5H 3D 4S", 2),
])
def test_straight_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(10)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("7C 5C 1C 3C 4C", "4C 8S 7H 5D 6S", 1),
    ("7C 5C 1C 3C 4C", "4S 8S 7S 5S 6S", 2),
])
def test_flush_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(11)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3D 3S 4C 3H 4D", "2C 5C 1C 3C 4C", 1),
    ("3D 3S 4C 3H 4D", "4H 4S 5C 4B 5H", 2),
])
def test_full_house_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(12)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 3D 3H 3S", "4H 4S 5C 4B 5H", 1),
    ("3C KC 3D 3H 3S", "4H 4S 4C 5H 4B", 2),
])
def test_four_of_a_kind_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(13)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("3C 5C 1D 3H 4S", "4S 7S AD 5D JC", 1),
    ("3C 5C 1D 3H 4S", "JC 7S 4H AD 4S", 2),
])
def test_straight_hands_whoops(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(14)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("2C 5C 1C 3C 4C", "JC 7S 4H AD 4S", 1),
    ("2C 5C 1C 3C 4C", "2S 5S 3S 6S 4S", 2),
])
def test_straight_flush_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result


@pytest.mark.level(15)
@pytest.mark.parametrize("h1, h2, expected_result", [
    ("JC AC TC QC KC", "2S 5S 3S 6S 4S", 1),
    ("JC AC TC QC KC", "JS AS TS QS KS", 0),
])
def test_royal_flush_hands(h1, h2, expected_result):
    assert score_poker_hands(h1, h2) == expected_result

@pytest.mark.level(16)
@pytest.mark.parametrize("h1, h2", [
    ("JC AC AC QC KC", "2S 5S 3S 6S 4S"),
    ("JC AC TC QC KC", "JS AC TS QS KS"),
])
def test_duplicate_cards(h1, h2):
    with pytest.raises(ValueError):
        assert score_poker_hands(h1, h2)
