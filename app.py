import streamlit as st
import pandas as pd



st.title("L'app sterile Il Meteo")
st.header(f'Il tuo meteo sempre a portata di mano.', divider = True)
st.subheader('Inserisci di seguito il nome della città:')
city_name = st.text_input(' ')
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2020/04/05/17/42/sky-5007053_1280.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

import requests
API_key='4b9242f32a9f38ddfc7dfbe3c0a4c501'
url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'


result=requests.get(url)
json=result.json()

if city_name:
    y = json.get("temp")
    x=json['main']['temp']
    temperatura= round((x-273.15),1)
    st.write(f'Temperatura percepita:\n\n {temperatura}°')
    st.divider()
    x=json['main']['temp_min']
    temperatura_minima= round((x-273.15),1)
    st.write(f'Temperatura minima:\n\n {temperatura_minima}°')
    x=json['main']['temp_max']
    st.divider()
    temperatura_massima= round((x-273.15),1)
    if temperatura_massima > 30:
        st.write(f'Temperatura massima:\n\n :red[{temperatura_massima}°]')
    else:
        st.write(f'Temperatura massima:\n\n :green[{temperatura_massima}°]')
    st.divider()
    x=json['main']['pressure']
    pressione= x
    st.write(f'Pressione:\n\n :blue[{pressione}hPa]')
    st.divider()
    x=json['main']['humidity']
    umidità= x
    st.write(f'Percentuale di umidità:\n\n {umidità}%')
    st.divider()
    x=json['wind']['speed']
    vento=x
    st.write(f'La velocità del vento è di:\n\n {vento}km/h')
else:
    st.write(f':red[Questo campo non può essere vuoto]')





