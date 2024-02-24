import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed", page_title="sale")

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


with st.container(border=True):
    st.title('Sale-Sale')
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
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    submit_btn = st.button(label='See offer price', use_container_width=True)
    if submit_btn:
        empty_box.success('ไม่บอกกกกก!! hahahaha', icon="✅")

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