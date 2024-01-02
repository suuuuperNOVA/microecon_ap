#!/usr/bin/env python
# coding: utf-8

# # Market Failure and the Role of Government

# ## Socially Efficient and Inefficient Market Outcomes

# In previous chapters, we learned that:
# - Perfectly competitive markets allocate resources efficiently in the long run.
#     - Allocatively efficient
#     - Productively efficient
# - Imperfect competition often results in market inefficiencies.

# ### Social Efficiency
# 
# **Social efficiency** is achieved when **MC = MB** (market equilibrium) as show in the figure below:
# - No deadweight loss;
# - Total surplus are maximized.

# In[1]:


import pandas as pd
import altair as alt


# In[2]:


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

fig_mu_1 = fig_mu + fig_mc + text6 + text7 + text8
fig_mu_1


# Market failure
# : When a market fails to provide an efficient allocation of resources.
# 
# > Governments may step in to attempt to intervene an attempt to promote a more desirable social outcome in different market failures.
# > - Public goods
# > - Externalities
# > - Imperfect competition
# > - Unequal distribution of income

# ```{admonition} Definitions
# Public good
# : Commodities or services that benefit all members of society.
# : Non-rival and non-exclude.
# : Often provided for free through public taxation.
# : e.g. law enforcement, national defense, parks<br><br>
# 
# Positive externality/External benefit
# : External benefit is a benefit that an individual or a firm confers on others without receiving compensation.
# : e.g. free parks<br><br>
# 
# Negative externality/External cost
# : External cost is an uncompensated cost that an individual or a firm imposes on others.
# : e.g. traffic congestion<br><br>
# 
# Externalities
# : Third-person side effects.
# : External costs and benefits.
# : Usually arise from lack of well-defined property rights and/or high transaction costs.<br><br>
# 
# Marginal private benefit/MPB
# : Marginal benefit that accrues to consumers of a good, not including any external benefits.
# : Take as **consumers' demand**.<br><br>
# 
# Marginal external benefit/MEB
# : Addition to external benefits created by one more unit of the good.<br><br>
# 
# Marginal social benefit/MSB
# : Additional benefit to society as a whole from one additional unit.
# : **MSB = MPB + MEB**
# : Take as **total demand**.<br><br>
# 
# Marginal private cost/MPC
# : Marginal cost of producing that good, not including any external costs.
# : Take as **producers' supply**.<br><br>
# 
# Marginal external cost
# : Increase in external costs to society created by one more unit of the good.<br><br>
# 
# Marginal social cost/MSC
# : Additional cost imposed on society as a whole by one additional unit.
# : **MSC = MPC + MEC**
# : Take as **supply**.<br><br>
# 
# Socially optimal quantity
# : MSB = MSC
# ```

# ## Externalities
# 
# The free market fails to include external costs or external benefits (**market failure**) because rational consumers and producers only respond to private costs and benefits and not to external costs and benefits. Rational agents have the incentive to free ride when a good is non-excludable. With no government involvement there would be too much of some goods and too little of others.

# ### Positive Externalities

# #### Positive Externality in Production
# 
# When there is the marginal excess benefit (MEB) like a new office building, the good is **underproduced** as MSC > MPC in the figure below.
# - Supply curve is S where S = MPC;
# - The supply good has positive externality to society, so the society expect to produce at the curve MSC (MSC = MPC + MEB);
# - QS is the socially optimal quantity, but the market is producing at QMKT;
# - There is **deadweight loss**.
# 
# **With positive externalities, the good is underproduced but at a higher price.**

# <img src="../pic/unit06_pes.png" alt="pes" width="600"/>

# #### Positive Externality in Consumption
# 
# When there is the marginal excess benefit (MEB) like paid vaccine, the good is **underproduced** as MSB > MPB in the figure below.
# - Demand curve is D where D = MPB;
# - The demand good has positive externality to society, so the society expect to consume at the curve MSB (MSB = MPB + MEB);
# - QS is the socially optimal quantity, but the market is producing at QMKT;
# - There is **deadweight loss**.
# 
# **With positive externalities, the good is underproduced but at a higher price.**

# <img src="../pic/unit06_pec.png" alt="pec" width="600"/>

# ### Negative Externalities

# #### Negative Externality in Production

# When there is the marginal excess cost (MEC) like logging company and gas company, the good is **overproduced** as MSC < MPC in the figure below.
# - Supply curve is S where S = MPC;
# - The supply good has negative externality to society, so the society expect to produce at a higher cost at the curve MSC (MSC = MPC - MEB);
# - QS is the socially optimal quantity, but the market is producing at QMKT;
# - There is **deadweight loss**.
# 
# **With negative externalities, the good is overproduced but at a lower price.**

# <img src="../pic/unit06_nes.png" alt="nes" width="600"/>

# #### Negative Externality in Consumption

