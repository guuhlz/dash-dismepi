import streamlit as st
from pedidos import Pedido
import pandas as pd
import plotly.express as px

import st_plots

from numerize.numerize import numerize

pedido = Pedido('.\data\PLANILHA DE PEDIDO DISMEPI_st.xlsx')


st.set_page_config(layout="wide")

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

col = []

col = st.columns(7, gap="small")

with col[0]:
    st.metric("Over",(numerize(pedido.estoque_over())))
with col[1]:
    st.metric("Estoque máximo",numerize(pedido.estoque_maximo()))
with col[2]:
    st.metric("Estoque minimo",numerize(pedido.estoque_minimo()))
with col[3]:
    delta_estoque = pedido.estoque_real() - pedido.estoque_maximo()
    st.metric("Estoque Real",numerize(pedido.estoque_real()),
              delta=numerize(delta_estoque))
with col[4]:
    st.metric("Down",numerize(pedido.estoque_down()))
with col[5]:
    st.metric("Ambev hl",(pedido.estoque_ambev_hl()))
with col[6]:
    st.metric("MKTP","R$" +str(numerize(pedido.estoque_mktp_valor())))

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(st_plots.fig_top10_impacto_over(pedido),use_container_width=True)
with col2:
    st.plotly_chart(st_plots.fig_top10_impacto_down(pedido),use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    st.plotly_chart(st_plots.fig_percentual_over_10(pedido),use_container_width=True)
with col4:
    st.plotly_chart(st_plots.fig_percentual_down_10(pedido),use_container_width=True)
