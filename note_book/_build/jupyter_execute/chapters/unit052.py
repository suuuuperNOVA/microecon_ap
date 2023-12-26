#!/usr/bin/env python
# coding: utf-8

# # Changes in Factor Demand and Factor Supply

# > The demand in the product market in turn creates a demand for the inputs used in production such as labor, which is known as **derived demand**.

# The supply and demand model can also be used to show the resource/input market as show in the figure below.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_e = pd.DataFrame(data={'price': [5.5],
                        'q': [4.5]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity of Workers', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Wage Rate', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity of Workers', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Wage Rate', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='DL',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='SL',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5, 'y': 5.5}]}).mark_text(
    text='E',
    fontSize=15
).encode(x='x:Q', y='y:Q')

df_h1 = pd.DataFrame(data={'price': [5.5, 5.5], 'q': [0, 4.5]})
fig_h1 = alt.Chart(df_h1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v1 = pd.DataFrame(data={'price': [0, 5.5], 'q': [4.5, 4.5]})
fig_v1 = alt.Chart(df_v1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + fig_h1 + fig_v1).properties(title='Supply and Demand for Labor')


# ## Shifting Resource Demand
# 
# **Changes in the product demand**<br>
# An increase in the price of a product then increases MRP and the resources used in production. This would result in more labor being hired.
# 
# Price of product ↑/Product demand ↑ increases the demand of labor (shifting to right).
# 
# **Changes in productivity**<br>
# Increases in productivity can make a firm more profitable and give it a greater incentive to employ more resources and utilize the increased productivity of resources.
# 
# Productivity ↑ increases the demand of labor (shifting to right).
# 
# **Changes in the prices of other resources**<br>
# - Substitute resources<br>If the price of farm machinery decreases relative to farm laborers, the demand of machinery will increase and the demand of laborers will decrease.
# - Complementary resources<br>If the price of raw materials decreases, more profitable and the demand of laborers will increase.
# 

# In[3]:


df_d2 = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(11,1,-1))
                       })

df_e = pd.DataFrame(data={'price': [6.5],
                        'q': [5.5]
                       })

fig_eq2 = alt.Chart(df_d2).mark_line(clip=True, color='green').encode(
    alt.X('qd', title='Quantity of Workers', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Wage Rate', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9.2, 'y': 1.5}]}).mark_text(
    text='DL0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5, 'y': 5.5}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6, 'y': 6.5}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 8, 'y': 2.9}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 9.7, 'y': 3}]}).mark_text(
    text='DL1',
    fontSize=15
).encode(x='x:Q', y='y:Q')


(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 +fig_eq2).properties(title='Shifts of Demand of Labor')


# ## Shifting Resource Supply
# 
# **Changes in preferences for leisure**<br>
# If people prefer less leisure time, they will choose to work more, increasing the supply of laborers (shift to right).
# 
# **Changes in population/immigration**<br>
# If the population increases, or immigrants increases, the supply of laborers will increase (shift to right).
# 
# **Changes in working condition**<br>
# If the work condition is improved, the supply of laborers will increase (shift to right).
# 
# **Changes in education/training**<br>
# If the more people are educated , the supply of skilled laborers will increase (shift to right).

# In[4]:


df_s2 = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(2,12))
                       })

df_e = pd.DataFrame(data={'price': [4.5],
                        'q': [5.5]
                       })

fig_eq2 = alt.Chart(df_s2).mark_line(clip=True, color='green').encode(
    alt.X('qs', title='Quantity of Workers', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Wage Rate', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='SL0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5, 'y': 5.5}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6, 'y': 4.5}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 8, 'y': 8}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 9, 'y': 7.5}]}).mark_text(
    text='SL1',
    fontSize=15
).encode(x='x:Q', y='y:Q')


(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 +fig_eq2).properties(title='Shifts of Supply of Labor')

