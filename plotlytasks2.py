import pandas as pd

#df = pd.read_excel(r'C:\Users\conor\Downloads\Crelytica python\residata.xlsx')
#df = pd.read_excel('https://github.com/CRELYTICA-MatthewYoung/streamlit_upload/blob/main/20220508%20Residential%20Data%20-%20Purchase%20(1)%20(1).xlsx?raw=true', engine='openpyxl')



#print(data.head(10))
from PIL import Image
import streamlit as st
import numpy as np
#import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import gmplot
import pydeck as pdk
import altair as alt
import plotly.io as pio
from plotly.graph_objs import Bar, Data, Figure, Layout, Marker, Scatter
import requests
import seaborn as sns
import openpyxl
from io import BytesIO
from plotly import tools
import pip
import plotly.express as px

pip.main(["install", "openpyxl"])

df = pd.read_excel('https://github.com/ConorQuah/Ldn-property-data/blob/aa067c514426c4f6696e4a19251a06e3156c7c6a/residata.xlsx?raw=true', engine='openpyxl')

data = df.head(2000)

data.rename(columns = {'F7':'Bedrooms'}, inplace = True)

st.header("Basic Graphs to show Relationship Between Bedrooms, Location and Price")

bed_df = data.groupby('Bedrooms')
bed_dfmean = bed_df.mean()
bed_dfmean['Bedrooms'] = bed_dfmean.index.tolist()
for x in bed_dfmean.index:
    if bed_dfmean.loc[x, 'Bedrooms']<1:
        bed_dfmean.drop(x, inplace = True)
priceVbedrooms = px.scatter(y=bed_dfmean['Price'], x=bed_dfmean['Bedrooms'], title = 'Relationship Between Bedrooms and Price', labels=dict(x="Bedrooms", y="Average Price", color="Black"))

###priceVbedrooms.show()
st.write(priceVbedrooms)
st.subheader("Interestingly, the data here shows a negative correlation between the number of beds and average property price. This result may be because I have used only the top 2000 rows of data to increase loading efficiency.")
#priceVbedrooms = bed_dfmean.plot(kind = 'line', x = 'Bedrooms', y = 'Price')
#plt.show()
#st.write(priceVbedrooms) 
new_df = data.groupby('Borough')
#print(new_df)
new_dfmean = new_df.mean()
#print(new_dfmean)
new_dfmean['Borough'] = new_dfmean.index.tolist()
#print(new_dfmean)
#boroughprices = new_dfmean.plot(kind = 'scatter', y = 'Price', x = 'Borough')
boroughprices = px.bar(new_dfmean, x = 'Borough', y = 'Price', title = 'Average house price per Borough')
###boroughprices.show()
#plt.show()
st.write(boroughprices)
for x in data.index:
    if data.loc[x, 'Bedrooms']<1:
        data.drop(x, inplace = True)
beds = px.histogram(data, x='Bedrooms', title = 'Number of Bedrooms and frequencies')

###beds.show()
st.write(beds)
#histo = data['Bedrooms'].plot(kind = 'hist')
#plt.show()
import plotly.graph_objects as go
#pieexplode = go.Figure(data=[go.Pie(names='Bedrooms', values='Bedrooms', pull=[0,0.2,0])])
#pieexplode.show()
pie = px.pie(data, values='Bedrooms', names='Bedrooms', color_discrete_sequence=px.colors.sequential.RdBu, labels={"1":"1 Bedroom properties", "2":"2 Bedroom properties", "3":"3 Bedroom properties"})
pie.update_layout(title='Proportion of 1,2 and 3 Bed Houses in London')
###pie.show()
st.write(pie)
zones_df = data.groupby('Tube Zone')
zones_dfmean = bed_df.mean()
zones_dfmean['Tube Zone'] = zones_dfmean.index.tolist()
zoneVprice = px.line(zones_dfmean, x='Tube Zone', y='Price', title='How Average house price changes with Tube Zone')
###zoneVprice.show()
st.write(zoneVprice)
st.header("Map of Properties and Prices")
fig = px.density_mapbox(data, lat='Latitude', lon='Longitude', z='Price', radius=10,
                        center=dict(lat=0, lon=180), zoom=0,
                        mapbox_style="stamen-terrain", title = 'Geographical distribution of properties and prices in London')            
#fig.show()
st.write(fig)

#region_df = data.groupby('Region')
#region_dfmean = region_df.mean()
#region_dfmean['Region'] = region_dfmean.index.tolist()
#boroughpriceline = px.line(region_dfmean, x = 'Region', y = 'Price')
#boroughpriceline.update_layout(xaxis={'categoryorder':'total descending'})
#boroughpriceline.show()
#Regionfrequency = px.bar(region_dfmean, y='Price', x='Region')
#Regionfrequency.add_hline(y='Price', line_width=3, line_color="black") 
#Regionfrequency.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
#Regionfrequency.show()
#df=pd.data
#dfg=region_dfmean.groupby('Region').count().reset_index()

