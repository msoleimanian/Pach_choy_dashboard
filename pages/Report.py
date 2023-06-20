import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, JsCode, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import plotly.express as px
from statistics import mean
import matplotlib.pyplot as plt


# Functions

def data_upload(path):
    dataframe = pd.read_csv(path)
    return dataframe




def printCostumTitleAndContenth3(title, context):
    return f"""
        <div class="jumbotron">
        <h3>{title}</h3>
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """

def printCostumTitleAndContenth4(title, context):
    return f"""
        <div class="jumbotron">
        <h4>{title}</h4>
        <p>{context}</p>
        </div>
        <div class="container">
        </div>
        """


DataFrameAction = 0



#Main Core

options = st.sidebar.radio('Sections',
                           options=('Summary of all plots', 'Action Plan', 'Result of the ActionPlan'))

# base on the Plot id

if options == 'Summary of all plots':
    st.header("Summary of Pak Choy greenhouse growth")

    st.markdown(printCostumTitleAndContenth3('Status of all plots',
                                 'In this section, the growth status of all plots is predicted. The criterion is to compare the predicted weight of each plot and compare it with the target state of each plot. According to this metric, the plots are divided into three general categories that indicate the state of the plot. By selecting each plot, it first displays the graphs related to growth.' ) , unsafe_allow_html=True)



    #st.set_page_config(layout="wide")
    dataframe = data_upload('data_Growth_Plot_Weight.csv')
    print(data_upload('data_Growth_Plot_Weight.csv'))
    gd = GridOptionsBuilder.from_dataframe(dataframe)
    gd.configure_pagination(enabled=True)
    gd.configure_default_column(editable=False , groupable=True)
    gd.configure_selection(use_checkbox=True)
    gridoption = gd.build()
    grid_table = AgGrid(dataframe , gridOptions=gridoption , update_mode=GridUpdateMode.SELECTION_CHANGED,
           allow_unsafe_jscode=True )
    sel_row = grid_table["selected_rows"]
    if sel_row :
        plotid = sel_row[0]["Plot"]
        # create graph for each plot
        dataframe1 = data_upload('data_gorwth_allplots.csv')
        dataframe2 = dataframe1.query(f'plot == {plotid}')
        print("DataFrame 1 : ")
        print(dataframe1)

        st.markdown(printCostumTitleAndContenth4('Bar Chat' , f'The graph below shows the amount of growth metrics of the plot {plotid} from week 5 to week 8 that is predicted, which is displayed separately by week.') , unsafe_allow_html=True)

        fig = px.bar(dataframe2, x='week ', y=['PreplantHeight','Preweight','PreLongestLeaf','PreLeafCount','PreLeafArea','TarplantHeight','TarPreweight','TarPreLongestLeaf','TarPreLeafCount','TarPreLeafArea'], barmode='group', height=400)
        # st.dataframe(df) # if need to display dataframe
        st.plotly_chart(fig)


        # base on the subplot id

        st.markdown(printCostumTitleAndContenth4(f'Growth status of subplots of plot {plotid} ' ,
                                                 f'In the table below, all the subplots related to the selected plot are displayed and the growth status of each of them is displayed.') , unsafe_allow_html=True)


        subp = 1
        subplots = []
        preweights = []
        target = []
        risk = []
        while subp < 11 :
            data1 = dataframe1.query(f'plot == {plotid} and subplot == {subp}')
            subplots.append(subp)
            preweight = data1['Preweight'].iloc[-1]
            tarpreweight  = data1['TarPreweight'].iloc[-1]
            preweights.append(preweight)
            target.append(tarpreweight)
            result = tarpreweight - preweight
            print(result)
            if tarpreweight - preweight < 200:
                risk.append('NO RISK')
            elif tarpreweight - preweight < 230:
                risk.append('LOW RISK')
            else:
                risk.append('HIGH RISK')
            subp = subp + 1

        data = {'subplot': subplots,
                'preweights': preweights,
                'target': target,
                'RISK' : risk}
        df = pd.DataFrame(data)
        print(df)

        gd = GridOptionsBuilder.from_dataframe(df)
        gd.configure_pagination(enabled=True)
        gd.configure_default_column(editable=False , groupable=True)
        gd.configure_selection(use_checkbox=True)
        gridoption = gd.build()
        grid_table = AgGrid(df , gridOptions=gridoption , update_mode=GridUpdateMode.SELECTION_CHANGED,
               allow_unsafe_jscode=True )
        sel_row2 = grid_table["selected_rows"]

        if sel_row2 :
            subplotid = sel_row2[0]["subplot"]
            st.markdown(printCostumTitleAndContenth4(f'bar chart' ,
                                                     f'In this graph, all the metrics considered for growth are displayed for the selected subplot') , unsafe_allow_html=True)

            data1 = dataframe2.query(f' subplot == {subplotid}')
            print(data1)
            fig = px.bar(data1, x='week ', y=['PreplantHeight','Preweight','PreLongestLeaf','PreLeafCount','PreLeafArea','TarplantHeight','TarPreweight','TarPreLongestLeaf','TarPreLeafCount','TarPreLeafArea'], barmode='group', height=400)
            # st.dataframe(df) # if need to display dataframe
            st.plotly_chart(fig)

