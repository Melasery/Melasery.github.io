# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """
    # DFS strategy + fringe is a LIFO stack
    frontier = util.Stack()
    # Each entry: (state, actions_taken_to_get_here)
    start = problem.getStartState()
    frontier.push((start, []))
    # remember which STATES we've already expanded
    visited = set()
    while not frontier.isEmpty():
        state, path = frontier.pop()
        # If this state is a goal, we’re done and return the action sequence
        if problem.isGoalState(state):
            return path
        if state in visited:
            # Already expanded this state before
            continue
        visited.add(state)
        # Expand: get successors = [(succ_state, action, step_cost),...]
        for succ, action, _ in problem.getSuccessors(state):
            if succ not in visited:
                # Push the new plan
                frontier.push((succ, path + [action]))
    return [] # If no solution is found 


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()
    start = problem.getStartState()
    frontier.push((start, []))  # store (state, path)
    visited = set()  # keep track of expanded states

    while not frontier.isEmpty():
        state,path = frontier.pop()
        # if we already visited this state, skip it
        if state in visited:
            continue
        visited.add(state)

        # check if we reached the goal
        if problem.isGoalState(state):
            return path
        # expand successors (go through all neighbors)
        for next_state, action, cost in problem.getSuccessors(state):
            if next_state not in visited:
                # build new path to successor
                new_path = path + [action]
                frontier.push((next_state, new_path))
    
    return []  # if no solution



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    frontier = util.PriorityQueue()
    start = problem.getStartState()
    frontier.push((start, [], 0), 0)
    # best_g[s] = best (lowest) cost to reach state s that we've seen so far
    best_g = {start: 0}
    closed = set()
    while not frontier.isEmpty():
        state, path, g = frontier.pop()
        # If we've already finalized this state with a lower cost, skip
        if state in closed:
            continue
        closed.add(state)
        # Goal test: first time we pop goal is guaranteed least-cost
        if problem.isGoalState(state):
            return path
        # Expand successors
        for succ, action, stepCost in problem.getSuccessors(state):
            new_g = g + stepCost
            # Only push if this path improves the best known cost to succ
            if succ not in best_g or new_g < best_g[succ]:
                best_g[succ] = new_g
                frontier.push((succ, path + [action], new_g), new_g)
    # No solution found
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""

    start = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push((start, [], 0), heuristic(start, problem))  # (state, path, g), priority=f

    # Best known g-costs to states we've discovered so far
    best_g = {start: 0}
    # Once we pop a state, we finalize it at its minimal g 
    closed = set()
    while not frontier.isEmpty():
        state, path, g = frontier.pop()
        if state in closed:
            continue
        closed.add(state)

        if problem.isGoalState(state):
            return path
        # expand
        for succ, action, stepCost in problem.getSuccessors(state):
            new_g = g + stepCost
            # only improve if this path is better
            if succ not in best_g or new_g < best_g[succ]:
                best_g[succ] = new_g
                f = new_g + heuristic(succ, problem)
                frontier.push((succ, path + [action], new_g), f)
    # no solution found 
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
