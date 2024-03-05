import streamlit as st
import condb as con
import time
import base64

st.set_page_config(initial_sidebar_state="collapsed", page_title="sale history", layout="wide")

if 'update_state' not in st.session_state or 'confrim_state' not in st.session_state:
    st.session_state.update_state = False
    st.session_state.confrim_state = False

def open_image(path: str):
    with open(path, "rb") as p:
        file = p.read()
        return f"data:image/png;base64,{base64.b64encode(file).decode()}"

def check_sales_status(sale_id):
    try:
        status = con.selectData(table='sales_history', column='status', condition=f"sale_id = '{sale_id}'" )
        if len(status) > 0:
            return status[0][0]
        else:
            return None
    except:
        return None

path_pic = './public/picture/'
table_data = []

car_data = con.selectData(table='admin_sale_history_data')

for i in car_data:
    table_data.append({'pic': open_image(path_pic+i[0]), 
                        'sale id': i[1],
                        'user id': i[2], 
                        'user name': i[3],
                        'phone number': i[8],
                        'car model': i[4], 
                        'production year': i[5], 
                        'mile used': i[6], 
                        'license plate': i[7], 
                        'predict price': i[9], 
                        'user offer price': i[10],
                        'admin offer price': i[11],
                        'status': i[12]
                        })

with st.container(border=True):
    st.title('Sale history for Admin', anchor=False)
    with st.container(border=True):
        edited_df = st.dataframe(table_data, width=1500, height=400, column_config={
                                                            "pic": st.column_config.ImageColumn("pic", help="form user uplaod")
                                                            })
    con_col1, con_col2 = st.columns(2)

with con_col1.container(border=True):
    st.subheader('Offer price')
    col1, col2 = st.columns(2)
    sale_id = col1.text_input('Sale ID')
    offer_price = col2.text_input('Offer price')
    alert_box = st.empty()
    submit_btn = st.button('Save', key=1456999)

    if submit_btn:
        alert_box.empty()
        st.session_state.update_state = True
    
    if st.session_state.update_state:
        sale_status = check_sales_status(sale_id)
        if sale_status:
            update_state = con.updateData(table='sales_history', set=f"admin_offer_price={offer_price}, status='admin offer'", condition=f'sale_id ={sale_id}')
            if update_state:
                alert_box.success('Update success', icon='✅')
                st.session_state.update_state = False
                time.sleep(1.5)
                alert_box.empty()
            else:
                alert_box.error('Update fail', icon='❌')
                st.session_state.update_state = False
                time.sleep(1.5)
                alert_box.empty()
        else:
            alert_box.warning(f'Sale ID {sale_id} not found', icon="⚠️")
            st.session_state.update_state = False

with con_col2.container(border=True):
    st.subheader('Confirm order')
    col1, col2 = st.columns(2)
    sale_id = col1.text_input('Sale ID', key=888)
    option = col2.selectbox('Status option', ('Confirm', 'Cancel'))
    if option == 'Confirm':
        update_option = 'admin confirm'
    elif option == 'Cancel':
        update_option = 'admin cancel'
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
                alert_box.error('Update fail', icon='❌')
                st.session_state.confrim_state = False
                time.sleep(1.5)
                alert_box.empty()
        else:
            alert_box.warning(f'Sale ID {sale_id} not found!', icon="⚠️")
            st.session_state.confrim_state = False


st.markdown(
    """
    <style>
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

