#!/usr/bin/env python
# coding: utf-8

# # Supply

# Supply
# : The different quantities of a good that sellers are willing and able to sell or produce at different prices.<br><br>
# 
# Supply schedule
# : Shows how much of a good or service producers would supply at different prices.
# : The table below shows Supply Schedule for Cotton.<br><br>
# 
# |Price of cotton<br>(\$ per pound)|Quantity of cotton supplied<br>(billions of pounds)|
# |---|---|
# |2.00|11.6|
# |1.75|11.5|
# |1.50|11.2|
# |1.25|10.7|
# |1.00|10.0|
# |0.75|9.1|
# |0.5|8.0|
# 
# 
# Quantity supplied
# : Actual amount of a good or service people are willing to sell at some specific price.
# : It is shown as a single point in a supply schedule or along a supply curve.
# : When cotton is $1.75 per pound, the quantity supplied is 11.5 billion pounds.<br><br>
# 
# Supply curve
# : Graphical representation of the supply schedule. It shows the relationship between quantity supplied and price (the figure below).
# : Quantity supplied on the x-axis.
# : Price on the y-axis.

# In[1]:


import pandas as pd
import altair as alt

df_supply = pd.DataFrame(data={'price': [2, 1.75, 1.50, 1.25, 1, 0.75, 0.5], 'quantity': [11.6, 11.5, 11.2, 10.7, 10.0, 9.1, 8.0]})
fig1 = alt.Chart(df_supply).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Quantity of Cotton (billion of pounds)', scale=alt.Scale(domain=[5,15])),
    alt.Y('price', title='Price of Cotton ($ per pound)', scale=alt.Scale(domain=[0,2.2])),
).properties(title='Supply Curve of Cotton')

text1 = alt.Chart({'values':[{'x': 12, 'y': 2}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig1 + text1


# Market supply
# : Sum of individual supplies.
# 
# 
# ```{admonition} Law of supply
# There is a **positive** relationship between price and quantity supplied.<br>
# 
# Why does the law of supply occur?<br>
# 
# Because, at higher prices profit seeking firms have an incentive to produce more.
# ```
# 
# Movement along the supply curve
# : **Change in the quantity supplied** of a good that is the result of a change in that goods' price (as shown in the figure below).

# In[2]:


text2 = alt.Chart({'values':[{'x': 10.3, 'y': 0.95}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 11.7, 'y': 1.46}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 11.2, 'y': 1.2}]}).mark_text(
    text='➘',
    fontSize=30,
    angle=270
).encode(x='x:Q', y='y:Q')

fig1 + text1 + text2 + text3 + text4


# ## Shifts in Supply
# 
# > When the *ceteris paribus* assumption is dropped, movement no longer occurs along the supply curve. The entire supply curve shifts, which means the quantity supplied changes at any given price.

# In[3]:


df_supply['quantity2'] = df_supply['quantity'] + 3
df_supply['quantity3'] = df_supply['quantity'] - 3
df_supply_fig = pd.melt(df_supply, id_vars=['price'], value_vars=['quantity', 'quantity2', 'quantity3'])
fig2 = alt.Chart(df_supply_fig).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('value', title='Quantity of Cotton (billion of pounds)', scale=alt.Scale(domain=[3,18])),
    alt.Y('price', title='Price of Cotton ($ per pound)', scale=alt.Scale(domain=[0,2.2])),
    alt.Color('variable', legend=None)
).properties(title='Supply Curve of Cotton')

text1 = alt.Chart({'values':[{'x': 11.8, 'y': 2.12}]}).mark_text(
    text='D1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 14.8, 'y': 2.12}]}).mark_text(
    text='D2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 8.8, 'y': 2.12}]}).mark_text(
    text='D3',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 12.5, 'y': 1.385}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 9.2, 'y': 1.41}]}).mark_text(
    text='➟',
    fontSize=40,
    angle=180 
).encode(x='x:Q', y='y:Q')

fig2+text1+text2+text3+text4+text5


# - When the supply increases, the supply curve shifts outward or to the right.
# - When the supply decreases, the supply curve shifts inward or to the left.
# 
# 
# (content:references:label_supplyfactor)=
# ```{admonition} What causes a shift in supply?
# - Prices/Availability of inputs (resources)
# - Prices of related goods
#     - Substitutes
#     - Complements
# - Number of sellers
# - Technology
# - Government action
#     - Taxes
#     - Subsidies
# - Expectations of future profits
# ```

