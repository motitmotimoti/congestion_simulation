import numpy as np
import pandas as pd
import random as rnd
import Agent_man
import Agent_store
import Move
import Decision
import Manage_store


def main():
    ###Calcualtion setting ###
    
    #low:100, 30
    #medium:130, 60
    #high: 160, 100
    num_agent = 160

    """
    average_range
    beta
    gamma
    param_ramge
    """
    max_season = 37
    list_state = []
    list_task = []
    result_list_state = []
    result_list_task = []
    state_to_nextstate = []
    list_Gr = []
    list_Cl = []
    list_Rt = []
    list_Cf = []
    list_Mg = []
    info = pd.DataFrame({'Gr':[],
                         'Cl':[],
                         'Rt':[],
                         'Cf':[],
                         'Mg':[],
                         'New':[],
                         's0':[],
                         'Sa':[],
                         'sA':[],
                         'sB':[],
                         'sC':[]
                         })
    #initialization of ramdom int
    num_new_agent = 0


    #Prepare agents & initialize state & task &strategy
    agents = Agent_man.generate_agents(num_agent)
    agents_store = Agent_store.generate_agent_store(5)
    Agent_store.init_agent_store(agents_store)
    Agent_store.show_store_info(agents_store)
    Move.initialize_state_task(agents)
    Decision.initial_strategy(agents)
    #Agent_man.show_agent_info(agents)

    for season in range(1, max_season):




        print('###########################')
        print(f'simulate season:{season}')
        if season != 1 and season != max_season-1:

            num_new_agent = rnd.randint(1,100)
            #generate new agents
            print('==== generate new agents ====')
            Agent_man.new_generate_agents(num_new_agent,agents)

        #move next_state
        print('===== agent move =====')
        Move.agents_moves(agents,season)
        #divide visitor per stores
        list_Gr, list_Cl,list_Rt,list_Cf,list_Mg = Manage_store.divide_visitor(agents)

        if season == 1:
            #manage instore & waiting for 1st season
            Manage_store.manage_instore_waiting_first(agents,agents_store,list_Gr,'Gr')
            Manage_store.manage_instore_waiting_first(agents,agents_store,list_Cl,'Cl')
            Manage_store.manage_instore_waiting_first(agents,agents_store,list_Rt,'Rt')
            Manage_store.manage_instore_waiting_first(agents,agents_store,list_Cf,'Cf')
            Manage_store.manage_instore_waiting_first(agents,agents_store,list_Mg,'Mg')
        if season != 1:
            Manage_store.manage_instore_waiting_second(agents,agents_store,list_Gr,'Gr')
            Manage_store.manage_instore_waiting_second(agents,agents_store,list_Cl,'Cl')
            Manage_store.manage_instore_waiting_second(agents,agents_store,list_Rt,'Rt')
            Manage_store.manage_instore_waiting_second(agents,agents_store,list_Cf,'Cf')
            Manage_store.manage_instore_waiting_second(agents,agents_store,list_Mg,'Mg')


        #Agent_man.show_agent_info(agents)


        #strategy determine next_state
        print('==== decide next state ====')
        Decision.strategy_determine_state(agents,agents_store)
        #agents determine next_strategy
        print('==== decide next strategy ====')
        Decision.decide_next_strategy(agents)

        print('==== insert next strategy into strategy ====')
        Decision.insert_strategy(agents)



        Gr,Cl,Rt,Cf,Mg,s0 = Move.count_state_num(agents)
        Sa = Move.count_store_all(agents)
        sA,sB,sC = Decision.count_strategy(agents)
        new_info = pd.DataFrame([[Gr,Cl,Rt,Cf,Mg,num_new_agent,s0,Sa,sA,sB,sC]],columns=['Gr','Cl','Rt','Cf','Mg','New','s0','Sa','sA','sB','sC'])
        #new_info = pd.DataFrame([[format(Gr, '.4'),format(Cl,'.4'),format(Rt,'.4'),format(Cf,'.4'),format(Mg,'.4'),num_new_agent,format(s0,'.4'),Sa,sA,sB,sC]],columns=['Gr','Cl','Rt','Cf','Mg','New','s0','Sa','sA','sB','sC'])
        info = info.append(new_info)
        #print(f'info:{info}')

        #infomation of state store result_list_state
        for id, agent in enumerate(agents):
            list_state.append(agent.state+'_'+agent.status)
            list_task.append(agent.task)
        #print(f'list_state:{list_state}')
        #print(f'result_list_state:{result_list_state}')
        result_list_state.append(list_state)
        result_list_task.append(list_task)
        #print(f'result_list_state:{result_list_state}')

        list_state = []
        list_task = []
        list_Gr = []
        list_Cl = []
        list_Rt = []
        list_Cf = []
        list_Mg = []

        #print(f'list_state:{list_state}')


    state = pd.DataFrame(result_list_state)
    task = pd.DataFrame(result_list_task)

    print(f'result:{state}')

    #ディレクトリの変更必須！！！
    state.to_csv(f'result/high/result_list_state_high.csv')
    task.to_csv(f'result/high/result_list_task_high.csv')
    info.to_csv(f'result/high/result_info_high.csv')





if __name__=='__main__':
    main()
