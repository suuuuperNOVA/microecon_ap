#!/usr/bin/env python
# coding: utf-8

# # Basic Economic Concepts

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
# : Since everything is planned (such as price and quantity to produce), command economies lack incentives.<br>
# 
# Mixed economy
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


# ## Comparative Advantage and Trade
# 
# ```{admonition} Comparative advantage vs. Absolute advantage
# 
# Comparative advantage
# : An individual has a comparative advantage in producing a good or service if the **opportunity cost** of producing the good or service is **lower** for that individual than for other people.<br><br>
# 
# Absolute advantage
# : An individual has an absolute advantage in producing a good or service if he or she can make more of it with a given amount of time and resources. Having an absolute advantage is not the same thing as having a comparative advantage.
# ```
# 
# Example
# > Alex is a skilled fisherman and Kirk is very good at climbing trees to gather coconuts, but Kirk is less well suited to primitive life than Alex. So, Kirk is not nearly as good at catching fish, and compared to Alex, even his coconut-gathering leaves something to be desired. (See the figure below)

# In[3]:


df_ca = pd.DataFrame(data={'person': ['Alex', 'Alex', 'Alex', 'Kirk', 'Kirk', 'Kirk'], 'fish': [40, 20, 0, 10, 5, 0], 'coconut': [0, 15, 30, 0, 10, 20]})

fig_alex = alt.Chart(df_ca).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('fish', title='Quantity of fish'),
    alt.Y('coconut', title='Quantity of Coconuts'),
    alt.Color('person', title='Person')
).properties(title='Production Possibilities Curves of Alex and Kirk')

fig_alex


# From the PPC figure, we know:
# - Alex can produce either 40 fish or 30 coconuts at a maximum a day;
# - Kirk can produce either 10 fish or 20 coconuts at a maximum a day;
# - Alex has an absolute advantage in both products.
# 
# From the table below, we know:
# - Alex's opportunity cost of 1 fish is less than Kirk's;
# - Kirk's opportunity cost of 1 coconut is less than Alex's;
# - Alex has a comparative advantage in fish;
# - Kirk has a compareative advantage in coconut.
# 
# ||Alex's opportunity cost|Kirk's opportunity cost|
# |---|---|---|
# |1 fish|3/4 coconut|2 coconuts|
# |1 coconut|4/3 fish|1/2 fish|
# 

# ```{note}
# Now let's add **trade** and **specialization** to the case!
# ```
# 
# 
# Trade
# : In a market economy, individuals engage in trade.
# : They provide goods and services to others and receive goods and services in return.<br><br>
# 
# Specialization
# : This increase in output is due to specialization each person specializes in the task that he or she is good at performing.<br><br>
# 
# 
# > Let's assume that Alex need 28 fish and 9 coconuts a day and Kirk needs 6 fish and 8 coconuts a day in a primitive village.<br>
# > Also, they can trade with each other and specialize in one task:
# > - Alex specializes in fish since he has a comparative advantage in fish;
# > - Kirk specializes in coconut since he has a comparative advantage in coconut.
# >
# > Alex trades 10 fish with Kirk for 10 coconuts (1 fish for 1 coconut).
# 
# |   |   |Without trade<br>Production|<br>Consumption|With trade<br>Production|<br>Consumption|Gains from trade|
# |---|---|---|---|---|---|---|
# |**Alex**|Fish|28|28|40|30|+2|
# |    |Coconuts|9|9|0|10|+1|
# |**Kirk**|Fish|6|6|0|10|+4|
# |   |Coconuts|8|8|20|10|+2|
# 
# 
# ```{admonition} Conclusion
# Gains from trade
# : People can get more of what they want through trade than they could if they tried to be self-sufficient.<br>
# 
# Terms of trade
# : The rate at which one good can be exchange for another.
# : In the example above, 1 fish for 1 coconut.<br><br>
# 
# **Mutually beneficial terms of trade** for a good fall between the producer's opportunity cost for the good and the buyer's opportunity cost for the good.
# 
# 
# |   |Without trade<br>Alex's opportunity cost|<br>Kirk's opportunity cost|With trade<br>Alex's opportunity cost|<br>Kirk's opportunity cost|
# |---|---|---|---|---|
# |1 fish|3/4 coconut|2 coconuts|   |1 coconut|
# |1 coconut|4/3 fish|1/2 fish|1 fish|   |
# 
# 
# Trade can benefit everyone in a society because it allows people to specialize in activities in which they have a comparative advantage.
# ```
# 
# > Now, Alex and Kirk can achieve points outside the PPC. (see the figure below)

