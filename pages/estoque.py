import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

st.title("Estoque")
estoque = pd.read_excel('data\PLANILHA DE PEDIDO DISMEPI_st.xlsx',sheet_name='PEDIDO')
estoque['Código Promax'].astype('str')
estoque['PERCENTUAL OVER/DOWN'] = estoque['PERCENTUAL OVER/DOWN'] * 100

st.dataframe(estoque[['Código Promax',
                      'Prod. Completo',
                      'ESTOQUE',
                      #'PALETIZAÇÃO',
                      #'ESTOQUE \nPALETE',
                      'ESTOQUE MÍNIMO',
                      'ESTOQUE MÁXIMO',
                      'ESTOQUE REAL',
                      'PERCENTUAL OVER/DOWN',
                      'OVER/DOWN']]
                      ,hide_index=True) 