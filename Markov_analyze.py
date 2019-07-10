import numpy as np
import pandas as pd

#シーズン数の入力
season = 36

#初期状態の入力
#result_info.csvの読み込み
#ディレクトリの変更を忘れずに！！！
df_info = pd.read_csv('result_info.csv',index_col=0)
df_info_init = df_info.iloc[:1,0:6]

df_info_0 = df_info.iloc[:,7]
df_info_0 = df_info_0.values.tolist()
new = df_info.iloc[:,5]
new = new.values.tolist()
#print(f'df_info_init:\n{df_info_init}')
state = df_info_init.values

print(f'new:{new[1]}')
print(f'df_info_0:{df_info_0[1]}')
state[0,5] = new[1]
#print(f'dist:{dist}')
print(f'state:{state}')


state_n = state / df_info_0[1] #初期状態
print(f'state_init:{state_n}')

result_markov = []

for x in range(1,season):
    matrix = np.load(f'matrix/high/2019-07-10/result_test_{x}.npy')
    print(f'matrix:{matrix}')
    state_n = np.dot(state_n,matrix)
    print(f'{x}シーズン')
    print(f'state_n:\n{state_n}')

    state_m = state_n.round(4)
    result_markov.append(state_m[0].tolist())

#print(result_markov)
#matrixで使った尺度のディレクトリに保存
#ファイル名は(用いた初期状態)_(用いたmatrix)_markov_analyze.csv
markov = pd.DataFrame(result_markov, columns=['Gr','Cl','Rt','Cf','Mg','0_out'])
markov.to_csv(f'analyze/high/test_high_markov_analyze.csv')