#figure3 = px.bar(region_dfmean, x = "Region", y = "dfg",
# color = "Region",
# labels={
# "Price": "Average price (£)"})
#figure3.add_hline(y='Price', line_width =3,
 #line_dash = "dash", line_color="black",
 #annotation_text="Affordability line",
 #annotation_position="top right")
#figure3.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})



#grouped_df = df.groupby("Region")
#print(grouped_df)
    #####!!!!!Take the mean of this column
#mean_df = grouped_df.mean()
#print(mean_df)
    #####!!!!!When you group on a column, that column becomes the index. So here I add the column back in so it is able to be used.
#Geography = ["Central", "East", "North", "North East", "North West", "South", "South East", "South West", "West"]
#mean_df["Region"] = Geography
#print(Geography)
    #st.write(mean_df)
    #####!!!!!Normal graph plotting continues
#figure3 = px.bar(mean_df, x = "Region", y = "Price",
#           color = "Region",
#           labels={
#               "Price": "Average price (£)"})
#figure3.add_hline(y=Price, line_width =3,
#                  line_dash = "dash", line_color="black",
 #                 annotation_text="Affordability line",
#                  annotation_position="top right")
#figure3.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
#figure3.show()


#regfrequency = px.bar(data, x='Region', y='Price') 

st.header("Different type of graph. Here I have used a Box Plot to show the distribution of prices within different regions") 
box = px.box(data, x='Region', y='Price')
###box.show()
st.write(box)

pip.main(["install", "openpyxl"])
#####!!!!!Starting header and reading the excel file from the GitHub repository
#####!!!!!Anywhere you see a 'st.' is referring to a streamlit functionality
#####!!!!!Green text just refers to a string in IDLE, doesn't matter if they are single or double quotes
st.header("Layered Chart to show property count and mean prices over different regions")



#df = pd.read_excel('https://github.com/CRELYTICA-MatthewYoung/streamlit_upload/blob/main/20220508%20Residential%20Data%20-%20Purchase%20(1)%20(1).xlsx?raw=true', engine='openpyxl')
#st.write(df)

df2 = data.groupby('Region') \
       .agg(Count=('One', 'size'), Price=('Price', 'mean')) \
       .reset_index()
st.write(df2)
fig13 = make_subplots(specs=[[{"secondary_y": True}]])
fig13.add_trace(
    go.Bar(x=df2['Region'], y=df2['Price'], name="Price"),
    secondary_y=False,
)


fig13.add_trace(
    go.Scatter(x=df2['Region'], y=df2['Count'], name="Count"),
    secondary_y=True,
)

    # Set x-axis title
fig13.update_xaxes(title_text="Region")

    # Set y-axes titles
fig13.update_yaxes(title_text="Mean_Price", secondary_y=False)
fig13.update_yaxes(title_text="Count", secondary_y=True)
fig13.update_layout(barmode='stack')
fig13.update_yaxes(rangemode="tozero")
###fig13.show()

st.write(fig13)


import plotly.offline as off

###off.init_notebook_mode(connected=True)

###filterprep = [dict(
###  type = 'scatter',
###  x = "Region",
#  y = "Count",
#  mode = 'markers',
#  transforms = [dict(
#    type = 'filter',
#    target = 'Bedrooms',
#    operation = '>',
#    value = 2
#  )]
#)]

#layout = dict(
#    title = 'Scores > 4'
#)

#off.iplot({'filterprep': data, 'layout': layout}, validate=False)


st.header("Interactive Charts")

#st.slider(label="Tube Zone", min_value=1, max_value=6, step=1, value=None, format=None)
df4=data
#df4['Tube Zone'] = df4.index.tolist()
zone_slider = st.slider("Tube Zone", 1, 6)
#zones = df4['Tube Zone'].drop_duplicates()
#zone_choice = st.sidebar.selectbox('Tube Zone', Tube Zone)
filtered = df4.loc[(df4['Tube Zone']==zone_slider)]
#st.write(zone_choice)
#zone_df = data.groupby('Tube Zone')
#zone_dfmean = zone_df.mean()
#zone_dfmean['Tube Zone'] = zone_dfmean.index.tolist()

pie2 = px.pie(filtered, values='Bedrooms', names='Bedrooms', color_discrete_sequence=px.colors.sequential.RdBu, title='See how composition of 1,2 and 3 bed properties changes over different tube zones')
#pie2.update_layout(title='Proportion of 1,2 and 3 bed properties over different tube zones')
###pie.show()
#pie2.show()
st.write(pie2)
st.subheader("The purpose of this interactive chart is to test the hypothesis that as as properties get closer to zone 1, the composition of properties leans further towards smaller 1 and 2 bed properties")

