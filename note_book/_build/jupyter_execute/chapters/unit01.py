#!/usr/bin/env python
# coding: utf-8

# # Unit 01: Basic Economic Concepts

# ```{admonition} Microeconomics vs. Macroeconomics
# :class: tip
# 
# Microeconomics
# : Study principles of how individuals, households, and firms make decisions. 
# : e.g. Will you buy an IPhone or a Samsung?<br><br>
# 
# Macroeconomics
# : Examine the overall behavior of the economy to understand why there are ups and downs.
# : e.g. How does the society as a whole respond to increasing gas price?
# ```

# ## Scarcity
# 
# > Economics is the study of **scarcity** and choice. 
# 
# We live in a world of limited resources that requires choices about how they are allocated. An individual needs to decide about what to do and not to do.<br><br>
# 
# ```{note}
# Scarce
# : A scarce resource is not available in sufficient quantities to satisfy all the various ways a society wants to use it.<br><br>
# ```

# ## Rescource allocation
# 
# > Resources are scarce. That's why people need to allocate resources effectively to achieve higher productivity.
# 
# ```{admonition} What does *resource* mean in economics?
# Resource
# : Anything can be used to produce something else.
# : In economics, it is called ***factors of production***.<br><br>
# 
# **Factors of production** are categorized into:
# - Land<br>Natural resources
#     - Water
#     - Minerals
#     - Oil
# - Labor<br>Workers
# - Capital<br>Goods used to make other goods and services
#     - Machinery
#     - Tools
#     - Buildings
# - Entrepreneurship<br>Abilities to create economic value
#     - Risk taking
#     - Innovation
#     - Organization of resources for production
# ```
# 
# **Resource allocation** means to answer the following questions:
# - What goods and services to produce?
# - How to produce?
# - Who consumes those goods and services?
# <br><br>
# 
# > When people make choices, there will be the **opportunity cost**.
# 
# Opportunity cost
# : The value of the **next best alternative** that you must give up in order to get the item.
# 
# ```{admonition} Example of opportunity cost
# I am thinking about buying a new cellphone, and I have 3 choices, IPhone 15 Pro Max, IPhone 15, and IPhone 14. If I choose IPhone 15, the opportunity cost will IPhone 15 Pro Max which is more valuable than IPhone 14.
# ```

# ## Economic systems
# 
# > An economic system determines how the resources are allocated, or how to coordinate a society's productive and consumptive activities.
# 
# Market economy
# : Individual producers and consumers largely determine what, how, and for whom to produce, with little government involvement in the decisions.<br>
# 
# Command economy
# : Industry is publicly owned and a central authority makes production and consumption decisions.
# : Since everything is planned (such as price and quantity to produce), command economies lack incentives.
# 
# Mixed economy:
# : Market economy + Command economy
# : Most countries are a mixed economy.

# ## Production Possibilities Curve (PPC)
# 
# > Most resources are scarce, and in most cases the use of resources involves constraints and trade-offs.
# 
# ```{important}
# Production possibilities curve/PPC
# : Show the **trade-offs** facing an economy that produces only two goods.
# : Show the **maximum** quantity of one good that can be produced for each possible quantity of the other good produced.<br><br>
# 
# Assumptions of PPC
# - Efficiency<br>Full employment of resources
# - Fixed resources<br> No more available
# - Fixed technology<br> No technology advance
# - Only two products
# ```
# 
# **Example**<br>
# 
# How to read the table below?
# - At *Point A*, we can produce 0 piece of pizza and 10 apples.
#     - If using all the resources to produce apples, the maximum quantity of apple produced is 10.
# - At *Point B*, we can produce 1 piece of pizza and 9 apples.<br>
# ...
# - At *Point E*, we can produce 4 pieces of pizza and 0 apples.
#     - If using all the resources to produce pizza, the maximum quantity of pizza produced is 4.
# 
# |Point|Quantity of pizza|Quantity of apple|
# |---|---|---|
# |A|0|10|
# |B|1|9|
# |C|2|7|
# |D|3|4|
# |E|4|0|
# 
# Now let's look at the points in the table below.
# 
# |Point|Quantity of pizza|Quantity of apple|
# |---|---|---|
# |F|2|5|
# |G|1|4|
# |H|3|8|
# 
# 

