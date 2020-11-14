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

