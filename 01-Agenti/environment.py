import random

# Environment class
class Environment:
    '''
    Class that defines an Environment. It provides the necessary
    methods to be analyzed by a vacuum.
    '''

    def __init__(self, load_env: dict):
        self.env = load_env
        self._vacuum_location = '0'


    @property
    def status(self) -> str:
        '''
        Return the status of the current position in the Environment.
        '''
        return self.env[self._vacuum_location]


    @property
    def _step(self):
        '''
        Let the environment evolve in the time.
        '''
        pass

    @property
    def vacuum_location(self) -> str:
        '''
        Return the current location of the agent in the Environment.
        '''
        return self._vacuum_location

    @vacuum_location.setter
    def vacuum_location(self, location: str):
        '''
        Set the new vacuum location in the Environment.
        '''
        self._vacuum_location = location



    def move_vacuum(self, direction: str):
        '''
        Move the vacuum in the direction give in input.
        '''
        # This environment is designed to be a 2x1 Matrix
        if direction == 'L' and self._vacuum_location == '1':
            self._vacuum_location = '0'

        elif direction == 'R' and self._vacuum_location == '0':
            self._vacuum_location = '1'
        else:
            print("Mantaining position.")


    def clean(self) -> None:
        '''
        Clean the current location in the environment.
        This method depends only on the position of the vacuum.
        '''
        self.env[self._vacuum_location] = 'Clean'

    def __str__(self) -> str:
        '''
        Return a synthetized string of the environment status.
        '''
        return str(self.env)



# Altri tipi di ambienti

class NonDeterministicEnvironment(Environment):
    def __init__(self):
        super().__init__()

    @Environment.vacuum_location.setter
    def vacuum_location(self, location : str):
        if random.random() > 0.9:
            self.vacuum_location = location

    def clean(self):
        if random.random() > 0.9:
            super().clean()

class DynamicEnvironment(Environment):
    def __init__(self):
        super().__init__()

    def step(self):
        if random.random() > 0.6:
            if random.random() > 0.5:
                self._world['A'] = 'Dirty'
            else:
                self._world['B'] = 'Dirty'
        super().step()

class NoisyEnvironment(Environment):
    def __init__(self):
        super().__init__()

    @property
    def status(self):
        if random.random() > 0.3:
            return self._world[self._vacuum_location]
        else:
            return 'Clean'

    @property
    def vacuum_location(self):
        if random.random() > 0.2:
            return self._vacuum_location
        else:
            return 'A' if random.random() > 0.5 else 'B'