import pandas as pd
import re
import requests
import streamlit as st
import application_function 
import matplotlib.pyplot as plt
st.set_page_config(layout='wide')
scatter_column, setting_column = st.columns((4,1))

user_input = setting_column.text_input("Enter the first 3 digits of your Postal Code(eg. H3G", 'Postal Code')
scatter_column.table(application_function.post_look_up(user_input))
scatter_column.line_chart(data=application_function.YoY(user_input))


