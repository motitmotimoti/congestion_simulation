import random as rnd
import Agent_man

def initialize_state_task(agents):
    """
    Ramdamly select initially state and task of agents
    """
    initial_state_list = ['1','2','3','4','5']
    initial_task_list = [1,2,3,4,5]

    for agent_id, agent in enumerate(agents):
        agent.state = rnd.choice(initial_state_list)
        agent.task = rnd.choice(initial_task_list)
        #print(f'agent:{agent_id}, state:{agent.state}, task:{agent.task}')

def state_task_for_new_agents(agents):
    """
    Ramdamly select state and task of new agents
    """

    state_list = ['1','2','3','4','5']
    task_list = [1,2,3,4,5]
    for agent_id, agent in enumerate(agents):
        agent.state= rnd.choice(state_list)
        agent.next_state = agent.state
        agent.task = rnd.choice(task_list)
        #print(f'new_agent:{agent_id}, state:{agent.state}, task:{agent.task}')



def agents_moves(agents):
    """
    agents go to next_state
    """

    for id, agent in enumerate(agents):
        if agent.state != '0':
            agent.state = agent.next_state
            agent.next_state = 'NULL'

        else:
            agent.state = '0'



def count_state_num(agents):
    """
    count the fraction of 1/2/3/4/5/0 state agents
    """

    f1 = len([agent for agent in agents if agent.state == '1']) / len(agents)
    f2 = len([agent for agent in agents if agent.state == '2']) / len(agents)
    f3 = len([agent for agent in agents if agent.state == '3']) / len(agents)
    f4 = len([agent for agent in agents if agent.state == '4']) / len(agents)
    f5 = len([agent for agent in agents if agent.state == '5']) / len(agents)
    f0 = len([agent for agent in agents if agent.state == '0']) / len(agents)

    return f1, f2, f3, f4, f5, f0

def count_all(agents):
    """
    count the all agents
    """

    all = len([agent for agent in agents])

    return all
