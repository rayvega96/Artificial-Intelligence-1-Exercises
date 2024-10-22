

class ResearchTree:

    def __init__(self):
        nodes = []
        # FIFO (First In - First Out)
        frontier = []





class ResearchNode:

    def __init__(self, state=None, parent=None, action=None, cost=None):
        self._state = state
        self._parent = parent
        self._action = action # defined as a list of  tuples (action, cost_of_action)
        self._cost = cost # total cost from start node to actual node

    @property
    def state(self):
        return self._state

    @property
    def parent(self):
        return self._parent

    @property
    def cost(self):
        return self._cost

    @state.setter
    def state(self, newstate):
        self._state = newstate

    @parent.setter
    def parent(self, newparent):
        self._parent = newparent

    @cost.setter
    def cost(self, newcost):
        self._cost = newcost


class CodaFIFO:

    def __init__(self, nodi=None):
        self._fifo = []
        if nodi is not None and type(nodi) == 'list': self._fifo = nodi

    def insert(self, node):
        self._fifo.insert(0, node)

    def pop(self):
        return self._fifo.pop()

    def print(self):
        print(self._fifo)


class CodaLIFO:

    def __init__(self, nodi=None):
        self._lifo = []
        if nodi is not None and type(nodi) == 'list': self._lifo = nodi

    def insert(self, node):
        self._lifo.insert(0, node)

    def pop(self):
        return self._lifo.pop(0)

    def print(self):
        print(self._lifo)
