from operator import itemgetter

# to run test in command line do: 
# 1- to run default test: python -m doctest <filename>
    # python -m doctest yatzy.py
# 2- to run test with verbos: python -m doctest <filename> -v
    # python -m doctest yatzy.py -v
# 3- to run tests with pytest: python -m pytest --doctest-modules


def small_straight(dice):
    """Score the given roll in the 'small straight' yatzy category
    
    >>> small_straight([1, 2, 3, 4, 5])
    15
    >>> small_straight([1, 2, 3, 5, 5])
    0

    It also handle sets and unsorted lists

    >>> small_straight({1, 2, 3, 4, 5})
    15
    >>> small_straight([1, 2, 3, 5, 4])
    15
    """
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return sum(dice)
    return 0

def chance(dice):
    """Score the given role in the 'Chance' Yatzy category

    >>> chance([5,5,5,5,5])
    25
    >>> chance([1,2,3,4,5])
    15
    """
    return sum(dice)

def yatzy(dice):
    """Score the given roll in the 'Yatzy' category

    >>> yatzy([1,1,1,1,1])
    50
    >>> yatzy([4,4,4,4,4])
    50
    >>> yatzy([4,4,4,4,1])
    0
    """
    counts = dice_counts(dice)
    if 5 in counts.values():
        return 50
    return 0

def large_straight(dice):
    """Score the given roll in the 'Large Straight' Yatzy category.

    >>> large_straight([2,3,4,5,6])
    20
    >>> large_straight([1,2,3,4,5])
    0
    """
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return sum(dice)
    return 0

def pair(dice):
    """Score the given roll in the 'Pair' category

    >>> pair([1,2,3,4,4])
    8
    >>> pair([1,2,3,4,5])
    0

    It uses the highest scoring pair if there is more than one pair

    >>> pair([1,3,3,4,4])
    8
    >>> pair([3,3,3,4,4])
    8
    """

    counts = dice_counts(dice)
    for i in range(6, 0, -1):
        if counts[i] >= 2:
            return i * 2
    return 0

def three_of_a_kind(dice):
    """Score the given roll in the 'Three of a kind' category

    >>> three_of_a_kind([1,1,5,5,5])
    15
    >>> three_of_a_kind([1,5,5,5,5])
    15
    >>> three_of_a_kind([1,2,3,4,5])
    0
    """
    counts = dice_counts(dice)

    for i in range(1, 7):
        if counts[i] >= 3:
            return i * 3
    return 0

def four_of_a_kind(dice):
    """Score the given roll in the 'Four of a kind' category

    >>> four_of_a_kind([1,6,6,6,6])
    24
    >>> four_of_a_kind([1,1,6,6,6])
    0
    """
    counts = dice_counts(dice)

    for i in range(1, 7):
        if counts[i] >= 4:
            return i * 4
    return 0

def two_pairs(dice):
    """Score the given roll in the 'Two Pairs' category

    The score is calculated as the sum of all the dice
    belonging to the two pairs

    >>> two_pairs([1,1,3,4,4])
    10
    >>> two_pairs([2,2,3,4,4])
    12

    >>> two_pairs([2,2,3,4,5])
    0

    """
    counts = dice_counts(dice)

    pairs = [i for i in range(1, 7) if counts[i] >= 2]
    return sum(pairs) * 2 if len(pairs) == 2 else 0


def dice_counts(dice):
    """Make a dictionary of how many of each value are in the dice

    >>> dice_counts([1,2,2,3,3])
    {1: 1, 2: 2, 3: 2, 4: 0, 5: 0, 6: 0}

    This function only accepts collections containing integers:

    >>> dice_counts("12345")  #doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TypeError:  Can't convert 'int' object to str implicitly
    """

    return {x: dice.count(x) for x in range(1, 7)}


