import numpy as np
import random as rnd
import Agent_man
import Agent_store

def initial_strategy(agents):
    """
    Ramdamly select initially strategy
    """
    #initial_strategy_list = ['A','B','C','D','E','F']
    initial_strategy_list = ['C','D','E','F']


    for agent_id, agent in enumerate(agents):
        agent.strategy = rnd.choice(initial_strategy_list)
        #agent.strategy = 'F'
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

    #Agent_man.show_agent_info(agents)

def likely_crowded(agents,tmp):
    """
    like to visit crowded store
    """
    #max_1 = '0'
    #tmp = {'Gr':0, 'Cl':0, 'Rt':0, 'Cf':0 ,'Mg':0}
    tmp_list = list( set(agents.list_store) - set(agents.visited_store) )

    if len(tmp_list) != 0:
        list_crowded = sorted(tmp_list, key=lambda x:tmp[x])
        #print(f'list_crowded:{list_crowded}')
        print(f'A_next_state:{list_crowded[-1]}')

        return list_crowded[-1]
    else:

        return '0'

def likely_vacant(agents,tmp):
    """
    like to viedsit vacant store
    """
    #min_1 = '0'
    #tmp = {'Gr':100000, 'Cl':100000, 'Rt':100000, 'Cf':100000 ,'Mg':100000}
    tmp_list = list(set(agents.list_store) - set(agents.visited_store))

    if len(tmp_list) != 0:
        list_vacant = sorted(tmp_list, key=lambda x:tmp[x])
        #print(f'list_vacant:{list_vacant}')
        print(f'B_next_state:{list_vacant[0]}')

        return list_vacant[0]
    else:

        return '0'

def prioritize_store(agents, agents_id):
    """
    prioritize store from your list_store
    """

    tmp_0 = {'Gr':5, 'Cl':1, 'Rt':0, 'Cf':4, 'Mg':2}
    tmp_1 = {'Gr':5, 'Cl':2, 'Rt':0, 'Cf':4, 'Mg':1}
    tmp_2 = {'Gr':5, 'Cl':2, 'Rt':4, 'Cf':0, 'Mg':1}
    tmp_3 = {'Gr':5, 'Cl':1, 'Rt':4, 'Cf':0, 'Mg':2}

    tmp = list(set(agents.list_store) - set(agents.visited_store))
    order = []

    if len(tmp) != 0:
        if agents_id % 4 == 0:
            order = sorted(tmp, key=lambda x:tmp_0[x])
            #print(f'order_0:{order}')
        elif agents_id % 4 == 1:
            order = sorted(tmp, key=lambda x:tmp_1[x])
            #print(f'order_1:{order}')
        elif agents_id % 4 == 2:
            order = sorted(tmp, key=lambda x:tmp_2[x])
            #print(f'order_2:{order}')
        elif agents_id % 4 == 3:
            order = sorted(tmp, key=lambda x:tmp_3[x])
            #print(f'order_3:{order}')
        print(f'id:{agents_id}, C_next_state:{order[0]}')

        return order[0]
    else:

        return '0'

def randam_store(agent):
    """
    ramdamly select next_store
    """

    if len(list(set(agent.list_store) - set(agent.visited_store))) != 0:
         test = rnd.choice(list(set(agent.list_store) - set(agent.visited_store)))
         print(f'D_next_state:{test}')
         return test
    else:

        return '0'

def likely_distane(agents,agents_store):
    """
    現在、自分のいるところから一番近いところを次の場所にする戦略
    """
    now_state = agents.state
    tmp_list = list(set(agents.list_store) - set(agents.visited_store))
    #print(f'now_state:{now_state}, list:{tmp_list}')

    if len(tmp_list) != 0:
        dis = {state: Agent_store.calc_distance(now_state, state, agents_store) for state in tmp_list}
        print(f'now:{now_state}, dis:{dis},min_dis:{min(dis, key=dis.get)}')
        return min(dis,key=dis.get)
    else:

        return '0'

def likely_time(agents,time):
    """
    時間帯に合わせて次の目的地を決める戦略
    """
    time_10_11 = {'Gr':3, 'Cl':4, 'Rt':2, 'Cf':1, 'Mg':4}
    time_11_13 = {'Gr':1, 'Cl':2, 'Rt':4, 'Cf':3, 'Mg':2}
    time_13_15 = {'Gr':1, 'Cl':4, 'Rt':2, 'Cf':3, 'Mg':4}
    time_15_17 = {'Gr':2, 'Cl':3, 'Rt':1, 'Cf':4, 'Mg':3}
    time_17_18 = {'Gr':4, 'Cl':1, 'Rt':3, 'Cf':2, 'Mg':1}
    time_18_20 = {'Gr':3, 'Cl':1, 'Rt':4, 'Cf':2, 'Mg':1}

    tmp_list = list(set(agents.list_store) - set(agents.visited_store))
    next_list = []

    if len(tmp_list) != 0:
        hour = int(time.strftime('%H'))
        if hour < 11:
            next_list = sorted(tmp_list, key=lambda x:time_10_11[x])
            #print(f'next_list_10_11:{next_list}')
        elif hour >= 11 & hour < 13:
            next_list = sorted(tmp_list, key=lambda x:time_11_13[x])
            #print(f'next_list_11_13:{next_list}')
        elif hour >= 13 & hour < 15:
            next_list = sorted(tmp_list, key=lambda x:time_13_15[x])
            #print(f'next_list_13_15:{next_list}')
        elif hour >= 15 & hour < 17:
            next_list = sorted(tmp_list, key=lambda x:time_15_17[x])
            #print(f'next_list_15_17:{next_list}')
        elif hour >= 17 & hour < 18:
            next_list = sorted(tmp_list, key=lambda x:time_17_18[x])
            #print(f'next_list_17_18:{next_list}')
        elif hour >= 18 & hour < 20:
            next_list = sorted(tmp_list, key=lambda x:time_18_20[x])
            #print(f'next_list18_20:{next_list}')

        if len(next_list) > 2:
            check = next_list[len(next_list)-1:len(next_list)-3:-1]
            print(f'check:{check}')
        else:
            check = next_list

        if 'Mg' in check and 'Cl' in check:

            return rnd.choice(check)
        else:
            return next_list[-1]

    else:

        return '0'