# ```{important}
# Points *A*, *B*, *C*, *D* and *E* on PPC are **attainable** and **efficient** with current resources.
# 
# *F* and *G* are inside PPC or under PPC, meaning
# - Production doesn't operate at maximum productivity (**inefficiency**).
# - There is a waste of resources.
# 
# *H* is outside PPC
# - Not attainable with current resources and technology level.
# - It can only be attainable with
#     - Inputting more resource, such as labor, capital, land
#     - Technology advance
# ```

# In[1]:


import pandas as pd
import altair as alt

df_ppc = pd.DataFrame({'point': ['A', 'B', 'C', 'D', 'E'],
                   'pizza': [0, 1, 2, 3, 4],
                   'apple': [10, 9, 7, 4, 0]
                  })
df1 = alt.Chart(df_ppc).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('pizza', title='Quantity of Pizza', scale=alt.Scale(domain=[0,5]), axis=alt.Axis(tickCount=6)),
    alt.Y('apple', title='Quantity of Apple', scale=alt.Scale(domain=[0,11]), axis=alt.Axis(tickCount=12)),
)
df2 = df1.mark_text(align='left', baseline='bottom', dx=5, dy=-1).encode(text='point')

df_nppc = pd.DataFrame({'point': ['F', 'G', 'H'],
                   'pizza': [2, 1, 3],
                   'apple': [5, 4, 8]
                  })

df3 = alt.Chart(df_nppc).mark_point(color='red').encode(x='pizza', y='apple')
df4 = df3.mark_text(align='left', baseline='bottom', dx=5, dy=-1).encode(text='point')

text1 = alt.Chart({'values':[{'x': 4, 'y': 8}]}).mark_text(
    text='Not attainable',
    fontSize=15
).encode(x='x:Q', y='y:Q')
text2 = alt.Chart({'values':[{'x': 2, 'y': 3}]}).mark_text(
    text='Inefficiency',
    fontSize=15
).encode(x='x:Q', y='y:Q')

(df1 + df2 + df3 + df4 + text1 + text2).properties(title='Production Possibilities Curve')


# ```{admonition} Opportunity cost on PPC
# Suppose moving from *A* to *B*, the opportunity cost is an apple. At *A* we produce 10 apples and no pizza, whereas we produce 9 apples and 1 piece of pizza. It means we sacrifice 1 apple to get 1 piece of pizza.
# 
# |p1 to p2|Opportunity cost|Gain from sacrifice|
# |---|---|---|
# |A to B|1 apple|1 pizza|
# |B to C|2 apples|1 pizza|
# |C to D|3 apples|1 pizza|
# |D to E|4 apples|1 pizza|
# 
# The table above shows we need to sacrifice more apples to get 1 pizza more along PPC from A to E. This is because economic resources are not completely adaptable. The curved line (PPC) shows the adaptability and **increasing opportunity cost**.<br>
# 
# If PPC is a straight line, it means constant opportunity cost.
# ```

# Economic growth
# : An expansion of the economy's production possibility (economy can produce more).
# : PPC shifts outward shown in the figure below.
# 
# Driving forces of economic growth
# - More factors of production to input
# - Technology improvement in productivity

# In[2]:


df_ppc2 = pd.DataFrame({'point': ['A', 'B', 'C', 'D', 'E', 'F'],
                   'pizza': [0, 1, 2, 3, 4, 5],
                   'apple': [15, 14, 12, 9, 5, 0]
                  })

df1_ppc2 = alt.Chart(df_ppc2).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white', color='green'), color='green').encode(
    alt.X('pizza', title='Quantity of Pizza', scale=alt.Scale(domain=[0,5]), axis=alt.Axis(tickCount=6)),
    alt.Y('apple', title='Quantity of Apple', scale=alt.Scale(domain=[0,15]), axis=alt.Axis(tickCount=12)),
)

text3 = alt.Chart({'values':[{'x': 2.3, 'y': 9}]}).mark_text(
    text='➟',
    fontSize=50
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 1.4, 'y': 9.2}]}).mark_text(
    text='PPC_0',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text5 = alt.Chart({'values':[{'x': 3.5, 'y': 9.2}]}).mark_text(
    text=r'PPC_new',
    fontSize=15
).encode(x='x:Q', y='y:Q')

(df1 + df1_ppc2 + text3 + text4 + text5).properties(title='Production Possibilities Curve')

