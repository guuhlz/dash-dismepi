import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.header("Data App Dismepi")
data = datetime.now((pytz.timezone('America/Sao_Paulo')))

#st.subheader("Atualização - " + str(data.day) +"/"+ str(data.month) +"/"+ str(data.year) +" - "+ str(data.hour) +":"+ str(data.minute) + ":" + str(data.second))
st.subheader("Atualização - 17/06/2024 - 08:40:00")
#st.page_link("./app.py")
#st.page_link("./pages/Dashboard.py")
#st.page_link("./pages/Estoque.py")
#st.page_link("./pages/Grade.py")