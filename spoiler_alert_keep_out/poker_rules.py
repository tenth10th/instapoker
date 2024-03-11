poker_rules = [
    {
        "level": 0,
        "sort_order": 100,
        "text": """
score_poker_hands should accept two Hands (strings) and return an Integer.
""",
    },
    {
        "level_range": (1, 2),
        "sort_order": 99,
        "text": """
Each hand will be a single card, for example, "2H" for Two of Hearts
(Return 1 if the first hand wins, or 2 if the second hand wins)
""",
    },
    {
        "level_range": (3, 3),
        "sort_order": 99,
        "text": """
Each hand should be a single card, for example, "2H" for the Two of Hearts
    (Given invalid Ranks or Suits, raise a ValueError!)
Return 1 if the first hand wins, or 2 if the second hand wins.
""",
    },
    {
        "level": 4,
        "sort_order": 99,
        "text": """
Each hand should be a string of space-separated cards, e.g. "2H KS 5D 9C JH"
    (Given invalid Ranks or Suits, raise a ValueError!)
Return 1 if the first hand wins, or 2 if the second hand wins.
""",
    },
    {
        "level_range": (1, 1),
        "sort_order": 98,
        "text": """
Ranks by value, ascending: 2, 3, 4, 5, 6, 7, 8, 9
Suits (no particular order): H, D, C, S
""",
    },
    {
        "level_range": (2, 4),
        "sort_order": 98,
        "text": """
Ranks by value, ascending: 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
Suits (no particular order): H, D, C, S
""",
    },
    {
        "level": 5,
        "sort_order": 98,
        "text": """
Ranks by value, ascending: 2, 3, 4, 5, 6, 7, 8, 9, T, J, Q, K, A
Suits (no particular order): H, D, C, S
""",
    },
    {
        "level_range": (1, 6),
        "sort_order": 1,
        "text": """
Highest Card: The Hand with the single highest-ranked card wins.
""",
    },
    {
        "level": 7,
        "sort_order": 1,
        "text": """
Highest Card: The Hand with the single highest-ranked card wins.
(Resolve ties by comparing the next-highest cards. If tie remains, it's a Draw)
""",
    },
    {
        "level_range": (6, 6),
        "sort_order": 2,
        "text": """
Pair: A Hand containing two cards of the same Rank (of any Suits)
""",
    },
    {
        "level": 7,
        "sort_order": 2,
        "text": """
Pair: A Hand containing two cards of the same Rank (of any Suits)
(Resolve ties based on Pair ranks - If still tied, resolve as per Highest Card.)
""",
    },
    {
        "level": 8,
        "sort_order": 3,
        "text": """
Two Pairs: A Hand containing two differently-ranked Pairs, as per "Pair"
(Resolve ties as per Pair, starting with the highest-ranked Pair in each Hand)
""",
    },
    {
        "level": 9,
        "sort_order": 4,
        "text": """
Three of a Kind: A Hand containing three cards of the same Rank (any Suits)
(Resolve ties based on the Ranks of the triplets - If still tied, as per Highest Card.)
""",
    },
    {
        "level_range": (10, 13),
        "sort_order": 5,
        "text": """
Straight: A Hand containing five cards of sequential Rank (any Suits)
(Resolve ties as per Highest Card.)
""",
    },
    {
        "level": 11,
        "sort_order": 6,
        "text": """
Flush: A Hand containing five cards of the same Suit (any Ranks)
(Resolve ties as per Highest Card.)
""",
    },
    {
        "level": 12,
        "sort_order": 7,
        "text": """
Full House: A Hand containing a Three of a Kind AND a Pair of a different suit
(Resolve ties as per Three of a Kind)
""",
    },
    {
        "level": 13,
        "sort_order": 8,
        "text": """
Four of a Kind: A Hand containing four cards of the same Rank (any Suit)
(Resolve ties using the Ranks of the four-card sets)
""",
    },
    {
        "level": 14,
        "sort_order": 5,
        "text": """
Straight: A Hand containing five cards of sequential Rank (but NOT the same Suit - whoops)
(Resolve ties as per Highest Card.)
""",
    },
    {
        "level": 15,
        "sort_order": 9,
        "text": """
Straight Flush: A Hand consisting of five sequentially-ranked cards of the same Suit.
(Resolve ties using the Ranks of the four-card sets)
""",
    },
    {
        "level": 16,
        "sort_order": 10,
        "text": """
Royal Flush: The best possible Straight Flush (10, J, Q, K, A of the same Suit)
(Resolve ties as per Highest Card)
""",
    },
    {
        "level": 17,
        "sort_order": 11,
        "text": """
Duplicate Cards (within or across hands) should raise a ValueError!
""",
    },
]
