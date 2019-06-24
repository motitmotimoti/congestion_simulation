import numpy as np
import random as rnd
import Agent_man

def initial_strategy(agents):
    """
    Ramdamly select initially strategy
    """
    initial_strategy_list = ['A','B','C']

    for agent_id, agent in enumerate(agents):
        agent.strategy = rnd.choice(initial_strategy_list)
        #print(f'agent:{agent_id}, strategy:{agent.strategy}')




def decide_next_strategy(agents):
    """
    Ramdamly select next strategy
    """
    strategy_list = ['A','B','C']

    for agent_id, agent in enumerate(agents):
        agent.next_strategy = rnd.choice(strategy_list)
        #print(f'agent:{agent_id}, strategy:{agent.next_strategy}')

def insert_strategy(agents):
    """
    insert next strategy into strategy
    """
    for agent_id, agent in enumerate(agents):
        agent.strategy = agent.next_strategy

    Agent_man.show_agent_info(agents)


def strategy_determine_state(agents):
    """
    each strategy determine next state
    """
    state_list = ['Gr','Cl','Rt','Cf','Mg']

    for id, agent in enumerate(agents):
        #first, insert now state into visited list
        agent.visited_store.append(agent.state)

        if agent.task > 1:

            #stay same state
            if agent.strategy == 'A':
                agent.next_state = agent.state

            #move other states
            elif agent.strategy == 'B':
                candidate_list = [e for e in state_list if e != agent.state]
                agent.next_state = rnd.choice(list(set(candidate_list) ^ set(agent.visited_store)))
                #agent.task = agent.task - 1

            #30-70
            elif agent.strategy == 'C':
                if rnd.random() <= 0.3:
                    agent.next_state = agent.state
                else:
                    candidate_list = [e for e in state_list if e != agent.state]
                    agent.next_state = rnd.choice(list(set(candidate_list) ^ set(agent.visited_store)))
                    #agent.task = agent.task - 1

        else:
            agent.next_state = '0'
            #agent.task = 0

def count_strategy(agents):
    """
    count the number of each strategy
    """

    num_a = len([agent for agent in agents if agent.strategy == 'A'])
    num_b = len([agent for agent in agents if agent.strategy == 'B'])
    num_c = len([agent for agent in agents if agent.strategy == 'C'])


    return num_a, num_b, num_c
