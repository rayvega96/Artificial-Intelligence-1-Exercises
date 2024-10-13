from environment import Environment
from vacuum import Vacuum
import random
import time


class BlindVacuum(Vacuum):

    def __init__(self, env: Environment):
        self.environment = env

    def perceive(self) -> str:
        # The agent is blind, cannot perceive
        return ''

    def getLocation(self) -> str:
        # The agent is blind, cannot get his location
        return ''

    def applyAction(self, action: str) -> None:
        if action == 'C': print("Cleaning");     self.environment.clean()
        if action == 'L': print("Moving Left");  self.environment.move_vacuum('L')
        if action == 'R': print("Moving Right"); self.environment.move_vacuum('R')

    def agentFunction(self) -> None:
        '''
        BlindVacuum cannot perceive his position or location status.

        Thus it always execute his main action and then randomly chooses where to move.
        '''
        while True:
            self.applyAction('C') # Always clean first
            time.sleep(0.5)
            self.applyAction('R') if random.randint(1, 10) >= 5 else self.applyAction('L')
            time.sleep(1)