from datetime import datetime
import streamlit as st
import condb as con
import pickle
import time

st.set_page_config(initial_sidebar_state="collapsed", page_title="sale")

# try:
#     print(st.session_state)
# except:
#     print(st.session_state) 


# INITIAL STATE
if 'ai_offer_price' not in st.session_state or 'offer_btn_state' not in st.session_state or 'accept_btn_state' not in st.session_state or 'to_sale_page_button_state' not in st.session_state or 'confirm_offer_btn_state' not in st.session_state:
    st.session_state.ai_offer_price = None
    st.session_state.offer_btn_state = False
    st.session_state.accept_btn_state = False
    st.session_state.to_sale_page_button_state = False
    st.session_state.confirm_offer_btn_state = False

model_mapping = {
    'Fiesta': 0,
    'Focus': 1,
    'Kuga': 2,
    'EcoSport': 3,
    'C-MAX': 4,
    'Ka+': 5,
    'Mondeo': 6,
    'B-MAX': 7,
    'S-MAX': 8,
    'Grand C-MAX': 9,
    'Galaxy': 10,
    'Edge': 11,
    'KA': 12,
    'Puma': 13,
    'Tourneo Custom': 14,
    'Grand Tourneo Connect': 15,
    'Mustang': 16,
    'Tourneo Connect': 17,
    'Fusion': 18,
    'Streetka': 19,
    'Ranger': 20,
    'Escort': 21,
    'Transit Tourneo': 22
}

transmission_mapping = {
    'Manual': 0,
    'Automatic': 1,
    'Semi-Auto': 2
}

fuel_mapping = {
    'Petrol': 0,
    'Diesel': 1,
    'Hybrid': 2,
    'Electric': 3,
    'Other': 4
}

keys_model = tuple(model_mapping.keys())
keys_trans = tuple(transmission_mapping.keys())
keys_fuel = tuple(fuel_mapping.keys())

current_time = datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

def save_image(pic_file, file_name: str) -> bool:
    with open(f'public/picture/{file_name}', "wb") as f:
        f.write(pic_file.read())

def find_car_id(model,  production_year, engine_size, miles_per_gallon, trans_id, fuel_id):
    """
        if found exist car in DB return exist car id
        if not found insert new car and return new car id
    """
    condition_find_car = f"model='{model}' and production_year={production_year} and engine_size={engine_size} and miles_per_gallon={miles_per_gallon} and trans_id={trans_id} and fuel_id={fuel_id}"
    exist_car = con.selectData(table='car', condition=condition_find_car)
    
    if len(exist_car) <= 0:
        format_insert_data = f"'{model}', {production_year}, {engine_size}, {miles_per_gallon}, {trans_id}, {fuel_id}"
        max_car_id = con.selectData(table='car', column='max(car_id)')
        max_car_id = max_car_id[0][0]
        
        if max_car_id == None:
            max_car_id = 0
        con.insertData(table='car', primary_key=max_car_id+1, values=format_insert_data)
        return max_car_id+1
    else:
        return exist_car[0][0]

if 'user_data' in st.session_state:
    user_data = st.session_state.user_data
else:
    print(formatted_time,'user data not found! ', st.session_state)
    st.error('user data not found! redirect to login', icon='❌')
    time.sleep(3)
    st.switch_page("pages/login.py")

if ('ai_model' in st.session_state):
    ai_model = st.session_state.ai_model
else:
    print("ai model not found lodaing....")
    with st.container(border=False):
        with st.spinner('Loading...'):
            with open(r'D:\KKU_World\1_2\DBMS\termProject\python\Ai\random_forest_model.pkl', 'rb') as f:
                loaded_model = pickle.load(f)
    ai_model = loaded_model
    st.session_state.ai_model = loaded_model

with st.container(border=False):
    to_sale_history_btn = st.button('back to sale history', use_container_width=True)
    
    if to_sale_history_btn:
        st.switch_page('pages/sale_history.py')

with st.container(border=True):
    st.title(f'Welcome {user_data[1]} to Sale page', anchor=False)
    uploaded_file_box = st.empty()
    uploaded_file = st.file_uploader("Upload your car picture")
    if uploaded_file:
        uploaded_file_box.image(uploaded_file, use_column_width=True)
    model = st.selectbox(label='Your Ford car model', options=keys_model, placeholder="find your model")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    license_plate = col1.text_input(label='License plate')
    produc_year = col2.text_input(label='Production year')
    engine_size = col3.text_input(label='Engine size')
    
    col1, col2, col3, col4 = st.columns(4)
    trans = col1.selectbox(label='Transmission type', options=keys_trans)
    fuel = col2.selectbox(label='Fuel type', options=keys_fuel)
    mile_per_gal = col3.text_input(label='Mile per gallon')
    mile_used = col4.text_input(label='Mile used')
    
    empty_box = st.empty()
    
    submit_btn = st.button(label='See offer price', use_container_width=True)
    if submit_btn:
        if uploaded_file and model and produc_year and produc_year and engine_size and trans and fuel and mile_per_gal and mile_used:
            try:
                format_data = [int(model_mapping[model]), int(produc_year), int(transmission_mapping[trans]), float(mile_used), int(fuel_mapping[fuel]), float(mile_per_gal), float(engine_size)]
                try:
                    ai_offer_price = ai_model.predict([format_data])
                    ai_offer_price = int(ai_offer_price[0])
                    st.session_state.ai_offer_price = ai_offer_price
                    print('\nformat data:', format_data)
                    print('offer price:', ai_offer_price)
                except:
                    print('\nAi error!!')
                    empty_box.error('Ai error', icon="⚠️")
            except:
                empty_box.warning('Please fill only number in Production year, Engine size, Mile per gallon, Mile used', icon="⚠️")
                st.session_state.ai_offer_price = None
        else:
            empty_box.warning('Please fill up this form', icon="⚠️")
            st.session_state.ai_offer_price = None

