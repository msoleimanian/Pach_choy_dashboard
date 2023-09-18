import streamlit as st
from PIL import Image

import warnings


warnings.filterwarnings("ignore")

st.set_page_config(layout="wide")



#functions
def printCostumTitleAndContentTitle(title):
    return f"""
        <div class="jumbotron">
        <h1>{title}</h1>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth4(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h5>{context}</h5>
        </div>
        <div class="container">
        </div>
        """
def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <h6>{context}</h6>
        </div>
        <div class="container">
        </div>
        """
st.markdown(printCostumTitleAndContentTitle('Pak Choy') , unsafe_allow_html=True)


col5 , col6 = st.columns(2)

col5.image('dash3.png' , width= 350)
col6.markdown(printCostumTitleAndContenth3('Dashboard' , """Welcome to the Pak Choy Dashboard, your comprehensive tool for monitoring the growth and predicting the state of your pak choy plants. This dashboard is designed to provide you with valuable insights and actionable information to optimize the growth and yield of your pak choy crop."""),unsafe_allow_html=True)
col6.markdown(printCostumTitleAndContenth3('' , """With the help of this dashboard, you will have access to real-time reports that track the vital parameters necessary for successful pak choy cultivation. By monitoring these factors, you can make informed decisions about irrigation, nutrient management, and environmental control to create an optimal growing environment for your pak choy plants.."""),unsafe_allow_html=True)

col7 , col8 = st.columns(2)

col7.markdown(printCostumTitleAndContenth3('Analyze','In addition to real-time reports, this dashboard incorporates predictive analytics to estimate the growth state of your pak choy crop. Leveraging historical data and machine learning algorithms, the dashboard can forecast growth milestones, such as seedling emergence, vegetative growth, and expected harvest dates. This predictive capability empowers you to plan and manage your crop effectively, ensuring maximum yield and quality.'), unsafe_allow_html=True)
col7.markdown(printCostumTitleAndContenth3('','Furthermore, the dashboard provides personalized recommendations based on the specific growth stage of your pak choy plants. These recommendations may include nutrient adjustments, pest and disease management strategies, and pruning techniques to optimize plant health and productivity. By following these tailored suggestions, you can proactively address any challenges that may arise during the growth cycle and achieve the best possible outcomes.'), unsafe_allow_html=True)
col8.image('dash5.jpg' , width= 350)
