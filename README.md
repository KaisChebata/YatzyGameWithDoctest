Yatzy Game
==========
You can use this code to play Yatzy. 

A whole game with all 14 categories is quite long. 

Here you can see how to play a full game played with only four categories.

```
>>> from yatzy_game import *
>>> play_yatzy_with_categories([pair, two_pairs, chance])
Your roll is:
[1, 2, 5, 6, 6]
Which dice will you re-roll?
1, 2, 5                   # chose to re-roll all the dice that aren't 6
[3, 4, 4, 6, 6]
Which dice will you re-roll?
3                         # chose to re-roll all the dice that aren't 4,and 6
[4, 4, 5, 6, 6]
Hint: available categories and scores:
[(25, 'chance'), (20, 'two_pairs'), (12, 'pair')] 
Which category would you like to score this roll in?
chance                    # chose one of categories score
Your score is now 25
Your roll is:
[3, 3, 3, 5, 5]
Which dice will you re-roll?
5
[3, 3, 3, 4, 5]
Which dice will you re-roll?
5
[2, 3, 3, 3, 4]
Hint: available categories and scores:
[(6, 'pair'), (0, 'two_pairs')]
Which category would you like to score this roll in?
pair
Your score is now 31
Your roll is:
[1, 1, 5, 6, 6]
Which dice will you re-roll?
1, 5
[1, 1, 4, 6, 6]
Which dice will you re-roll?
4
[1, 1, 4, 6, 6]
Hint: available categories and scores:
[(14, 'two_pairs')]
Which category would you like to score this roll in?
two_pairs
Your score is now 45
chance:       25
two_pairs:       14
pair:       6

Final Score: 45
```