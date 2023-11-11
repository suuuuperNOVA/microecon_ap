#!/usr/bin/env python
# coding: utf-8

# # Unit 02: Supply and Demand

# ```{admonition} Background
# :class: tip
# 
# We focus on ***competitive market***, where behavior is well described by **supply and demand model**.<br>
# 
# Competitive market
# : There are many buyers and sellers of the same good or service. No individual's actions have a noticeable effect on the price of the good or service.
# ```

# ## Demand
# 
# Demand
# : The different quantities of goods that consumers are **willing** and **able** to buy at different prices.<br><br>
# 
# Demand schedule
# : Shows how much of a good or service consumers will be willing and able to buy at different prices.
# : The table below shows Demand Schedule for Cotton.<br>
# 
# |Price of cotton<br>(\$ per pound)|Quantity of cotton demanded<br>(billions of pounds)|
# |---|---|
# |2.00|7.1|
# |1.75|7.5|
# |1.50|8.1|
# |1.25|8.9|
# |1.00|10.0|
# |0.75|11.5|
# |0.5|14.2|

# Quantity demanded
# : Actual amount of a good or service consumers are willing and able to buy at some specific price.
# : It is shown as a single point in a demand schedule or along a demand curve.
# : When cotton is $1.75 per pound, the quantity demanded is 7.5 billion pounds.<br><br>
# 
# Demand curve
# : Graphical representation of the demand schedule. It shows the relationship
# between quantity demanded and price (the figure below).
# : **Quantity demanded** on the x-axis.
# : **Price** on the y-axis.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


df_demand = pd.DataFrame(data={'price': [2, 1.75, 1.50, 1.25, 1, 0.75, 0.5], 'quantity': [7.1, 7.5, 8.1, 8.9, 10.0, 11.5, 14.2]})
fig1 = alt.Chart(df_demand).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Quantity of Cotton (billion of pounds)', scale=alt.Scale(domain=[5,15])),
    alt.Y('price', title='Price of Cotton ($ per pound)', scale=alt.Scale(domain=[0,2.2])),
).properties(title='Demand Curve of Cotton')

text1 = alt.Chart({'values':[{'x': 14.5, 'y': 0.55}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig1 + text1


# Market demand
# : Sum of individual demands.<br>
# 
# > For example, there are 3 parties in the market, Billy, Jean and other individuals. So, the market demand is sum of individual quantity demanded at each price level. We will have the market demand (as shown in the table below).
# 
# |Price (\$)|Quantity demanded<br>Billy|Quantity demanded<br>Jean|Quantity demanded<br>Other individuals|Quantity demanded<br>Market|
# |---|---|---|---|---|
# |5|1|0|9|**10**|
# |4|2|1|17|**20**|
# |3|3|2|25|**30**|
# |2|5|3|42|**50**|
# |1|7|5|68|**80**|

# ```{admonition} Law of demand
# There is an **inverse** relationship between price and quantity demanded.<br>
# 
# Why does the law of demand occur?<br>
# 
# 1. Substitution effect<br>If the price goes up for a product, consumers will buy less of that product and more of another substitute product that has become relatively cheaper for the good that has become relatively more expensive.
# 1. Income effect<br>If the price goes down for a product, the purchasing power increases for consumers to allow them to purchase more. 
# 1. Law of diminishing marginal utility<br>Law of diminishing marginal utility states that the more you buy of any good, the less satisfaction you get from each new unit consumed.
# ```
# 
# 
# ```{tip}
# *Ceteris paribus*
# : Assume all other factors are constant.
# 
# When reading a demand curve, we assume all outside factors, such as income, are held constant (*ceteris paribus*). We only study the relationship between price and quantity demanded here. <br>
# 
# When the prices changes only, the quantity demanded will change **along the demand curve**, *ceteris paribus*.
# ```
# 
# Movement along the demand curve
# : **Change in the quantity demanded** of a good that is the result of a change in that goods' price (as shown in the figure below).

# In[3]:


text2 = alt.Chart({'values':[{'x': 7.5, 'y': 1.45}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 9.5, 'y': 0.95}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 8.5, 'y': 1.14}]}).mark_text(
    text='➘',
    fontSize=30
).encode(x='x:Q', y='y:Q')

fig1 + text1 + text2 + text3 + text4


# ### Shifts in Demand
# 
# > When the *ceteris paribus* assumption is dropped, movement no longer occurs along the demand curve. The entire demand curve shifts, which means the quantity demanded changes at any given price.

# In[4]:


df_demand['quantity2'] = df_demand['quantity'] + 3
df_demand['quantity3'] = df_demand['quantity'] - 3
df_demand_fig = pd.melt(df_demand, id_vars=['price'], value_vars=['quantity', 'quantity2', 'quantity3'])
fig2 = alt.Chart(df_demand_fig).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('value', title='Quantity of Cotton (billion of pounds)', scale=alt.Scale(domain=[3,18])),
    alt.Y('price', title='Price of Cotton ($ per pound)', scale=alt.Scale(domain=[0,2.2])),
    alt.Color('variable', legend=None)
).properties(title='Demand Curve of Cotton')

