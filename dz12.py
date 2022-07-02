#!/usr/bin/env python
# coding: utf-8

# In[217]:


import pandas as pd
import matplotlib.pyplot as plt


# In[218]:


pd_df = pd.read_csv('company_sales_data.csv')
pd_df.head()


# In[219]:


month_list = pd_df['month_number']
facecream_list = pd_df['facecream']
facewash_list = pd_df['facewash']
toothpaste_list = pd_df['toothpaste']
bathingsoap_list = pd_df['bathingsoap']
shampoo_list = pd_df['shampoo']
moisturizer_list = pd_df['moisturizer']
units_list = pd_df['total_units']
profit_list = pd_df['total_profit']


# In[220]:


plt.plot(month_list,facecream_list, label = 'facecream')
plt.plot(month_list,facewash_list, label = 'facewash')
plt.plot(month_list,toothpaste_list, label = 'toothpaste')
plt.plot(month_list,bathingsoap_list, label = 'bathingsoap')
plt.plot(month_list,shampoo_list, label = 'shampoo')
plt.plot(month_list,moisturizer_list, label = 'moisturizer')
plt.title('данные о продажах продукта')
plt.xticks(month_list)
plt.yticks([2500, 5000, 7500, 10000, 12500, 15000, 17500])
plt.grid()
plt.legend(loc = 2)
plt.show()


# In[221]:


fig, ax = plt.subplots()
ax.bar(month_list, bathingsoap_list)
plt.title('данные о продажах мыла для купания')
plt.xticks(month_list)
plt.grid()
plt.show()


# In[222]:


facecream_sum = facecream_list.sum()
facewash_sum = facewash_list.sum()
toothpaste_sum = toothpaste_list.sum()
bathingsoap_sum = bathingsoap_list.sum()
shampoo_sum = shampoo_list.sum()
moisturizer_sum = moisturizer_list.sum()


# In[223]:


labels = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
values = [facecream_sum,facewash_sum,toothpaste_sum,bathingsoap_sum,shampoo_sum,moisturizer_sum]
plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title('общие данные о продажах за год для каждого продукта')
plt.show()


# In[ ]:




