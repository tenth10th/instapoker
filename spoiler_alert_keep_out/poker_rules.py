poker_rules = [
    {
        "level_range": (0, 3),
        "sort_order": 100,
        "text": """
Ranks by value, ascending: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
Suits (no particular order): H, D, C, S
""",
    },
    {
        "level": 4,
        "sort_order": 100,
        "text": """
Ranks by value, ascending: 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A
Suits (no particular order): H, D, C, S
""",
    },
    {
        "level_range": (1, 5),
        "sort_order": 1,
        "text": """
Highest Card: The Hand with the single highest-ranked card wins.
"""
    },
    {
        "level": 6,
        "sort_order": 1,
        "text": """
Highest Card: The Hand with the single highest-ranked card wins.
(Resolve ties by comparing the next-highest cards. If tie remains, it's a Draw)
"""
    },
    {
        "level_range": (5,5),
        "sort_order": 2,
        "text": """
Pair: A Hand containing two cards of the same Rank (of any Suits)
"""
    },
    {
        "level": 6,
        "sort_order": 2,
        "text": """
Pair: A Hand containing two cards of the same Rank (of any Suits)
(Resolve ties based on Pair ranks - If still tied, resolve as per Highest Card.)
"""
    },
    {
        "level": 7,
        "sort_order": 3,
        "text": """
Two Pairs: A Hand containing two differently-ranked Pairs, as per "Pair"
(Resolve ties as per Pair, starting with the highest-ranked Pair in each Hand)
"""
    },
    {
        "level": 8,
        "sort_order": 4,
        "text": """
Three of a Kind: A Hand containing three cards of the same Rank (any Suits)
(Resolve ties based on the Ranks of the triplets - If still tied, as per Highest Card.)
"""
    },
    {
        "level_range": (9, 10),
        "sort_order": 5,
        "text": """
Straight: A Hand containing five cards of sequential Rank (any Suits)
(Resolve ties as per Highest Card.)
"""
    },
    {
        "level": 10,
        "sort_order": 6,
        "text": """
Flush: A Hand containing five cards of the same Suit (any Ranks)
(Resolve ties as per Highest Card.)
"""
    },
    {
        "level": 11,
        "sort_order": 7,
        "text": """
Full House: A Hand containing a Three of a Kind AND a Pair of a different suit
(Resolve ties as per Three of a Kind)
"""
    },
    {
        "level": 12,
        "sort_order": 8,
        "text": """
Four of a Kind: A Hand containing four cards of the same Rank (any Suit)
(Resolve ties using the Ranks of the four-card sets)
"""
    },
    {
        "level": 13,
        "sort_order": 5,
        "text": """
Straight: A Hand containing five cards of sequential Rank (but NOT the same Suit - whoops)
(Resolve ties as per Highest Card.)
"""
    },
    {
        "level": 14,
        "sort_order": 9,
        "text": """
Straight Flush: A Hand consisting of five sequentially-ranked cards of the same Suit.
(Resolve ties using the Ranks of the four-card sets)
"""
    },
    {
        "level": 15,
        "sort_order": 10,
        "text": """
Royal Flush: The best possible Straight Flush (10, J, Q, K, A of the same Suit)
(Resolve ties as per Highest Card)
"""
    }
]
