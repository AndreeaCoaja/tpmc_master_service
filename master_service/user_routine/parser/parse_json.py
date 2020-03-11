from ..components.base.routine import Routine, Phase
from ..components.finance.condition import FinanceCondition
from ..components.messaging.operation import MessagingOperation


def parse_json_routines(my_json):
    routine = Routine(my_json["Name"], [], [])

    for component in my_json["components"]:
        if component["type"] == "condition":
            condition = create_condition(component)
            routine.components.append(condition)

        if component["type"] == "operation":
            operation = create_operation(component)
            routine.components.append(operation)

    for phase in my_json["phases"]:
        ph = Phase(phase["id"], phase["type"], phase["component_ids"])
        routine.phases.append(ph)


def create_operation(operation):
    """
    :param dict operation:
    :return:
    """
    if operation["category"] == "messaging":
        return MessagingOperation(
            operation["id"],
            operation["recipient_email_addres"],
            operation["subject"],
            operation["text"]
        )
    raise Exception(f"Unrecognised operation category: {operation['category']}!")


def create_condition(condition):
    """
    :param dict condition:
    :return:
    """
    if condition["category"] == "finance":
        return FinanceCondition(
            condition["id"],
            condition["company_name"],
            condition["stock_price"],
            condition["relate"]
        )
    raise Exception(f"Unrecognised condition category: {condition['category']}!")
