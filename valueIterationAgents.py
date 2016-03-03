# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discountRate = 0.9, iters = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discountRate = discountRate
    self.iters = iters
    self.values = util.Counter() # A Counter is a dict with default 0
    self.policy = util.Counter()
    self.qVal = util.Counter()
    self.ViPlus = util.Counter()

    """Description:
    This was the most fun out of this project as it required a bit of mind bending
    to work through. I first loop through each state and populate a list with all
    transistionStates/probs with their corresponding action. Then, looping through
    those transistionStates, I append a list, curSum, with the summation. Taking the max
    of those returns the correct value along with the optimal action.
    """
    """ YOUR CODE HERE """


    """----------------------------------------------------------------------------"""

    while self.iters > 0:
        temp = util.Counter()
        tempQ = util.Counter()
        tempPol = util.Counter()
        for s in self.mdp.getStates():
            if not self.mdp.isTerminal(s):
                T = [(self.mdp.getTransitionStatesAndProbs(s, a), a) for a in self.mdp.getPossibleActions(s)]
                curSum = []
                for t, a in T:
                    testing = [prob*(self.mdp.getReward(s, a, tState) + (self.discountRate*self.getValue(tState))) for tState, prob in t]
                    curSum.append((sum(testing), a))
                    self.qVal[s, a] = sum(testing)
                theMax = max(curSum)
                if theMax[0] == 0.0:
                    theMax = (0.0 , 'north')
                #updates for v_i+1
                temp[s] = theMax[0]
                tempPol[s] = theMax[1]

        self.policy = tempPol
        self.values = temp
        self.iters -= 1
    """ END CODE """

  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    return self.values[state]
    """ END CODE """

  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    return self.qVal[state, action]
    """ END CODE """

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    if state == "TERMINAL_STATE":
        self.policy[state] = None
    return self.policy[state]
    """ END CODE """

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
