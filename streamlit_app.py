import streamlit
import pandas 

streamlit.title('Nar is learning Streamlit')
streamlit.header ('Nar is enjoying Streamlit') 

#streamlit.text('hi, this is Nar , learning snowflake')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:",  list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)

