from operator import itemgetter

def small_straight(dice):
    """Score the given roll in the 'small straight' yatzy category
    
    >>> small_straight([1, 2, 3, 4, 5])
    15
    >>> small_straight([1, 2, 3, 5, 5])
    0

    It also handle sets, or unsorted lists

    >>> small_straight({1, 2, 3, 4, 5})
    15
    >>> small_straight([1, 2, 3, 5, 4])
    15
    """
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return sum(dice)
    return 0

# to run test in command line do: 
# 1- to run default test: python -m doctest <filename>
    # python -m doctest yatzy.py
# 2- to run test with verbos: python -m doctest <filename> -v
    # python -m doctest yatzy.py -v
# 3- to run tests with pytest: python -m pytest --doctest-modules