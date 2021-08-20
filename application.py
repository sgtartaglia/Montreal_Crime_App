import pandas as pd
import streamlit as st
import application_function 
scatter_column, setting_column = st.columns((4,1))

user_input = setting_column.text_input("Enter the first 3 digits of your Postal Code(eg. H3G)")
scatter_column.table(application_function.post_look_up(user_input))
scatter_column.line_chart(data=application_function.YoY(user_input))


