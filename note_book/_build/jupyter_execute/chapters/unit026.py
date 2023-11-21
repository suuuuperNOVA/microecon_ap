#!/usr/bin/env python
# coding: utf-8

# # Market Equilibrium and Consumer and Producer Surplus

# > In previous sections, we have seen the demand curve and supply curve individually. Now, we are ready to put them together.

# ## Market Equilibrium
# 
# Market equilibrium
# : A state where the supply of good matches demand.
# : The intersection point E is the market equilibrium in the figure below<br><br>
# 
# Equilibrium quantity
# : The quantity of the good bought and sold in equilibrium.
# : <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <msub>
#     <mi>Q</mi>
#     <mrow class="MJX-TeXAtom-ORD">
#       <mi>E</mi>
#       <mi>q</mi>
#     </mrow>
#   </msub>
#   <mo>=</mo>
#   <msub>
#     <mi>Q</mi>
#     <mrow class="MJX-TeXAtom-ORD">
#       <mi>D</mi>
#     </mrow>
#   </msub>
#   <mo>=</mo>
#   <msub>
#     <mi>Q</mi>
#     <mrow class="MJX-TeXAtom-ORD">
#       <mi>S</mi>
#     </mrow>
#   </msub>
# </math>
# 
# Equilibrium price
# : The price of the good bought and sold in equilibrium.
# : Equilibrium price provides information to economic decision-makers to guide resource allocation.

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

(fig_eq + text1 + text2 + text3 + fig_h1 + fig_v1).properties(title='Market Equilibrium')


# ## Consumer Surplus
# 
# Consumer surplus
# : Happens when the price that consumers pay for a product or service is less than the price they're willing to pay.<br><br>
# : It's a measure of the additional benefit that consumers receive because they're paying less for something than what they were willing to pay.<br><br>
# : The figure below show the consumer surplus which equals the area of CS.

# In[3]:


fig2 = (fig_eq + text1 + text2 + text3 + fig_h1 + fig_v1).properties(title='Market Equilibrium')

text4 = alt.Chart({'values':[{'x': 1, 'y': 7}]}).mark_text(
    text='CS',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig2 + text4


# ## Producer Surplus
# 
# Producer surplus
# : Happens when the market price is greater than the prices they are willing to sell at.<br><br>
# : Difference between the price a seller receives and their willingness to sell for each quantity.<br><br>
# : The figure below show the producer surplus which equals the area of PS.

# In[4]:


text5 = alt.Chart({'values':[{'x': 1, 'y': 4}]}).mark_text(
    text='PS',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig2 + text4 + text5


# ```{Note}
# Total Surplus = Consumer Surplus + Producer Surplus<br><br>
# Consumer surplus and producer surplus are the benefits from the price they are getting. Economists use consumer surplus and producer surplus to measure the benefits markets create to buyers and sellers and understand market efficiency.<br><br>
# Market equilibrium maximizes total economic surplus in the absence of market failures, meaning that perfectly competitive markets are efficient.
# ```
