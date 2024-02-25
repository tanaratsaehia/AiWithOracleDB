import streamlit as st
import pickle
st.set_page_config(initial_sidebar_state="collapsed", page_title="loading...")

with st.container(border=False):
    with st.spinner('Loading...'):
        with open(r'D:\KKU_World\1_2\DBMS\termProject\python\Ai\random_forest_model.pkl', 'rb') as f:
            loaded_model = pickle.load(f)

st.session_state.ai_model = loaded_model
# print(type(loaded_model))

st.switch_page("pages/login.py")