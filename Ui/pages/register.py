import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed", page_title="Register")

# try:
#     print(st.session_state.user_data)
# except:
#     print(st.session_state)

with st.container(border=True):
    st.title('Register')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    
    col1, col2 = st.columns(2)
    with col1:
        phone_number = st.text_input('Phone number')
    with col2:
        email = st.text_input('Email')

    col1, col2 = st.columns(2)
    with col1:
        bank_name = st.text_input('Bank name')
    with col2:
        bank_number = st.text_input('Bank number')
    
    address = st.text_area("Address")

    st.markdown("<div style='margin-top: 25px;'></div>", unsafe_allow_html=True)
    alert_box = st.empty()
    col1, col2 = st.columns(2)
    with col1:
        submit_btn = st.button('Register')
    with col2:
        register_text = "Already have an account? Go to login here"
        if st.button(register_text, type="primary"):
            st.switch_page("pages/login.py")
    if submit_btn:
            if username and password and phone_number and email and bank_name and bank_number and address:
                st.switch_page("pages/page_3.py")
            else:
                alert_box.warning('กรอกให้หมดไอ้เด็กเหี้ย', icon="⚠️")


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