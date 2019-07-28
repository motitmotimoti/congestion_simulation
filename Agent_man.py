import random as rnd
import Decision
import Move


class Agent_man:

    def __init__(self):
        """
        state = ['0','Gr','Cl','Rt','Cf','Mg'] (0:exit 1~5:store)
        #strategy = ['A','B','C']    (A:like to stay here , B: like to move other stores, C:50-50 )
        strategy = ['A','B','C','D']    (A:likely visit crowed store, B: likely visit vacant store, C: prioritize store, D: randamly visit store)
        task: how many have something to do
        status = ['In':in the store, 'Wt':waiting to enter store 'Out':exit]
        visited_store: store Agent visited in past
        list_store: store lists that will wants to visit
        spent_time: how nuch spent for each list_store
        """

        self.state = '0'
        self.next_state = '0'
        self.strategy = 'A'
        self.next_strategy = '0'
        self.task = 0
        self.status = '0'
        self.neighbors_id = []
        self.visited_store = []
        self.list_store = []
        self.spent_time = {'Gr':0, 'Cl':0, 'Rt':0, 'Cf':0, 'Mg':0}


def generate_agents(num_agent):
    agents = [Agent_man() for agent_id in range(num_agent)]
    return agents

def new_generate_agents(num_new_agent,agents,agents_store, time,length):
    """
    new agents generate in Move section
    """
    #num_new_agent = rnd.randrange(num_new_generate)
    new_agents = [Agent_man() for new_agent_id in range(num_new_agent)]
    Decision.initial_strategy(new_agents)
    Move.state_task_for_new_agents(new_agents,agents_store,time,length)
    for id,agent in enumerate(new_agents):
        print(f'new_agents No.{id}, state:{agent.state}, next_state:{agent.next_state}, strategy:{agent.strategy}, next_strategy:{agent.next_strategy}, task:{agent.task - 1}')
    agents.extend(new_agents)



def show_agent_info(agents):
    """
    show information of agents
    """
    for agent_id, agent in enumerate(agents):
        print(f'agent No:{agent_id}, state:{agent.state}, next_state:{agent.next_state}, strategy:{agent.strategy}, next_strategy:{agent.next_strategy}, task:{agent.task}, status:{agent.status}, visited:{agent.visited_store}, list:{agent.list_store}, spent_time:{agent.spent_time}')
