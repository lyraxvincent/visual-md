# EDA on the final sub dataframe


```python
# import necessary libraries
##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')
sns.set_palette('bright')
sns.set_context('notebook')
```


```python
df = pd.read_csv("csv files/final_subdf.csv", parse_dates=['Date'])
```


```python
df.head(3)
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>HomeTeam</th>
      <th>AwayTeam</th>
      <th>HomeTeam_n</th>
      <th>AwayTeam_n</th>
      <th>FTHG</th>
      <th>FTAG</th>
      <th>B365H</th>
      <th>B365D</th>
      <th>B365A</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010-08-14</td>
      <td>Aston Villa</td>
      <td>West Ham</td>
      <td>25.0</td>
      <td>11.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>3.30</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010-08-14</td>
      <td>Blackburn</td>
      <td>Everton</td>
      <td>33.0</td>
      <td>14.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.88</td>
      <td>3.25</td>
      <td>2.5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010-08-14</td>
      <td>Bolton</td>
      <td>Fulham</td>
      <td>3.0</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.20</td>
      <td>3.30</td>
      <td>3.4</td>
    </tr>
  </tbody>
</table>





```python
# A plot of how much the teams played from home
##
plt.figure(figsize=(12,6))
sns.countplot(y='HomeTeam', data=df)
plt.tight_layout()
```


    
![png](epl_bets_pred_files/epl_bets_pred_4_0.png)
    



```python
# A plot of how much the teams played from away
##
plt.figure(figsize=(12,6))
sns.countplot(y='AwayTeam', data=df)
plt.tight_layout()
```


    
![png](epl_bets_pred_files/epl_bets_pred_5_0.png)
    



```python
# new column 'result' to show home-win, draw or away-win
##
df['result'] = np.nan

for i, team in enumerate(df.HomeTeam):
    if df.loc[i, 'FTHG'] > df.loc[i, 'FTAG']:
        df.loc[i, 'result'] = 'Home Win'
    elif df.loc[i, 'FTHG'] == df.loc[i, 'FTAG']:
        df.loc[i, 'result'] = 'Draw'
    elif df.loc[i, 'FTHG'] < df.loc[i, 'FTAG']:
        df.loc[i, 'result'] = 'Away Win'
    else:
        pass
```


```python
df.head()
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>HomeTeam</th>
      <th>AwayTeam</th>
      <th>HomeTeam_n</th>
      <th>AwayTeam_n</th>
      <th>FTHG</th>
      <th>FTAG</th>
      <th>B365H</th>
      <th>B365D</th>
      <th>B365A</th>
      <th>result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010-08-14</td>
      <td>Aston Villa</td>
      <td>West Ham</td>
      <td>25.0</td>
      <td>11.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>3.30</td>
      <td>4.0</td>
      <td>Home Win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010-08-14</td>
      <td>Blackburn</td>
      <td>Everton</td>
      <td>33.0</td>
      <td>14.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.88</td>
      <td>3.25</td>
      <td>2.5</td>
      <td>Home Win</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010-08-14</td>
      <td>Bolton</td>
      <td>Fulham</td>
      <td>3.0</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.20</td>
      <td>3.30</td>
      <td>3.4</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2010-08-14</td>
      <td>Chelsea</td>
      <td>West Brom</td>
      <td>31.0</td>
      <td>21.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1.17</td>
      <td>7.00</td>
      <td>17.0</td>
      <td>Home Win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2010-08-14</td>
      <td>Sunderland</td>
      <td>Birmingham</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.10</td>
      <td>3.30</td>
      <td>3.6</td>
      <td>Draw</td>
    </tr>
  </tbody>
</table>




