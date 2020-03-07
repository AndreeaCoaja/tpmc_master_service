class Phase:
    def __init__(self, id, type, componentIds):
        self.id = id
        self.type = type
        self.componentIds = componentIds

class Component:
    def __init__(self, Id, type, category, description):
        self.Id = Id
        self.type = type
        self.category = category
        self.description = description


class Routine:
    def __init__(self, name, phases, components):
        self.name = name
        self.phases = phases
        self.components = components