text1 = alt.Chart({'values':[{'x': 14.8, 'y': 0.53}]}).mark_text(
    text='D1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 17.8, 'y': 0.53}]}).mark_text(
    text='D2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 11.8, 'y': 0.53}]}).mark_text(
    text='D3',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 10, 'y': 1.385}]}).mark_text(
    text='➟',
    fontSize=40
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 7, 'y': 1.41}]}).mark_text(
    text='➟',
    fontSize=40,
    angle=180 
).encode(x='x:Q', y='y:Q')

fig2+text1+text2+text3+text4+text5


# - When the demand increases, the demand curve shifts outward or to the right.
# - When the demand decreases, the demand curve shifts inward or to the left.
# 
# 
# ```{admonition} What causes a shift in demand?
# - Tastes and preferences
# - Number of consumers
# - Price of related goods
#     - Substitutes
#     - Complements
# - Income
#     - Normal good
#     - Inferior good
# - Future expectations
# ```

# **Tastes and preferences**<br>
# When tastes change in favor of a good, more people want to buy it at any given price, so the demand curve shifts to the right. When tastes change against a good, fewer people want to buy it at any given price, so the demand curve shifts to the left.
# 
# 
# **Number of consumers/Population**<br>
# Because of population growth, overall demand for cotton would have risen even if the demand of each individual wearer of cotton clothing had remained unchanged.

# **Price of related goods**<br>
# 
# Substitutes
# : Goods used in place of one another, such as Coke-Cola and Pepsi.
# : If the price of one increases, the demand for the other will increase (or vice versa).
# 
# > For example, Coke-Cola and Pepsi are substitutes. A rise in the price of Coke-Cola makes consumers more willing to buy Pepsi, *vice versa*.

# In[5]:


df_cokecola = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[1,2,3,4]})
df_pepsi = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[1,2,3,4], 'quantity2': [2,3,4,5]})

fig1 = alt.Chart(df_cokecola).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Quantity demanded of Coke-Colar (# of bottles)', scale=alt.Scale(domain=[0,5])),
    alt.Y('price', title='Price of Coke-Cola ($ per bottle)', scale=alt.Scale(domain=[0,3])),
).properties(title='Demand Curve of Coke-Cola')

text1 = alt.Chart({'values':[{'x': 4.15, 'y': 1}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 3, 'y': 1.3}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 2, 'y': 1.8}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 2.5, 'y': 1.5}]}).mark_text(
    text='➘',
    fontSize=30,
    angle=180
).encode(x='x:Q', y='y:Q')

fig1 = fig1 + text1 + text2 + text3 + text4


df_pepsi = pd.melt(df_pepsi, id_vars=['price'], value_vars=['quantity', 'quantity2'])

