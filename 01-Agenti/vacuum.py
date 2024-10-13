from environment import Environment

class Vacuum:

    def __init__(self, env: Environment):
        pass

    def perceive(self) -> str:
        '''
        Return the condition of the current location in the Environment.
        '''
        pass

    def getLocation(self) -> str:
        '''
        Return the Vacuum's location relative to the Environment.
        '''
        pass

    def applyAction(self, action: str) -> None:
        '''
        Applies the action taken from the agent_function to the current location
        in the environment.
        '''
        pass

    def agentFunction(self) -> None:
        pass
