#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from sympy import symbols


# In[22]:


from sympy import simplify


# In[52]:


sigma, uH, lambda_, theta, u, q, c = symbols('sigma uH lambda theta u q c', real=True, positive=True)


# In[53]:


rL = (1-lambda_)*((1-sigma)*u+sigma*lambda_-sigma*(theta-1))


# In[54]:


rH = (1-lambda_)*((1-sigma)*u+sigma*lambda_-sigma*(theta-1)) +lambda_*theta


# In[55]:


RH=(1-lambda_)*((1-sigma)*uH+sigma*lambda_-sigma*(theta-1)) +lambda_*theta #wrong rh in separating contract


# In[56]:


pH = (1-sigma)*uH+sigma*lambda_ - sigma*(theta-1)


# In[57]:


ph = (1-sigma)*u+sigma*lambda_ - sigma*(theta-1)


# In[58]:


pL = (1-sigma)*u+sigma*lambda_ 


# In[59]:


pL


# In[60]:


a=u +sigma*(lambda_-u)


# In[61]:


simplify(pL-a)==0


# In[30]:


Ssep=q**2*(pH-rH+lambda_*theta)+q*(1-q)*(ph-rH+lambda_*theta)+(1-q)*(pL-rL)


# In[31]:


Ssep


# In[36]:


SSEP_paper=lambda_*((1-sigma)*u+sigma*lambda_-sigma*(theta-1))+q**2*(1-sigma)*(uH-u)+(1-q)*sigma*(theta-1)


# In[37]:


SSEP_guess=q**2.*(pH-RH+lambda_*theta)+q*(1.-q)*(ph-RH+lambda_*theta)+(1.-q)*(pL-rL)


# In[ ]:





# In[47]:


SSEP==lambda_*((1-sigma)*u+sigma*lambda_-sigma*(theta-1))+q**2*(1-sigma)*(uH-u)+(1-q)*sigma*(theta-1)


# In[48]:


SSEP


# In[ ]:





# In[62]:


def check_equal(Expr1,Expr2):
    if Expr1==None or Expr2==None:
        return(False)
    if Expr1.free_symbols!=Expr2.free_symbols:
        return(False)
    vars = Expr1.free_symbols
    your_values=np.random.random(len(vars))
    Expr1_num=Expr1
    Expr2_num=Expr2
    for symbol,number in zip(vars, your_values):
        Expr1_num=Expr1_num.subs(symbol, sp.Float(number))
        Expr2_num=Expr2_num.subs(symbol, sp.Float(number))
    Expr1_num=float(Expr2_num)
    Expr2_num=float(Expr2_num)
    if not np.allclose(Expr1_num,Expr2_num):
        return(False)
    if (Expr1.equals(Expr2)):
        return(True)
    else:
        return(False)


# In[63]:


check_equal(SSEP_guess,SSEP_paper)


# In[64]:


check_equal(SSEP_paper,Ssep)


# In[65]:


#Formula for rH as in the paper, with u, instead of uH
rH_CB = (1-lambda_)*((1-sigma)*u+sigma*lambda_)+lambda_*theta


# In[71]:


rH_St = rH_CB


# In[72]:


rL_CB = (1-lambda_)*((1-sigma)*u+sigma*lambda_)

rL_St = rL_CB
# In[68]:


#Formula for sellers payoff using CBDC
SCBDC = q*(pH-rH_CB+lambda_*theta) + (1-q)*(pL-rL_CB)


# In[69]:


SCBDC_paper = lambda_*((1-sigma)*u+sigma*lambda_)+q*((1-sigma)*(uH-u)-sigma*(theta-1))


# In[70]:


check_equal(SCBDC_paper,SCBDC)


# In[47]:


simplify(SCBDC_paper-SCBDC)==0


# In[49]:


#rH using deposit with the given parameters
(1-0.4)*12-0.4*(4-1)


# In[50]:


#rH using stablecoi
(1-0.4)*8


# In[51]:


1/1.025


# In[73]:


#payoff using stablecoins
piH_form = pH - rH_St + lambda_*theta - c


# In[81]:


piH_res = (1-sigma)*(uH-(1-lambda_)*u)+lambda_**2*sigma-sigma*(theta-1)-c


# In[82]:


simplify(piH_form-piH_res)==0


# In[80]:


piH_form


# In[ ]:




