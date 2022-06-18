import streamlit

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie-adu 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New section to display fruityvise api response
streamlit.header('Fruityvise Fruit Adivce!')
import requests
fruityvise_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvise_response.json())

#Convert JSON response to normalized
fruityvise_normalized = pandas.normalize(fruityvise_response.json())
streamlit.dataframe(fruityvise_normalized)
