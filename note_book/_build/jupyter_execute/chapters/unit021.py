#!/usr/bin/env python
# coding: utf-8

# # Unit 02.1: Demand
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


# ## Shifts in Demand
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
