import streamlit as st
import condb as con
import base64

st.set_page_config(initial_sidebar_state="collapsed", page_title="sale history", layout="wide")

def open_image(path: str):
    with open(path, "rb") as p:
        file = p.read()
        return f"data:image/png;base64,{base64.b64encode(file).decode()}"

path_pic = 'D:/KKU_World/1_2/DBMS/termProject/python/Ui/public/picture/'
# path_pic = '../public/picture/'
table_data = []

car_data = con.selectData(table='admin_sale_history_data')

for i in car_data:
    table_data.append({'pic': open_image(path_pic+i[0]), 
                        'user': (str(i[1]) + ' '+ i[2]), 
                        'car model': i[3], 
                        'production year': i[4], 
                        'mile used': i[5], 
                        'license plate': i[6], 
                        'phone number': i[7], 
                        'predict price': i[8], 
                        'user offer price': i[9],
                        'admin offer price': i[10],
                        'status': i[11]
                        })

# print(table_data[0]['pic'])

with st.container(border=True):
    st.title('Sale history for Admin', anchor=False)
    edited_df = st.data_editor(table_data, width=1500, height=400, column_config={
                                                            "pic": st.column_config.ImageColumn(
                                                            "pic", help="form user uplaod"
                                                        )})
    # edited_df = st.data_editor(df, width=1189)