# eightpuzzle
Determine steps needed to solve an eight puzzle based on initial and goal states. It can use two different methods for solving. Cityblock determines the heuristic score of a state based on how many blocks away (in the cardinal directions) every tile is from their spot in the goal state. Misplaced determines the score by counting how many tiles aren't in the right spot. Both have merits and may produce a different set of steps.

## Usage
Using python2, 0 represents the empty square:
```python
import eightpuzzle
initial =       [3, 1, 2, 6, 4, 5, 0, 7, 8]
goal =          [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(eightpuzzle.solve(initial, goal, 'cityblock'))
print(eightpuzzle.solve(initial, goal, 'misplaced'))
```
Output:
```python
[6, 3]
[6, 3]
```
These are the tiles that need to be moved into the empty spot: move tile 6 down one then move tile 3 down one.
