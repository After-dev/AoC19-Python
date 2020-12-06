import numpy as np



def new_stack(cards):
    cards.reverse()


def cut(cards, N):
    return cards[N:]+cards[:N]


def increment(cards, N):
    new_cards = cards[:]

    for i in range(len(cards)):
        new_cards[i*N % len(cards)] = cards[i]

    return new_cards


def shuffle_cards(cards, shuffles):
    for shuffle in shuffles:
        [cmd, N] = shuffle.rsplit(" ", 1)
        if cmd == 'deal into new':
            new_stack(cards)
        elif cmd == 'cut':
            cards = cut(cards, int(N))
        elif cmd == 'deal with increment':
            cards = increment(cards, int(N))

    return cards



# Examples
print("Result for examples:")
deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffles = [
    'deal with increment 7',
    'deal into new stack',
    'deal into new stack'
]
print(shuffle_cards(deck, shuffles))

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffles = [
    'cut 6',
    'deal with increment 7',
    'deal into new stack'
]
print(shuffle_cards(deck, shuffles))

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffles = [
    'deal with increment 7',
    'deal with increment 9',
    'cut -2'
]
print(shuffle_cards(deck, shuffles))

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffles = [
    'deal into new stack',
    'cut -2',
    'deal with increment 7',
    'cut 8',
    'cut -4',
    'deal with increment 7',
    'cut 3',
    'deal with increment 9',
    'deal with increment 3',
    'cut -1'
]
print(shuffle_cards(deck, shuffles))





# My puzzle
print("Result for my puzzle:")
# Load data
file = open('./input.data', 'r')
shuffles = [i[:-1] for i in file.readlines()]

# Calculate the solution
deck = range(0, 10007)
solution = shuffle_cards(deck, shuffles)

# Print the solution
print(solution.index(2019))
