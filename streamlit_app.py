import streamlit
import pandas 


streamlit.title('Nar is learning Streamlit')
streamlit.header ('Nar is enjoying Streamlit') 

#streamlit.text('hi, this is Nar , learning snowflake')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(my_fruit_list)

fruits_selected = streamlit.multiselect("Pick some fruits:",  list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


import snowflake.connector
streamlit.text('new test')



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

my_cur = my_cnx.cursor()

my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

my_data_row = my_cur.fetchone() 

streamlit.text("Hello from Snowflake:")

streamlit.text(my_data_row)

my_cur.execute("select *from garden_plants.veggies.lu_soil_type")
my_data_rows = my_cur.fetchall() 
streamlit.dataframe(my_data_rows)









