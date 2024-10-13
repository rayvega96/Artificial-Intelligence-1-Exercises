from environment import Environment
from manual_vacuum import ManualVacuum
from table_vacuum import TableVacuum
from reflex_vacuum import ReflexVacuum
from blind_vacuum import BlindVacuum
from model_vacuum import ModelVacuum

env1_dict = {
    '0': 'Dirty',
    '1': 'Dirty',
}


manual_vacuum = ManualVacuum(env=Environment(env1_dict))
table_vacuum = TableVacuum(env=Environment(env1_dict))
reflex_vacuum = ReflexVacuum(env=Environment(env1_dict))
blind_vacuum = BlindVacuum(env=Environment(env1_dict))
model_vacuum = ModelVacuum(env=Environment(env1_dict))

while True:
    print("0 - Manual Vacuum")
    print("1 - Table Vacuum")
    print("2 - Reflex Vacuum")
    print("3 - Blind Vacuum")
    print("4 - Model Vacuum")
    print("9 - Quit")
    choice = input('\nChoice: ')

    if choice == '0': manual_vacuum.agentFunction()
    if choice == '1': table_vacuum.agentFunction()
    if choice == '2': reflex_vacuum.agentFunction()
    if choice == '3': blind_vacuum.agentFunction()
    if choice == '4': model_vacuum.agentFunction()
    if choice == '9': break