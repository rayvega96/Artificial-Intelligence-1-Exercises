from environment import Environment
from vacuum import Vacuum
import time


class ModelVacuum(Vacuum):

    def __init__(self, env: Environment):
        self.environment = env
        self.model = { '0': None, '1': None}

    def perceive(self) -> str:
        return self.environment.status

    def getLocation(self) -> str:
        return self.environment.vacuum_location

    def applyAction(self, action: str) -> None:
        if action == 'C': self.environment.clean()
        if action == 'L': self.environment.move_vacuum('L')
        if action == 'R': self.environment.move_vacuum('R')


    def agentFunction(self) -> None:

        while True:

            time.sleep(1)

            location = self.getLocation()
            perception = self.perceive()

            print("Current Location:", location)
            print("Current Status:", perception)

            if self.model == {'0': 'Clean', '1': 'Clean'}:
                print("Environment cleaned. Quitting...")
                break

            if perception == 'Dirty':
                print("Cleaning...")
                time.sleep(0.5)
                self.applyAction('C')
                perception = self.perceive()
                self.model[location] = perception
            else:
                print("Location Clean. Changing Location...")
                time.sleep(0.5)
                if location == '0': self.applyAction('R')
                if location == '1': self.applyAction('L')
