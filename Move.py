import random as rnd
import Agent_man

def initialize_state_task(agents):
    """
    Ramdamly select initially state and task of agents
    """
    initial_state_list = ['Gr','Cl','Rt','Cf','Mg']
    initial_task_list = [3,4,5]

    for agent_id, agent in enumerate(agents):
        agent.next_state = rnd.choice(initial_state_list)
        agent.task = rnd.choice(initial_task_list)
        #print(f'agent:{agent_id}, state:{agent.state}, task:{agent.task}')

def state_task_for_new_agents(agents):
    """
    Ramdamly select state and task of new agents
    """

    state_list = ['Gr','Cl','Rt','Cf','Mg']
    task_list = [1,2,3,4,5]
    for agent_id, agent in enumerate(agents):
        agent.next_state= rnd.choice(state_list)
        #agent.next_state = agent.state
        agent.task = rnd.choice(task_list)
        #print(f'new_agent:{agent_id}, state:{agent.state}, task:{agent.task}')



def agents_moves(agents,season):
    """
    agents go to next_state
    """

    for id, agent in enumerate(agents):
        if agent.next_state != '0':
            if agent.state != agent.next_state:
                if season != 1:
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
