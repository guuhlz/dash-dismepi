import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(layout="wide")


st.header("Data App Dismepi")
data = datetime.now((pytz.timezone('America/Sao_Paulo')))

#st.subheader("Atualização - " + str(data.day) +"/"+ str(data.month) +"/"+ str(data.year) +" - "+ str(data.hour) +":"+ str(data.minute) + ":" + str(data.second))
st.subheader("Atualização - 12/06/2024 - 09:32:00")
#st.page_link("./app.py")
#st.page_link("./pages/Dashboard.py")
#st.page_link("./pages/Estoque.py")
#st.page_link("./pages/Grade.py")