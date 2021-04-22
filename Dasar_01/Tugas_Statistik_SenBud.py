#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


stat="NilaiSeni.csv"
df = pd.read_csv(stat)
# print(df.to_string())
df


# In[11]:


nilai= df['nilai_uas']
nilai


# In[12]:


mean = nilai.mean()
print("mean :", mean)
median = nilai.median()
print("median :", median)
modus = nilai.mode()
print("modus :", modus)


# In[13]:


plt.figure(figsize=(15,5))
plt.hist(nilai,bins=35,color='grey')
plt.axvline(mean,color='red',label='Mean')
plt.axvline(median,color='yellow',label='Median')
plt.axvline(modus[0],color='green',label='Modus')
plt.xlabel('nilai_uas')
plt.ylabel('frekuensi')
plt.legend()
plt.show()


# In[17]:


maks = nilai.max()
minm = nilai.min()
jarak = maks - minm
varians = nilai.var()
simp_baku = nilai.std()
koef_var = simp_baku / mean

# menampilkan ukuran nilai deviasi
print('Nilai tertinggi: ',maks,'\nNilai terendah: ',minm,'\nRange: ',jarak, '\nVarians: ',varians,'\nSimpangan Baku: ', simp_baku,'\nKoefisien Variasi: ',koef_var)


# In[ ]:




