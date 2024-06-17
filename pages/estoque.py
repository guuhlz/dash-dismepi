import pandas as pd
import streamlit as st
import numerize

st.set_page_config(layout="wide")

op = st.radio ("Categorias",['Todos','Cerveja','Nab','Match','Mktp'],horizontal=True)


#st.header("Estoque")
estoque = pd.read_excel('./data/PLANILHA DE PEDIDO DISMEPI_st.xlsx',sheet_name='PEDIDO')
estoque['Código Promax'] = estoque['Código Promax'].apply(lambda x: '{:.0f}'.format(x))
#estoque['ESTOQUE'] = estoque['ESTOQUE'].apply(lambda x: '{:.0f}'.format(x))

#estoque['ESTOQUE MÁXIMO'] = estoque['ESTOQUE MÁXIMO'].apply(lambda x: '{:.2f}'.format(x))

estoque['PERCENTUAL OVER/DOWN'] = estoque['PERCENTUAL OVER/DOWN'] * 100
#estoque['PERCENTUAL OVER/DOWN'] = estoque['PERCENTUAL OVER/DOWN'].apply(lambda x: '{:.2f}'.format(x))


estoque = estoque.rename(
    columns={'ESTOQUE MÁXIMO': 'Estoque máximo (R$)',
             'ESTOQUE MÍNIMO': 'Estoque mínimo (R$)',
             'ESTOQUE': 'Estoque',
             'Código Promax': 'Código',
             'Prod. Completo': 'Produto',
             'ESTOQUE REAL': 'Estoque Real (R$)',
             #'PERCENTUAL OVER/DOWN': 'Percentual Over/Down (%)',
             'OVER/DOWN': 'Over/Down (R$)',
             'PALETIZAÇÃO': 'Paletização',
             }
)

if (op == 'Todos'):
    df = estoque
elif (op == 'Cerveja'):
    df = estoque[estoque['Categorização'] == '001 - CERVEJA']
elif (op == 'Nab'):
    df = estoque[estoque['Categorização'] == '002 - Nab']
elif (op == 'Match'):
    df = estoque[estoque['Categorização'] == '004 - BEBIDAS QUENTES']
else:
    df = estoque[estoque['Categorização'] == '003 - MKTP']






st.dataframe(df[['Código',
                    'Produto',
                    'Estoque',
                    'Paletização',
                    'Estoque mínimo (R$)',
                    'Estoque máximo (R$)',
                    'Estoque Real (R$)',
                    #'Percentual Over/Down (%)',
                    'Over/Down (R$)']]
                    ,hide_index=True,use_container_width=True
            )
