#!/usr/bin/env python
# coding: utf-8

# # Market Disequilibrium and Changes in Equilibrium

# ## Shortage
# 
# Shortage
# : Shortage is a condition where the quantity demanded is greater than the quantity supplied at the market price.<br><br>
# : The figure below shows the shortage at a price of 3. When the price is 3, the quantity supplied is 2 and the quantity demanded is 7. So, the shortage is 5 in this case.

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

df_h2 = pd.DataFrame(data={'price': [3, 3], 'q': [0, 7]})
fig_h2 = alt.Chart(df_h2).mark_line(color='blue', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v2 = pd.DataFrame(data={'price': [0, 3], 'q': [2, 2]})
fig_v2 = alt.Chart(df_v2).mark_line(color='blue', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [0, 3], 'q': [7, 7]})
fig_v3 = alt.Chart(df_v3).mark_line(color='blue', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + fig_h1 + fig_v1 + fig_h2 + fig_v2 + fig_v3).properties(title='Shortage When the Price is Below the Equilibrium Price')


# ## Surplus
# 
# Surplus
# : Surplus is a condition where the quantity supplied is greater than the quantity demanded at the market price.<br><br>
# : The figure below shows the surplus at a price of 8. When the price is 8, the quantity demanded is 2 and the quantity supplied is 7. So, the surplus is 5 in this case.

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

df_h2 = pd.DataFrame(data={'price': [8, 8], 'q': [0, 7]})
fig_h2 = alt.Chart(df_h2).mark_line(color='blue', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v2 = pd.DataFrame(data={'price': [0, 8], 'q': [2, 2]})
fig_v2 = alt.Chart(df_v2).mark_line(color='blue', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

df_v3 = pd.DataFrame(data={'price': [0, 8], 'q': [7, 7]})
fig_v3 = alt.Chart(df_v3).mark_line(color='blue', strokeDash=[4, 2]).encode(
    alt.X('q'),
    alt.Y('price')
)

(fig_eq + text1 + text2 + text3 + text4 + text5 + fig_h1 + fig_v1 + fig_h2 + fig_v2 + fig_v3).properties(title='Surplus When the Price is Above the Equilibrium Price')


# > Both shortage and surplus are market disequilibrium. The market forces will drive price and quantity toward equilibrium, which is also known as **invisible hand**.

# ## Shifting Demand
# 
# > Now, we are going to learn the effects on the equilibrium price and equilibrium quantity with a shifted demand curve.
# >
# > Recap <ins>[factors shifting a demand](content:references:label_demandfactor)</ins> 👀

# The figure below shows how the market equilibrium changes with a demand shift:
# - When the demand increases, the demand shifts to the right from D0 to D1.
#     - The market equilibrium shifts from E0 to E1.
#     - The equilibrium price increases.
#     - The equilibrium quantity increases.
# - When the demand decreases, the demand shifts to the left from D0 to D2.
#     - The market equilibrium shifts from E0 to E2.
#     - The equilibrium price decreases.
#     - The equilibrium quantity decreases.

# In[4]:


df_d = pd.DataFrame(data={'price': list(range(2, 10)),
                        'qd': list(range(8,0,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qs': list(range(0,10))
                       })

df_e = pd.DataFrame(data={'price': [5.5,4,7],
                        'q': [4.5,3,6]
                       })

df_d2 = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(12,2,-1))
                       })

df_d3 = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(6,-4,-1))
                       })

text1 = alt.Chart({'values':[{'x': 8.4, 'y': 2}]}).mark_text(
    text='D0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 9.2, 'y': 10}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 9.6, 'y': 4}]}).mark_text(
    text='D1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.4, 'y': 1}]}).mark_text(
    text='D2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 7.5}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 3, 'y': 4.5}]}).mark_text(
    text='E2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 8, 'y': 3.5}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 5, 'y': 3.55}]}).mark_text(
    text='➟',
    fontSize=40,
    angle = 180
).encode(x='x:Q', y='y:Q')


fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_d2).mark_line(color='green', clip=True).encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_d3).mark_line(color='red', clip=True).encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
) + text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9

fig_eq


# ## Shifting Supply
# 
# > Now, we are going to learn the effects on the equilibrium price and equilibrium quantity with a shifted supply curve.
# >
# > Recap <ins>[factors shifting a supply](content:references:label_supplyfactor)</ins> 👀

# The figure below shows how the market equilibrium changes with a supply shift:
# - When the supply increases, the supply shifts to the right from S0 to S1.
#     - The market equilibrium shifts from E0 to E1.
#     - The equilibrium price decreases.
#     - The equilibrium quantity increases.
# - When the supply decreases, the supply shifts to the left from S0 to S2.
#     - The market equilibrium shifts from E0 to E2.
#     - The equilibrium price increases.
#     - The equilibrium quantity decreases.

# In[5]:


df_d = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(9,-1,-1))
                       })

df_s = pd.DataFrame(data={'price': list(range(3, 10)),
                        'qs': list(range(2,9))
                       })

df_e = pd.DataFrame(data={'price': [5.5, 4, 7],
                        'q': [4.5, 6, 3]
                       })

df_s2 = pd.DataFrame(data={'price': list(range(1, 11)),
                        'qd': list(range(3,13))
                       })

df_s3 = pd.DataFrame(data={'price': list(range(5, 11)),
                        'qd': list(range(1,7))
                       })

text1 = alt.Chart({'values':[{'x': 9.2, 'y': 1}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 8.3, 'y': 9}]}).mark_text(
    text='S0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 9.6, 'y': 8}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 6.3, 'y': 10}]}).mark_text(
    text='S2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 4.5, 'y': 6}]}).mark_text(
    text='E0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 6, 'y': 4.5}]}).mark_text(
    text='E1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 3, 'y': 7.5}]}).mark_text(
    text='E2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 4, 'y': 3.5}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text9 = alt.Chart({'values':[{'x': 2.5, 'y': 5}]}).mark_text(
    text='➟',
    fontSize=40,
    angle = 180
).encode(x='x:Q', y='y:Q')


fig_eq = alt.Chart(df_d).mark_line().encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s).mark_line().encode(
    alt.X('qs', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s2).mark_line(color='green', clip=True).encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_s3).mark_line(color='red', clip=True).encode(
    alt.X('qd', title='Quantity', scale=alt.Scale(domain=[0,10])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,11])),
) + alt.Chart(df_e).mark_point(size=90, color='black', fill='black').encode(
    x='q',
    y='price'
) + text1 + text2 + text3 + text4 + text5 + text6 + text7 + text8 + text9

fig_eq


# ## Shifting Both Demand and Supply

# > Now, we are going to learn the effects on the equilibrium price and equilibrium quantity with shifts in both the demand and supply.
# 
# Based on the table below, it can be inferred, for example:
# - Demand to right + Supply to left
#     - Equilibrium price increases
#     - Equilibrium quantity depends
#         - If the shift in supply is greater than that in demand, the shift in supply will dominate and the equilibrium quantity will decrease.
#         - If the shift in demand is greater than that in supply, the shift in demand will dominate and the equilibrium quantity will increase.
# 
# |  |Direction|Equilibrium Price|Equilibrium Quantity| 
# |---|---|---|---|
# |Demand|Right|Increase|Increase|
# |Demand|Left|Decrease|Decrease|
# |Supply|Right|Decrease|Increase|
# |Supply|Left|Increase|Decrease|