if options == 'Action Plan' :
    st.header('Action Plan for Farmer')
    st.markdown(printCostumTitleAndContenth4('HIGH RISK PLOTS' , 'In this section, plots are displayed that are predicted to have the highest risk in growth and will have problems in the future.') , unsafe_allow_html=True )

    dataframe = data_upload('data_Growth_Plot_Weight.csv')
    dataframe = dataframe[['Plot' , 'RISKLEVEL']].query("""RISKLEVEL == 'High RISK'""")
    print(data_upload('data_Growth_Plot_Weight.csv'))
    gd = GridOptionsBuilder.from_dataframe(dataframe)
    gd.configure_pagination(enabled=True )
    gd.configure_default_column(editable=False, groupable=True )
    gd.configure_selection(use_checkbox=True ,)
    gridoption = gd.build()
    grid_table = AgGrid(dataframe, gridOptions=gridoption, update_mode=GridUpdateMode.SELECTION_CHANGED,
                        allow_unsafe_jscode=True )
    sel_row = grid_table["selected_rows"]
    if sel_row:
        plotid = sel_row[0]["Plot"]
        # create graph for each plot
        dataframe1 = data_upload('data_gorwth_allplots.csv')
        dataframe2 = dataframe1.query(f'plot == {plotid}')
        print("DataFrame 1 : ")
        print(dataframe1)
        dataframe3 = data_upload('data_pack.csv')
        dataframe3 = dataframe3.query(f'Plot == {plotid}')
        print(dataframe3)

        st.markdown(printCostumTitleAndContenth3(f'Compare nutrient status Plot{plotid}', ''),unsafe_allow_html=True)
        st.markdown(printCostumTitleAndContenth4(f'present comparison', 'In this section, the nutrients that are different from the ideal state in the plant are displayed in a linear diagram. This compares plant nutrients from the time of planting until now'),unsafe_allow_html=True)

        dataframe4 = dataframe3[['week', 'pH','SoilMoisture','N','P','EC','Zn','S','K','Mg','Ca','Temperature','Humidity' ]]
        dataframe4 = dataframe4.query(f'week < 5')

        dataframe5 = data_upload('Best Nutrients.csv')
        w = 0
        metrics = ['pH','SoilMoisture','N','P','EC','Zn','S','K','Mg','Ca','Temperature','Humidity' ]

        pH = []
        SoilMoisture = []
        N = []
        P = []
        EC = []
        Zn = []
        S = []
        K = []
        Mg = []
        Ca = []
        Temperature = []
        Humidity = []
        weeks = []
        BestpH = []
        BestSoilMoisture = []
        BestN = []
        BestP = []
        BestEC = []
        BestZn = []
        BestS = []
        BestK = []
        BestMg = []
        BestCa = []
        BestTemperature = []
        BestHumidity = []

        while w < 5:
            weeks.append(w)
            dataframe5 = dataframe4.query(f'week == {w}')
            pH.append(dataframe5['pH'].mean())
            SoilMoisture.append(dataframe5['SoilMoisture'].mean())
            N.append(dataframe5['N'].mean())
            P.append(dataframe5['P'].mean())
            EC.append(dataframe5['EC'].mean())
            Zn.append(dataframe5['Zn'].mean())
            S.append(dataframe5['S'].mean())
            K.append(dataframe5['K'].mean())
            Mg.append(dataframe5['Mg'].mean())
            Ca.append(dataframe5['Ca'].mean())
            Temperature.append(dataframe5['Temperature'].mean())
            Humidity.append(dataframe5['Humidity'].mean())

            BestpH.append(7.5)
            BestSoilMoisture.append(80)
            BestN.append(115)
            BestP.append(132)
            BestEC.append(4.6)
            BestZn.append(233)
            BestS.append(212)
            BestK.append(321)
            BestMg.append(312)
            BestCa.append(2)
            BestTemperature.append(25)
            BestHumidity.append(100)

            w = w + 1

        Data1 = {'week' : weeks , 'pH' : pH ,
        'SoilMoisture' : SoilMoisture ,
        'N' : N ,
        'P' : P ,
        'EC' : EC ,
        'Zn' : Zn ,
        'S' : S ,
        'K' : K ,
        'Mg' : Mg ,
        'Ca' : Ca ,
        'Temperature' : Temperature ,
        'Humidity' : Humidity ,
        'weeks' : weeks ,
        'BestpH' : BestpH ,
        'BestSoilMoisture' : BestSoilMoisture ,
        'BestN' : BestN ,
        'BestP' : BestP ,
        'BestEC' : BestEC ,
        'BestZn' : BestZn ,
        'BestS' : BestS ,
        'BestK' : BestK ,
        'BestMg' : BestMg ,
        'BestCa' : BestCa ,
        'BestTemperature' : BestTemperature ,
        'BestHumidity' : BestHumidity  }

        dataframe6 = pd.DataFrame(Data1)
        print(dataframe6)
        fig = px.bar(dataframe6, x='week',
                         y=['SoilMoisture',
                                            'N',
                                            'P',
                                            'EC',
                                            'Zn',
                                            'S',
                                            'K',
                                            'Mg',
                                            'Ca',
                                            'Temperature',
                                            'Humidity',
                                            'weeks',
                                            'BestpH',
                                            'BestSoilMoisture',
                                            'BestN',
                                            'BestP',
                                            'BestEC',
                                            'BestZn',
                                            'BestS',
                                            'BestK',
                                            'BestMg',
                                            'BestCa',
                                            'BestTemperature',
                                            'BestHumidity'],
                                            barmode='group', height=400 , width= 800)
        # st.dataframe(df) # if need to display dataframe
        st.plotly_chart(fig)


        st.markdown(printCostumTitleAndContenth4(f'Future comparison', 'In this chart, all nutrients are predicted and compared to the ideal state'),unsafe_allow_html=True)
        dataframe4 = dataframe3[['week','PrepH','PreSoilMoisture','PreN','PreP','PreEC','PreZn','PreS','PreK','PreMg','PreCa','PreTemperature','PreHumidity','PreLight']]
        dataframe4 = dataframe4.query(f'week > 4')
        dataframe5 = data_upload('Best Nutrients.csv')
        w = 5
        metrics = ['PrepH','PreSoilMoisture','PreN','PreP','PreEC','PreZn','PreS','PreK','PreMg','PreCa','PreTemperature','PreHumidity','PreLight']
        pH = []
        SoilMoisture = []
        N = []
        P = []
        EC = []
        Zn = []
        S = []
        K = []
        Mg = []
        Ca = []

        ActionpH = []
        ActionSoilMoisture = []
        ActionN = []
        ActionP = []
        ActionEC = []
        ActionZn = []
        ActionS = []
        ActionK = []
        ActionMg = []
        ActionCa = []

        Temperature = []
        Humidity = []
        weeks = []
        BestpH = []
        BestSoilMoisture = []
        BestN = []
        BestP = []
        BestEC = []
        BestZn = []
        BestS = []
        BestK = []
        BestMg = []
        BestCa = []
        BestTemperature = []
        BestHumidity = []

        while w < 9:
            weeks.append(w)
            dataframe5 = dataframe4.query(f'week == {w}')
            pH.append(dataframe5['PrepH'].mean())
            SoilMoisture.append(dataframe5['PreSoilMoisture'].mean())
            N.append(dataframe5['PreN'].mean())
            P.append(dataframe5['PreP'].mean())
            EC.append(dataframe5['PreEC'].mean())
            Zn.append(dataframe5['PreZn'].mean())
            S.append(dataframe5['PreS'].mean())
            K.append(dataframe5['PreK'].mean())
            Mg.append(dataframe5['PreMg'].mean())
            Ca.append(dataframe5['PreCa'].mean())
            Temperature.append(dataframe5['PreTemperature'].mean())
            Humidity.append(dataframe5['PreHumidity'].mean())

            BestpH.append(7.5)
            BestSoilMoisture.append(80)
            BestN.append(115)
            BestP.append(132)
            BestEC.append(4.6)
            BestZn.append(233)
            BestS.append(212)
            BestK.append(321)
            BestMg.append(312)
            BestCa.append(2)
            BestTemperature.append(25)
            BestHumidity.append(100)
            w = w + 1

        Data1 = {'week': weeks, 'pH': pH,
                 'SoilMoisture': SoilMoisture,
                 'N': N,
                 'P': P,
                 'EC': EC,
                 'Zn': Zn,
                 'S': S,
                 'K': K,
                 'Mg': Mg,
                 'Ca': Ca,
                 'Temperature': Temperature,
                 'Humidity': Humidity,
                 'weeks': weeks,
                 'BestpH': BestpH,
                 'BestSoilMoisture': BestSoilMoisture,
                 'BestN': BestN,
                 'BestP': BestP,
                 'BestEC': BestEC,
                 'BestZn': BestZn,
                 'BestS': BestS,
                 'BestK': BestK,
                 'BestMg': BestMg,
                 'BestCa': BestCa,
                 'BestTemperature': BestTemperature,
                 'BestHumidity': BestHumidity}

        ActionpH.append(((7/10)-(mean(pH)/mean(BestpH)))*100)
        ActionSoilMoisture.append(((7/10)-(mean(SoilMoisture)/mean(BestSoilMoisture)))*100)
        ActionN.append(((7/10)-(mean(N)/mean(BestN)))*100)
        ActionP.append(((7/10)-(mean(P)/mean(BestP)))*100)
        ActionEC.append(((7/10)-(mean(EC)/mean(BestEC)))*100)
        ActionZn.append(((7/10)-(mean(Zn)/mean(BestZn)))*100)
        ActionS.append(((7/10)-(mean(S)/mean(BestS)))*100)
        ActionK.append(((7/10)-(mean(K)/mean(BestK)))*100)
        ActionMg.append(((7/10)-(mean(Mg)/mean(BestMg)))*100)
        ActionCa.append(((7/10)-(mean(Ca)/mean(BestCa)))*100)

        dataframe6 = pd.DataFrame(Data1)
        print(dataframe6)
        fig = px.bar(dataframe6, x='week',
                     y=['SoilMoisture',
                        'N',
                        'P',
                        'EC',
                        'Zn',
                        'S',
                        'K',
                        'Mg',
                        'Ca',
                        'Temperature',
                        'Humidity',
                        'weeks',
                        'BestpH',
                        'BestSoilMoisture',
                        'BestN',
                        'BestP',
                        'BestEC',
                        'BestZn',
                        'BestS',
                        'BestK',
                        'BestMg',
                        'BestCa',
                        'BestTemperature',
                        'BestHumidity'],
                     barmode='group', height=400, width=800)
        # st.dataframe(df) # if need to display dataframe
        st.plotly_chart(fig)
        Data2 = {'ActionpH':ActionpH ,
        'ActionSoilMoisture':ActionSoilMoisture ,
        'ActionN':ActionN ,
        'ActionP':ActionP ,
        'ActionEC':ActionEC ,
        'ActionZn':ActionZn ,
        'ActionS':ActionS ,
        'ActionK':ActionK ,
        'ActionMg':ActionMg ,
        'ActionCa':ActionCa }
        dataframe7 = pd.DataFrame(Data2)
        st.markdown(printCostumTitleAndContenth4(f'AcionPlan', 'The table below shows the amount of each nutrient that should be changed. The values are in percentages, and the number that is positive should be added as much as it is in the table, and the number that is negative should be reduced by the same amount.'),unsafe_allow_html=True)
        st.write(dataframe7)
        DataFrameAction = dataframe7

