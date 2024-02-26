from datetime import datetime
import streamlit as st
import pickle
import time

st.set_page_config(initial_sidebar_state="collapsed", page_title="sale")

# try:
#     print(st.session_state)
# except:
#     print(st.session_state) 


# INITIAL STATE
if 'offer_price' not in st.session_state or 'offer_btn_state' not in st.session_state:
    st.session_state.offer_price = None
    st.session_state.offer_btn_state = False


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

if 'user_data' in st.session_state:
    user_data = st.session_state.user_data
else:
    print(formatted_time,'user data not found! ', st.session_state)
    st.error('user data not found! redirect to login', icon='❌')
    time.sleep(3)
    st.switch_page("main.py")

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
    # st.markdown("<div></div>", unsafe_allow_html=True)
    submit_btn = st.button(label='See offer price', use_container_width=True)
    if submit_btn:
        if uploaded_file and model and produc_year and produc_year and engine_size and trans and fuel and mile_per_gal and mile_used:
            try:
                format_data = [int(model_mapping[model]), int(produc_year), int(transmission_mapping[trans]), float(mile_used), int(fuel_mapping[fuel]), float(mile_per_gal), float(engine_size)]
                try:
                    offer_price = ai_model.predict([format_data])
                    offer_price = int(offer_price[0])
                    st.session_state.offer_price = offer_price
                    print('\nformat data:', format_data)
                    print('offer price:', offer_price)
                except:
                    print('\nAi error!!')
                    empty_box.error('Ai error', icon="⚠️")
            except:
                empty_box.warning('Please fill only number in Production year, Engine size, Mile per gallon, Mile used', icon="⚠️")
                st.session_state.offer_price = None
        else:
            empty_box.warning('Please fill up this form', icon="⚠️")
            st.session_state.offer_price = None

if st.session_state.offer_price:
    offer_price = st.session_state.offer_price
    with st.container(border=True):
        st.subheader('Confirm price', anchor=False)
        st.info(f'we offer {offer_price:,} dollar')
        
        offer_box = st.empty()
        alert_box = st.empty()
        
        col1, col2= st.columns([1, 3])
        col1_container = col1.empty()
        col2_container = col2.empty()
        offer_btn = col1_container.button(label='Offer', use_container_width=True)
        accept_btn = col2_container.button(label='Accept', type='primary', use_container_width=True)
        
        if offer_btn:
            col1_container.empty()
            col2_container.empty()
            user_offer = offer_box.text_input(label='Offer your price', value=offer_price)
            confirm_offer_btn = st.button(label='Confirm offer', type='primary', use_container_width=True)
            
            if confirm_offer_btn:
                try:
                    user_offer = int(user_offer)
                    time.sleep(2)
                    print("here")
                except:
                    alert_box.warning('Please fill number', icon="⚠️")

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


