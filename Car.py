import pickle
import streamlit as st

model = pickle.load(open('Car.sav', 'rb'))

st.title('Estimasi Car Price')

car_ID = st.number_input('Masukan ID Mobil', step=0,
                         max_value=100, min_value=1)
symboling = st.number_input(
    'Masukan Speed Mobil')
wheelbase = st.number_input(
    'Masukan Generasi Mobil', step=0, max_value=100, min_value=1)
carlength = st.number_input(
    'Masukan Requests Plat Nomer', step=0, max_value=4, min_value=0)
carwidth = st.number_input('Masukan Size', step=0, max_value=100, min_value=1)
carheight = st.number_input('Masukan Nomer Mesin',
                            step=0, max_value=100, min_value=1)
curbweight = st.number_input('KM Mobil', step=0, max_value=100, min_value=1)
enginesize = st.number_input(
    'Tahun Mobil', step=0, max_value=100, min_value=1)


predict = ''

if st.button(' Estimasi Car PRICE'):
    predict = model.predict(
        [[car_ID, symboling, wheelbase, carlength,
            carwidth, carheight, curbweight, enginesize]]
    )
    st.write('Estimasi Car PRICE: ', predict)
    st.write('Estimasi Car PRICE: ', predict*2000)
