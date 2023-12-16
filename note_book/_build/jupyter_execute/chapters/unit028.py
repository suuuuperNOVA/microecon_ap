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
# : Upper limit on the quantity of some good that can be bought or sold.<br><br>
# 
# License
# : Give its owner the right to supply a good or service.<br><br>
# 
# > Previously, the market was at the equilibrium (Point E) where the equilibrium price was 5.5 dollars. Then, the government imposes a quota on the products. Although suppliers are willing to produce 2 units at a price of 3 dollars (Point B), buyers are willing to pay 8 dollars (Point A). So, the producers will sell their products at 8 dollars. The price difference of Point A and Point B is known as the quota cost, and producers transfer the quota cost to buyers.
# 
# Wedge
# : Quantity control/Quota drives a wedge between the demand price and the supply price of a good. The price paid by buyers ends up being higher than that received by sellers.<br><br>
# 
# Quota rent
# : The difference between the demand and supply price at the quota amount.
# : Market price of the license when the licenses are traded.
# : Opportunity cost of license-holder.

# In[4]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 8, 3],
                        'q': [4.5, 2, 2]
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

text4 = alt.Chart({'values':[{'x': 2.3, 'y': 8.2}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 2.3, 'y': 2.9}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 2.6, 'y': 1}]}).mark_text(
    text='Quota',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 1.7, 'y': 5.5}]}).mark_text(
    text='Wedge',
    fontSize=15,
    angle=270
).encode(x='x:Q', y='y:Q')

df_v2 = pd.DataFrame(data={'price': [0, 10], 'q': [2, 2]})
fig_v2 = alt.Chart(df_v2).mark_line(color='black').encode(
    alt.X('q'),
    alt.Y('price')
)

df_h2 = pd.DataFrame(data={'price': [3, 3], 'q': [0, 2]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h3 = pd.DataFrame(data={'price': [8, 8], 'q': [0, 2]})
fig_h3 = alt.Chart(df_h3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 + text7 + fig_v2 + fig_h2 + fig_h3).properties(title='Quota')


# ### Inefficient Allocation with Quantity Control
# - Missed opportunities
# - Illegal activities

# ## Taxation

# When the government imposes a tax on producers, the supply curve will shift to the left from S0 to S1 and the market equilibrium will shift from E0 to E1. Buyers will pay 7 dollars (at Point E1), but producers will only receive 4 dollars (at Point A). The difference between Point A and Point E1 is the tax return of the government.

# In[5]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_s1 = pd.DataFrame(data={'price': list(range(4, 14)),
                        'qs': list(range(0,10))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 7, 4],
                        'q': [4.5, 3, 3]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s1).mark_line(clip=True).encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11]))
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 5, 'y': 5.5}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 3.5, 'y': 7}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 5.7, 'y': 8.2}]}).mark_text(
    text='Tax',
    fontSize=15,
    angle=270
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 3.5, 'y': 4}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 7, 'y': 10.5}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 2.7, 'y': 5.3}]}).mark_text(
    text='Tax',
    fontSize=15,
    angle=270
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 8, 'y': 10}]}).mark_text(
    text='➟',
    fontSize=40,
    angle = 180
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [8, 8], 'q': [0, 10]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black').encode(
    alt.X('q'),
    alt.Y('price')
)

df_v2 = pd.DataFrame(data={'price': [7, 10], 'q': [6, 6]})
fig_v2 = alt.Chart(df_v2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [4, 7], 'q': [3, 3]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9 + fig_v2 + fig_v3).properties(title='Tax')


# ## Subsidy
# 
# When the government subsidizes producers, the supply curve will shift the right from S0 to S1 and the market equilibrium will shift from E0 to E1. Buyers will 4 dollars (at Point E1), but producers will only receive 7 dollars (at Point A). The difference between Point A and Point E1 is the subsidy from the government.

# In[6]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_s1 = pd.DataFrame(data={'price': list(range(-2, 9)),
                        'qs': list(range(0,11))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 4, 7],
                        'q': [4.5, 6, 6]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s1).mark_line(clip=True).encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11]))
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.5, 'y': 4}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 7.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 9.6, 'y': 7}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 5.7, 'y': 5.5}]}).mark_text(
    text='Subsidy',
    fontSize=15,
    angle=270
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 8, 'y': 7.5}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [8, 8], 'q': [0, 10]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black').encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [4, 7], 'q': [6, 6]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text6 + text7 + text8 + text9 + fig_v3).properties(title='Subsidy')


# ## Deadweight Loss

# Deadweight loss
# : Loss of total surplus when a market fails to reach a competitive equilibrium.

# Within the market equilibrium, there is no deadweight loss and the total surplus (consumer surplus + producer surplus) is maximized.

# In[7]:


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

fig2 = (fig_eq + text1 + text2 + text3 + fig_h1 + fig_v1).properties(title='Market Equilibrium')

