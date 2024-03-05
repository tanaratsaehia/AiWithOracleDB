from datetime import datetime
import streamlit as st
import condb as con
import base64
import time

st.set_page_config(initial_sidebar_state="collapsed", page_title="sale history", layout="wide")

if 'update_state' not in st.session_state or 'confrim_state' not in st.session_state:
    st.session_state.update_state = False
    st.session_state.confrim_state = False

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
        select path_picture, sale_id, model, production_year, mile_used, license_plate, predict_price, user_offer_price, admin_offer_price, status
        from sales_history, car
        where sales_history.car_id = car.car_id and sales_history.user_id = {user_id}
        order by sale_id
    """
    path_pic = './public/picture/'
    table_data = []
    try:
        car_data = con.querySql(query_str)   
        for i in car_data:
            table_data.append({'pic': open_image(path_pic+i[0]), 
                                'sale id': i[1],
                                'car model': i[2], 
                                'production year': i[3], 
                                'mile used': i[4], 
                                'license plate': i[5],
                                'predict price': i[6], 
                                'user offer price': i[7],
                                'admin offer price': i[8],
                                'status': i[9]
                                })
        return table_data
    except:
        st.error('Database Error', icon='❌')
        return None

def check_sales_status(sale_id):
    try:
        status = con.selectData(table='sales_history', column='status', condition=f"sale_id = '{sale_id}'" )
        if len(status) > 0:
            return status[0][0]
        else:
            return None
    except:
        return None

with st.container(border=False):
    to_sale_btn = st.button('Go to sale page', use_container_width=True)
    
    if to_sale_btn:
        with st.spinner('Loading...'):
            st.switch_page('pages/sale.py')

with st.container(border=True):
    user_name = user_data[1]
    st.title(f'{user_name} sale history', anchor=False)
    table_data = get_data()
    
    with st.container(border=False):
        edited_df = st.dataframe(table_data, width=1500, height=400, column_config={
                                                            "pic": st.column_config.ImageColumn(
                                                            "pic", help="form user uplaod"
                                                        )})
    
    con_col1, con_col2 = st.columns(2)

with con_col1.container(border=True):
    st.subheader('Offer price')
    col1, col2 = st.columns(2)
    sale_id = col1.text_input('Sale ID')
    offer_price = col2.text_input('Offer price')
    alert_box = st.empty()
    submit_btn = st.button('Save', key=2555555)

    if submit_btn:
        alert_box.empty()
        st.session_state.update_state = True
    
    if st.session_state.update_state:
        sale_status = check_sales_status(sale_id)
        if sale_status:
            update_state = con.updateData(table='sales_history', set=f"user_offer_price={offer_price}, status='user offer'", condition=f'sale_id ={sale_id}')
            if update_state:
                alert_box.success('Update success', icon='✅')
                st.session_state.update_state = False
                table_data = get_data()
                time.sleep(2)
                alert_box.empty()
            else:
                alert_box.error('Update fail', icon='❌')
                st.session_state.update_state = False
                time.sleep(2)
                alert_box.empty()
        else:
            alert_box.warning(f'Sale id {sale_id} not found', icon="⚠️")
            st.session_state.update_state = False

with con_col2.container(border=True):
    st.subheader('Confirm order')
    col1, col2 = st.columns(2)
    sale_id = col1.text_input('Sale ID', key=888)
    option = col2.selectbox('Status option', ('Confirm', 'Cancel'))
    if option == 'Confirm':
        update_option = 'user confirm'
    elif option == 'Cancel':
        update_option = 'user cancel'
    alert_box = st.empty()
    submit_btn = st.button('Save')
    
    if submit_btn:
        alert_box.empty()
        st.session_state.confrim_state = True
    
    if st.session_state.confrim_state:
        sale_status = check_sales_status(sale_id)
        
        if sale_status:
            update_state = con.updateData(table='sales_history', set=f"status='{update_option}'", condition=f'sale_id ={sale_id}')
            if update_state:
                alert_box.success('Update success', icon='✅')
                st.session_state.confrim_state = False
                time.sleep(1.5)
                alert_box.empty()
                
            else:
                alert_box.error('Confirm fail', icon='❌')
                st.session_state.confrim_state = False
                time.sleep(1.5)
                alert_box.empty()
        else:
            alert_box.warning(f'Sale ID {sale_id} not found!', icon="⚠️")
            st.session_state.confrim_state = False

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