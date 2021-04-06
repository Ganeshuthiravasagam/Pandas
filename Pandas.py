#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.DataFrame({'From_To': ['LoNDon_paris', 'MAdrid_miLAN',
'londON_StockhOlm','Budapest_PaRis', 'Brussels_londOn'],
'FlightNumber': [10045, np.nan, 10065, np.nan, 10085],
'RecentDelays': [[23, 47], [], [24, 43, 87], [13], [67, 32]],
'Airline': ['KLM(!)', '<Air France> (12)', '(British Airways. )',
'12. Air France', '"Swiss Air"']})
df['FlightNumber'] = df['FlightNumber'].interpolate().astype(int)
df[["First", "Last"]]= df["From_To"].str.split("_", expand=True)
del df["From_To"]
df["First"]=df["First"].str.lower()
df["Last"]=df["Last"].str.lower()
df["First"]=df["First"].str.capitalize()

df["city"]=df["First"] + "_" + df["Last"]
df = df.drop(["First", "Last"], axis=1)
delays = pd.DataFrame(df.RecentDelays.values.tolist())
delays.columns = ['delay_1', 'delay_2', 'delay_3']
df.pop("RecentDelays")
df = pd.concat([df, delays[['delay_1', 'delay_2', 'delay_3']]], axis=1)
df


# In[ ]:




