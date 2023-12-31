import july as july
import numpy as np
import streamlit as st
import pandas as pd
import plotly.express as px
from statistics import mean

from PIL import Image
from matplotlib import pyplot as plt
from pandas import date_range
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode

st.set_page_config(layout="wide")


def data_upload(path):
   dataframe = pd.read_csv(path)
   return dataframe


def printCostumTitleAndContenth1(title, context):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """
def printCostumTitleAndContenth4(title, context):
    return f"""
        <div class="jumbotron">
        <h6>{title}</h6>
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """


def printCostumTitleAndContentext( context):
   return f"""
        <div class="jumbotron">
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """

st.markdown(printCostumTitleAndContenth1('Pak Choy Farms ' , '') , unsafe_allow_html=True)


tab1, tab2, tab3, tab4 = st.tabs(["Farm1", "Farm2", "Farm3", "Farm4"])

with tab1:
   st.header("Farm1")
   col1, col2 = st.columns([2,1])

   col1.subheader("Live farm video feed")
   col1.image("Farm1.jpeg", width=600)

   col2.subheader("Details")
   col2.markdown(printCostumTitleAndContenth4('Plot and SubPlot' , 'No. Plot : 10 and No. Subplot: 10') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location' , 'UPM') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle', 'Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Weekly schedule', ' growth period: 9 week '), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContentext('elapsed time:  7 week'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time left until harvest', '15-20 days'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Status of the Farm', 'Low Risk'), unsafe_allow_html=True)
   st.markdown(printCostumTitleAndContenth4('Status of the Farm', 'In the chart below, the target and predicted and actual state are displayed for each week, which allows you to see the trend and the final value.'), unsafe_allow_html=True)

   dataframe = data_upload('farm11.csv')
   st.line_chart(dataframe , x='week')

   st.markdown(printCostumTitleAndContenth4('Status of Nutrients', 'The chart below shows the changes of important nutrients during the week and how the predicted nutrient values will be in the weeks.'), unsafe_allow_html=True)

   dataframe = data_upload('Nutrients.csv')
   st.line_chart(dataframe , x='week')
   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients' , 'In the table below, the actual values of nutrients since the time of planting and its average in the last time are displayed, and the values of nutrients predicted in the last week are displayed, which will be at the time of harvest.') , unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   st.write(dataframe)



with tab2:
   st.header("Farm2")
   col1, col2 = st.columns([2, 1])

   col1.subheader("Live farm video feed")
   col1.image("Farm2.jpeg", width=340)

   col2.subheader("Details")
   col2.markdown(printCostumTitleAndContenth4('Plot and SubPlot', 'No. Plot : 10 and No. Subplot: 10'),
                 unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location', 'UPM'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle', 'Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Weekly schedule', ' growth period: 8 week '), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContentext('elapsed time:  6 week'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time left until harvest', '17-22 days'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Status of the Farm', 'Low Risk'), unsafe_allow_html=True)
   st.markdown(printCostumTitleAndContenth4('Status of the Farm', 'In the chart below, the target and predicted and actual state are displayed for each week, which allows you to see the trend and the final value.'), unsafe_allow_html=True)

   dataframe = data_upload('farm11.csv')
   st.line_chart(dataframe , x='week')

   st.markdown(printCostumTitleAndContenth4('Status of Nutrients', 'The chart below shows the changes of important nutrients during the week and how the predicted nutrient values will be in the weeks.'), unsafe_allow_html=True)

   dataframe = data_upload('Nutrients.csv')
   st.line_chart(dataframe , x='week')
   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients', 'In the table below, the actual values of nutrients since the time of planting and its average in the last time are displayed, and the values of nutrients predicted in the last week are displayed, which will be at the time of harvest.'), unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   st.write(dataframe)



with tab3:
   st.header("Farm3")
   col1, col2 = st.columns([2, 1])

   col1.subheader("Live farm video feed")
   col1.image("Farm3.jpeg", width=600)

   col2.subheader("Details")

   col2.markdown(printCostumTitleAndContenth4('Plot and SubPlot', 'No. Plot : 10 and No. Subplot: 10'),
                 unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location', 'UPM'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle', 'Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Weekly schedule', ' growth period: 10 week '), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContentext('elapsed time:  7 week'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time left until harvest', '20-25 days'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Status of the Farm', 'Low Risk'), unsafe_allow_html=True)
   st.markdown(printCostumTitleAndContenth4('Status of the Farm', 'In the chart below, the target and predicted and actual state are displayed for each week, which allows you to see the trend and the final value.'), unsafe_allow_html=True)

   dataframe = data_upload('farm11.csv')
   st.line_chart(dataframe , x='week')

   st.markdown(printCostumTitleAndContenth4('Status of Nutrients', 'The chart below shows the changes of important nutrients during the week and how the predicted nutrient values will be in the weeks.'), unsafe_allow_html=True)

   dataframe = data_upload('Nutrients.csv')
   st.line_chart(dataframe , x='week')
   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients', 'In the table below, the actual values of nutrients since the time of planting and its average in the last time are displayed, and the values of nutrients predicted in the last week are displayed, which will be at the time of harvest.'), unsafe_allow_html=True)

   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   st.write(dataframe)


with tab4:
   st.header("Farm4")
   col1, col2 = st.columns([2, 1])

   col1.subheader("Live farm video feed")
   col1.image("Farm4.jpeg", width=600)

   col2.subheader("Details")

   col2.markdown(printCostumTitleAndContenth4('Plot and SubPlot', 'No. Plot : 10 and No. Subplot: 10'),
                 unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location', 'UPM'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle', 'Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Weekly schedule', ' growth period: 8 week '), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContentext('elapsed time:  3 week'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time left until harvest', '45-50 days'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Status of the Farm', 'Low Risk'), unsafe_allow_html=True)

   st.markdown(printCostumTitleAndContenth4('Status of the Farm', 'In the chart below, the target and predicted and actual state are displayed for each week, which allows you to see the trend and the final value.'), unsafe_allow_html=True)
   dataframe = data_upload('farm11.csv')
   st.line_chart(dataframe , x='week')
   st.markdown(printCostumTitleAndContenth4('Status of Nutrients', 'The chart below shows the changes of important nutrients during the week and how the predicted nutrient values will be in the weeks.'), unsafe_allow_html=True)

   dataframe = data_upload('Nutrients.csv')
   st.line_chart(dataframe , x='week')


   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients', 'In the table below, the actual values of nutrients since the time of planting and its average in the last time are displayed, and the values of nutrients predicted in the last week are displayed, which will be at the time of harvest.'), unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   st.write(dataframe)



