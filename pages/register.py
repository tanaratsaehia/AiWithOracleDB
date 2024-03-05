import streamlit as st
import condb as con
import hashlib

st.set_page_config(initial_sidebar_state="collapsed", page_title="Register")

# try:
#     print(st.session_state.user_data)
# except:
#     print(st.session_state)

with st.container(border=True):
    st.title('Register', anchor=False)
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
    empty_container = st.container(border=False)
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
                find_user = con.selectData(table='users', condition=f"user_name='{username}'")
                if len(find_user) > 0:
                    alert_box.warning(f'username "{username}" already used', icon="⚠️")
                else:
                    with st.spinner('Loading...'):
                        hash_pass = hashlib.sha1(password.encode())
                        insert_data = f"'{username}', '{hash_pass.hexdigest()}', '{phone_number}', '{email}', '{address}', 'user', '{bank_number}', '{bank_name}'"
                        try:
                            max_primary = con.selectData(table='users', column='max(user_id)')
                            max_primary = max_primary[0][0]
                            if max_primary == None:
                                max_primary = 0
                            # insert into users values (1, 'oil', '4c39de83231366548c7756c3ff20f1ad97c1b6c3', '0984321907', null, 'หลังมอ', 'user', '0984321907', 'กรุงโรม');
                            insert_state = con.insertData(table='users', primary_key=max_primary+1, values=insert_data)
                            if insert_state:
                                alert_box.success('register complete please go to login', icon='✅')
                            else:
                                alert_box.warning('something wrong please try again', icon="⚠️")
                        except:
                            alert_box.error('database error', icon="❌")
            else:
                alert_box.warning('Please fill up this form', icon="⚠️")


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