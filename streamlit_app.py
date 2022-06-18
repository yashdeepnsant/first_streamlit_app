import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healthy Dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard Boiled free-range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie-adu 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

# adding function
def get_fruityvice_data(this_fruit_choice):
    fruityvise_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    #Convert JSON response to normalized
    fruityvise_normalized = pandas.json_normalize(fruityvise_response.json())
    retrun fruityvise_normalized

#New section to display fruityvise api response
streamlit.header('Fruityvise Fruit Adivce!')
try:
  fruit_choice = streamlit.text_input('What Fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:  
   back_from_function = get_fruityvice_data(fruit_choice)
   streamlit.dataframe(back_from_function)
    
except URLError as e:
  streamlit.error()





streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.header("The Fruit List contains:")
streamlit.dataframe(my_data_rows)

add_fruit = streamlit.text_input('What Fruit you would like to add?','jackfruit')
streamlit.write('Thanks for adding ', add_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
