import streamlit as st
import requests
import json
import subprocess
from datetime import date
import numpy as np
import pandas as pd
import random

DATA_URL = ('https://waop.s3.amazonaws.com/sort.csv')
st.title('Sorteo de fin de año')

names = pd.read_csv('https://waop.s3.amazonaws.com/sort.csv')
categoria = ['Grande','Grande','Chico','Chico','Grande','Grande','Chico','Grande','Grande','Grande','Chico','Grande','Grande','Grande','Grande','Chico','Grande']
names['Categoria'] = categoria
names['Nombre'][names['Nombre']=='Juan Pablo'] = 'Pablo'
st.dataframe(names)
def secret_santa(category_name):

  def shuffling (category_name):
    category = names[names["Categoria"]==category_name]
    category = category.sample(len(category))

    L = pd.DataFrame()
    for fam in category["Familia"].drop_duplicates():
      df = category[category["Familia"] == fam]
      df = df.reset_index()[["Nombre", "Familia", "Categoria"]]
      L = L.append(df.reset_index(), ignore_index=True)

    L = L.sort_values(by="index")[["Nombre", "Familia", 'index']]

    first = L.iloc[0]["Familia"]
    last = L.iloc[len(L)-1]["Familia"]

    ups = False
    ll = list(L['Familia'])
    for i in range(len(ll)-1):
      if ll[i] == ll[i+1]:
        ups = True
        break

    if(first != last and ups == False):
      return(L)
    else:
      return(shuffling(category_name))
    
    

  chain = shuffling(category_name)["Nombre"]

  def closed_circle (chain_list):
    S = len(chain_list)-1
    pairs = {}
    for i in range(S):
      pairs[chain_list[i]] = chain_list[i+1]

    pairs[chain_list[S]] = chain_list[0]
    return(pairs)

  return closed_circle(chain.to_list())

if st.button('Sortear'):
    d = secret_santa("Chico")
    st.write(d)
    graph_grande = "{}".format(d)
    s0 = graph_grande.replace("'",'')
    s1 = s0.replace(":",' -> ')
    s2 = s1.replace(",","\n")
    s3 = s2.replace("{","").replace("}","")

    sf = """
    digraph {{
    {}
    }} 
    """.format(s3)
    
    g = secret_santa("Grande")
    st.write(g)
    graph_grande = "{}".format(g)
    s0 = graph_grande.replace("'",'')
    s1 = s0.replace(":",' -> ')
    s2 = s1.replace(",","\n")
    s3 = s2.replace("{","").replace("}","")

    sfg = """
    digraph {{
    {}
    }} 
    """.format(s3)
    st.graphviz_chart(sf)
    st.graphviz_chart(sfg)
else:
    st.write('...')
    
