#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[71]:


import pandas as pd
import numpy as np


# In[72]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[78]:


def q1():
    return(black_friday.shape)


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[79]:


def q2():
    return(black_friday[(black_friday['Gender'] == "F") & (black_friday['Age'] == "26-35")].shape[0])


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[80]:


def q3():
    return(black_friday['User_ID'].nunique())


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[81]:


def q4():
    aux = pd.DataFrame({"Tipos": black_friday.dtypes})
    return(aux['Tipos'].nunique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[82]:


def q5():
    nan_rows = black_friday[black_friday.isnull().T.any().T]
    return(nan_rows.shape[0] / black_friday.shape[0])


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[83]:


def q6():
    return(black_friday[(black_friday['Product_Category_3'].isna())].shape[0])


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[84]:


def q7():  
    return(float(black_friday[(black_friday['Product_Category_3'].notna())]['Product_Category_3'].mode().values))


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[88]:


def q8():
    df_purchase = black_friday['Purchase']
    min_purchase = df_purchase.min()
    max_purchase = df_purchase.max()
    return(((df_purchase - min_purchase)/(max_purchase - min_purchase)).mean()).item()   


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[93]:


def q9():
    #df_purchase = black_friday['Purchase']
    #min_purchase = df_purchase.min()
    #max_purchase = df_purchase.max()
    #df_purchase_norm = ((df_purchase - df_purchase.mean())/(df_purchase.std()))
    #return((df_purchase_norm >= - 1) & (df_purchase_norm <= 1)).sum().item()
    df_padronizado = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std()
    return ((df_padronizado >= -1) & (df_padronizado <= 1)).sum().item()
q9()


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[95]:


def q10():
    qntd_null_pc2 = black_friday[(black_friday['Product_Category_2'].isna())].shape[0]
    qntd_null_pc2_e_pc3 = black_friday[(black_friday['Product_Category_2'].isna()) & (black_friday['Product_Category_3'].isna())].shape[0]
    return(qntd_null_pc2 == qntd_null_pc2_e_pc3)


# In[ ]:




