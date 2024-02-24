import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed", page_title="Login")

with st.container(border=True):
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    col1, col2 = st.columns(2)
    with col1:
        if st.button('Login'):
            st.switch_page("pages/sale.py")

    with col2:
        register_text = "Doesn't have an account? Go to register here"
        if st.button(register_text, type="primary"):
            st.switch_page("pages/register.py")

st.markdown(
    """
    <style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 4%;}
    .eczjsme1 {
        display: none;
    }
    .st-b9:hover{
        border-color: #00ccff !important;
        box-shadow: 3px #00ccff !important;
    }
    .st-by:hover{
        border-color: #00ccff !important;
        box-shadow: 3px #00ccff !important;
    }
    button {
        background: none!important;
    }
    button:hover {
        text-decoration: none;
        color: #00ccff !important;
        border-color: #00ccff !important;
    }
    button:focus {
        text-decoration: none;
        color: #00ccff !important;
        border-color: #00ccff !important;
    }
    button[kind="primary"] {
        background: none!important;
        border: none;
        padding: 0!important;
        color: white !important;
        text-decoration: none;
        cursor: pointer;
        border: none !important;
    }
    button[kind="primary"]:hover {
        text-decoration: none;
        color: #00ccff !important;
    }
    button[kind="primary"]:focus {
        outline: none !important;
        box-shadow: none !important;
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)