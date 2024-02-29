import streamlit as st
import condb as con
import hashlib 
st.set_page_config(initial_sidebar_state="collapsed", page_title="Login")

# try:
#     print(st.session_state)
# except:
#     print(st.session_state) 

if 'ai_offer_price' in st.session_state:
    st.session_state.ai_offer_price = None

with st.container(border=True):
    st.title('Login', anchor=False)
    user_name = st.text_input('Username')
    password = st.text_input('Password', type='password')

    alert_box = st.empty()
    col1, col2 = st.columns(2)
    with col1:
        login_btn = st.button('Login')

    with col2:
        register_text = "Doesn't have an account? Go to register here"
        if st.button(register_text, type="primary"):
            st.switch_page("pages/register.py")

    if login_btn:
        if user_name and password:
            user_data = con.selectData(table='users', condition=f"user_name='{user_name}'")
            if len(user_data) <= 0:
                alert_box.error('invalid username or password', icon="⚠️")
            else:
                # CHECK INPUT PASS WITH PASS IN DB
                hash_pass = hashlib.sha1(password.encode())
                user_pass = user_data[0][2]
                if hash_pass.hexdigest() == user_pass:
                    st.session_state.user_data = user_data[0]
                    if user_data[0][6]:
                        if user_data[0][6].strip() == 'admin':
                            st.switch_page("pages/sale_history_admin.py")
                    st.switch_page("pages/sale.py")
                else:
                    alert_box.error('invalid username or password', icon="⚠️")
        else:
            alert_box.warning('username and password can\'t be blank!', icon="⚠️")

st.markdown(
    """
    <style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 6%;}
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