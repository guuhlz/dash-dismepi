import streamlit as st
from datetime import datetime
import pytz

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

st.header("Data App Dismepi")
data = datetime.now((pytz.timezone('America/Sao_Paulo')))

#st.subheader("Atualização - " + str(data.day) +"/"+ str(data.month) +"/"+ str(data.year) +" - "+ str(data.hour) +":"+ str(data.minute) + ":" + str(data.second))
st.subheader("Atualização - 08/07/2024 - 10:00:00")
#st.page_link("./app.py")
#st.page_link("./pages/Dashboard.py")
#st.page_link("./pages/Estoque.py")
#st.page_link("./pages/Grade.py")