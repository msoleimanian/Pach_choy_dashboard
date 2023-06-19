import numpy as np
import streamlit as st
import pandas as pd

from PIL import Image
from matplotlib import pyplot as plt
from pandas import date_range
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode


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

st.markdown(printCostumTitleAndContenth1('Pack Choy Farms ' , '') , unsafe_allow_html=True)


tab1, tab2, tab3, tab4 = st.tabs(["Farm1", "Farm2", "Farm3", "Farm4"])

with tab1:
   st.header("Farm1")
   col1, col2 = st.columns([2,1])

   col1.subheader("Live Image")
   col1.image("Farm1.jpeg", width=600)

   col2.subheader("Details")
   col2.markdown(printCostumTitleAndContenth4('Plot: ' , 'Each row is a Plot. 4 Plot and 10 subplot') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location' , 'UPM') , unsafe_allow_html=True)
   #col2.markdown(printCostumTitleAndContenth4('Location: ' , '') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle:', 'state : Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time Table', 'week : 6/8'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Estimate of the Harvest', '15-20 days'), unsafe_allow_html=True)

   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients' , '') , unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   dataframe1 = dataframe[['pH','SoilMoisture','N','P','EC','Zn','S','K','Mg','Ca']]
   st.write(dataframe1)

   st.markdown(printCostumTitleAndContenth4('Prediction Average of the Nutrients' , 'Nutrient prediction has been done with 98% accuracy in 8th week') , unsafe_allow_html=True)
   dataframe1 = dataframe[['PrepH','PreSoilMoisture','PreN','PreP','PreEC','PreZn','PreS','PreK','PreMg','PreCa']]
   st.write(dataframe1)

with tab2:
   st.header("Farm2")
   col1, col2 = st.columns([2, 1])

   col1.subheader("Live Image")
   col1.image("Farm2.jpeg", width=340)

   col2.subheader("Details")
   col2.markdown(printCostumTitleAndContenth4('Plot: ', 'Each row is a Plot. 4 Plot and 10 subplot'),
                 unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location' , 'UPM') , unsafe_allow_html=True)

   # col2.markdown(printCostumTitleAndContenth4('Location: ' , '') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle:', 'state : Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time Table', 'week : 7/8'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Estimate of the Harvest', '10-6 days'), unsafe_allow_html=True)

   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients', ''), unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   dataframe1 = dataframe[['pH', 'SoilMoisture', 'N', 'P', 'EC', 'Zn', 'S', 'K', 'Mg', 'Ca']]
   st.write(dataframe1)

   st.markdown(printCostumTitleAndContenth4('Prediction Average of the Nutrients',
                                            'Nutrient prediction has been done with 98% accuracy in 8th week '),
               unsafe_allow_html=True)
   dataframe1 = dataframe[
      ['PrepH', 'PreSoilMoisture', 'PreN', 'PreP', 'PreEC', 'PreZn', 'PreS', 'PreK', 'PreMg', 'PreCa']]
   st.write(dataframe1)



with tab3:
   st.header("Farm3")
   col1, col2 = st.columns([2, 1])

   col1.subheader("Live Image")
   col1.image("Farm3.jpeg", width=600)

   col2.subheader("Details")
   col2.markdown(printCostumTitleAndContenth4('Plot: ', 'Each row is a Plot. 4 Plot and 10 subplot'),
                 unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Location' , 'UPM') , unsafe_allow_html=True)
   # col2.markdown(printCostumTitleAndContenth4('Location: ' , '') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle:', 'state : Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time Table', 'week : 5/8'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Estimate of the Harvest', '30-33 days'), unsafe_allow_html=True)

   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients', ''), unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   dataframe1 = dataframe[['pH', 'SoilMoisture', 'N', 'P', 'EC', 'Zn', 'S', 'K', 'Mg', 'Ca']]
   st.write(dataframe1)

   st.markdown(printCostumTitleAndContenth4('Prediction Average of the Nutrients',
                                            'Nutrient prediction has been done with 98% accuracy in 8th week'),
               unsafe_allow_html=True)
   dataframe1 = dataframe[
      ['PrepH', 'PreSoilMoisture', 'PreN', 'PreP', 'PreEC', 'PreZn', 'PreS', 'PreK', 'PreMg', 'PreCa']]
   st.write(dataframe1)




with tab4:
   st.header("Farm4")
   col1, col2 = st.columns([2, 1])

   col1.subheader("Live Image")
   col1.image("Farm4.jpeg", width=600)

   col2.subheader("Details")
   col2.markdown(printCostumTitleAndContenth4('Plot: ', 'Each row is a Plot. 4 Plot and 10 subplot'),
                 unsafe_allow_html=True)
   # col2.markdown(printCostumTitleAndContenth4('Location: ' , '') , unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Growth Cycle:', 'state : Maturation'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Time Table', 'week : 3/8'), unsafe_allow_html=True)
   col2.markdown(printCostumTitleAndContenth4('Estimate of the Harvest', '45-50 days'), unsafe_allow_html=True)

   st.markdown(printCostumTitleAndContenth4('Average of the Nutrients', ''), unsafe_allow_html=True)
   dataframe = data_upload('farm 1.csv')
   print(dataframe)
   dataframe1 = dataframe[['pH', 'SoilMoisture', 'N', 'P', 'EC', 'Zn', 'S', 'K', 'Mg', 'Ca']]
   st.write(dataframe1)

   st.markdown(printCostumTitleAndContenth4('Prediction Average of the Nutrients',
                                            'Nutrient prediction has been done with 98% accuracy in 8th week'),
               unsafe_allow_html=True)
   dataframe1 = dataframe[
      ['PrepH', 'PreSoilMoisture', 'PreN', 'PreP', 'PreEC', 'PreZn', 'PreS', 'PreK', 'PreMg', 'PreCa']]
   st.write(dataframe1)



