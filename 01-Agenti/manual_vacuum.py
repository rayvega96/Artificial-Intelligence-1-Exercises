from vacuum import Vacuum
from environment import Environment
from os import system

class ManualVacuum(Vacuum):
    '''
    This model is explicitly directed by the user.

    The AgentFunction is a loop that allows the user to
    choose the action to do.
    '''
    def __init__(self, env: Environment):
        self.environment = env
        self.current_location = self.getLocation()


    def perceive(self) -> str:
        return self.environment.status

    def getLocation(self) -> str:
        return self.environment.vacuum_location


    def applyAction(self, action: str) -> None:

        if action == 'P':
            print(f"Location Status: {self.perceive()}"),

        elif action == 'C':
            self.environment.clean()

        elif action == 'L' or action == 'R':
            self.environment.move_vacuum(action)


    def agentFunction(self) -> None:
        while(True):
            print(f'Current location: {self.getLocation()}')
            print("Available Commands:")
            print(" - 'P': Perceive\n - 'C': Clean\n - 'L': Move Left\n - 'R': Move Right\n - 'Q': Quit")
            self.action = input("Command: ")
            if not self.action == 'Q':
                system('clear')
                self.applyAction(self.action)
            else:
                print("Quitting...")
                break