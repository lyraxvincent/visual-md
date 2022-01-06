<h1 align="center">Plots</h1>

-----

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
# distribution of results
##
sns.countplot('result', data=df, order=['Home Win', 'Away Win', 'Draw'])
```

![png](epl_bets_pred_files/epl_bets_pred_8_1.png)

```python
# plot to show home wins for every team
##
plt.figure(figsize=(12,7))
sns.countplot(y='HomeTeam',data=df[df.result == 'Home Win'])
```

![png](epl_bets_pred_files/epl_bets_pred_9_1.png)

```python
# plot to show Away wins for every team
##
plt.figure(figsize=(12,7))
sns.countplot(y='AwayTeam',data=df[df.result == 'Away Win'])
```

![png](epl_bets_pred_files/epl_bets_pred_11_1.png)

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

```python
plt.figure(figsize=(12,7))
sns.countplot(y='AwayTeam', data=df[(df.HomeTeam == 'Everton') & (df.result == 'Draw')])
plt.title("Teams that did Draw with Everton(Home)")
```

![png](epl_bets_pred_files/epl_bets_pred_16_1.png)

```python
plt.figure(figsize=(12,7))
sns.countplot(y='HomeTeam', data=df[(df.AwayTeam == 'Everton') & (df.result == 'Draw')])
plt.title("Teams that did Draw with Everton(Away)")
```

![png](epl_bets_pred_files/epl_bets_pred_18_1.png)

```python
# heatmap
##
plt.figure(figsize=(12,7))
sns.heatmap(df.corr())
```

![png](epl_bets_pred_files/epl_bets_pred_20_1.png)

```python
# pairplot
##
sns.pairplot(df, hue='result')
```

![png](epl_bets_pred_files/epl_bets_pred_21_1.png)