if options == 'Result of the ActionPlan':
    st.markdown(printCostumTitleAndContenth3('HIGH RISK PLOTS AND RESULT OF THE ACTION PLAN FOR PLOT',
                                             'In this section, the plots that had high risk and were given suggestions to the farmer can be seen separately. The graphs show how the crop will be in the last week if the farmer follows the suggestions.'),
                unsafe_allow_html=True)

    dataframe = data_upload('data_Growth_Plot_Weight.csv')
    dataframe = dataframe[['Plot', 'RISKLEVEL']].query("""RISKLEVEL == 'High RISK'""")

    dataframe3 = data_upload('data_pack.csv')

#    dataframe3 = dataframe3.query(f'Plot == {plotid}')
    plot = 0
    dict1 = dataframe.to_dict()
    print(dict1)
    print(dict1['Plot'].keys())
    dataframe3 = data_upload('data_pack.csv')

    for key  in dict1['Plot']:
        print(dict1['Plot'][key])
        dataframe3.query(f"""Plot == {dict1['Plot'][key]}""")
        dataframe4 = dataframe3[
            ['week', 'PrepH', 'PreSoilMoisture', 'PreN', 'PreP', 'PreEC', 'PreZn', 'PreS', 'PreK', 'PreMg', 'PreCa',
             'PreTemperature', 'PreHumidity', 'PreLight']]
        dataframe4 = dataframe4.query(f'week > 4')

        metrics = ['PrepH', 'PreSoilMoisture', 'PreN', 'PreP', 'PreEC', 'PreZn', 'PreS', 'PreK', 'PreMg', 'PreCa',
                   'PreTemperature', 'PreHumidity', 'PreLight']
        pH = []
        SoilMoisture = []
        N = []
        P = []
        EC = []
        Zn = []
        S = []
        K = []
        Mg = []
        Ca = []

        ActionpH = []
        ActionSoilMoisture = []
        ActionN = []
        ActionP = []
        ActionEC = []
        ActionZn = []
        ActionS = []
        ActionK = []
        ActionMg = []
        ActionCa = []

        Temperature = []
        Humidity = []
        weeks = []
        BestpH = []
        BestSoilMoisture = []
        BestN = []
        BestP = []
        BestEC = []
        BestZn = []
        BestS = []
        BestK = []
        BestMg = []
        BestCa = []
        BestTemperature = []
        BestHumidity = []
        w = 5

        while w < 9:
            weeks.append(w)
            dataframe5 = dataframe4.query(f'week == {w}')
            pH.append(dataframe5['PrepH'].mean())
            SoilMoisture.append(dataframe5['PreSoilMoisture'].mean())
            N.append(dataframe5['PreN'].mean())
            P.append(dataframe5['PreP'].mean())
            EC.append(dataframe5['PreEC'].mean())
            Zn.append(dataframe5['PreZn'].mean())
            S.append(dataframe5['PreS'].mean())
            K.append(dataframe5['PreK'].mean())
            Mg.append(dataframe5['PreMg'].mean())
            Ca.append(dataframe5['PreCa'].mean())
            Temperature.append(dataframe5['PreTemperature'].mean())
            Humidity.append(dataframe5['PreHumidity'].mean())

            BestpH.append(7.5)
            BestSoilMoisture.append(80)
            BestN.append(115)
            BestP.append(132)
            BestEC.append(4.6)
            BestZn.append(233)
            BestS.append(212)
            BestK.append(321)
            BestMg.append(312)
            BestCa.append(2)
            BestTemperature.append(25)
            BestHumidity.append(100)
            w = w + 1

        Data1 = {'week': weeks, 'pH': pH,
                 'SoilMoisture': SoilMoisture,
                 'N': N,
                 'P': P,
                 'EC': EC,
                 'Zn': Zn,
                 'S': S,
                 'K': K,
                 'Mg': Mg,
                 'Ca': Ca,
                 'Temperature': Temperature,
                 'Humidity': Humidity,
                 'weeks': weeks,
                 'BestpH': BestpH,
                 'BestSoilMoisture': BestSoilMoisture,
                 'BestN': BestN,
                 'BestP': BestP,
                 'BestEC': BestEC,
                 'BestZn': BestZn,
                 'BestS': BestS,
                 'BestK': BestK,
                 'BestMg': BestMg,
                 'BestCa': BestCa,
                 'BestTemperature': BestTemperature,
                 'BestHumidity': BestHumidity}

        ActionpH.append(((7 / 10) - (mean(pH) / mean(BestpH))) * 100)
        ActionSoilMoisture.append(((7 / 10) - (mean(SoilMoisture) / mean(BestSoilMoisture))) * 100)
        ActionN.append(((7 / 10) - (mean(N) / mean(BestN))) * 100)
        ActionP.append(((7 / 10) - (mean(P) / mean(BestP))) * 100)
        ActionEC.append(((7 / 10) - (mean(EC) / mean(BestEC))) * 100)
        ActionZn.append(((7 / 10) - (mean(Zn) / mean(BestZn))) * 100)
        ActionS.append(((7 / 10) - (mean(S) / mean(BestS))) * 100)
        ActionK.append(((7 / 10) - (mean(K) / mean(BestK))) * 100)
        ActionMg.append(((7 / 10) - (mean(Mg) / mean(BestMg))) * 100)
        ActionCa.append(((7 / 10) - (mean(Ca) / mean(BestCa))) * 100)

        dataframe6 = pd.DataFrame(Data1)
        print(dataframe6)

        # st.dataframe(df) # if need to display dataframe
        Data2 = {'ActionpH': ActionpH,
                 'ActionSoilMoisture': ActionSoilMoisture,
                 'ActionN': ActionN,
                 'ActionP': ActionP,
                 'ActionEC': ActionEC,
                 'ActionZn': ActionZn,
                 'ActionS': ActionS,
                 'ActionK': ActionK,
                 'ActionMg': ActionMg,
                 'ActionCa': ActionCa}
        dataframe7 = pd.DataFrame(Data2)
        st.markdown(printCostumTitleAndContenth4(f"""AcionPlan Plot{dict1['Plot'][key]}""",
                                                 'The table below shows the amount of each nutrient that should be changed. The values are in percentages, and the number that is positive should be added as much as it is in the table, and the number that is negative should be reduced by the same amount.'),
                    unsafe_allow_html=True)


        st.write(dataframe7)
        DataFrameAction = dataframe7
        dataframe1 = data_upload('data_gorwth_allplots.csv')
        dataframe2 = dataframe1.query(f"""plot == {dict1['Plot'][key]}""")
        print("DataFrame 1 : ")
        print(dataframe1)

        st.markdown(printCostumTitleAndContenth4('Bar Chat',
                                                 f"""The graph below shows the amount of growth metrics of the plot from week 5 to week 8 that is predicted, which is displayed separately by week."""),
                    unsafe_allow_html=True)

        dataframe10 = data_upload('data_pack31.csv')
        dataframe11 = dataframe10.query(f"""plot == {dict1['Plot'][key]}""")
        fig = px.bar(dataframe11, x='week ',
                     y=['ActionlantHeight','ActionPreweight','ActionPreLongestLeaf','ActionPreLeafCount','ActionPreLeafArea',
                        'TarplantHeight', 'TarPreweight', 'TarPreLongestLeaf', 'TarPreLeafCount', 'TarPreLeafArea'],
                     barmode='group', height=400)
        # st.dataframe(df) # if need to display dataframe
        st.plotly_chart(fig)

        plot = plot + 1



























