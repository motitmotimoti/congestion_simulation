import pandas as pd
import numpy as np



df = pd.read_csv('result_list_state.csv', index_col=0)
df = df.fillna('Na')
length = len(df)
#print(length)
#print(df)



def generate_matrix(df_csv,df_info, x):

    df_0 = df_csv[x:x+2]
    #print(df_0)
    list_0 = df_0.values.tolist()
    list_1 = [state for state in list_0[0] if state != 'Na']
    #print(len(list_1))
    list_2 = [state for state in list_0[1] if state != 'Na']
    #print(len(list_2))
    list_1 = list_1 + ['0_Out' for i in range(len(list_2)-len(list_1))]
    #print(len(list_1))
    #print(list_1)
    #print(list_2)
    #print(list_2)

    df_info_0 = df_info.iloc[:,6]
    df_info_0 = df_info_0.values.tolist()
    #print(type(df_info_0))
    #print(df_info_0[0])

    Gr_Gr, Gr_Cl, Gr_Rt, Gr_Cf, Gr_Mg, Gr_Out = 0, 0, 0, 0, 0, 0
    Cl_Gr, Cl_Cl, Cl_Rt, Cl_Cf, Cl_Mg, Cl_Out = 0, 0, 0, 0, 0, 0
    Rt_Gr, Rt_Cl, Rt_Rt, Rt_Cf, Rt_Mg, Rt_Out = 0, 0, 0, 0, 0, 0
    Cf_Gr, Cf_Cl, Cf_Rt, Cf_Cf, Cf_Mg, Cf_Out = 0, 0, 0, 0, 0, 0
    Mg_Gr, Mg_Cl, Mg_Rt, Mg_Cf, Mg_Mg, Mg_Out = 0, 0, 0, 0, 0, 0
    Out_Gr, Out_Cl, Out_Rt, Out_Cf, Out_Mg, Out_Out = 0, 0, 0, 0, 0, 0

    for i, list in enumerate(list_1):
        #print(f'i{i}:{list}')
        if list == 'Gr_In':
            if list_2[i] == 'Gr_In':
                Gr_Gr = Gr_Gr + 1
            elif list_2[i] =='Cl_In':
                Gr_Cl = Gr_Cl + 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Gr_Rt = Gr_Rt + 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Gr_Cf = Gr_Cf + 1
            elif list_2[i] == 'Mg_In':
                Gr_Mg = Gr_Mg + 1
            elif list_2[i] == '0_Out':
                Gr_Out = Gr_Out + 1

        elif list == 'Cl_In':
            if list_2[i] == 'Gr_In':
                Cl_Gr = Cl_Gr + 1
            elif list_2[i] == 'Cl_In':
                Cl_Cl = Cl_Cl + 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Cl_Rt = Cl_Rt + 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Cl_Cf = Cl_Cf + 1
            elif list_2[i] == 'Mg_In':
                Cl_Mg = Cl_Mg + 1
            elif list_2[i] == '0_Out':
                Cl_Out = Cl_Out + 1

        elif list == 'Rt_In' or list == 'Rt_Wt':
            if list_2[i] == 'Gr_In':
                Rt_Gr = Rt_Gr + 1
            elif list_2[i] == 'Cl_In':
                Rt_Cl = Rt_Cl + 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Rt_Rt = Rt_Rt + 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Rt_Cf = Rt_Cf + 1
            elif list_2[i] == 'Mg_In':
                Rt_Mg = Rt_Mg + 1
            elif list_2[i] == '0_Out':
                Rt_Out = Rt_Out + 1

        elif list == 'Cf_In' or list == 'Cf_Wt':
            if list_2[i] == 'Gr_In':
                Cf_Gr = Cf_Gr + 1
            elif list_2[i] == 'Cl_In':
                Cf_Cl = Cf_Cl + 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Cf_Rt = Cf_Rt + 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Cf_Cf = Cf_Cf + 1
            elif list_2[i] == 'Mg_In':
                Cf_Mg = Cf_Mg + 1
            elif list_2[i] == '0_Out':
                Cf_Out = Cf_Out + 1

        elif list == 'Mg_In':
            if list_2[i] == 'Gr_In':
                Mg_Gr = Mg_Gr + 1
            elif list_2[i] == 'Cl_In':
                Mg_Cl = Mg_Cl + 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Mg_Rt = Mg_Rt + 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Mg_Cf = Mg_Cf + 1
            elif list_2[i] == 'Mg_In':
                Mg_Mg = Mg_Mg + 1
            elif list_2[i] == '0_Out':
                Mg_Out = Mg_Out + 1

        elif list == '0_Out':
            if list_2[i] == 'Gr_In':
                Out_Gr = Out_Gr + 1
            elif list_2[i] == 'Cl_In':
                Out_Cl = Out_Cl + 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Out_Rt = Out_Rt + 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Out_Cf = Out_Cf + 1
            elif list_2[i] == 'Mg_In':
                Out_Mg = Out_Mg + 1
            #elif list_2[i] == '0_Out':
                #Cl_Out = Cl_Out + 1

    matrix = np.array(
    [[Gr_Gr, Gr_Cl, Gr_Rt, Gr_Cf, Gr_Mg, Gr_Out],
    [Cl_Gr, Cl_Cl, Cl_Rt, Cl_Cf, Cl_Mg, Cl_Out],
    [Rt_Gr, Rt_Cl, Rt_Rt, Rt_Cf, Rt_Mg, Rt_Out],
    [Cf_Gr, Cf_Cl, Cf_Rt, Cf_Cf, Cf_Mg, Cf_Out],
    [Mg_Gr, Mg_Cl, Mg_Rt, Mg_Cf, Mg_Mg, Mg_Out],
    [Out_Gr, Out_Cl, Out_Rt, Out_Cf, Out_Mg, Out_Out]])

    print(df_info_0[x+1])
    matrix_n = matrix / (df_info_0[x+1])
    np.set_printoptions(precision=4)

    #print(f'matrix:\n{matrix}')
    #print(f'matrix_n:\n{matrix_n}')

    return matrix, matrix_n

#↓　使用例ーこれでマトリックスが取得可能
# lengthはcsvの行数を表す
#for x in range(0,length-1):
    #mat_x, result_x = generate_matrix(df,x)
    #print(f'mat_{x}:\n{mat_x}\nresult_{x}:\n{result_x}')
