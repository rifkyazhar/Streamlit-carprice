import pickle
import streamlit as st

model = pickle.load(open('Car.sav', 'rb'))

st.title('Estimasi Car Price')

car_ID = st.number_input('Masukan ID Mobil', step=0,
                         max_value=100, min_value=1)
symboling = st.number_input(
    'Masukan simbol')
wheelbase = st.number_input(
    'Masukan jarak sumbu mobil', step=0, max_value=100, min_value=1)
carlength = st.number_input(
    'Masukan panjang mobil', step=0, max_value=4, min_value=0)
carwidth = st.number_input('Masukan Tahun', step=0, max_value=100, min_value=1)
carheight = st.number_input('Masukan Tinggi Mobil',
                            step=0, max_value=100, min_value=1)
curbweight = st.number_input('Masukan ketahan muatan', step=0, max_value=100, min_value=1)
enginesize = st.number_input(
    'Masukan ukuran mesin', step=0, max_value=100, min_value=1)
boreratio = st.number_input('Masukan rasio goresan', step=0, max_value=100, min_value=1)
stroke = st.number_input('Masukan akselarasi', step=0, max_value=100, min_value=1)
compressionratio = st.number_input('Masukan rasio kompresi', step=0, max_value=100, min_value=1)
horsepower = st.number_input('Masukan horsepower', step=0, max_value=100, min_value=1)
peakrpm = st.number_input('Masukan rasio goresan', step=0, max_value=100, min_value=1)
citympg = st.number_input('Masukan rasio goresan', step=0, max_value=100, min_value=1)

predict = ''

if st.button(' Estimasi Car PRICE'):
    predict = model.predict(
        [[car_ID, symboling, wheelbase, carlength,
            carwidth, carheight, curbweight, enginesize]]
    )
    st.write('Estimasi Car PRICE: ', predict)
    st.write('Estimasi Car PRICE: ', predict*2000)
