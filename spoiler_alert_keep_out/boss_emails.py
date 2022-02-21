boss_emails = [

# 0
"""
Okay, to start, let's just get the basic API working. We'll want to accept two
poker hands, as strings, and return a scoring result as an Integer.

I can't imagine us ever needing to change this API, so let's lock that in first!
Don't worry about the rules yet, just --submit when the API is in the right shape.

Let's do this!
""",

# 1
"""
The UI team has decided to represent Poker Hands as pairs of Ranks and Suits,
in that order: So "2H" for a Two of Hearts, "5D" for a Five of Diamonds, etc.
For now, let's assume each hand is a single card - I've added some ranks and
suits to the --rules. The basic rule sounds pretty simple:

  * The hand with the highest-ranked card wins! (I guess Suits don't matter?)

  * Return 1 if the first hand won, or 2 if the second hand won

Let's do it! (And don't forget to --submit when you're finished.)
""",

# 2
"""
So, playing cards have a ton of Ranks and Suits. There are a lot of them!
Like, a whole bunch. After 2 - 9, there's also a 10, and then a bunch of
letters for Jack, Queen, King, and Ace (J, Q, K, A).

But that's it!  I've updated the --rules with the order.

(Suits don't have an order, or a value. Weird! Maybe we should replace
them with banner ads and get some money out of that real estate?)

Let's get those added as well. I think we're almost done! Home Stretch!
""",

# 3
"""
Sooo, Q&A is already seeing some problems with bad Hand inputs...

For now, let's just say that if the Hand inputs aren't valid (e.g. are not
strings), we'll raise a ValueError, or something? And we probably shouldn't
accept any Ranks or Suits that aren't in the official list! (see --rules)

Make it so! (get it? Like that star wars thing?)
""",

# 4
"""
So, I just watched a poker match on YouTube, and those guys all had, like,
a BUNCH of cards in their Hands. (I don't think you're supposed to have more
than five cards at once? Not 100% sure on that, will confirm.)

Hands will now have cards separated by spaces, like "2H 4D 7C 2H 3S", but
that rule about the Highest Card winning works the same, just with more
cards. Also, I guess the cards won't be in any particular order?

So easy! We must be almost done... I am _crushing_ this!
""",

# 5
"""
Sooo... slight change of plans, but no big deal:

The UI folks decided that all Ranks should be a single character. And I was
like, no problem, they are! But I guess somebody forgot about "10".

They're saying we should use "T" instead. Just check the --rules and fix that
real quick, and then we can get back to crushing it! 
""",

# 6
"""
Full disclosure: It turns out there are different kinds of Hands? (Who knew?)

The first one is a "Pair", a Hand that has two cards of the same Rank - A Pair
always beats a Hand without a Pair, even if the cards are better, which is
confusing, but I guess that's Poker for you. (I guess the Suits still don't
matter? Why do cards even have them?) Anyway, I've added this to the --rules.

This Poker e-book keeps talking about "kickers" - sounds weird, so I'm
ignoring it for now.
""",

# 7
"""
Super duper minor thing: I guess two Hands can be "tied"? Like, if the highest
cards from both hands have the same rank? Or two hands have the same Pair?

When that happens, I guess just compare the next-highest cards in the Hands,
until you can break the tie. Problem solved! --rules updated!

(Unless all the cards in both hands are tied? Then it's a Draw... I guess,
return a 0 as the result in that case? BRB, need to clear Draws with Finance!
Half the award goes to each player - fractional money shouldn't be a big deal?)
""",

# 8
"""
Okay, believe it or not, a Hand could have two Pairs in it - But it says in
this Google I found that the two Pairs have to be of different ranks!?

(I hope this doesn't mean that four of the same rank is some other Poker
thing, though! Ugh. Who comes up with this stuff? Added to --rules.)

So a "Two Pair" beats any single Pair hand, which beats any single card.
(I guess you still have to figure that out when there's a tie, though.)
Crush it! I believe in you!
""",

# 9
"""
Ugh. So, there's more Hands. Like, a LOT of them. Poker is the worst.

The next one is "Three of a Kind" - Like a Pair, except with three of the
same card, instead of two. (and I guess you resolve ties the same way?) It
also beats Two Pairs, and Pairs, and all the other Hands so far.

This is now in --rules as well. Hopefully we're like, almost done with all
these Hands!
""",

# 10
"""
uuuuuugh Poker is making me write SO MANY EMAILS. So, there is also a
"Straight" Hand, which is super weird: It's when the ranks of all five cards
lead into the next one. Like 2, 3, 4, 5, 6, or 7, 8, 9, T, J, you get the idea.

(Have you been putting the cards in order by rank? That is probably important.)

Added to --rules. Crush it?
""",

# 11
"""
All right, so, "Flush" hands. Like, I want to flush this dumb Poker e-book
down the toilet! But Kindles are hard to find right now, so I better not.

A Flush is when all five cards have the same... Suit? And that beats all the
other previous Hands so far.

Ahh, crap. Have you been deleting the Suits? I think you need the suits. If
you decided they weren't important for some reason, well... Gotta be
detail-oriented, you know? Added to the --rules. Crush?
""",

# 12
"""
I can't get the stupid FULL HOUSE song out of my head now! But it blows my
mind, that the show was about Poker this whole time! TIL.

A Full House is when a Hand has a Three Of A Kind, AND a Pair in it, and
(go figure) it beats all the other hands. Poker is making me sad today.

(OH But the Three and the Pair have to be different suits?! I'm starting to
get a bad feeling about this...)
""",

# 13
"""
Ugh. Guess What? More Hands.

The Four Of a Kind is... yeah, you guessed it, just like a Pair or a Three of
a Kind, but, with four cards of the rank! And it beats all the previous Hands,
because of course it does.

Addded to --rules. You have my permission to crush stuff.
""",

# 14
"""
Okay, so, somebody missed something in all this Poker junk: I think we got the
Straight wrong? The Suits in a Straight CAN'T all be the same Suit... Because
there is a DIFFERENT HAND for that. (Who came up with all these Hands?) So,
first, let's make sure Straight hands are done right.

(Straight Hands? is that an Interpol track? I'll check.)

Fixed the --rules. Go forth and crush!
""",

# 15
"""
Right. So! There are Straights, and there are Flushes, and believe it or not,
a Straight Flush (true story, I heard that in a Clint Eastwood movie once.)

It means the cards have "sequential" ranks (that's a cool Computer Science
word for you), AND all the cards also have the same Suit. Like, if you got all
the Red cards with Hearts on them in a row... Well, not all of them, because you
can only have five cards, but you get the idea.

--rules Updated! Proceed with the crushing.
""",

# 16
"""
It's the Home Stretch, my dude! Bases are loaded, and it's nothing but net!
Let's touch down the conversion! (I kind of want to make a Sports Betting site
now - Are those hard to do? Let's talk tomorrow.)

Anyway, now we just need to implement the Royal Flush, which is the best kind
of Straight Flush, which is an Ace, King, Queen, Jack, and 10 of the same card.
In hindsight it's kind of obvious that the best Straight Flush would beat the
less good Straight Flushes, but I guess that's why it gets a cool name.

Nice job crushing it! (after you get Royal Flushes working)
""",

#17
"""
Hey, thanks for Crushing It, but we have a situation - People are, like,
cheating? The UI folks said something about "web requests" and "dev consoles"
- I guess it must be Hackers! They're always one step ahead. Anyway, Finance
is upset, and I told them you fixed it already, so while I don't think this
will be a big deal - Please do actually fix this. (Before you go home tonight)

People are like, making stuff up, and not "POSTing" the Hands they have - We
need to make sure they aren't copying cards (like, putting the same card in
their Hand twice, or that the same card isn't in both Hands) - If so, raise
a ValueError. That should pretty much take care of it?
""",

#18
"""
Nice work! You actually Crushed It! And you know what? I'm proud of us.

I'm about to meet with Finance and our Venture Capital peeps about how the
first day of Poker payouts have gone. Wish me luck!

Tomorrow: Sports Betting! Or fantasy football? Wait, can you place bets on
Fantasy Football?!? <img src="galaxy_brain.gif">

See you tomorrow!
""",

]