```python
# distribution of results
##
sns.countplot('result', data=df, order=['Home Win', 'Away Win', 'Draw'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f68189759a0>




    
![png](epl_bets_pred_files/epl_bets_pred_8_1.png)
    



```python
# plot to show home wins for every team
##
plt.figure(figsize=(12,7))
sns.countplot(y='HomeTeam',data=df[df.result == 'Home Win'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f68189fd7f0>




    
![png](epl_bets_pred_files/epl_bets_pred_9_1.png)
    


Man City has the most Home Wins  
Leeds has the least


```python
# plot to show Away wins for every team
##
plt.figure(figsize=(12,7))
sns.countplot(y='AwayTeam',data=df[df.result == 'Away Win'])
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f6818df2e80>




    
![png](epl_bets_pred_files/epl_bets_pred_11_1.png)
    


Man City has the most Away Wins  
Middlesbrough has the least  


```python
# plot to show draws
##
fig, ax = plt.subplots(1, 2, figsize=(12,8))
sns.countplot(y='HomeTeam', data=df[df.result == 'Draw'], ax=ax[0])
ax[0].set_title("HomeTeam")
sns.countplot(y='AwayTeam', data=df[df.result == 'Draw'], ax=ax[1])
ax[1].set_title("AwayTeam")

plt.tight_layout()
```


    
![png](epl_bets_pred_files/epl_bets_pred_13_0.png)
    


Everton has most Draws from Home  
Leeds has the least  

Everton also has the most Draws from Away  
Reading has the least




```python
# preview which teams the above teams(esp. Everton) have Drawn with
##
df[(df.HomeTeam == 'Everton') & (df.result == 'Draw')]
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>HomeTeam</th>
      <th>AwayTeam</th>
      <th>HomeTeam_n</th>
      <th>AwayTeam_n</th>
      <th>FTHG</th>
      <th>FTAG</th>
      <th>B365H</th>
      <th>B365D</th>
      <th>B365A</th>
      <th>result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>2010-08-21</td>
      <td>Everton</td>
      <td>Wolves</td>
      <td>14.0</td>
      <td>17.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.50</td>
      <td>4.00</td>
      <td>7.00</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>31</th>
      <td>2010-11-09</td>
      <td>Everton</td>
      <td>Man United</td>
      <td>14.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>4.20</td>
      <td>3.40</td>
      <td>1.91</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>114</th>
      <td>2010-10-11</td>
      <td>Everton</td>
      <td>Bolton</td>
      <td>14.0</td>
      <td>3.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.62</td>
      <td>3.75</td>
      <td>6.00</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>160</th>
      <td>2010-11-12</td>
      <td>Everton</td>
      <td>Wigan</td>
      <td>14.0</td>
      <td>18.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.40</td>
      <td>4.50</td>
      <td>9.00</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>224</th>
      <td>2011-01-22</td>
      <td>Everton</td>
      <td>West Ham</td>
      <td>14.0</td>
      <td>11.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.50</td>
      <td>4.00</td>
      <td>7.50</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>11461</th>
      <td>2014-03-12</td>
      <td>Everton</td>
      <td>Hull</td>
      <td>14.0</td>
      <td>26.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.53</td>
      <td>4.33</td>
      <td>7.00</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>11526</th>
      <td>2015-10-01</td>
      <td>Everton</td>
      <td>Man City</td>
      <td>14.0</td>
      <td>34.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>4.50</td>
      <td>3.75</td>
      <td>1.85</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>11542</th>
      <td>2015-01-19</td>
      <td>Everton</td>
      <td>West Brom</td>
      <td>14.0</td>
      <td>21.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.85</td>
      <td>3.60</td>
      <td>4.75</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>11554</th>
      <td>2015-07-02</td>
      <td>Everton</td>
      <td>Liverpool</td>
      <td>14.0</td>
      <td>30.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>3.40</td>
      <td>3.40</td>
      <td>2.30</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>11580</th>
      <td>2015-02-22</td>
      <td>Everton</td>
      <td>Leicester</td>
      <td>14.0</td>
      <td>16.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.83</td>
      <td>3.60</td>
      <td>5.00</td>
      <td>Draw</td>
    </tr>
  </tbody>
</table>




```python
plt.figure(figsize=(12,7))
sns.countplot(y='AwayTeam', data=df[(df.HomeTeam == 'Everton') & (df.result == 'Draw')])
plt.title("Teams that did Draw with Everton(Home)")
```




    Text(0.5, 1.0, 'Teams that did Draw with Everton(Home)')




    
![png](epl_bets_pred_files/epl_bets_pred_16_1.png)
    


Liverpool did Draw the most with Everton while Everton was the Home Team



```python
plt.figure(figsize=(12,7))
sns.countplot(y='HomeTeam', data=df[(df.AwayTeam == 'Everton') & (df.result == 'Draw')])
plt.title("Teams that did Draw with Everton(Away)")
```




    Text(0.5, 1.0, 'Teams that did Draw with Everton(Away)')




    
![png](epl_bets_pred_files/epl_bets_pred_18_1.png)
    


Crystal Palace did Draw the most with Everton while Everton was the Away Team


```python
# heatmap
##
plt.figure(figsize=(12,7))
sns.heatmap(df.corr())
```




    <matplotlib.axes._subplots.AxesSubplot at 0x7f6817e3d9a0>




    
![png](epl_bets_pred_files/epl_bets_pred_20_1.png)
    



```python
# pairplot
##
sns.pairplot(df, hue='result')
```




    <seaborn.axisgrid.PairGrid at 0x7f681898bdf0>




    
![png](epl_bets_pred_files/epl_bets_pred_21_1.png)
    



```python
df.head()
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>HomeTeam</th>
      <th>AwayTeam</th>
      <th>HomeTeam_n</th>
      <th>AwayTeam_n</th>
      <th>FTHG</th>
      <th>FTAG</th>
      <th>B365H</th>
      <th>B365D</th>
      <th>B365A</th>
      <th>result</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010-08-14</td>
      <td>Aston Villa</td>
      <td>West Ham</td>
      <td>25.0</td>
      <td>11.0</td>
      <td>3.0</td>
      <td>0.0</td>
      <td>2.00</td>
      <td>3.30</td>
      <td>4.0</td>
      <td>Home Win</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010-08-14</td>
      <td>Blackburn</td>
      <td>Everton</td>
      <td>33.0</td>
      <td>14.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2.88</td>
      <td>3.25</td>
      <td>2.5</td>
      <td>Home Win</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010-08-14</td>
      <td>Bolton</td>
      <td>Fulham</td>
      <td>3.0</td>
      <td>29.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2.20</td>
      <td>3.30</td>
      <td>3.4</td>
      <td>Draw</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2010-08-14</td>
      <td>Chelsea</td>
      <td>West Brom</td>
      <td>31.0</td>
      <td>21.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1.17</td>
      <td>7.00</td>
      <td>17.0</td>
      <td>Home Win</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2010-08-14</td>
      <td>Sunderland</td>
      <td>Birmingham</td>
      <td>5.0</td>
      <td>20.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.10</td>
      <td>3.30</td>
      <td>3.6</td>
      <td>Draw</td>
    </tr>
  </tbody>
</table>




```python
# the last dataframe for use in modeling
##
last_df = df[['Date', 'HomeTeam', 'AwayTeam', 'HomeTeam_n', 'AwayTeam_n', 'B365H', 'B365D', 'B365A', 'result']]
```


```python
# sort by date
##
last_df = last_df.sort_values('Date')

last_df.reset_index(drop=True, inplace=True)
```


```python
last_df.to_csv("csv files/lastdf.csv", index=False)
```
