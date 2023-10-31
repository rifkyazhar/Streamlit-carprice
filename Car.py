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
carheight = st.number_input('Masukan Tin32ggi Mobil',
                            step=0, max_value=100, min_value=1)
curbweight = st.number_input('Masukan ketahan mu3223atan', step=0, max_value=100, min_value=1)
enginesize = st.number_input(
    'Masukan ukuran21 mesin', step=0, max_value=100, min_value=1)
boreratio = st.number_input('Masukan r33asio goresan', step=0, max_value=100, min_value=1)
stroke = st.number_input('Masukan aksel33arasi', step=0, max_value=100, min_value=1)
compressionratio = st.number_input('Masukan rasio 1133kompresi', step=0, max_value=100, min_value=1)
horsepower = st.number_input('Masukan horsepow11er', step=0, max_value=1100, min_value=1)
peakrpm = st.number_input('Masukan rasio gore33san', step=0, max_value=1020, min_value=1)
citympg = st.number_input('Masukan rasio gore22san', step=0, max_value=1010, min_value=1)

predict = ''

if st.button(' Estimasi Car PRICE'):
    predict = model.predict(
        [[car_ID, symboling, wheelbase, carlength,
            carwidth, carheight, curbweight, enginesize, boreratio, stroke, compressionratio,
           horsepower, peakrpm, citympg  ]]
    )
    st.write('Estimasi Car PRICE: ', predict)
    st.write('Estimasi Car PRICE: ', predict*2000)
