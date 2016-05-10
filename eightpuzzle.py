# Danny Dutton
# eightpuzzle.py
# This python script will take in the initial and goal states of an eight
# puzzle and then find the steps needed to get to the goal state.

import search
import sys

# Overloaded methods for EightPuzzle
class EightPuzzle(search.Problem):
	def __init__(self, initial, goal, method):
		""" Override init() of Problem class """
		super(EightPuzzle, self).__init__(initial, goal)
		self.method = method
		self.numnode = 0
	def actions(self, state):
		""" Return all possible actions that could
			occur. These are the tiles that can be
			swapped with the zero tile """
		zero = state.index(0)
		if zero == 0:
			return [state[1], state[3]]
		elif zero == 1:
			return [state[0], state[2], state[4]]
		elif zero == 2:
			return [state[1], state[5]]
		elif zero == 3:
			return [state[0], state[4], state[6]]
		elif zero == 4:
			return [state[1], state[3], state[5], state[7]]
		elif zero == 5:
			return [state[2], state[4], state[8]]
		elif zero == 6:
			return [state[3], state[7]]
		elif zero == 7:
			return [state[4], state[6], state[8]]
		elif zero == 8:
			return [state[5], state[7]]
		else:
			return []

	def result(self, state, action):
		""" Return the state of the board after	the action tile is swapped with
			the zero tile. Kill the search if there more than 9! states.
			Note: This can take a long time to reach."""
		statelist = list(state)
		zero, tile = statelist.index(0), statelist.index(action)
		statelist[zero], statelist[tile] = statelist[tile], statelist[zero]
		self.numnode += 1
		if self.numnode >= 362880:
			print("None")
			sys.exit()
		return tuple(statelist)

	def value(self, state):
		""" Cityblock: Sum up the x/y distance between tile state and goal.
			Misplaced: Sum the number of tiles not in the right spot."""
		current = state.state
		if self.method == "cityblock":
			val = 0
			for tile in current:
				x = current.index(tile) % 3
				xgoal = tile % 3
				y = current.index(tile) // 3
				ygoal = tile // 3
				val += abs(x - xgoal) + abs(y - ygoal)
		elif self.method == "misplaced":
			val = 0
			for tile in current:
				if tile != current.index(tile):
					val += 1
		return val


def solve(initial, goal, method):
	""" Setup a new EightPuzzle object and then get the solution to it. """
	x = EightPuzzle(tuple(initial), tuple(goal), method)
	return search.astar_search(x, x.value).solution()


if __name__ == "__main__":
	""" Test cases """
	initial = 	[3, 1, 2, 6, 4, 5, 0, 7, 8]
	goal = 		[0, 1, 2, 3, 4, 5, 6, 7, 8]
	print(solve(initial, goal, 'cityblock'))
	print(solve(initial, goal, 'misplaced'))
