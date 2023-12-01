#!/usr/bin/env python
# coding: utf-8

# # The Effects of Government Intervention in Markets

# > When a government intervenes to regulate prices, we say that it imposes price controls.<br>
# > When a government intervenes to regulate quantity, we say that it imposes quantity controls.
# 
# Price control
# : Legal restrictions on how high or low a market price may go.
# : e.g. price ceiling, price floor.<br><br>
# 
# Quantity control/Quota
# : An upper limit on the quantity of some good that can be bought or sold.

# ## Price Controls
# ### Price Ceiling
# 
# Price ceiling
# : A type of price control set by governments as shown in the figure below.
# : It sets the maximum amount a seller can charge for a good or service.
# : Typically imposed on consumer staples, like food, gas, or medicine, often after a crisis or particular event sends costs skyrocketing.

# ```{Tip}
# The price ceiling will always be lower than the original equilibrium price. Otherwise, it will be meaningless as the market will always reach the equilibrium without touching the price ceiling.
# ```

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

df_e = pd.DataFrame(data={'price': [5.5, 3, 3],
                        'q': [4.5, 2, 7]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5, 'y': 5.5}]}).mark_text(
    text='E',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 2, 'y': 3.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 7, 'y': 3.5}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 8.7, 'y': 3.3}]}).mark_text(
    text='Price Ceiling',
    fontSize=15
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [3, 3], 'q': [0, 10]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black').encode(
    alt.X('q'),
    alt.Y('price')
)

df_v2 = pd.DataFrame(data={'price': [0, 3], 'q': [2, 2]})
fig_v2 = alt.Chart(df_v2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [0, 3], 'q': [7, 7]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 + fig_h2 + fig_v2 + fig_v3).properties(title='Price Ceiling')


# #### Inefficient Allocation at the Price Ceiling
# 
# - Shortage
# - Wasted resources<br>
# People expend money, effort, and time to cope with the shortages caused by the price ceiling.
# - Inefficiently low quality
# - Black markets
# 
# Black market
# : A market in which goods or services are bought and sold illegally, either because it is illegal to sell them at all or because the prices charged are legally prohibited by a price ceiling.
# : Encourage disrespect for the law and illegal activities.

# ### Price Floor
# 
# Price floor
# : A type of price control set by governments as shown in the figure below. 
# : It sets the minimum price for a good or service.
# : Typically imposed on wages and agricultural products, such as wheat and milk.

# ```{Tip}
# The price floor will always be higher than the original equilibrium price. Otherwise, it will be meaningless as the market will always reach the equilibrium without touching the price floor.
# ```

# In[3]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 8, 8],
                        'q': [4.5, 2, 7]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5, 'y': 5.5}]}).mark_text(
    text='E',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 2, 'y': 8.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 7, 'y': 8.5}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 8.7, 'y': 8.3}]}).mark_text(
    text='Price Floor',
    fontSize=15
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [8, 8], 'q': [0, 10]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black').encode(
    alt.X('q'),
    alt.Y('price')
)

df_v2 = pd.DataFrame(data={'price': [0, 8], 'q': [2, 2]})
fig_v2 = alt.Chart(df_v2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [0, 8], 'q': [7, 7]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 + fig_h2 + fig_v2 + fig_v3).properties(title='Price Floor')


# #### Inefficient Allocation at the Price Floor
# 
# - Surplus/Inefficiently low quantity
# - Wasted resources<br>
# Unwanted goods or services.
# - Inefficiently high quality
# - Illegal activities

# ## Quantity Control
# 
# Quantity control/Quota
# : Upper limit on the quantity of some goof that can be bought or sold.<br><br>
# 
# License
# : Give its owner the right to supply a good or service.

# In[ ]:




