from environment import Environment
from vacuum import Vacuum
import time


class TableVacuum(Vacuum):
    '''
    This Implementation automatically choose the action to do
    from a State's Table manually written.

    This is possible since all the possible states are so few that
    can be manually managed.
    '''

    def __init__(self, env: Environment):
        self.environment = env
        self.table = {
            (('0', 'Clean'),): 'R',
            (('0', 'Dirty'),): 'C',
            (('1', 'Clean'),): 'L',
            (('1', 'Dirty'),): 'C',
            (('0', 'Dirty'), ('0', 'Clean'),): 'R',
            (('0', 'Clean'), ('1', 'Dirty'),): 'C',
            (('1', 'Clean'), ('0', 'Dirty'),): 'C',
            (('1', 'Dirty'), ('1', 'Clean'),): 'L',
            (('0', 'Dirty'), ('0', 'Clean'), ('1', 'Dirty'),): 'C',
            (('1', 'Dirty'), ('1', 'Clean'), ('0', 'Dirty'),): 'C'
        }
        self.perception_sequence = []

    def perceive(self) -> str:
        return self.environment.status

    def getLocation(self) -> str:
        return self.environment.vacuum_location


    def applyAction(self, action: str) -> None:

        if action == 'L': self.environment.move_vacuum('L')
        elif action == 'R': self.environment.move_vacuum('R')
        elif action == 'C': self.environment.clean()

    def agentFunction(self) -> None:
        '''
        Must percept environment status and add it to his perception_sequence,
        then it must find the perception sequence in the table and apply its
        action. If the perception sequence is not in the table, the agent stops
        (ideally leaving the environment clean).
        '''
        while True:
            perception = (self.getLocation(), self.perceive())
            self.perception_sequence.append(perception)

            sequence = tuple(self.perception_sequence)

            print(f"Actual Perception: {perception}")

            if sequence in self.table.keys():
                action = self.table[sequence]
                print(f"Executing Action: {action}")
                self.applyAction(action)

            else:
                print("No action found.")
                print("Quitting.")
                break

            time.sleep(1)