# **Price/Availability of inputs**<br>
# To produce output, you need inputs. An input is any good or service that is used to produce another good or service. An increase in the price of an input makes the production of the final good more costly for those who produce and sell it. So, producers are less willing to supply the final good at any given price, and the supply curve shifts to the left.
# 
# 
# **Prices of related goods**
# 
# Substitutes<br>
# A single producer often produces a mix of goods rather than a single product. For example, an oil refinery produces gasoline from crude oil, but it also produces heating oil and other products from the same raw material. When a producer sells several products, the quantity of any one good it is willing to supply at any given price depends on the prices of its other co-produced goods.<br><br>
# An oil refiner will supply less gasoline at any given price when the price of heating oil rises, shifting the supply curve for gasoline to the left.

# In[4]:


df_heat = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[4,3,2,1]})
df_gas = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[5,4,3,2], 'quantity2': [4,3,2,1]})

fig1 = alt.Chart(df_heat).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Quantity supplied of heating oil', scale=alt.Scale(domain=[0,5])),
    alt.Y('price', title='Price of heating oil', scale=alt.Scale(domain=[0,3])),
).properties(title='Supplied Curve of Heating Oil')

text1 = alt.Chart({'values':[{'x': 4.1, 'y': 2.6}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 2, 'y': 1.35}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 3, 'y': 1.8}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 2.6, 'y': 1.6}]}).mark_text(
    text='➘',
    fontSize=30,
    angle=290
).encode(x='x:Q', y='y:Q')

fig1 = fig1 + text1 + text2 + text3 + text4


df_gas = pd.melt(df_gas, id_vars=['price'], value_vars=['quantity', 'quantity2'])

fig2 = alt.Chart(df_gas).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('value', title='Quantity supplied of gasoline', scale=alt.Scale(domain=[0,6])),
    alt.Y('price', title='Price of gasoline', scale=alt.Scale(domain=[0,3])),
    alt.Color('variable', legend=None)
).properties(title='Supply Curve of Gasoline')


text1 = alt.Chart({'values':[{'x': 4.1, 'y': 2.6}]}).mark_text(
    text='S2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 5.1, 'y': 2.6}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 3, 'y': 1.75}]}).mark_text(
    text='➟',
    fontSize=40,
    angle=180
).encode(x='x:Q', y='y:Q')

fig2 = fig2 + text1 + text2 + text3

alt.hconcat(fig1, fig2)


# Complements<br>
# Producers (oil-well drillers) of crude oil often find that oil wells also produce natural gas as a by-product of oil extraction. The higher the price at which a driller can sell its natural gas, the more oil wells it will drill and the more oil it will supply at any given price for oil.

# In[5]:


df_heat = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[4,3,2,1]})
df_gas = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[4,3,2,1], 'quantity2': [5,4,3,2]})

fig1 = alt.Chart(df_heat).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Quantity supplied of natural gas', scale=alt.Scale(domain=[0,5])),
    alt.Y('price', title='Price of natural gas', scale=alt.Scale(domain=[0,3])),
).properties(title='Supplied Curve of Natural Gas')

text1 = alt.Chart({'values':[{'x': 4.1, 'y': 2.6}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 2, 'y': 1.35}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 3, 'y': 1.8}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 2.6, 'y': 1.6}]}).mark_text(
    text='➘',
    fontSize=30,
    angle=290
).encode(x='x:Q', y='y:Q')

fig1 = fig1 + text1 + text2 + text3 + text4


df_gas = pd.melt(df_gas, id_vars=['price'], value_vars=['quantity', 'quantity2'])

fig2 = alt.Chart(df_gas).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('value', title='Quantity supplied of oil', scale=alt.Scale(domain=[0,6])),
    alt.Y('price', title='Price of oil', scale=alt.Scale(domain=[0,3])),
    alt.Color('variable', legend=None)
).properties(title='Supply Curve of Oil')


text1 = alt.Chart({'values':[{'x': 4.1, 'y': 2.6}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 5.1, 'y': 2.6}]}).mark_text(
    text='S2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 3, 'y': 1.75}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

fig2 = fig2 + text1 + text2 + text3

alt.hconcat(fig1, fig2)


# **Number of sellers**<br>
# A market with many producers will supply a larger quantity of a good than a market with a single producer, all other things equal.
# 
# 
# **Technology**<br>
# When economists talk about "technology", they mean all the methods people can use to turn inputs into useful goods and services. Improvements in technology enable producers to spend less on inputs yet still produce the same output. When a better technology becomes available, reducing the cost of production, supply increases, and the supply curve shifts to the right.
# 
# 
# **Government action**<br>
# Taxes<br>
# Governments will impose taxes on the production of goods or services they discourage, such as cigarettes. So, it will increase the production cost, shifting the supply curve to the left.
# 
# Subsidies<br>
# In order to encourage the production of goods or services, governments will subsidize supplies, such as health care services. So, it will compensate suppliers, shifting the supply curve to the right.
# 
# 
# **Expectations of future profits**<br>
# An increase in the anticipated future price of a good or service reduces supply today, a leftward shift of the supply curve. Similarly, a fall in the anticipated future price increases supply today, a rightward shift of the supply curve.
