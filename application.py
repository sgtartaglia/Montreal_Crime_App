import pandas as pd
import streamlit as st
import application_function 
scatter_column, setting_column = st.columns((4,1))

user_input = setting_column.text_input('Enter first 3 characters of postal')
if user_input is not None:
    scatter_column.table(application_function.post_look_up(user_input))
    scatter_column.line_chart(data=application_function.YoY(user_input))
else:
    scatter_column.header("please enter a postal code")



