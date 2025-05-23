import pytest

from poker_scoring_api import score_poker_hands, rank_value


def test_api():
    assert isinstance(score_poker_hands("2H", "5D"), int)


@pytest.mark.parametrize(
    ("hand1", "hand2", "result"),
    (
        ("2H", "5D", 2),
        ("JH", "AD", 2),
        ("AH", "KD", 1),
        ("QH", "JD", 1),
        ("5H", "2D", 1),
        ("AH", "JD", 1),
        ("KH", "AD", 2),
        ("JH", "QD", 2),
        ("KH", "QD", 1),
        ("10H", "9D", 1),
        ("9H", "10D", 2),
    ),
)
def test_single_card_hands(hand1, hand2, result):
    assert score_poker_hands(hand1, hand2) == result


@pytest.mark.parametrize(("rank", "result"), (("5", 5), ("7", 7), ("J", 11), ("K", 13)))
def test_the_rank_value(rank, result):
    assert rank_value(rank) == result


@pytest.mark.parametrize(("hand"), ("", "1h", 1, "2F", {}, []))
def test_bad_inputs(hand):
    with pytest.raises(ValueError):
        score_poker_hands("9H", hand)
        score_poker_hands(hand, "9H")
