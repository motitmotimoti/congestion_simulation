import random as rnd
import Decision
import Move


class Agent_man:

    def __init__(self):
        """
        state = ['0','1','2','3','4','5'] (0:exit 1~5:store)
        strategy = ['A','B','C']    (A:like to stay here , B: like to move other stores, C:50-50 )
        task: how many have something to do
        """

        self.state = '1'
        self.next_state = '0'
        self.strategy = 'A'
        self.next_strategy = 'A'
        self.task = 0
        self.neighbors_id = []
        self.visited_sstore_list = []


def generate_agents(num_agent):
    agents = [Agent_man() for agent_id in range(num_agent)]
    return agents

def new_generate_agents(num_new_agent,agents):
    """
    new agents generate in Move section
    """
    #num_new_agent = rnd.randrange(num_new_generate)
    new_agents = [Agent_man() for new_agent_id in range(num_new_agent)]
    Move.state_task_for_new_agents(new_agents)
    Decision.initial_strategy(new_agents)
    for id,agent in enumerate(new_agents):
        print(f'new_agents No.{id}, state:{agent.state}, next_state:{agent.next_state}, strategy:{agent.strategy}, next_strategy:{agent.next_strategy}, task:{agent.task}')
    agents.extend(new_agents)



def show_agent_info(agents):
    """
    show information of agents
    """
    for agent_id, agent in enumerate(agents):
        print(f'agent No:{agent_id}, state:{agent.state}, next_state:{agent.next_state}, strategy:{agent.strategy}, next_strategy:{agent.next_strategy}, task:{agent.task}')
