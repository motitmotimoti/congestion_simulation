import random as rnd
import Agent_man
import Agent_store
import Decision

def initialize_state_task(agents,agents_store,time):
    """
    Ramdamly select initially state and task of agents
    """
    initial_state_list = ['Gr','Cl','Rt','Cf','Mg']
    initial_task_list = [1,2,3,4,5]

    for agent_id, agent in enumerate(agents):
        agent.task = rnd.choice(initial_task_list)
        agent.list_store = rnd.sample(initial_state_list, agent.task)
        #agent.next_state = rnd.choice(agent.list_store)

        for list in agent.list_store:
            agent.spent_time[list] = Agent_store.service_time(list)


        if agent.strategy == 'C':
            agent.next_state = Decision.prioritize_store(agent, agent_id)
        elif agent.strategy =='D':
            agent.next_state = Decision.randam_store(agent)
        elif agent.strategy == 'E':
            agent.next_state = Decision.likely_distane(agent, agents_store)
        elif agent.strategy == 'F':
            agent.next_state = Decision.likely_time(agent, time)

        #print(f'agent:{agent_id}, state:{agent.state}, task:{agent.task}')





def state_task_for_new_agents(agents,agents_store, time,length):
    """
    Ramdamly select state and task of new agents
    """

    initial_state_list = ['Gr','Cl','Rt','Cf','Mg']
    initial_task_list = [1,2,3,4,5]

    for agent_id, agent in enumerate(agents):
        #print(f'id:{agent_id+length}')
        agent.task = rnd.choice(initial_task_list)
        agent.list_store = rnd.sample(initial_state_list, agent.task)
        #agent.next_state = rnd.choice(agent.list_store)
        agent.task = agent.task + 1
        #print(f'agent:{agent_id}, state:{agent.state}, task:{agent.task}')
        for list in agent.list_store:
            agent.spent_time[list] = Agent_store.service_time(list)

        if agent.strategy == 'C':
            agent.next_state = Decision.prioritize_store(agent, agent_id+length)
        elif agent.strategy =='D':
            agent.next_state = Decision.randam_store(agent)
        elif agent.strategy == 'E':
            agent.next_state = Decision.likely_distane(agent, agents_store)
        elif agent.strategy == 'F':
            agent.next_state = Decision.likely_time(agent, time)


def agents_moves(agents,season):
    """
    agents go to next_state
    """

    for id, agent in enumerate(agents):
        if agent.next_state != '0':
            if agent.state != agent.next_state:
                if season != 0:
                    agent.task = agent.task -1
            agent.state = agent.next_state
            agent.next_state = 'NULL'

        else:
            agent.state = '0'
            agent.status = 'Out'
            agent.task = 0

def count_store_all(agents):
    """
    count agents in shoppingmoll except state'0'
    """
    f1 = len([agent for agent in agents if agent.state == 'Gr'])
    f2 = len([agent for agent in agents if agent.state == 'Cl'])
    f3 = len([agent for agent in agents if agent.state == 'Rt'])
    f4 = len([agent for agent in agents if agent.state == 'Cf'])
    f5 = len([agent for agent in agents if agent.state == 'Mg'])

    num = f1+f2+f3+f4+f5

    return num



def count_state_num(agents):
    """
    count the fraction of 1/2/3/4/5/0 state agents
    """

    f1 = len([agent for agent in agents if agent.state == 'Gr']) #/ count_store_all(agents,num_new)
    f2 = len([agent for agent in agents if agent.state == 'Cl']) #/ count_store_all(agents,num_new)
    f3 = len([agent for agent in agents if agent.state == 'Rt']) #/ count_store_all(agents,num_new)
    f4 = len([agent for agent in agents if agent.state == 'Cf']) #/ count_store_all(agents,num_new)
    f5 = len([agent for agent in agents if agent.state == 'Mg']) #/ count_store_all(agents,num_new)
    #new = num_new / count_store_all(agents,num_new)
    f0 = len([agent for agent in agents if agent.state == '0']) #/ len(agents)

    #print(f'store_all:{count_store_all(agents,num_new)}')

    return f1, f2, f3, f4, f5, f0

def count_all(agents):
    """
    count the all agents
    """

    all = len([agent for agent in agents])

    return all
