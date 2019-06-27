import random as rnd
import Agent_store
import Agent_man

def divide_visitor(agents):
    """
    divide visitor from next_state per store & shuffle list randomly
    """

    list_Gr = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Gr']
    list_Cl = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Cl']
    list_Rt = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Rt']
    list_Cf = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Cf']
    list_Mg = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Mg']

    print(f'list_Gr:{list_Gr}\n list_Cl:{list_Cl}\n list_Rt:{list_Rt}\n list_Cf:{list_Cf}\n list_Mg:{list_Mg}\n')

    rnd.shuffle(list_Gr)
    rnd.shuffle(list_Cl)
    rnd.shuffle(list_Rt)
    rnd.shuffle(list_Cf)
    rnd.shuffle(list_Mg)

    print(f'list_Gr:{list_Gr}\n list_Cl:{list_Cl}\n list_Rt:{list_Rt}\n list_Cf:{list_Cf}\n list_Mg:{list_Mg}\n')

    return list_Gr, list_Cl, list_Rt, list_Cf, list_Mg

def manage_instore_waiting_first(agents,agents_store,list,type):
    """
    manage instore & waiting  & manage agents_status
    """

    for agent_store in agents_store:
        if agent_store.type == type:
            print(f'type:{type}')
            tmp = agent_store.instore + list
            print(f'tmp:{tmp}')
            print(f'capa:{agent_store.capacity}')
            agent_store.instore, agent_store.waiting = tmp[:agent_store.capacity], tmp[agent_store.capacity:]
            print(f'instore:{agent_store.instore}, waiting:{agent_store.waiting}')
            for id, agent in enumerate(agents):
                if id in agent_store.instore:
                    agent.status = 'In'
                elif id in agent_store.waiting:
                    agent.status = 'Wt'
