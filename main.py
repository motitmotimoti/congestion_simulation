import numpy as np
import pandas as pd
import random as rnd
import Agent_man
import Move
import Decision


def main():
    ###Calcualtion setting ###
    num_agent = 10
    """
    average_range
    beta
    gamma
    param_ramge
    """
    max_season = 5
    list_state = []
    list_task = []
    result_list_state = []
    result_list_task = []
    info = pd.DataFrame({'s1':[],
                         's2':[],
                         's3':[],
                         's4':[],
                         's5':[],
                         's0':[],
                         'sA':[],
                         'sB':[],
                         'sC':[]
                         })
    #initialization of ramdom int
    num_new_agent = rnd.randint(1,10)


    #Prepare agents & initialize state & task
    agents = Agent_man.generate_agents(num_agent)
    Move.initialize_state_task(agents)
    Decision.initial_strategy(agents)
    Agent_man.show_agent_info(agents)

    for season in range(1, max_season):


        print('###########################')
        print(f'simulate season:{season}')
        if season != 1:
            #generate new agents
            print('==== generate new agents ====')
            Agent_man.new_generate_agents(num_new_agent,agents)

            #move next_state
            print('===== agent move =====')
            Move.agents_moves(agents)
            Agent_man.show_agent_info(agents)

        #strategy determine next_state
        print('==== decide next state ====')
        Decision.strategy_determine_state(agents)
        #agents determine next_strategy
        print('==== decide next strategy ====')
        Decision.decide_next_strategy(agents)

        print('==== insert next strategy into strategy ====')
        Decision.insert_strategy(agents)



        s1,s2,s3,s4,s5,s0 = Move.count_state_num(agents)
        sA,sB,sC = Decision.count_strategy(agents)
        new_info = pd.DataFrame([[format(s1, '.2%'),format(s2,'.2%'),format(s3,'.2%'),format(s4,'.2%'),format(s5,'.2%'),format(s0,'.2%'),sA,sB,sC]],columns=['s1','s2','s3','s4','s5','s0','sA','sB','sC'])
        info = info.append(new_info)
        print(f'info:{info}')

        #infomation of state store result_list_state
        for id, agent in enumerate(agents):
            list_state.append(agent.state)
            list_task.append(agent.task)
        #print(f'list_state:{list_state}')
        #print(f'result_list_state:{result_list_state}')
        result_list_state.append(list_state)
        result_list_task.append(list_task)
        #print(f'result_list_state:{result_list_state}')

        list_state = []
        list_task = []
        #print(f'list_state:{list_state}')


    state = pd.DataFrame(result_list_state)
    task = pd.DataFrame(result_list_task)

    print(f'result:{state}')

    state.to_csv(f'result_list_state.csv')
    task.to_csv(f'result_list_task.csv')
    info.to_csv(f'result_info.csv')





if __name__=='__main__':
    main()
