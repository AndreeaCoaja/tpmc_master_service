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
