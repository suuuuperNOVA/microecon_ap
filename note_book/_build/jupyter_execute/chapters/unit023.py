#!/usr/bin/env python
# coding: utf-8

# # Unit 02.3: Price Elasticity of Demand
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

# ## Interpretation of PED
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

# The figure below shows 2 extreme cases:
# - When the demand is a vertical line, elasticity coefficient is 0, called **Perfectly Inelastic**.
# - When the demand is a horizontal line, elasticity coefficient is Infinity, called **Perfectly Elastic**.

# In[1]:


import pandas as pd
import altair as alt

df_ped_0 = pd.DataFrame(data={'price': list(range(10,-1,-1)), 'q': [5]*11})
fig1 = alt.Chart(df_ped_0).mark_line().encode(
    alt.X('q', title='Quantity demanded', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('price', title='Price',  axis=alt.Axis(tickCount=10))
).properties(title='Perfectly Inelastic Demand') 

text1 = alt.Chart({'values':[{'x': 5.5, 'y': 1}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig1 = fig1 + text1

fig2 = alt.Chart(df_ped_0).mark_line().encode(
    alt.X('price', title='Quantity demanded', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('q', title='Price',  scale=alt.Scale(domain=[0,10]),axis=alt.Axis(tickCount=10))
).properties(title='Perfectly Elastic Demand') 

text2 = alt.Chart({'values':[{'x': 9.5, 'y': 5.5}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig2 = fig2 + text2

alt.hconcat(fig1, fig2)


# The figure below compares the demand curves with different PED. D2 is relatively more elastic than D1 since a small change in price results in a greater change in the quantity demanded of D2.

# In[2]:


import numpy as np

ar = np.array(list(range(10,0,-1)))
df = pd.DataFrame(data={'price': list(range(1,11)), 'q1': ar*2 - 6, 'q2': (ar+5)*0.5})

fig3 = alt.Chart(df).mark_line().encode(
    alt.X('q2', title='Quantity demanded', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('price', title='Price',  axis=alt.Axis(tickCount=10)),
)

text1 = alt.Chart({'values':[{'x': 8, 'y': 1}]}).mark_text(
    text='D1',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig3 = fig3 + text1

df2 = df[(df.price > 3) & (df.price < 8)]

fig4 = alt.Chart(df2).mark_line(color='green').encode(
    alt.X('q1', title='Quantity demanded', scale=alt.Scale(domain=[0,10]), axis=alt.Axis(tickCount=10)),
    alt.Y('price', title='Price',  axis=alt.Axis(tickCount=10)),
)

text2 = alt.Chart({'values':[{'x': 8.2, 'y': 4.5}]}).mark_text(
    text='D2',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig4 = fig4 + text2

(fig3 + fig4).properties(title='Demand Curves with Different PED') 


# ```{note}
# It can be concluded that the flatter the demand curve, the more elastic the demand is.
# ```

# ## Price Elasticity Along the Demand Curve
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

# In[3]:


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
    alt.X('qd', title='Quantity demanded'),
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


# ## Factors determining PED
# 
# ```{admonition} Factors of PED
# - Availability of close substitutes
# - Share of income spent on the good
# - Necessity or luxury good
# - Time
# ```
# 
# **Availability of close substitutes**<br>
# The price elasticity of demand tends to be high if there are other goods that consumers regard as similar and would be willing to consume instead. The price elasticity of demand tends to be low if there are no close substitutes.<br><br>
# 
# **Share of income spent on the good**<br>
# The price elasticity of demand tends to be low when spending on a good accounts for a small share of a consumer’s income. In that case, a significant change in the price of the good has little impact on how much the consumer spends, vice versa.<br><br>
# 
# **Necessity or luxury good**<br>
# 
# Necessity good
# : Goods and services that consumers will buy regardless of the changes in their income levels, therefore making these products less sensitive to income change.
# : The price elasticity of demand tends to be low if a good is something you must have, like a life-saving medicine, or something you feel like you must have due to an addiction.
# : e.g. medicine, milk, bread
# 
# Luxury good
# : Goods and services for which demand increases more than what is proportional as income rises, so that expenditures on the good become a greater proportion of overall spending.
# : The price elasticity of demand tends to be high if the good is a luxury, something you can easily live without.
# : e.g. luxury car<br><br>
# 
# **Time**<br>
# The price elasticity of demand tends to increase as consumers have more time to adjust to a price change. This means that the long-run price elasticity of demand is often higher than the short-run elasticity.
# 

# ## Elasticity and Total Revenue
# 
# Total revenue
# : Total value of sales of a good or service.
# : <math xmlns="http://www.w3.org/1998/Math/MathML">
#   <mtext>Total Revenue</mtext>
#   <mo>=</mo>
#   <mi>P</mi>
#   <mi>r</mi>
#   <mi>i</mi>
#   <mi>c</mi>
#   <mi>e</mi>
#   <mo>&#x00D7;<!-- × --></mo>
#   <mtext>Quantity Sold</mtext>
# </math>
# 
# 
# > Previously, we mentioned that PED helps firms decide the product's price.
# 
# Except in the rare case of a good with perfectly elastic or perfectly inelastic demand, when a seller raises the price of a good, 2 countervailing effects are present:
# - Price effect
# - Quantity effect
# 
# 
# But the quantity responds differently for elastic and inelastic products.
# - Inelastic demand
#     - Quantity is **insensitive** to a change in price.
#     - If price increases, quantity demanded will fall a little.
#     - If price decreases, quantity demanded increases a little.
#     - People will continue to buy it.
# - Elastic demand
#     - Quantity is **sensitive** to a change in price.
#     - If price increases, quantity demanded will fall a lot.
#     - If price decreases, quantity demanded increases a lot.
# 
# > Let's see how PED affects revenue.
# 
# **Inelastic demand**<br>
# The figure below shows how the revenue changes with a change in price.<br>
# Case 1: The quantity demanded is 130 when the price is 5.<br>
# Case 2: The quantity demanded is 120 when the price is 6.<br>
# Total revenue is the area of the rectangle (price x quantity). Both cases share a common area, A, but the area of B is greater than the area of C. Total revenue in the case 2 is greater than in the case 1.
# 
# This is because the percentage change of quantity demanded is less than the percentage change of quantity price.<br>
# 
# **If demand for a good is inelastic (the price elasticity of demand is less than 1), a higher price increases total revenue.**

# In[4]:


df = pd.DataFrame(data={'price': list(range(2,9)), 'q':list(range(160,99,-10))})
fig1 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('q', title='Quantity demanded', scale=alt.Scale(domain=[0,170])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,9])),
).properties(title='Inelastic Demand Curve')

text1 = alt.Chart({'values':[{'x': 170, 'y': 2}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

df_v1 = pd.DataFrame(data={'price': [6, 6], 'q': [0, 120]})
fig_v1 = alt.Chart(df_v1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

df_h1 = pd.DataFrame(data={'price': [0, 6], 'q': [120, 120]})
fig_h1 = alt.Chart(df_h1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

df_v2 = pd.DataFrame(data={'price': [5, 5], 'q': [0, 130]})
fig_v2 = alt.Chart(df_v2).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

df_h2 = pd.DataFrame(data={'price': [0, 5], 'q': [130, 130]})
fig_h2 = alt.Chart(df_h2).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

text2 = alt.Chart({'values':[{'x': 60, 'y': 3}]}).mark_text(
    text='A',
    fontSize=30
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 60, 'y': 5.5}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 125, 'y': 2.5}]}).mark_text(
    text='C',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig1 + text1 + fig_v1 + fig_h1 + fig_v2 + fig_h2 + text2 + text3 + text4


# **Elastic demand**<br>
# The figure below shows how the revenue changes with a change in price.<br>
# Case 1: The quantity demanded is 1100 when the price is 5.<br>
# Case 2: The quantity demanded is 800 when the price is 6.<br>
# Total revenue is the area of the rectangle (price x quantity). Both cases share a common area, A, but the area of C is greater than the area of B. Total revenue in the case 1 is greater than in the case 2.
# 
# This is because the percentage change of quantity demanded is greater than the percentage change of quantity price.
# 
# **If demand for a good is elastic (the price elasticity of demand is greater than 1), a lower price increases total revenue.**

# In[5]:


df = pd.DataFrame(data={'price': list(range(2,9)), 'q':list(range(2000,199,-300))})
fig1 = alt.Chart(df).mark_line(point=alt.OverlayMarkDef(filled=False, fill='white')).encode(
    alt.X('q', title='Quantity demanded', scale=alt.Scale(domain=[0,2010])),
    alt.Y('price', title='Price', scale=alt.Scale(domain=[0,9])),
).properties(title='Elastic Demand Curve')

text1 = alt.Chart({'values':[{'x': 2070, 'y': 2}]}).mark_text(
    text='D',
    fontSize=15
).encode(x='x:Q', y='y:Q')

df_v1 = pd.DataFrame(data={'price': [6, 6], 'q': [0, 800]})
fig_v1 = alt.Chart(df_v1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

df_h1 = pd.DataFrame(data={'price': [0, 6], 'q': [800, 800]})
fig_h1 = alt.Chart(df_h1).mark_line(color='black', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

df_v2 = pd.DataFrame(data={'price': [5, 5], 'q': [0, 1100]})
fig_v2 = alt.Chart(df_v2).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

df_h2 = pd.DataFrame(data={'price': [0, 5], 'q': [1100, 1100]})
fig_h2 = alt.Chart(df_h2).mark_line(color='red', strokeDash=[4, 2]).encode(
    alt.X('q', title='Quantity demanded'),
    alt.Y('price', title='Price')
)

text2 = alt.Chart({'values':[{'x': 400, 'y': 3}]}).mark_text(
    text='A',
    fontSize=30
).encode(x='x:Q', y='y:Q')

text3 = alt.Chart({'values':[{'x': 400, 'y': 5.5}]}).mark_text(
    text='B',
    fontSize=15
).encode(x='x:Q', y='y:Q')

text4 = alt.Chart({'values':[{'x': 950, 'y': 2.5}]}).mark_text(
    text='C',
    fontSize=15
).encode(x='x:Q', y='y:Q')

fig1 + text1 + fig_v1 + fig_h1 + fig_v2 + fig_h2 + text2 + text3 + text4

