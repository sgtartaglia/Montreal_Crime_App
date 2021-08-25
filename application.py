import pandas as pd
import streamlit as st
import application_function 
scatter_column, setting_column = st.columns((3,1))
st.set_page_config(page_title='Montreal Crime App')

#app headers
scatter_column.title('Montreal Crime Data')
setting_column.title('Settings')
#app input
selection_button = setting_column.radio(label='look up postal',options=('look up postal code','By crime and year'))


if selection_button == 'look up postal code':
    user_input = setting_column.text_input(label='Enter first 3 characters of postal',key='user_choice')
    if user_input != '':
        scatter_column.dataframe(application_function.post_look_up(user_input[:3]))
        scatter_column.line_chart(data=application_function.YoY(user_input[:3]))
        setting_column.text(application_function.get_neighbourhood(user_input[:3]))
    else:
        scatter_column.header("please enter a postal code")

if selection_button == 'By crime and year':
        drop_down_crime = setting_column.selectbox(label='Choose a Crime',options= application_function.crimes,key='crime')
        drop_down_year = setting_column.selectbox(label='Choose a Year', options=application_function.year,key='year')
        scatter_column.table(application_function.top_4_by_crime(drop_down_crime,drop_down_year))




