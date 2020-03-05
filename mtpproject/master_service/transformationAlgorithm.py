#this method defines what to be done for each type of phase (condition, operations) from a routine which is given as a parameter

def transform(routine):
    for phase in routine.phases:
        if phase.type == "operations":
            for id in phase.ComponentsId:
                for component in routine.components:
                    if component.id == id:
                        component.execute()
        else:
            if phase.type == "condition":
                for id in phase.ComponentsId:
                    for component in routine.components:
                        if component.id == id:
                            if not component.activate():
                                break
