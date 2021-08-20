import pandas as pd
import streamlit as st
import application_function 
scatter_column, setting_column = st.columns((3,1))

scatter_column.title('Montreal Crime Data')
setting_column.title('Settings')


user_input = setting_column.text_input('Enter first 3 characters of postal')
if user_input != '':
    scatter_column.table(application_function.post_look_up(user_input[:3]))
    scatter_column.line_chart(data=application_function.YoY(user_input[:3]))
    setting_column.text(application_function.get_neighbourhood(user_input[:3]))
else:
    scatter_column.header("please enter a postal code")