text4 = alt.Chart({'values':[{'x': 1, 'y': 7}]}).mark_text(
    text='CS',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 1, 'y': 4}]}).mark_text(
    text='PS',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig2 + text4 + text5


# **Price Ceiling**<br>
# 
# <img src="../pic/unit02_8_dead_ceil.png" alt="dead_ceil" width="500"/>

# **Price Floor**<br>
# 
# <img src="../pic/unit02_8_dead_floor.png" alt="dead_floor" width="500"/>

# **Quota**

# In[8]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 8, 3],
                        'q': [4.5, 2, 2]
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

text4 = alt.Chart({'values':[{'x': 2.3, 'y': 8.2}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 2.3, 'y': 2.9}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 2.6, 'y': 1}]}).mark_text(
    text='Quota',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 1.7, 'y': 5.5}]}).mark_text(
    text='Wedge',
    fontSize=15,
    angle=270
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 3.1, 'y': 5.5}]}).mark_text(
    text='DWL',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

df_v2 = pd.DataFrame(data={'price': [0, 10], 'q': [2, 2]})
fig_v2 = alt.Chart(df_v2).mark_line(color='black').encode(
    alt.X('q'),
    alt.Y('price')
)

df_h2 = pd.DataFrame(data={'price': [3, 3], 'q': [0, 2]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h3 = pd.DataFrame(data={'price': [8, 8], 'q': [0, 2]})
fig_h3 = alt.Chart(df_h3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + fig_v2 + fig_h2 + fig_h3).properties(title='Deadweight Loss of Quota')


# **Taxation**
# - Consumer surplus is the area under the demand curve but above the price buyers pay for.
# - Producer surplus is the area above the supply curve but under the price producers receive.
# - The government has the tax revenue which amounts to the area of the gray rectangle.<br>Q=15, Tax Rate = Price Diff=7-4, Area=15 x 3
# - Tax is paid by both producers and consumers and the proportion is related to elasticity.

# <img src="../pic/unit02_8_dead_tax.png" alt="dead_tax" width="600"/>

# **Subsidy**

# The figure below shows that the amount of money paid by the government for subsidies is the **total area of V, W, X, Y and Z**.

# In[9]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_s1 = pd.DataFrame(data={'price': list(range(-2, 9)),
                        'qs': list(range(0,11))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 4, 7],
                        'q': [4.5, 6, 6]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s1).mark_line(clip=True).encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11]))
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.5, 'y': 4}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 7.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 9.6, 'y': 7}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 5.5, 'y': 5.5}]}).mark_text(
    text='Z',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 8, 'y': 7.5}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

text10 = alt.Chart({'values':[{'x': 2, 'y': 6.2}]}).mark_text(
    text='V',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text11 = alt.Chart({'values':[{'x': 4.5, 'y': 6.2}]}).mark_text(
    text='W',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text12 = alt.Chart({'values':[{'x': 2, 'y': 4.5}]}).mark_text(
    text='X',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text13 = alt.Chart({'values':[{'x': 4.5, 'y': 4.5}]}).mark_text(
    text='Y',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [7, 7], 'q': [0, 6]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h3 = pd.DataFrame(data={'price': [4, 4], 'q': [0, 6]})
fig_h3 = alt.Chart(df_h3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [4, 7], 'q': [6, 6]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h4 = pd.DataFrame(data={'price': [5.5, 5.5], 'q': [0, 4.5]})
fig_h4 = alt.Chart(df_h4).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text4 + text6 + text7 + text8 + text9
 + text10 + text11 + text12 + text13
 + fig_h2 + fig_h3 + fig_v3 + fig_h4).properties(title='Deadweight Loss of Subsidy (a)')


# When the supply curve shifts to the right, the consumer surplus will be increased by **the area of X and Y**.

# In[10]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_s1 = pd.DataFrame(data={'price': list(range(-2, 9)),
                        'qs': list(range(0,11))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 4],
                        'q': [4.5, 6]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s1).mark_line(clip=True).encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11]))
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.5, 'y': 4}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 7.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 9.6, 'y': 7}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 5.5, 'y': 5.5}]}).mark_text(
    text='Z',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 8, 'y': 7.5}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