fig2 = alt.Chart(df_pepsi).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('value', title='Quantity demanded of Pepsi (# of bottles)', scale=alt.Scale(domain=[0,6])),
    alt.Y('price', title='Price of Pepsi ($ per bottle)', scale=alt.Scale(domain=[0,3])),
    alt.Color('variable', legend=None)
).properties(title='Demand Curve of Pepsi')


text1 = alt.Chart({'values':[{'x': 4.2, 'y': 1}]}).mark_text(
    text='D1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 5.2, 'y': 1}]}).mark_text(
    text='D2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 3, 'y': 1.75}]}).mark_text(
    text='➟',
    fontSize=40,
).encode(x='x:Q', y='y:Q')

fig2 = fig2 + text1 + text2 + text3

alt.hconcat(fig1, fig2)


# Complements
# : Goods that are bought and used together, such as Coke-Cola and Cheetos.
# : If the price of one increases, the demand for the other will fall (or vice versa).
# 
# > For example, Coke-Cola and Cheetos are complements. A rise in the price of Coke-Cola makes consumers less willing to buy Cheetos, *vice versa*. Because consumers like to consume the Coke-Cola and Cheetos together, a change in the price of Coke-Cola will reduce the quantity demanded of Coke-Cola, and meanwhile, the demand of Cheetos will decrease.

# In[6]:


df_cokecola = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[1,2,3,4]})
df_pepsi = pd.DataFrame(data={'price': [2.5, 2, 1.5, 1], 'quantity':[2,3,4,5], 'quantity2': [1,2,3,4]})

fig1 = alt.Chart(df_cokecola).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('quantity', title='Quantity demanded of Coke-Colar (# of bottles)', scale=alt.Scale(domain=[0,5])),
    alt.Y('price', title='Price of Coke-Cola ($ per bottle)', scale=alt.Scale(domain=[0,3])),
).properties(title='Demand Curve of Coke-Cola')

text1 = alt.Chart({'values':[{'x': 4.15, 'y': 1}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 3, 'y': 1.3}]}).mark_text(
    text='A',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 2, 'y': 1.8}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 2.5, 'y': 1.5}]}).mark_text(
    text='➘',
    fontSize=30,
    angle=180
).encode(x='x:Q', y='y:Q')

fig1 = fig1 + text1 + text2 + text3 + text4


df_pepsi = pd.melt(df_pepsi, id_vars=['price'], value_vars=['quantity', 'quantity2'])

fig2 = alt.Chart(df_pepsi).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('value', title='Quantity demanded of Cheetos (# of pack)', scale=alt.Scale(domain=[0,6])),
    alt.Y('price', title='Price of Cheetos ($ per pack)', scale=alt.Scale(domain=[0,3])),
    alt.Color('variable', legend=None)
).properties(title='Demand Curve of Cheetos')


text1 = alt.Chart({'values':[{'x': 4.2, 'y': 1}]}).mark_text(
    text='D2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text2 = alt.Chart({'values':[{'x': 5.2, 'y': 1}]}).mark_text(
    text='D1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 3, 'y': 1.75}]}).mark_text(
    text='➟',
    fontSize=40,
    angle=180
).encode(x='x:Q', y='y:Q')

fig2 = fig2 + text1 + text2 + text3

alt.hconcat(fig1, fig2)


# **Income**<br>
# When individuals have more income, they are normally more likely to purchase a good or service at any given price (**only applies to normal good**).
# 
# 
# Normal good
# : A rise in income increases the demand for a good, such as cars.
# 
# 
# Inferior good
# : A rise in income decreases the demand for a good, such as public transport.
# 
# 
# **Future expectations**<br>
# Expectations of a future drop in price lead to a decrease in demand today. Alternatively, expectations of a future rise in price are likely to cause an increase in demand today.

# ## Supply
# 
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

# In[7]:


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

# In[8]:


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


# ### Shifts in Supply
# 
# > When the *ceteris paribus* assumption is dropped, movement no longer occurs along the supply curve. The entire supply curve shifts, which means the quantity supplied changes at any given price.

# In[9]:


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