if st.session_state.ai_offer_price:
    ai_offer_price = st.session_state.ai_offer_price
    with st.container(border=True):
        st.subheader('Confirm price', anchor=False)
        st.info(f'We offer {ai_offer_price:,} dollar')
        
        offer_box = st.empty()
        alert_box = st.empty()
        
        col1, col2= st.columns([1, 3])
        col1_container = col1.empty()
        col2_container = col2.empty()
        
        offer_btn = col1_container.button(label='Offer', use_container_width=True)
        accept_btn = col2_container.button(label='Accept', type='primary', use_container_width=True)

        user_id = st.session_state.user_data[0]
        user_name = st.session_state.user_data[1]
        max_sale_his_primary = con.selectData(table='sales_history', column='max(sale_id)')
        max_sale_his_primary = max_sale_his_primary[0][0]
        
        if max_sale_his_primary == None:
            max_sale_his_primary = 0
        file_name = f'{user_name}_{max_sale_his_primary+1}.png'
        
        if offer_btn:
            st.session_state.offer_btn_state = True
            st.session_state.accept_btn_state = False
        elif accept_btn:
            st.session_state.offer_btn_state = False
            st.session_state.accept_btn_state = True
        
        if st.session_state.accept_btn_state:
            try:
                try:
                    save_image(uploaded_file, file_name)
                    car_id = find_car_id(model, produc_year, engine_size, mile_per_gal, transmission_mapping[trans], fuel_mapping[fuel])
                    format_insert_data = f"'{user_id}', 'user confirm', '{file_name}', '{mile_used}', '{ai_offer_price}', null, null, '{license_plate}', '{car_id}'"
                    con.insertData(table='sales_history', primary_key=max_sale_his_primary+1, values=format_insert_data)
                    alert_box.success('Data saved please wait response from admin', icon='✅')
                    
                    col1_container.empty()
                    col2_container.empty()
                    to_sale_page_button = st.button('Go to sales history', use_container_width=True)
                    if to_sale_page_button:
                        st.session_state.accept_btn_state = False
                        st.session_state.to_sale_page_button_state = True
                except:
                    alert_box.error('Database Error', icon="⚠️")
            except:
                alert_box.warning('Please fill number', icon="⚠️")
            
        
        if st.session_state.offer_btn_state:
            col1_container.empty()
            col2_container.empty()
            confirm_offer_btn_container = st.empty()
            user_offer_price = offer_box.text_input(label='Offer your price', value=ai_offer_price)
            confirm_offer_btn = confirm_offer_btn_container.button(label='Confirm offer', type='primary', use_container_width=True)
            if confirm_offer_btn:
                st.session_state.confirm_offer_btn_state = True
            
            if st.session_state.confirm_offer_btn_state:
                try:
                    user_offer_price = int(user_offer_price)
                    try:
                        save_image(uploaded_file, file_name)
                        car_id = find_car_id(model, produc_year, engine_size, mile_per_gal, transmission_mapping[trans], fuel_mapping[fuel])
                        format_insert_data = f"'{user_id}', 'user offer', '{file_name}', '{mile_used}', '{ai_offer_price}', '{user_offer_price}', null, '{license_plate}', '{car_id}'"
                        con.insertData(table='sales_history', primary_key=max_sale_his_primary+1, values=format_insert_data)
                        alert_box.success('Data saved please wait response from admin', icon='✅')
                        
                        confirm_offer_btn_container.empty()
                        col1_container.empty()
                        col2_container.empty()
                        to_sale_page_button = st.button('Go to sales history', use_container_width=True)
                        print(st.session_state.confirm_offer_btn_state)
                        if to_sale_page_button:
                            print('Good')
                            st.session_state.confirm_offer_btn_state = False
                            st.session_state.to_sale_page_button_state = True
                            st.session_state.offer_btn_state = False
                    except:
                        alert_box.error('Database Error', icon="⚠️")
                except:
                    alert_box.warning('Please fill number', icon="⚠️")
        
        if st.session_state.to_sale_page_button_state:
            st.session_state.ai_offer_price = None
            st.session_state.to_sale_page_button_state = False
            st.switch_page('pages/sale_history.py')



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