
# coding: utf-8

# In[52]:

#Mohamad Ashraf Mohamad Hosny . 
#3/9/2019 
#This is a simple Python Calculator Code .


#basic operations implemented by 4 funs. : 

def Sum(q,w):
    return q+w 
def Sub(e,r):
    return e-r

def Mul(t,y):
    return t*y 

def Div(o,p):
    return o/p


# fun. Calc is what u have to call to calculate 
def Calc(z,x,oprtn) :
    if oprtn=='sum' or oprtn=='Sum' :
        return Sum(z,x)
    
    if oprtn=='sub' or oprtn=='Sub' :
        return Sub(z,x)
    
    if oprtn=='mul' or oprtn=='Mul' :
        return Mul(z,x)
    
    if oprtn=='div' or oprtn=='Div' :
        return Div(z,x)



# In[53]:

Calc(4,5,'div')


# In[54]:

Calc(4,5,'Mul')


# In[55]:

Calc(4,5,'sum')


# In[56]:

Calc(4,5,'sub')


# In[ ]:




# In[ ]:



