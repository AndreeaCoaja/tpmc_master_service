class Phase:
    def __init__(self, id, type, component_ids):
        self.id = id
        self.type = type
        self.component_ids = component_ids


class Component:
    def __init__(self, id, type, category, description):
        self.id = id
        self.type = type
        self.category = category
        self.description = description

    def activate(self):
        raise NotImplementedError("Component.activate() method not implemented!")


class Routine:
    def __init__(self, name, phases, components):
        self.name = name
        self.phases = phases
        self.components = components
