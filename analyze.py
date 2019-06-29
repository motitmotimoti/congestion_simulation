import pandas as pd



df = pd.read_csv('result_list_state.csv', index_col=0)
df = df.fillna('Na')
#print(df)

df_0 = df[0:2]
#print(df_0)
list_0 = df_0.values.tolist()
list_1 = [state for state in list_0[0] if state != 'Na']
#print(len(list_1))
list_2 = [state for state in list_0[1] if state != 'Na']
#print(len(list_2))
list_1 = list_1 + [0 for i in range(len(list_2)-len(list_1))]
#print(len(list_1))
#print(list_1)
#print(list_2)
#list_1.append(list_2)
#print(type(list_0))
list_0 = []
list_0.append(list_1)
list_0.append(list_2)
print(list_0)
print(f'[0][0]:{list_0[0][108]}, [1][1]:{list_0[1][1]}')
