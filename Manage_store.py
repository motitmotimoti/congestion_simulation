import random as rnd
import Agent_store
import Agent_man

def divide_visitor(agents):
    """
    divide visitor per store
    """

    list_Gr = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Gr']
    list_Cl = [agent_id for agent_id ,agent in enumerate(agents) if agent.state == 'Cl']
    list_Rt = [agent_id for agent_id ,agent in enumerate(agents) if agent.state == 'Rt']
    list_Cf = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Cf']
    list_Mg = [agent_id for agent_id, agent in enumerate(agents) if agent.state == 'Mg']

    

    return list_Gr, list_Cl, list_Rt, list_Cf, list_Mg
