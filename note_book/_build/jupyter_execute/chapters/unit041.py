#!/usr/bin/env python
# coding: utf-8

# # Introduction to Imperfectly Competitive Markets

# ```{admonition} Perfect vs. Imperfect Competition
# 
# - Perfectly competitive firms are **price takers**, so the demand curve is constant and equal to MR.
# - Imperfectly competitive firms have downward sloping demand curves.
#     - MR is **not** equal to the demand!!!
#     - Firms must lower price to sell additional units.
# ```
# 
# > The table below shows the demand and marginal revenue curves in an imperfectly competitive market.

# |P(\$)|Qd|TR(\$)|MR(\$)|
# |---|---|---|---|
# |6|0|0|-|
# |5|1|5|5|
# |4|2|8|3|
# |3|3|9|1|
# |2|4|8|-1|
# |1|5|5|-3|

# In an imperfectly competitive market,
# - Firms must lower price to sell additional units, so MR is below D.
# - PED of points along the demand curve are different
#     - Point of MR = 0 is unit elastic;
#     - Points above unit elasticity are more elastic;
#     - Points below unit elasticity are more inelastic.
# - Firms only produce at elastic points because the total revenue reduces.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df = pd.DataFrame(data={'p': list(range(5,0,-1)),
                        'q': list(range(1,6)),
                        'mr':[5, 3, 1, -1, -3],
                        'tr': [5, 8, 9, 8, 5]})

fig1 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('q', title='Q', scale=alt.Scale(domain=[0,6]), axis=alt.Axis(tickMinStep=1, offset=-120)),
    alt.Y('p', title='P', scale=alt.Scale(domain=[0,6])),
).properties(title='Demand and Marginal Revenue of Imperfect Competition')

fig2 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white', color='green'), color='green').encode(
    alt.X('q', title='Q', scale=alt.Scale(domain=[0,6])),
    alt.Y('mr', title='P', scale=alt.Scale(domain=[-4,6])),
)

text1 = alt.Chart({'values':[{'x': 5.2, 'y': 1}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 5.3, 'y': -3}]}).mark_text(
    text='MR',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig_mr = fig1 + fig2 + text1 + text2


fig3 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('q', title='Q', scale=alt.Scale(domain=[0,6]), axis=alt.Axis(tickMinStep=1)),
    alt.Y('tr', title='Total Revenue', scale=alt.Scale(domain=[5,9])),
).properties(title='Total Revenue of Imperfect Competition')
fig_mr&fig3

