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

from game import Directions


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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    (successor, action, stepCost)
    """

    # each node is a tuple of the state, the actions to get there from the start state, and its ancestor states.
    open_nodes = util.Stack()

    start_state = problem.getStartState()
    open_nodes.push((start_state, [], [start_state]))

    while not open_nodes.isEmpty():

        cur_node = open_nodes.pop()

        # print (cur_node)

        if problem.isGoalState(cur_node[0]):
            return cur_node[1]

        suc_nodes = problem.getSuccessors(cur_node[0])

        for sun in suc_nodes:
            if sun[0] not in cur_node[2]:
                sn_action_path = cur_node[1] + [sun[1]]
                ancestor_nodes = cur_node[2] + [sun[0]]
                open_nodes.push((sun[0], sn_action_path, ancestor_nodes))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""

    # each node is a tuple of the state, the actions to get there from the start state.

    open_nodes = util.Queue()
    open_nodes.push((problem.getStartState(), []))

    seen_nodes = set()

    while not open_nodes.isEmpty():

        cur_node = open_nodes.pop()

        if problem.isGoalState(cur_node[0]):
            return cur_node[1]

        if cur_node[0] not in seen_nodes:

            seen_nodes.add(cur_node[0])

            suc_nodes = problem.getSuccessors(cur_node[0])

            for sun in suc_nodes:

                sn_action_path = cur_node[1] + [sun[1]]
                open_nodes.push((sun[0], sn_action_path))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # each node is a tuple of the state, the actions to get there from the start state, and its action cost.

    open_nodes = util.PriorityQueue()
    open_nodes.push((problem.getStartState(), [], 1), 1)

    seen_nodes = set()

    while not open_nodes.isEmpty():

        cur_node = open_nodes.pop()

        if problem.isGoalState(cur_node[0]):
            return cur_node[1]

        if cur_node[0] not in seen_nodes:

            seen_nodes.add(cur_node[0])

            suc_nodes = problem.getSuccessors(cur_node[0])

            for sun in suc_nodes:

                sn_action_path = cur_node[1] + [sun[1]]
                action_cost = cur_node[2] + sun[2]

                open_nodes.push(
                    (sun[0], sn_action_path, action_cost), action_cost)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # each node is a tuple of the state, the actions to get there from the start state, and its action cost + h(n).

    start_state = problem.getStartState()

    open_nodes = util.PriorityQueue()
    # print(start_state)

    init_cost = heuristic(start_state, problem)

    open_nodes.push((start_state, [], init_cost), init_cost)

    seen_nodes = set()

    while not open_nodes.isEmpty():
        # print(open_nodes.count)

        cur_node = open_nodes.pop()

        if problem.isGoalState(cur_node[0]):
            return cur_node[1]

        if cur_node[0] not in seen_nodes:

            seen_nodes.add(cur_node[0])
            # print('cur_node')
            # print(cur_node)
            suc_nodes = problem.getSuccessors(cur_node[0])

            # print('suc_nodes')
            # print(suc_nodes)

            for sun in suc_nodes:
                # print('sun')
                # print(sun[0])

                sn_action_path = cur_node[1] + [sun[1]]
                action_cost = cur_node[2] + sun[2]
                hcost = heuristic(sun[0], problem)

                # print(hcost)

                open_nodes.push(
                    (sun[0], sn_action_path, action_cost), action_cost + hcost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