# In[4]:


df_ca_trade = pd.DataFrame(data={'person': ['Alex', 'Kirk'], 'fish': [30, 10], 'coconut': [10, 10]})
fig_alex_trade = alt.Chart(df_ca_trade).mark_point().encode(
    alt.X('fish', title='Quantity of fish'),
    alt.Y('coconut', title='Quantity of Coconuts'),
    alt.Color('person', title='Person')
).properties(title='Production Possibilities Curves of Alex and Kirk')

fig_alex + fig_alex_trade


# ## Cost-Benefit Analysis
# 
# > Rational economic decisions require the evaluation of costs and benefits, **maximizing total net benefits**.
# 
# - Rational people consider opportunity cost:
#     - Implict opportunity cost
#     - Explicit opportunity cost
# - Consumers consider total benefits as **utility**.
#     - In economics, utility is a term used to determine the worth or value of a good or service.
# - Firms consider total benefits as **total revenue**.
# - Total next benefits are maximized at the optimal choice.
# 
# ```{note}
# Total Economic Costs = Implicit Opportunity Cost + Explicit Opportunity Cost<br><br>
# Total Net Benefits = Total Benefits - Total Costs
# ```

# ```{margin} Hint
# Explicit opportunity cost = $50<br>
# Implicit opportunity cost = $40<br>
# Total = $90
# ```

# ```{admonition} Example
# Karen works part-time at a local convenience store and earns $10 per hour. She wants to spend next Saturday afternoon attending a music concert. The full price of a concert ticket is $75, but Karen was able to get a discounted price of $50 from a friend who purchased the ticket but has become unable to attend. If Karen took 4 hours off from her job to attend the concert, what was her opportunity cost of attending the concert?
# ```

# ## Marginal Analysis and Consumer Choice
# 
# Marginal analysis
# : The study of the costs and benefits of doing a little bit more of an activity versus a little bit less.<br><br>
# 
# Marginal benefit
# : Represents the incremental satisfaction (utility) that a consumer receives when an additional good or service is purchased.
# : Represents the maximum cost a consumer will pay for an additional good or service (because utility = maximum cost a consumer will pay for).<br><br>
# 
# Marginal cost
# : The cost to produce one additional unit of production.<br><br>
# 
# ```{admonition} Example
# A can of Coke is $2, and there is a promotion that 2 for $3. The marginal cost of a 2nd Coke is $1.
# ```
# 
# Cost can be categorized into:
# - Fixed cost
#     - Rent
#     - Machines
# - Variable cost
#     - Material
#     - Employees
#     
# That's why the more produced, the lower the average cost. (aka **Economies of Scale**)
# 
# ```{admonition} Example
# Suppose that a factory is currently producing 5,000 units and wishes to increase its production to 10,000 units. If the factory’s current cost of production is $100,000, and if increasing their production level would raise their costs to $150,000, then the marginal cost of production is $10, or ($150,000 - $100,000) / (10,000 - 5,000).
# ```

# > Let's try to explain consumers' behavior.
# 
# ### Consumer Choice Theory
# 
# Key assumptions of **consumer choice theory**:
# - Utility maximization (maximizing **total net benefits**)
# - Non-satiation
#     - People are seldom satisfied and always want to consume more.
# - Decreasing marginal utility
#     - Consumers lose satisfaction with a product the more they consume it.
#     
# 
# ```{admonition} Example -- Would you see the movie three times?
# |# Times watching movie|Benefit|Cost|Cumulative benefits|Cumulative costs|Total net benefits|
# |---|---|---|---|---|---|
# |1st|\$30|\$10|\$30|\$10|\$20|
# |2nd|\$15|\$10|\$45|\$20|\$25|
# |3rd|\$5|\$10|\$50|\$30|\$20|
# 
# > **No, the total net benefits is the greatest in the 2nd.**
# ```

# ```{admonition} Example
# Assume you are buying slices of pizza at a sporting event:
# - Each slice of pizza gives you less and less additional benefit (downward sloping MB).
# - Each additional slice costs more and more since you miss more and more of the game (upward sloping MC).
# ```
# 
# **Total net benefits are maximized when *MB = MC*.**

# In[5]:


