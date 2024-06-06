import pandas as pd
import streamlit as st
import numerize

st.set_page_config(layout="wide")

grade = pd.read_csv('./data/grade.csv',sep=';')

grade['Cod'] = grade['Cod'].apply(lambda x: '{:.0f}'.format(x))

st.dataframe(grade[['Cod',
                    'Descricao',
                    'UN',
                    'Inicial',
                    'Saidas',
                    'Disp.']],hide_index=True,use_container_width=True)