# When there is the marginal excess cost (MEC) like cigarette, the good is **overproduced** as MSB < MPB in the figure below.
# - Demand curve is D where D = MPB;
# - The demand good has negative externality to society, so the society expect to consume at the curve MSB (MSB = MPB - MEB);
# - QS is the socially optimal quantity, but the market is producing at QMKT;
# - There is **deadweight loss**.
# 
# **With negative externalities, the good is overproduced but at a lower price.**

# <img src="../pic/unit06_nec.png" alt="nec" width="600"/>

# ### Policies to Address Externalities
# 
# - Positive externality
#     - Subsidies
#     - Public provision
#     - Assignment of property rights
# - Negative externality
#     - Taxes
#     - Environmental regulation
#     - Assignment of property rights

# ## Public and Private Goods

# ```{admonition} Public goods vs. Private goods
# 
# Public goods
# : Both non-excludable and non-rival in consumption.
# : Free riders.
# : e.g. free parks, national defense<br><br>
# 
# Private goods
# : Excludable and rival in consumption.
# : Consumers have the right to exclude others from the benefits.
# ```

# ### Free-Rider Problem
# 
# ```{admonition}
# 
# As public goods are non-exclusive, people know they can benefit from public good without paying for them. If consumers are free riders, demand drops to 0 for the product. Due to the free-rider problem, private firms will not supply public goods. If society wants a public good to be produced, it will have to direct government to do it.
# ```

# ## The Effects of Government Intervention in Different Market Structures

# > Government intervention in imperfect markets can increase efficiency if the policy correctly addresses the incentives that led to the market failure.
# 
# <br>
# 
# Government can use (<ins>[recap **Taxes and Shifting Cost Curves**](content:references:label_tax)</ins> 👀):
# - Taxes
#     - Per-Unit tax<br>Shift the supply curve left.
#     - Lump-Sum tax<br>Shift the ATC upward.
# - Subsidies
#     - Per-Unit subsidy<br>Shift the supply curve right.
#     - Lump-Sum subsidy<br>Shift the ATC downward.
#     
# > **Per-Unit tax/subsidy is more efficient than lump-sum because lump-sum does not control the quantity.**

# ### Monopoly/Natural Monopoly
# 
# - Government can use **price regulation** 
#     - To keep prices low (**fair-return pricing**);
#     - To make monopolies efficient.
# - Government can use **lump-sum subsidy** to make the firm produce at the **socially optimal price**.
# - Governments can use **antitrust policy** in an attempt to make markets more competitive.
#     - Also applied to oligopolies.
#     
# Antitrust policy
# : Regulations that encourage competition by limiting the market power of any particular firm. 
# : This often involves ensuring that mergers and acquisitions don’t overly concentrate market power or form monopolies, as well as breaking up firms that have become monopolies.
# : Prevent multiple firms from colluding or forming a cartel to limit competition through practices such as price fixing. 

# <img src="../pic/unit04_2_nmono.png" alt="namono" width="600"/>

# ## Inequality

# > Income levels and poverty rates vary greatly both across and within groups (e.g., age, gender, race) and countries.

# ### Lorenze Curve

# We use the **Lorenze curve** to measure the income inequality as shown in the figure below.
# 
# Lorenze curve consists of:
# - % of income on the vertical axis
# - % of family on the horizontal axis
# - Diagonal<br>Noted as the perfect equality case.
#     - At the Point B, 50% of the families make 50% of total income in a country.
# - Lorenz curve<br>Real case
#     - At the Point A, 50% of families make 25 of total income in a country.
# 
# When the Lorenze curve is more apart from the perfect equality line, there is more income inequality. So, the right case below is more unequal than the left case.

# <div class="row">
#   <div class="column">
#     <img src="../pic/unit06_incomea.png" alt="lca" width="490" style="float:left">
#   </div>
#   <div class="column">
#     <img src="../pic/unit06_incomeb.png" alt="lcb" width="470" style="float:right">
#   </div>
# </div>

# ### Gini Coefficient
# 
# We also use the **Gini coefficient** to measure the income inequality.
# - Gini coefficient ranges from 0 to 1;
# - 0 means perfectly equality;
# - The greater value, the more unequal.

# <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mtext>Gini Coefficient</mtext>
#   <mo>=</mo>
#   <mfrac>
#     <mi>A</mi>
#     <mrow>
#       <mi>A</mi>
#       <mo>+</mo>
#       <mi>B</mi>
#     </mrow>
#   </mfrac>
# </math>
# <br>

# <img src="../pic/unit06_gini.png" alt="gini" width="600"/>

# ### Sources of Income and Wealth Inequality
# 
# Each factor of production receives the value of its marginal product, which can contribute to income inequality. Sources of income and wealth inequality include:
# - Tax structures
#     - Progressive tax<br>Higher tax rates as income increases.
#     - Proportional tax<br>Flat tax rates.
#     - Regressive tax<br>Lower tax rates as income decreases.
# - Human capital
# - Social capital
# - Inheritance
# - Effects of discrimination
# - Access to financial markets
# - Mobility
# - Bargaining power within economic and social units
#     - Firms, labor unions, and families.
