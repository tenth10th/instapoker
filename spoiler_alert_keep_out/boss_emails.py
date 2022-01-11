boss_emails = [

# 0
"""
For now, let's just get the basic API working:
We'll want to be able to accept two poker hands, as strings,
and return a scoring result as an Integer - How about:

 * 1 if the first Hand wins

 * 2 if the second Hand wins

I can't imagine us ever needing to change this API, so let's get it locked in first!

Don't worry about the rules yet, just submit when you have the API in the right shape.
""",

# 1
"""
I've added the current list of Rank and Suit symbols to the --rules.
There are a lot of them! Like, a whole bunch.

The UI team has decided to represent Poker Hands as pairs of Ranks and Suits,
in that order: So "2H" for a Two of Hearts, "KD" for King of Diamonds, etc.

The base rule of poker scoring sounds pretty simple:

  * The hand with the highest-ranked card wins! (I guess Suits don't matter?)

For now, let's assume Hands of a single card only. Super easy!

Let's do it! (And don't forget to submit it when you're finished.)
""",

# 2
"""
Sooo, we're already seeing some problems with bad Hand inputs...

For now, let's just say that if the Hand inputs aren't valid
(e.g. are not strings), we'll raise a ValueError, or something?

Oh, and we probably shouldn't accept any Ranks or Suits that
aren't in the official list...

Make it so! (get it? Like that star wars thing?)
""",

# 3
"""
Okay! Everything is going great, so now we just have to deal
with multiple-card hands. (I don't think you're supposed to have
more than five cards at once? Not 100% sure about that.)

The pairs of Rank and Suit will be separated by spaces, but
that rule about the Highest Card winning should still work,
as long as you apply it across all the cards in the hand.

So easy! We must be almost done... I am _crushing_ this!
""",

# 4
"""
Sooo... slight change of plans, but no big deal:

The UI folks decided that all Ranks should be represented by a
single character. And I was like, no problem, they are! But I
guess somebody forgot about "10".

They're saying we should use "T" instead - Just fix that real
quick, and then we can get back to _crushing_it_!
""",

# 5
"""
So: full disclosure, I thought we were done scoring Hands, but
it turns out there are a couple of different kinds of them. Who knew?

The first one is called a "Pair", which is a Hand that
has two cards of the same Rank - I've added this to the --rules.
A Hand with a Pair always beats a Hand without one, which is confusing.

(I guess Suit still doesn't matter? Why do cards even have them?)

This Poker book also keeps talking about "kickers", but that sounds
lame, and I'm ignoring it for now.
""",

# 6
"""
Super duper minor thing that somebody forgot to tell me about
when I started this Online Poker company: I guess two Hands can
be "tied"? Like, if the highest cards from both hands have the same rank?

When that happens, I guess just compare the next-highest card in
each Hand, until you can break the tie. Problem solved!

(Unless all the cards in both hands are tied? Then it's a Draw...
Crap. I guess, return a 0 as the result in that case?)

I just need to clear the concept of Draws with Finance - I guess
you're supposed to, like, split the award evenly in half? I'm sure
that'll be simple, though - how could fractional money go wrong?
""",

# 7
"""
Okay, believe it or not, you can have Two Pairs in a Hand, also -
That's two pairs of two of the same card. But it says in this
Google I found that the two pairs have to be of different ranks!

(I hope this doesn't mean that four of the same rank is some
other Poker thing, though! Ugh. Who comes up with this stuff?)

Two Pairs beats any single Pair, which beats any single card.
(I guess you still have to figure that out when there's a tie.)
Crush it! I believe in you!

Anyway, I added this to the --rules.
""",

# 8
"""
Ugh. So, there's more Hands. Like, a LOT of them. Poker sucks.

The next one is a Three of a Kind - It's like a Pair, except
that there are three cards, instead of two. (and I guess you
resolve ties the same way). It also beats Two Pairs and Pairs
and all the other Hands so far. I guess they're all like that?

(Also, Ties and Draws and stuff - I guess you have to go
through all of these until one hand wins, or you draw.)

This is now in --rules as well. Hopefully we're like, almost
done with all these Hands.
""",

# 9
"""
uuuuuugh Poker is making me write SO MANY EMAILS. So, there
is also a "Straight" Hand, which are super weird: It's when
the ranks of all five cards lead into the next one.

(Um, if you put them in order. Have you been putting them
into order? It probably matters. By Rank, I mean.)

Added to --rules. Crush it?
""",

# 10
"""
All right, so, "Flush" hands. Like, I want to flush this dumb
Poker audiobook down the toilet. Anyway, I guess this is like,
what they're talking about when they say "Royal Flush" on the
Poker channel?

A Flush is when all five cards have the same... Suit? And that
(as usual) beats all the other previous Hands so far.

Ahh, crap. Have you been deleting the Suits? I think you need
the suits. If you decided they weren't important for some
reason, well... Gotta be detail-oriented, you know?

Added to the --rules. Crush stuff?
""",

# 11
"""
I can't get the stupid FULL HOUSE song out of my head now!
But it blows my mind, that the show was about Poker this
whole time! No wonder people like it so much!

The show, I mean, not Poker. Poker is making me mad today.

A Full House is when a Hand has a Three Of A Kind, and a
Pair in it, and it beats all the previous hands.

(But the Three and the Pair have to be different suits?
I'm getting a bad feeling about this...)
""",

# 12
"""
Ugh. Guess What? More Hands.

The Four Of a Kind is... yeah, you guessed it, just like
a Pair or a Three of a Kind, but, there's four of the rank!
And it beats all the previous Hands.

Addded to --rules. You have my permission to crush stuff.
""",

# 13
"""
Okay, so, I think maybe the old Boss-Person kinda missed
something in all this crazy Poker talk...

I think we got the Straight wrong originally - The Suits
in a Straight CAN'T all be the same Suit... Because there
is a different Hand for that. (Who came up with all these
dumb Hands?) So, first, let's make sure Straight hands are
done right.

(Straight Hands? is that an Interpol track? I'll check.)

Fixed the --rules. Go forth and crush!
""",

# 14
"""
Right. So, there are Straights, and there are Flushes, and
believe it or not, a Straight Flush (true story, I heard
them say that in a Clint Eastwood movie once).

It means the cards have "sequential" ranks (that's a cool
Computer Science word for you), AND all the cards also
have the same Suit. Like, if you got all the Red cards
with Hearts on them in a row. Well, not all of them,
because you can only have five cards, but you get the idea.

--rules Updated! Proceed with the crushing.
""",

# 15
"""
It's the Home Stretch, my dude! Bases are loaded,
and it's nothing but net! Let's touch down the conversion!

(I kind of want to make a Sports Betting site now - Are those
hard to do? Let's talk tomorrow.)

Anyway, now we just need to implement the Royal Flush,
which is the best kind of Straight Flush, which is the
Ace, King, Queen, Jack, and 10 of the same card.

I guess in hindsight it's kind of obvious that the best
Straight Flush would beat the less good Straight Flushes,
but I guess that's why they gave it a cool name.

Nice job crushing it! (after you get Royal Flushes working)
""",

#16
"""
Hey, um, so, thanks for Crushing It, but we have a situation...

The poker rules seem to be working well, but people are, like,
cheating? The UI folks are saying something about "web requests"
and "browser dev tools" - I guess it's Hackers! They're always
one step ahead.

Anyway, Finance is upset, and I told them you fixed it, and
I don't think this is going to be a big deal - But, could you,
like, also actually fix this? Before you go home tonight.

I guess the problem is that people are like, not POSTing the
Hands they actually have, and making stuff up - So I
think as long as you make sure they aren't copying cards
(like, putting the same card in their Hand twice, or that
the same card isn't in both Hands) and raise a ValueError,
that should pretty much take care of it?

I'm about to meet with the Venture Capital peeps about how
the first day of Poker payouts have gone. Wish me luck!

Tomorrow: Sports Betting! Or fantasy football? Wait, can you
place bets on Fantasy Football?!? <img src="galaxy_brain.gif">
"""
]