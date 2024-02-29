from datetime import datetime
import streamlit as st
import condb as con
import base64
import time

st.set_page_config(initial_sidebar_state="collapsed", page_title="sale history", layout="wide")

if 'user_data' in st.session_state:
    user_data = st.session_state.user_data
    st.session_state.ai_offer_price = None
else:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print(formatted_time,'user data not found! ', st.session_state)
    st.error('user data not found! redirect to login', icon='❌')
    time.sleep(3)
    st.switch_page("pages/login.py")

def open_image(path: str):
    with open(path, "rb") as p:
        file = p.read()
        return f"data:image/png;base64,{base64.b64encode(file).decode()}"

def get_data():
    user_id = user_data[0]
    query_str = f"""
        select path_picture, model, production_year, mile_used, license_plate, predict_price, user_offer_price, admin_offer_price, status
        from users, sales_history, car
        where users.user_id = sales_history.user_id and sales_history.car_id = car.car_id and sales_history.user_id = {user_id}
        order by sale_id
    """
    
    path_pic = 'D:/KKU_World/1_2/DBMS/termProject/python/Ui/public/picture/'
    table_data = []
    try:
        car_data = con.querySql(query_str)   
        for i in car_data:
            table_data.append({'pic': open_image(path_pic+i[0]), 
                                'car model': i[1], 
                                'production year': i[2], 
                                'mile used': i[3], 
                                'license plate': i[4],
                                'predict price': i[5], 
                                'user offer price': i[6],
                                'admin offer price': i[7],
                                'status': i[8]
                                })
        return table_data
    except:
        st.error('Database Error', icon='❌')
        return None

with st.container(border=False):
    to_sale_btn = st.button('Go to sale page', use_container_width=True)
    
    if to_sale_btn:
        st.switch_page('pages/sale.py')

with st.container(border=True):
    user_name = user_data[1]
    st.title(f'{user_name} sale history', anchor=False)
    table_data = get_data()
    edited_df = st.data_editor(table_data, width=1500, height=400, column_config={
                                                            "pic": st.column_config.ImageColumn(
                                                            "pic", help="form user uplaod"
                                                        )})


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
    .st-emotion-cache-1n9qh9a {
        border-radius: 0.5rem;
        border: 1px solid rgba(250, 250, 250, 0.2);
    }
    .st-emotion-cache-1n9qh9a:hover {
        text-decoration: none;
        color: #33cc33 !important;
        border-color: #33cc33 !important;
    }
    .st-emotion-cache-1n9qh9a:focus {
        text-decoration: none;
        color: #33cc33 !important;
        border-color: #33cc33 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)