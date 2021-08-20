import pandas as pd
import re
import plotly.express as px
import requests
import streamlit as st
import application_function 
st.set_page_config(layout='wide')
scatter_column, setting_column = st.columns((4,1))

user_input = setting_column.text_input("Enter the first 3 digits of your Postal Code(eg. H3G", 'Postal Code')
scatter_column.table(application_function.post_look_up(user_input))
scatter_column.plotly_chart(px.bar(data_frame=application_function.YoY(user_input)))


