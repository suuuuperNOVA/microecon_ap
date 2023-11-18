#!/usr/bin/env python
# coding: utf-8

# # Price Elasticity of Supply
# 
# Price elasticity of supply (PES)
# : Measures how sensitive quantity supplied is to a change in price.
# : <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mi>P</mi>
#   <mi>E</mi>
#   <mi>S</mi>
#   <mo>=</mo>
#   <mfrac>
#     <mrow>
#       <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#       <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#       <msub>
#         <mi>Q</mi>
#         <mi>S</mi>
#       </msub>
#     </mrow>
#     <mrow>
#       <mi mathvariant="normal">&#x0025;<!-- % --></mi>
#       <mi mathvariant="normal">&#x0394;<!-- Δ --></mi>
#       <mi>P</mi>
#     </mrow>
#   </mfrac>
# </math>
# 
# 
# - Most goods have inelastic supply in the short run.
# - Most goods have elastic supply in the long run.
# 
# > The table below shows the characteristics of inelastic and elastic supply.
# 
# |Inelastic Supply|Elastic Supply|
# |---|---|
# |Hard to produce|Easier to produce|
# |High barriers to entry|Low barriers to entry|
# |High cost or specialized inputs|Low cost or generic inputs|
# |Hard to switch from producing alternative goods|Easy to switch from producing alternative goods|

# The figure below shows 2 extreme cases:
# - When the demand is a vertical line, elasticity coefficient is 0, called **Perfectly Inelastic**.
# - When the demand is a horizontal line, elasticity coefficient is Infinity, called **Perfectly Elastic**.

# In[1]:


import pandas as pd
import altair as alt

df_ped_0 = pd.DataFrame(data={'price': list(range(10,-1,-1)), 'q': [5]*11})
fig1 = alt.Chart(df_ped_0).mark_line().encode(
    alt.X('q', title='Quantity supplied', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('price', title='Price',  axis=alt.Axis(tickCount=10))
).properties(title='Perfectly Inelastic Supply') 

text1 = alt.Chart({'values':[{'x': 5.5, 'y': 1}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig1 = fig1 + text1

fig2 = alt.Chart(df_ped_0).mark_line().encode(
    alt.X('price', title='Quantity supplied', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('q', title='Price',  scale=alt.Scale(domain=[0,10]),axis=alt.Axis(tickCount=10))
).properties(title='Perfectly Elastic Supply') 

text2 = alt.Chart({'values':[{'x': 9.5, 'y': 5.5}]}).mark_text(
    text='S',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig2 = fig2 + text2

alt.hconcat(fig1, fig2)


# The figure below compares the supply curves with different PES. S2 is relatively more elastic than S1 since a small change in price results in a greater change in the quantity demanded of S2.

# In[2]:


import numpy as np

ar = np.array(list(range(0,10)))
df = pd.DataFrame(data={'price': list(range(1,11)), 'q1': ar*2-4.5, 'q2': (ar+5)*0.5})

fig3 = alt.Chart(df).mark_line().encode(
    alt.X('q2', title='Quantity supplied', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('price', title='Price',  axis=alt.Axis(tickCount=10)),
)

text1 = alt.Chart({'values':[{'x': 8, 'y': 9.8}]}).mark_text(
    text='S1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig3 = fig3 + text1

df2 = df[(df.price > 3) & (df.price < 8)]

fig4 = alt.Chart(df2).mark_line(color='green').encode(
    alt.X('q1', title='Quantity supplied', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('price', title='Price',  axis=alt.Axis(tickCount=10)),
)

text2 = alt.Chart({'values':[{'x': 8, 'y': 7}]}).mark_text(
    text='S2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig4 = fig4 + text2

(fig3 + fig4).properties(title='Supply Curves with Different PES')


# ```{note}
# It can be concluded that the flatter the supply curve, the more elastic the supply is.
# ```
