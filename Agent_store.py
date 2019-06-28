import random as rnd

class Agent_store:

    def __init__(self):
        """
        type = [Groceries:Gr, Clothes:Cl, Restaurant:Rt, Cafe:Cf, Miscellaneous goods:Mg]
        storage: number of people store can accommodate
        instore[]: agent_id in store
        waiting[]: number of people waiting
        visitor[]: store visiting people each season
        """
        self.type = 'None'
        self.capacity = 0
        self.instore = []
        self.waiting = []
        self.visitor = []

def generate_agent_store(num_store):
    """
    generate store agents
    num_store is always 5
    """
    agents_store = [Agent_store() for store_id in range(num_store)]

    return agents_store

def init_agent_store(agents_store):
    """
    generate 5 kinds of store
    """
    for store_id, agent_store in enumerate(agents_store):
        if store_id == 0:
            agent_store.type = 'Gr'
            agent_store.capacity = 1000000
        elif store_id == 1:
            agent_store.type = 'Cl'
            agent_store.capacity = 1000000
        elif store_id == 2:
            agent_store.type = 'Rt'
            agent_store.capacity = 80
        elif store_id == 3:
            agent_store.type = 'Cf'
            agent_store.capacity = 60
        else:
            agent_store.type = 'Mg'
            agent_store.capacity = 1000000


def show_store_info(agents_store):
    """
    show agents_store infomation
    """

    for agent_store in agents_store:
        print(f'type:{agent_store.type}, capa:{agent_store.capacity}, instore:{agent_store.instore}, waiting:{agent_store.waiting}, visitor:{agent_store.visitor}')