text10 = alt.Chart({'values':[{'x': 2, 'y': 6.2}]}).mark_text(
    text='V',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text11 = alt.Chart({'values':[{'x': 4.5, 'y': 6.2}]}).mark_text(
    text='W',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text12 = alt.Chart({'values':[{'x': 2, 'y': 4.5}]}).mark_text(
    text='X',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text13 = alt.Chart({'values':[{'x': 4.5, 'y': 4.5}]}).mark_text(
    text='Y',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [7, 7], 'q': [0, 6]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h3 = pd.DataFrame(data={'price': [4, 4], 'q': [0, 6]})
fig_h3 = alt.Chart(df_h3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [4, 7], 'q': [6, 6]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h4 = pd.DataFrame(data={'price': [5.5, 5.5], 'q': [0, 4.5]})
fig_h4 = alt.Chart(df_h4).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text4 + text7 + text9
 + text12 + text13
 + fig_h3 + fig_h4).properties(title='Deadweight Loss of Subsidy (b)')


# When the supply curve shifts to the right, the producer surplus will be increased by **the area of V and W**.

# In[11]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_s1 = pd.DataFrame(data={'price': list(range(-2, 9)),
                        'qs': list(range(0,11))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 4, 7],
                        'q': [4.5, 6, 6]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s1).mark_line(clip=True).encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11]))
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.5, 'y': 4}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 7.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 9.6, 'y': 7}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 5.5, 'y': 5.5}]}).mark_text(
    text='Z',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 8, 'y': 7.5}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

text10 = alt.Chart({'values':[{'x': 2, 'y': 6.2}]}).mark_text(
    text='V',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text11 = alt.Chart({'values':[{'x': 4.5, 'y': 6.2}]}).mark_text(
    text='W',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text12 = alt.Chart({'values':[{'x': 2, 'y': 4.5}]}).mark_text(
    text='X',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text13 = alt.Chart({'values':[{'x': 4.5, 'y': 4.5}]}).mark_text(
    text='Y',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [7, 7], 'q': [0, 6]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h3 = pd.DataFrame(data={'price': [4, 4], 'q': [0, 6]})
fig_h3 = alt.Chart(df_h3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [4, 7], 'q': [6, 6]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h4 = pd.DataFrame(data={'price': [5.5, 5.5], 'q': [0, 4.5]})
fig_h4 = alt.Chart(df_h4).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text4 + text6 + text7 + text9
 + text10 + text11
 + fig_h2 + fig_h4).properties(title='Deadweight Loss of Subsidy (c)')


# To summarize:
# - Consumer surplus will be increased by the area of X and Y.
# - Producer surplus will be increased by the area of V and W.
# - Total surplus gain will be V + W + X + Y.
# - Government pays V + W + X + Y + Z.
# - The deadweight loss will be Z.

# In[12]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_s1 = pd.DataFrame(data={'price': list(range(-2, 9)),
                        'qs': list(range(0,11))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 4, 7],
                        'q': [4.5, 6, 6]
                       })

fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s1).mark_line(clip=True).encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11]))
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
)

text1 = alt.Chart({'values':[{'x': 9, 'y': 1.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.5, 'y': 4}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 7.5}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 9.6, 'y': 7}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 5.5, 'y': 5.5}]}).mark_text(
    text='DWL',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 8, 'y': 7.5}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

text10 = alt.Chart({'values':[{'x': 2, 'y': 6.2}]}).mark_text(
    text='V',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text11 = alt.Chart({'values':[{'x': 4.5, 'y': 6.2}]}).mark_text(
    text='W',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text12 = alt.Chart({'values':[{'x': 2, 'y': 4.5}]}).mark_text(
    text='X',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

text13 = alt.Chart({'values':[{'x': 4.5, 'y': 4.5}]}).mark_text(
    text='Y',
    fontSize=15,
).encode(x='x:Q', y='y:Q')

df_h2 = pd.DataFrame(data={'price': [7, 7], 'q': [0, 6]})
fig_h2 = alt.Chart(df_h2).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h3 = pd.DataFrame(data={'price': [4, 4], 'q': [0, 6]})
fig_h3 = alt.Chart(df_h3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [4, 7], 'q': [6, 6]})
fig_v3 = alt.Chart(df_v3).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_h4 = pd.DataFrame(data={'price': [5.5, 5.5], 'q': [0, 4.5]})
fig_h4 = alt.Chart(df_h4).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text4 + text6 + text7 + text8 + text9 + fig_v3).properties(title='Deadweight Loss of Subsidy (d)')


# ## Tax Incidence
# 
# > Consumers and producers are usually both partially responsible for paying the tax, but often one pays a greater percentage of the tax.<br><br>
# > The tax incidence is directly related to the price elasticity of supply and demand:
# > - If supply is more elastic than demand, consumers pay more.
# > - If demand is more elastic than supply, producers pay more.

# **A Tax Paid Mainly by Consumers**

# <img src="../pic/unit02_8_tax_consumer.png" alt="tax_consumer" width="600"/>

# **A Tax Paid Mainly by Producers**

# <img src="../pic/unit02_8_tax_producer.png" alt="tax_producer" width="600"/>

# |Elasticities|Tax Incidence|
# |---|---|
# |Elasticity of Demand > Elasticity of Supply|Producers pay more|
# |Elasticity of Supply > Elasticity of Demand|Consumers pay more|
# |Perfectly inelastic demand|Consumers pay all|
# |Perfectly elastic demand|Consumers pay none of the tax|
# |Perfectly inelastic supply|Producers pay all|
# |Perfectly elastic supply|Producers pay none of the tax|
