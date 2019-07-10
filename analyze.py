import pandas as pd
import numpy as np



#df = pd.read_csv('result_list_state.csv', index_col=0)
#df = df.fillna('Na')
#length = len(df)
#print(length)
#print(df)



def generate_matrix(df_csv,df_info,dist, x):

    #現在と1つ後の総Agent_manのstateの取得
    df_0 = df_csv[x:x+2]
    #print(df_0)
    list_0 = df_0.values.tolist()
    list_1 = [state for state in list_0[0] if state != 'Na']
    #print(len(list_1))
    list_2 = [state for state in list_0[1] if state != 'Na']
    #print(len(list_2))

    #現在と１つ後の総Agent_manのstateの総数を合わせる。（New_Agentは0_Outにいたこととする。）
    list_1_n = list_1 + ['0_Out' for i in range(len(list_2)-len(list_1))]

    #print(len(list_1))
    #print(len(list_1_n))
    #print(list_1)
    #print(list_2)
    #print(list_2)

    #count_store_allの取得
    df_info_0 = df_info.iloc[:,7]
    df_info_0 = df_info_0.values.tolist()

    #Newの取得
    new = df_info.iloc[:,5]
    new = new.values.tolist()

    """
    Gr_Gr, Gr_Cl, Gr_Rt, Gr_Cf, Gr_Mg, Gr_Out = 0, 0, 0, 0, 0, 0
    Cl_Gr, Cl_Cl, Cl_Rt, Cl_Cf, Cl_Mg, Cl_Out = 0, 0, 0, 0, 0, 0
    Rt_Gr, Rt_Cl, Rt_Rt, Rt_Cf, Rt_Mg, Rt_Out = 0, 0, 0, 0, 0, 0
    Cf_Gr, Cf_Cl, Cf_Rt, Cf_Cf, Cf_Mg, Cf_Out = 0, 0, 0, 0, 0, 0
    Mg_Gr, Mg_Cl, Mg_Rt, Mg_Cf, Mg_Mg, Mg_Out = 0, 0, 0, 0, 0, 0
    Out_Gr, Out_Cl, Out_Rt, Out_Cf, Out_Mg, Out_Out = 0, 0, 0, 0, 0, 0
    """

    #total = []
    Gr_x = [0] * 6 # 0:Gr 1:Cl 2:Rt 3:Cf 4:Mg 5:Out
    Cl_x = [0] * 6
    Rt_x = [0] * 6
    Cf_x = [0] * 6
    Mg_x = [0] * 6
    Out_x = [0] * 6



    #np.set_printoptions(precision=4)

    #初期状態の0_Outへの代入
    print(f'new:{new[x+1]}')
    print(f'df_info_0:{df_info_0[x]}')
    dist[0,5] = float( new[x+1] / (df_info_0[x]+new[x+1]))
    print(f'dist:{dist}')


    #遷移数のカウント
    for i, list in enumerate(list_1_n):
        #print(f'i{i}:{list}')
        if list == 'Gr_In':
            if list_2[i] == 'Gr_In':
                Gr_x[0] += 1
            elif list_2[i] =='Cl_In':
                Gr_x[1] += 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Gr_x[2] += 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Gr_x[3] += 1
            elif list_2[i] == 'Mg_In':
                Gr_x[4] += 1
            elif list_2[i] == '0_Out':
                Gr_x[5] += 1


        elif list == 'Cl_In':
            if list_2[i] == 'Gr_In':
                Cl_x[0] += 1
            elif list_2[i] == 'Cl_In':
                Cl_x[1] += 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Cl_x[2] += 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Cl_x[3] += 1
            elif list_2[i] == 'Mg_In':
                Cl_x[4] += 1
            elif list_2[i] == '0_Out':
                Cl_x[5] += 1

        elif list == 'Rt_In' or list == 'Rt_Wt':
            if list_2[i] == 'Gr_In':
                Rt_x[0] += 1
            elif list_2[i] == 'Cl_In':
                Rt_x[1] += 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Rt_x[2] += 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Rt_x[3] += 1
            elif list_2[i] == 'Mg_In':
                Rt_x[4] += 1
            elif list_2[i] == '0_Out':
                Rt_x[5] += 1

        elif list == 'Cf_In' or list == 'Cf_Wt':
            if list_2[i] == 'Gr_In':
                Cf_x[0] += 1
            elif list_2[i] == 'Cl_In':
                Cf_x[1] += 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Cf_x[2] += 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Cf_x[3] += 1
            elif list_2[i] == 'Mg_In':
                Cf_x[4] += 1
            elif list_2[i] == '0_Out':
                Cf_x[5] += 1

        elif list == 'Mg_In':
            if list_2[i] == 'Gr_In':
                Mg_x[0] += 1
            elif list_2[i] == 'Cl_In':
                Mg_x[1] += 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Mg_x[2] += 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Mg_x[3] += 1
            elif list_2[i] == 'Mg_In':
                Mg_x[4] += 1
            elif list_2[i] == '0_Out':
                Mg_x[5] += 1

        elif list == '0_Out':
            if list_2[i] == 'Gr_In':
                Out_x[0] += 1
            elif list_2[i] == 'Cl_In':
                Out_x[1] += 1
            elif list_2[i] == 'Rt_In' or list_2[i] == 'Rt_Wt':
                Out_x[2] += 1
            elif list_2[i] == 'Cf_In' or list_2[i] == 'Cf_Wt':
                Out_x[3] += 1
            elif list_2[i] == 'Mg_In':
                Out_x[4] += 1
            #elif list_2[i] == '0_Out':
                #Cl_Out = Cl_Out + 1

    #遷移数リストをnumpyへ変換
    Gr_x_num = np.array(Gr_x)
    Cl_x_num = np.array(Cl_x)
    Rt_x_num = np.array(Rt_x)
    Cf_x_num = np.array(Cf_x)
    Mg_x_num = np.array(Mg_x)
    Out_x_num = np.array(Out_x)

    #遷移数行列へ
    matrix = np.r_[Gr_x_num, Cl_x_num, Rt_x_num, Cf_x_num, Mg_x_num, Out_x_num]
    matrix = np.reshape(matrix,(6,6))

    #現在のショッピングモール内にいる人数 + New_Agentの数(0_Outにいる人数) = 現在の総数
    total = df_info_0[x]+new[x+1]
    print(f'total:{total}')



    #遷移確率分布　ex) P(Gr|Gr) = P(Gr∧Gr) / p(Gr)
    Gr_x_num_n = (Gr_x_num / total) / dist[0][0]
    Cl_x_num_n = (Cl_x_num / total) / dist[0][1]
    Rt_x_num_n = (Rt_x_num / total) / dist[0][2]
    Cf_x_num_n = (Cf_x_num / total) / dist[0][3]
    Mg_x_num_n = (Mg_x_num / total) / dist[0][4]
    Out_x_num_n = (Out_x_num / total) / dist[0][5]


    matrix_n = np.r_[Gr_x_num_n, Cl_x_num_n, Rt_x_num_n, Cf_x_num_n, Mg_x_num_n, Out_x_num_n]
    matrix_n = np.reshape(matrix_n,(6,6))



    return matrix, matrix_n

#↓　使用例ーこれでマトリックスが取得可能
# lengthはcsvの行数を表す
#for x in range(0,length-1):
    #mat_x, result_x = generate_matrix(df,x)
    #print(f'mat_{x}:\n{mat_x}\nresult_{x}:\n{result_x}')
