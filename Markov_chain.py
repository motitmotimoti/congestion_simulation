import analyze
import pandas as pd
import numpy as np

#result_list_state.csvの読み込み
#ディレクトリの変更をするように！！
df_state = pd.read_csv('result_list_state.csv', index_col=0)
df_state = df_state.fillna('Na')
length = len(df_state)


#result_info.csvの読み込み
#ディレクトリの変更を忘れずに！！！
df_info = pd.read_csv('result_info.csv',index_col=0)
df_info_init = df_info.iloc[:1,0:6]

df_info_0 = df_info.iloc[:,7]
df_info_0 = df_info_0.values.tolist()
#print(f'df_info_init:\n{df_info_init}')
state = df_info_init.values
state_n = state / df_info_0[1] #初期状態
print(f'init_state:\n{state}')
print(f'init_state_n:\n{state_n}')
#print(f'df_info_init:\n{df_info_init}')
#print(type(df_info_init))
result_markov = []


for x in range(0,length-1):
    print('########################')
    mat_x, result_x = analyze.generate_matrix(df_state, df_info,state_n, x)
    #ディレクトリは生成し、変更すること
    #np.save(f'matrix/high/2019-07-10/result_test_{x+1}',result_x)
    print(f'result_{x+1}:\n{result_x}')
    print(f'mat_{x+1}:\n{mat_x}')
    state_n = np.dot(state_n,result_x)
    print(f'{x+2}シーズン')
    print(state_n)

    state_m = state_n.round(4)
    result_markov.append(state_m[0].tolist())

#print(result_markov)
markov = pd.DataFrame(result_markov, columns=['Gr','Cl','Rt','Cf','Mg','0_out'])
markov.to_csv(f'markov_chain.csv')

print(np.load('matrix/high/2019-07-10/result_test_1.npy'))
