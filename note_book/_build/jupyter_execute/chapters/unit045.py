#!/usr/bin/env python
# coding: utf-8

# # Oligopoly and Game Theory

# Oligopoly
# : A very small number of firms have market dominance (less than 10).
# : Firms use strategic pricing (**price interdependence**).
# 
# Features of oligopoly:
# - A few large producers
# - Identical or differentiated products
# - High barriers to entry
# - Control over price (price maker)
# - Collusion

# Collusion
# : An agreement (usually illegal) is drawn up to agree on what price and quantity will be produced in a market.
# : e.g. OPEC, also called **cartel** (a groups of firms acting together and not to compete).

# ## Oligopoly with Game Theory

# ```{admonition} Prisoner's Dilemma
# Charged with a crime, each prisoner has one of 2 choices: Deny or Confess. What would they choose?<br>
# 
# Both A and B would choose to confess.<br>
# 
# |   |B|Deny|Confess|
# |:---|:---|:---|:---|
# |**A**|**Deny**|5 years<br>each|B = free<br>A = 20 years|
# ||**Confess**|A = free<br>B = 20 years|10 years<br>each|
# 
# This example shows that when each individual pursues their own self-interest, the outcome is worse than if they had both cooperated.<br>
# 
# So, firms have an incentive to collude but also an incentive to cheat on the agreement.
# ```

# Game theory
# : Study of how people and firms act strategically in the context of a game.

# > Within oligopolies, the strategies employed by a firm to maximize profits depend on other firms' actions. A firm may have a **dominant strategy**.

# Dominant strategy
# : Best choice for a player regardless of what the other players chooses.

# **Example**<br>
# Firm A and Firm B have 2 pricing options whether to set a high price or a low price. If both A and set a high price, A will make \$100 and B will make \$50.
# 
# |   |B|High|Low|
# |:---|:---|:---|:---|
# |**A**|**High**|A = \$100<br>B = \$50|A = \$60<br>B = \$90|
# ||**Lows**|A = \$50<br>B = \$40|A = \$20<br>B = \$10|

# - Based on the matrix above, A has a dominant strategy, pricing at a **high** price because A would always have greater profits regardless of B's choice.
# - But B doesn't have a dominant strategy.
# - Since A would set a high price anyway, B should set a low price to make more profits.
# - When A sets high and B sets low, it's called **nash equilibrium**.

# Nash equilibrium
# : Optimal outcome that will occur when both firms make decisions simultaneously and have no incentive to change.

# ## Graphs of Colluding Oligopolies
# 
# 1. Cartels set price and output at an agreed upon level; 
# 1. Firms require identical or highly similar demand and costs; 
# 1. Cartel must have a way to punish cheaters;
# 1. Together they act as a monopoly.
# 
# Firms in a colluding oligopoly act as a **monopoly** and share the profit.

# ### Kinked Demand Curve Model
# 
# > It shows how noncollusive firms are interdependent.
# 
# If firms are not colluding they are likely to react to competitors’ pricing in 2 ways:
# - Match price/**Price leadership**<br>If one firm cuts it’s prices, then the other firms follow suit causing inelastic demand.
# - Ignore change<br>If one firm raises prices, others maintain same price causing elastic demand.

# > The figure below shows the kinked demand curve model of a non-colluded oligopoly.
# 
# 1. If this firm increases its price, other firms will ignore it and keep prices the same. As the only firm with high prices, quantity demanded for this firm will decrease a lot and the demand curve will become **elastic**.
# 1. If this firm decreases its price, other firms will match it and lower their prices. Since all firms have lower prices, quantity demanded for this firm will increase only a little and the demand curve will become **inelastic**.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df = pd.DataFrame(data={'p': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                        'q': [4, 8, 12, 13, 14, 15, 16, 17, 18, 19]
                       })
fig1 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('q', title='Q', scale=alt.Scale(domain=[0,20])),
    alt.Y('p', title='P', scale=alt.Scale(domain=[0,11]))
).properties(title='Demand of Non-colluded Oligopolies')

df_v1 = pd.DataFrame(data={'p': [0, 8], 'q': [12, 12]})
fig_v1 = alt.Chart(df_v1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('p')
)

df_h1 = pd.DataFrame(data={'p': [8, 8], 'q': [0, 12]})
fig_h1 = alt.Chart(df_h1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('p')
)

text1 = alt.Chart({'values':[{'x': 12, 'y': 8.4}]}).mark_text(
    text='E',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 8, 'y': 9.4}]}).mark_text(
    text='Elastic',
    fontSize=15,
    angle=21
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 16, 'y': 4.7}]}).mark_text(
    text='Inelastic',
    fontSize=15,
    angle=52
).encode(x='x:Q', y='y:Q')

fig1 + fig_v1 + fig_h1 + text1 + text2 + text3

