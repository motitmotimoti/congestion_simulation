# congestion_simulation

これはショッピングモールを想定したシミュレーションである。

Agent_manの戦略：ランダム戦略(2019/07/10現在)

## 手順
* main.py内のnum_agentとnum_new_agentの乱数を設定
* `python3 main.py`の実行(__母数に応じてcsvファイルの保存先の変更を！！！__)
  * result/(high, medium, low)/日付　にcsvが生成されていることを確認
* 上記で得られたcsvファイルから状態遷移確率分布の取得
  * `python3 Markov_chain.py`の実行(__母数に応じてnumpyの保存先の変更を!!!__)
  *  matrix/(high, medium, low)/日付　に.npyが生成されていることを確認
  *  Markov_chain.pyを実行することで店舗ごとの確率分布も取得可能(markov/内に保存される）
 
 ## 分析
 * Markov_analyze.pyにおいて用いる初期状態とmatrixのディレクトリを指定する
 * `python3 Markov_analyze.py`の実行(__用いたmatrixに応じたディレクトリに保存する__)
   * analyze/に保存される
 * 用いた初期状態のデータに関してmarkov/内のものとanalyze/内のもので比較する
 
２つのデータの比較手法：？？？

