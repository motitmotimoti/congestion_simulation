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

    #print(f'list_Gr:{list_Gr}\n list_Cl:{list_Cl}\n list_Rt:{list_Rt}\n list_Cf:{list_Cf}\n list_Mg:{list_Mg}\n')

    rnd.shuffle(list_Gr)
    rnd.shuffle(list_Cl)
    rnd.shuffle(list_Rt)
    rnd.shuffle(list_Cf)
    rnd.shuffle(list_Mg)

    #print(f'list_Gr:{list_Gr}\n list_Cl:{list_Cl}\n list_Rt:{list_Rt}\n list_Cf:{list_Cf}\n list_Mg:{list_Mg}\n')

    return list_Gr, list_Cl, list_Rt, list_Cf, list_Mg

def manage_instore_waiting_first(agents,agents_store,list,type):
    """
    manage instore & waiting  & manage agents_status in 1st seacon
    """

    for agent_store in agents_store:
        if agent_store.type == type:
            #print(f'type:{type}')
            tmp = agent_store.instore + list
            #print(f'tmp:{tmp}')
            #print(f'capa:{agent_store.capacity}')
            agent_store.instore, agent_store.waiting = tmp[:agent_store.capacity], tmp[agent_store.capacity:]
            print(f'instore:{agent_store.instore}, waiting:{agent_store.waiting}')
            for id, agent in enumerate(agents):
                if id in agent_store.instore:
                    agent.status = 'In'
                elif id in agent_store.waiting:
                    agent.status = 'Wt'
                    # if task= 1 & Wt, next_state will be '0', so agent.task + 1
                    #if agent.task == 1:
                        #agent.task = agent.task + 1


def manage_instore_waiting_second(agents,agents_store,list_x,type):
    """
    manage instore & waiting  & manage agents_status after 1st seasons
    """

    for agent_store in agents_store:
        if agent_store.type == type:
            #print(f'type:{type}')
            tmp = agent_store.instore + agent_store.waiting + list_x
            #print(f'tmp:{tmp}')
            #print(f'capa:{agent_store.capacity}')
            tmp = list(dict.fromkeys(tmp))
            #print(f'tmp:{tmp}')
            agent_store.instore, agent_store.waiting = tmp[:agent_store.capacity], tmp[agent_store.capacity:]
            print(f'instore:{agent_store.instore}, waiting:{agent_store.waiting}')

            for id,agent in enumerate(agents):
                if id in agent_store.instore:
                    agent.status = 'In'
                elif id in agent_store.waiting:
                    agent.status = 'Wt'
                    # if task= 1 & Wt, next_state will be '0', so agent.task + 1
                    #if agent.task == 1:
                        #agent.task = agent.task + 1