# - When the supply increases, the demand curve shifts outward or to the right.
# - When the supply decreases, the demand curve shifts inward or to the left.
# 
# 
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

# In[10]:


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

# In[11]:


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

# ## Price Elasticity of Demand
# > Law of Demand states an inverse relationship between price (P) and quantity demanded (Q_D).<br>
# > Elasticity is about determining how much more or how much less consumers will buy with the price change.<br><br>
# > After this topic, we can explain why furniture stores have sales all the time but gas stations rarely have sales.
# 
# 
# ```{admonition} Background knowledge
# Elasticity
# : Measure the responsiveness of one variable to changes in another.<br><br>
# 
# For example, y = 3x, where x is the independent variable and y is the dependent variable. Elasticity measures how y responses to changes of x.
# ```

# Knowing how consumers will respond to a change in price is extremely useful to firms:
# - To help them decide what to charge and when to have sales.
# - To help them determine how many substitutes are in the market.
# - Governments decide when and how much to tax based on PED.

# ```{admonition} Formula
# Price elasticity of demand (PED)
# : Measures how **sensitive** quantity demanded is to a change in price.<br><br>
# &nbsp;<math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>P</mi>
#   <mi>E</mi>
#   <mi>D</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#       <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#       <msub>
#         <mi>Q</mi>
#         <mi>D</mi>
#       </msub>
#     </mrow>
#     <mrow>
#       <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#       <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#       <mi>P</mi>
#     </mrow>
#   </mfrac>
# </math>, where<br><br>
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <msub>
#     <mi>Q</mi>
#     <mi>D</mi>
#   </msub>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mtext>Change in&#xA0;</mtext>
#       <msub>
#         <mi>Q</mi>
#         <mi>D</mi>
#       </msub>
#     </mrow>
#     <mrow>
#       <mtext>Initial&#xA0;</mtext>
#       <msub>
#         <mi>Q</mi>
#         <mi>D</mi>
#       </msub>
#     </mrow>
#   </mfrac>
#   <mo>&#x00D7;<!-- × --></mo>
#   <mn>100</mn>
# </math>, % change in quantity demanded;<br><br>
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <mi>P</mi>
#   <mi>r</mi>
#   <mi>i</mi>
#   <mi>c</mi>
#   <mi>e</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mtext>Change in&#xA0;</mtext>
#       <mi>P</mi>
#     </mrow>
#     <mrow>
#       <mtext>Initial&#xA0;</mtext>
#       <mi>P</mi>
#     </mrow>
#   </mfrac>
#   <mo>&#x00D7;<!-- × --></mo>
#   <mn>100</mn>
# </math>, % change in price.;<br><br>
# 
# **Remember to drop the minus sign** because we have already known an inverse relationship based on Law of Demand.
# 
# Example<br>
# At a price of $20 per vaccination, consumers would demand 10 million vaccinations per year; at a price of $21, the quantity demanded would fall to 9.9 million vaccinations per year.<br><br>
# 
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <msub>
#     <mi>Q</mi>
#     <mi>D</mi>
#   </msub>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mn>9.9</mn>
#       <mo>&#x00D7;<!-- × --></mo>
#       <msup>
#         <mn>10</mn>
#         <mn>6</mn>
#       </msup>
#       <mo>&#x2212;<!-- − --></mo>
#       <mn>10</mn>
#       <mo>&#x00D7;<!-- × --></mo>
#       <msup>
#         <mn>10</mn>
#         <mn>6</mn>
#       </msup>
#     </mrow>
#     <mrow>
#       <mn>10</mn>
#       <mo>&#x00D7;<!-- × --></mo>
#       <msup>
#         <mn>10</mn>
#         <mn>6</mn>
#       </msup>
#     </mrow>
#   </mfrac>
#   <mo>=</mo>
#   <mo>&#x2212;<!-- − --></mo>
#   <mn>1</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
# </math><br><br>
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <mi>P</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mn>21</mn>
#       <mo>&#x2212;<!-- − --></mo>
#       <mn>20</mn>
#     </mrow>
#     <mn>20</mn>
#   </mfrac>
#   <mo>=</mo>
#   <mn>5</mn>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
# </math><br><br>
# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>P</mi>
#   <mi>E</mi>
#   <mi>D</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#       <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#       <msub>
#         <mi>Q</mi>
#         <mi>D</mi>
#       </msub>
#     </mrow>
#     <mrow>
#       <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#       <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#       <mi>P</mi>
#     </mrow>
#   </mfrac>
#   <mo>=</mo>
#   <mfrac>
#     <mn>1</mn>
#     <mn>5</mn>
#   </mfrac>
#   <mo>=</mo>
#   <mn>0.2</mn>
# </math>
# ```

