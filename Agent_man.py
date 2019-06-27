import random as rnd
import Decision
import Move


class Agent_man:

    def __init__(self):
        """
        state = ['0','Gr','Cl','Rt','Cf','Mg'] (0:exit 1~5:store)
        strategy = ['A','B','C']    (A:like to stay here , B: like to move other stores, C:50-50 )
        task: how many have something to do
        status = ['In':in the store, 'Wt':waiting to enter store '0':exit]
        visited_store: store Agent visited in past
        """

        self.state = '0'
        self.next_state = '0'
        self.strategy = 'A'
        self.next_strategy = 'A'
        self.task = 0
        self.status = '0'
        self.neighbors_id = []
        self.visited_store = []


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
        print(f'agent No:{agent_id}, state:{agent.state}, next_state:{agent.next_state}, strategy:{agent.strategy}, next_strategy:{agent.next_strategy}, task:{agent.task}, status:{agent.status}, visited:{agent.visited_store}')
