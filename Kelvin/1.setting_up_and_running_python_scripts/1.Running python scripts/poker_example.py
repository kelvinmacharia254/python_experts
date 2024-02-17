# python has a dedicated builtin modules for tasks involving iterations
# This module saves, implementing some algos from first principle.
# itertools comes with functions such as permutations, combinations, product etal

import itertools

ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']  # generate deck deck ranks for A t Q ie. 1 to 13
ranks = [str(rank) for rank in ranks]  # make all of them strings

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

deck = [card for card in itertools.product(ranks, suits)]  # a deck is made of product of ranks and suits

# Print all cards
for (index, card) in enumerate(deck):
    print(1 + index, card)