df_mu = pd.DataFrame(data={'MB': list(range(10,-1,-1)), 'pizza': list(range(0,11))})
df_mc = pd.DataFrame(data={'MB': list(range(0,11)), 'pizza': list(range(0,11))})
fig_mu = alt.Chart(df_mu).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('pizza', title='Quantity of pizza'),
    alt.Y('MB', title='MB/MC')
).properties(title='Benefits and Costs')

fig_mc = alt.Chart(df_mc).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white', color='green'), color='green').encode(
    alt.X('pizza', title='Quantity of pizza'),
    alt.Y('MB', title='MB/MC')
)

text6 = alt.Chart({'values':[{'x': 9, 'y': 2}]}).mark_text(
    text='MB',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text7 = alt.Chart({'values':[{'x': 9, 'y': 9.5}]}).mark_text(
    text='MC',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text8 = alt.Chart({'values':[{'x': 6.2, 'y': 5}]}).mark_text(
    text='MB = MC',
    fontSize=15
).encode(x='x:Q', y='y:Q')

df_mu_s = pd.DataFrame(data={'MB': [0, 3, 7], 'pizza': [7, 7, 7]})
fig_mu_s = alt.Chart(df_mu_s).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('pizza', title='Quantity of pizza'),
    alt.Y('MB', title='MB/MC')
)

df_mu_st = pd.DataFrame(data={'MB': [0, 3, 7], 'pizza': [3, 3, 3]})
fig_mu_st = alt.Chart(df_mu_st).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('pizza', title='Quantity of pizza'),
    alt.Y('MB', title='MB/MC')
)

text9 = alt.Chart({'values':[{'x': 1.5, 'y': 5}]}).mark_text(
    text='Not enough',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text10 = alt.Chart({'values':[{'x': 8, 'y': 5}]}).mark_text(
    text='Too much',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig_mu_0 = fig_mu + fig_mc + text6 + text7 + fig_mu_st + text9
fig_mu_1 = fig_mu + fig_mc + text6 + text7 + text8
fig_mu_2 = fig_mu + fig_mc + text6 + text7 + fig_mu_s + text10
alt.vconcat(fig_mu_0, fig_mu_1, fig_mu_2)


# ### Maximizing Utility Rule
# 
# > Now we know the consumer choice theory, but the example above is only about 1 product.<br>
# > How to maximize the utility when the consumer has 2 choices like Movies and Go Karts? (see the utility table below)
# > - Each movie costs \$10.
# > - Go Karts costs \$5 a time.
# >
# > If you only have \$40, what combination of movies and go karts maximizes your utility?
# 
# ```{margin} Hint
# 3 Movies and 2 Go Karts
# ```
# 
# |# Times going|MU<br>Movies|MU\/P<br>Movies|MU<br>Go Karts|MU\/P<br>Go Karts|
# |---|---|---|---|---|
# |1st|30|3|10|2|
# |2nd|20|2|5|1|
# |3rd|10|1|2|0.4|
# |4th|5|0.5|1|0.2|

# ```{admonition} Marginal utility per dollar
# In this case, we need to maximize the utility and meet the budget. We can do this by computing and comparing marginal utility per dollar of expenditure for each product.
# 
# Marginal utility per dollar
# : The amount of additional utility per dollar of expenditure for each product.
# : Marginal Utility per \$ = Marginal Utility / Price
# 
#     ```{important}
#     - Consumers will always start from the product with the **highest marginal utility per dollar**.<br>
#     - The utility-maximizing choice between consumption goods occurs where the marginal utility per dollar is the same for both goods, and the consumer has exhausted his or her budget.<br><br>
#     <math xmlns="http://www.w3.org/1998/Math/MathML">
#       <mfrac>
#         <mrow>
#           <mi>M</mi>
#           <msub>
#             <mi>U</mi>
#             <mn>1</mn>
#           </msub>
#         </mrow>
#         <msub>
#           <mi>P</mi>
#           <mn>1</mn>
#         </msub>
#       </mfrac>
#       <mo>=</mo>
#       <mfrac>
#         <mrow>
#           <mi>M</mi>
#           <msub>
#             <mi>U</mi>
#             <mn>2</mn>
#           </msub>
#         </mrow>
#         <msub>
#           <mi>P</mi>
#           <mn>2</mn>
#         </msub>
#       </mfrac>
#     </math>
#     ```
# ```