def store_crowded(agents_store):
    tmp = {'Gr':0, 'Cl':0, 'Rt':0, 'Cf':0 ,'Mg':0}

    for agent_store in agents_store:
        if agent_store.type == 'Gr':
            tmp['Gr'] = len(agent_store.instore + agent_store.waiting)
        elif agent_store.type == 'Cl':
            tmp['Cl'] = len(agent_store.instore + agent_store.waiting)
        elif agent_store.type == 'Rt':
            tmp['Rt'] = len(agent_store.instore + agent_store.waiting)
        elif agent_store.type == 'Cf':
            tmp['Cf'] = len(agent_store.instore + agent_store.waiting)
        elif agent_store.type == 'Mg':
            tmp['Mg'] = len(agent_store.instore + agent_store.waiting)
    print(f'tmp:{tmp}')

    return tmp



def strategy_determine_state(agents,agents_store,time):
    """
    ↓：滞在時間とagent毎の意思決定に基づくnext_stateの決定
    """
    state_list = ['Gr','Cl','Rt','Cf','Mg']
    crowded = store_crowded(agents_store)


    for id,agent in enumerate(agents):
         #first, insert now state into visited list
         agent.visited_store.append(agent.state)

         if agent.task > 0 or agent.status == 'Wt':

             if agent.status == 'Wt':
                 agent.next_state = agent.state

             elif agent.status == 'In':

                 if agent.visited_store.count(agent.state) < agent.spent_time[agent.state]:
                     agent.next_state =  agent.state

                 else:

                     if agent.strategy == 'A':
                         agent.next_state = likely_crowded(agent, crowded)
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
                     elif agent.strategy == 'B':
                         agent.next_state = likely_vacant(agent, crowded)
                         #agent.next_state = likely_distane(agent, agents_store)
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
                     elif agent.strategy == 'C':
                         agent.next_state = prioritize_store(agent, id)
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
                     elif agent.strategy == 'D':
                         agent.next_state = randam_store(agent)
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
                     elif agent.strategy == 'E':
                         agent.next_state = likely_distane(agent, agents_store)
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
                     elif agent.strategy == 'F':
                         agent.next_state = likely_time(agent, time)
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
         else:
             agent.next_state = '0'
             for agent_store in agents_store:
                 if id in agent_store.instore:
                     agent_store.instore.remove(id)




    """
    ↓: agent.status determine next_state(Ramdom strategy!!)

    for id,agent in enumerate(agents):
         #first, insert now state into visited list
         agent.visited_store.append(agent.state)

         if agent.task > 1 or agent.status == 'Wt':

             if agent.status == 'Wt':
                 agent.next_state = agent.state

             elif agent.status == 'In':

                 if agent.state == 'Rt' or agent.state == 'Cf':
                     if rnd.random() <= 0.6:
                         agent.next_state = agent.state
                     else:
                         if len(list(set(state_list) - set(agent.visited_store))) != 0:
                             agent.next_state = rnd.choice(list(set(state_list) - set(agent.visited_store)))
                         else:
                             agent.next_state = '0'
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)
                 else:
                     if rnd.random() <= 0.5:
                         agent.next_state = agent.state
                     else:
                         #candidate_list = [e for e in state_list if e != agent.state]
                         if len(list(set(state_list) - set(agent.visited_store))) != 0:
                             agent.next_state = rnd.choice(list(set(state_list) - set(agent.visited_store)))
                         else:
                             agent.next_state = '0'
                         for agent_store in agents_store:
                             if agent_store.type == agent.state:
                                 if id in agent_store.instore:
                                     agent_store.instore.remove(id)

         else:
              agent.next_state = '0'
              for agent_store in agents_store:
                  if id in agent_store.instore:
                      agent_store.instore.remove(id)
    """



    """
    ↓:each strategy determine next state
    """
    """
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
    """


def count_strategy(agents):
    """
    count the number of each strategy
    """

    num_a = len([agent for agent in agents if agent.strategy == 'A'])
    num_b = len([agent for agent in agents if agent.strategy == 'B'])
    num_c = len([agent for agent in agents if agent.strategy == 'C'])
    num_d = len([agent for agent in agents if agent.strategy == 'D'])
    num_e = len([agent for agent in agents if agent.strategy == 'E'])
    num_f = len([agent for agent in agents if agent.strategy == 'F'])


    return num_a, num_b, num_c,num_d,num_e,num_f
