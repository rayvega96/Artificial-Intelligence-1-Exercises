from environment import Environment
from vacuum import Vacuum
import time


class ReflexVacuum(Vacuum):
    '''
    This Implementation automatically choose the action to do
    based on current cell status.
    '''

    def __init__(self, env: Environment):
        self.environment = env

    def perceive(self) -> str:
        return self.environment.status

    def getLocation(self) -> str:
        return self.environment.vacuum_location


    def applyAction(self, action: str) -> None:

        if action == 'C':
            self.environment.clean()
        elif action == 'M':
            if self.getLocation() == '0':
                self.environment.move_vacuum('R')
            elif self.getLocation() == '1':
                self.environment.move_vacuum('L')
            else:
                print("Staying still")



    def agentFunction(self) -> None:
        # This agent function will occour infinite loop.
        while True:
            current_location = self.getLocation()
            print(f"\nCurrent Location: {current_location}")
            current_status = self.perceive()
            print(f"Location Status: {current_status}")

            if current_status == 'Dirty':
                print("Location Dirty. Cleaning...")
                time.sleep(0.500)
                self.applyAction('C') # Clean

            else:
                print("Location Clean. Moving...")
                time.sleep(0.500)
                self.applyAction('M') # Move

            print(f"\n{self.environment.__str__()}")

            time.sleep(2)