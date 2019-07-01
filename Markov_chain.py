import analyze
import pandas as pd
import numpy as np

#result_list_state.csvの読み込み
df_state = pd.read_csv('result_list_state.csv', index_col=0)
df_state = df_state.fillna('Na')
length = len(df_state)
#print(length)
#print(df)

#result_info.csvの読み込み
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


for x in range(0,length-1):
    print('########################')
    mat_x, result_x = analyze.generate_matrix(df_state, df_info,state_n, x)
    print(f'result_{x}:\n{result_x}')
    print(f'mat_{x}:\n{mat_x}')
    state_n = np.dot(state_n,result_x)
    print(f'{x+1}シーズン')
    print(state_n)
