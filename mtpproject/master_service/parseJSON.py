import json
from ConditionClass import Condition
from OperationClass import Operation
from RoutineClass import Routine, Components, Phase

# with open("test.json") as f:
#     my_json = json.load(f)


def parse_json_routines(my_json):
    routine = Routine(my_json["Name"], [],[])

    for component in my_json["components"]:
        if component["type"] == "condition":
            comp = Condition(component["id"], component["description"])
            routine.components.append(comp)

        if component["type"] == "operation":
            comp = Operation(component["id"], component["category"], component["description"])
            routine.components.append(comp)

    for phase in my_json["phases"]:
        ph = Phase(phase["id"], phase["type"], phase["componentIds"])
        routine.phases.append(ph)
