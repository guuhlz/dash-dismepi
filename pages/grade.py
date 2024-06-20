import pandas as pd
import streamlit as st
import numerize

st.set_page_config(layout="wide")


hide_css = """
<style>
.st-emotion-cache-15ecox0, .ezrtsby0 {
    display: none;
}
</style>
"""

# Injetar o CSS no Streamlit
st.markdown(hide_css, unsafe_allow_html=True)

#grade = st.session_state['df_grade']
grade = pd.read_csv('./data/grade.csv',sep=';')

#grade['Cod'] = (grade['Cod'].apply(lambda x: '{:.0f}'.format(x)))
grade['Cod'].replace(",","")

st.dataframe(grade[['Cod',
                    'Descricao',
                    'UN',
                    'Inicial',
                    'Saidas',
                    'Disp.']],hide_index=True,use_container_width=True)