# ### Interpretation of PED
# 
# - If PED = 1, it is called *Unit-Elastic*, where <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <msub>
#     <mi>Q</mi>
#     <mi>D</mi>
#   </msub>
#   <mo>=</mo>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <mi>P</mi>
# </math>.
# - If PED > 1, it is called *Elastic*, where <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <msub>
#     <mi>Q</mi>
#     <mi>D</mi>
#   </msub>
#   <mo>&gt;</mo>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <mi>P</mi>
# </math>.
#     - Quantity demanded is **sensitive** to the price change.
# - If PED < 1, it is called *Inelastic*, where <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <msub>
#     <mi>Q</mi>
#     <mi>D</mi>
#   </msub>
#   <mo>&lt;</mo>
#   <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#   <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#   <mi>P</mi>
# </math>.
#     -  Quantity demanded is **insensitive** to the price change.

# ### Price Elasticity Along the Demand Curve
# 
# ```{important}
# Elasticity is **NOT** slop!<br>
# 
# Even if the demand curve is linear, elasticity varies along the curve.
# ```

# Example<br>
# 
# |Point|Price (\$)|Quantity demanded|PED|
# |---|---|---|---|
# |A|0|10|NaN|
# |B|1|9|0.25|
# |C|2|8|0.43|
# |D|3|7|0.67|
# |E|4|6|1.00|
# |F|5|5|1.50|
# |G|6|4|2.33|
# |H|7|3|4.00|
# |I|8|2|9.00|
# |J|9|1|Inf|
# |K|10|0|NaN|

# In[12]:


df_ped = pd.DataFrame(data={'point':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
                        'price': list(range(0, 11)),
                        'qd': list(range(10,-1,-1))
                       })
df_ped['ped'] = (df_ped.qd.diff(1)/df_ped.qd.shift(-1)).abs()/(df_ped.price.diff(1)/df_ped.price.shift(-1)).abs()
df_ped['prop'] = 'Inelastic'
df_ped.loc[4, 'prop'] = 'Unit-elastic'
df_ped.loc[5:, 'prop'] = 'Elastic'

fig_ped = alt.Chart(df_ped).mark_line(color='grey').encode(
    alt.X('qd'),
    alt.Y('price'),
) + alt.Chart(df_ped).mark_point(size=80).encode(
    alt.X('qd', title='Quantity Demanded'),
    alt.Y('price', title='Price'),
    alt.Color('prop', title='PED')
).properties(title='Price Elasticity of Demand Changes Along the Demand')

text4 = alt.Chart({'values':[{'x': 4, 'y': 7}]}).mark_text(
    text='➘',
    fontSize=50,
    angle=180
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 7, 'y': 4.3}]}).mark_text(
    text='➘',
    fontSize=50,
).encode(x='x:Q', y='y:Q')

text6 = alt.Chart({'values':[{'x': 2.5, 'y': 8.4}]}).mark_text(
    text='More Elastic',
    fontSize=15,
    angle=37
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 8.7, 'y': 2.6}]}).mark_text(
    text='More Inelastic',
    fontSize=15,
    angle=37
).encode(x='x:Q', y='y:Q')

fig_ped + text4 + text5 + text6 + text7


# ## Price Elasticity of Supply

# ## Other Elasticities
