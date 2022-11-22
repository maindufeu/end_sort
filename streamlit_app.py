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
categoria = ['Grande','Grande','Chico','Chico','Grande','Grande','Chico','Grande','Grande','Chico','Chico','Grande','Grande','Grande','Grande','Chico','Grande']
names['Categoria'] = categoria
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

    L = L.sort_values(by="index")[["Nombre", "Familia"]]

    first = L.iloc[0]["Familia"]
    last = L.iloc[len(L)-1]["Familia"]

    if(first != last):
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

if st.button('Grandes'):
    d = secret_santa("Grande")
    st.write(d)
else:
    st.write('...')
    
if st.button('Chicos'):
    st.write(secret_santa("Chico"))
else:
    st.write('...')

import graphviz

# Create a graphlib graph object
graph = graphviz.Digraph()
graph.edge('run', 'intr')
graph.edge('intr', 'runbl')
graph.edge('runbl', 'run')
graph.edge('run', 'kernel')
graph.edge('kernel', 'zombie')
graph.edge('kernel', 'sleep')
graph.edge('kernel', 'runmem')
graph.edge('sleep', 'swap')
graph.edge('swap', 'runswap')
graph.edge('runswap', 'new')
graph.edge('runswap', 'runmem')
graph.edge('new', 'runmem')
graph.edge('sleep', 'runmem')

st.graphviz_chart(graph)
