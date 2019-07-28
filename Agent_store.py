import random as rnd
import numpy as np
import pprint

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
        self.floor = 0
        self.Es_distance = 0


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
            agent_store.floor = 0
            agent_store.Es_distance = 3
        elif store_id == 1:
            agent_store.type = 'Cl'
            agent_store.capacity = 1000000
            agent_store.floor = 3
            agent_store.Es_distance = 5
        elif store_id == 2:
            agent_store.type = 'Rt'
            agent_store.capacity = 60
            agent_store.floor = 4
            agent_store.Es_distance = 5
        elif store_id == 3:
            agent_store.type = 'Cf'
            agent_store.capacity = 30
            agent_store.floor = 2
            agent_store.Es_distance = 1
        else:
            agent_store.type = 'Mg'
            agent_store.capacity = 1000000
            agent_store.floor = 1
            agent_store.Es_distance = 6

def service_time(type):
    """
    determine service time using np.random.normal() for each store
    """
    if type == 'Gr':
        time = np.random.normal(20,2)
        time = 1 if time < 20 else 2
    elif type == 'Cl':
        time = np.random.normal(30,3)
        time = 2 if time < 30 else 3
    elif type == 'Rt':
        time = np.random.normal(60,3)
        time = 5 if time < 60 else 6
    elif type == 'Cf':
        if rnd.random() < 0.5:
            time = np.random.normal(30,2)
            time = 2 if time < 30 else 3
        else:
            time = np.random.normal(60,2)
            time = 5 if time < 60 else 6
    elif type == 'Mg':
        time = np.random.normal(20,2)
        time = 1 if time < 20 else 2

    return time

def store_map(agents_store):

    map = [[['00' for i in range(10)] for j in range(5)] for k in  range(5)]

    map[0][2][2] = 'Es'
    map[1][2][7] = 'Es'
    map[2][2][2] = 'Es'
    map[3][2][7] = 'Es'
    map[4][2][2] = 'Es'

    map[3][2][9] = 'Ex'
    map[3][3][9] = 'Ex'
    map[3][4][9] = 'Ex'

    for agent_store in agents_store:
        if agent_store.floor == 0:
            for i in range(5):
                for j in range(5):
                    map[4][i][5+j] = agent_store.type
        elif agent_store.floor == 1:
            for i in range(2):
                for j in range(3):
                    map[3][i+3][0+j] = agent_store.type
        elif agent_store.floor == 2:
            for i in range(5):
                for j in range(2):
                    map[2][i][0+j] = agent_store.type
        elif agent_store.floor == 3:
            for i in range(5):
                for j in range(3):
                    map[1][i][0+j] = agent_store.type
        elif agent_store.floor == 4:
            for i in range(2):
                for j in range(4):
                    map[0][3+i][6+j] = agent_store.type

    pprint.pprint(map)

    return map

def calc_distance(state_now, state_destination, agents_store):
    """
    現在いるところと目的地の間の距離を計算
    """
    #print(f'state_now:{state_now}, state_dest:{state_destination}')

    for agent_store in agents_store:
        if state_now == '0':
            now_floor = 0
            Es_now = 2
        if agent_store.type == state_now:
            now_floor = agent_store.floor
            Es_now = agent_store.Es_distance
        if agent_store.type == state_destination:
            dest_floor = agent_store.floor
            Es_dest = agent_store.Es_distance



    #print(f'now_floor:{now_floor}, Es_now:{Es_now}, dest_floor:{dest_floor}, Es_dest:{Es_dest}')
    distance = abs(dest_floor - now_floor)*10 + Es_now + Es_dest

    return distance


def show_store_info(agents_store):
    """
    show agents_store infomation
    """

    for agent_store in agents_store:
        print(f'type:{agent_store.type}, capa:{agent_store.capacity}, instore:{agent_store.instore}, waiting:{agent_store.waiting}, visitor:{agent_store.visitor}')
