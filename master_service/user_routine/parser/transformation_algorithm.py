from .parse_json import parse_json_routines
from ..components.base.routine import Routine, Phase, Component


def transform(routine):
    """
    transform method defines what to be done for each type of phase (condition, operations)
    from a routine which is given as a parameter
    it returns False when the conditions are not fullfield
    it returns True when the operations take place
    :param Routine routine:
    :return
    :rtype bool
    """
    for phase in routine.phases:
        if phase.type == "condition":  # type: Phase
            for id in phase.component_ids:
                for component in routine.components:  # type: Component
                    if component.id == id:
                        if not component.activate():
                            return False
        else:
            if phase.type == "operations":
                for id in phase.component_ids:
                    for component in routine.components:
                        if component.id == id:
                            component.execute()
    return True

def create_and_run_routine (my_json):
    """
    This method calls the parse_json_routine method which returns a routine
    This routine is given as a parameter to the call of the transform method which returns False
        if the condition is not fullfiled
    In this case appears an exception
    :param dict my_json:
    :return:
    """
    myRoutine = parse_json_routines(my_json)
    response = transform(myRoutine)

    if response == False:
        raise Exception(f"Condition {myRoutine.components['type']} is not active !")