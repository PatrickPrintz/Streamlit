import streamlit as st
import numpy as np
import random
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

@st.cache_data  # Cache the function to enhance performance
def load_data():
    # Define the file path
    file_path = 'https://raw.githubusercontent.com/SeniorHreff/edayoutube/main/global_youtube_data_2023.csv'
    
    # Load the CSV file into a pandas dataframe
    df = pd.read_csv(file_path)
    df = df.drop(columns = ['video views', 'Title', 'uploads', 'video_views_rank', 'country_rank', 'channel_type_rank','video_views_for_the_last_30_days', 'lowest_monthly_earnings', 'highest_monthly_earnings', 'lowest_yearly_earnings', 'highest_yearly_earnings', 'subscribers_for_last_30_days', 'created_month', 'created_date'])
    df = df.dropna()
    

    return df

# Load the data using the defined function
df = load_data()

geodf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
geodf.crs = "EPSG:4326"
geodf_crs = geodf.to_crs("EPSG:4326")

st.subheader("Spatial Distribution of Police Shootings, Public Schools and Neighborhoods")
    
m = folium.Map(location=[geodf.Longitude.mean(), geodf.Latitude.mean()], zoom_start=1, tiles="CartoDB positron")

# Create a marker cluster
marker_cluster = MarkerCluster().add_to(m)

# Loop through each police shooting and add it as a circle on the map within the marker cluster
for _, row in geodf_crs.iterrows():
    # Creating a pop-up message with some key information about the incident
    popup_content = f"""
    Rank: {row['rank']}<br>
    Youtuber: {row['Youtuber']}<br>
    Subscribers: {row['subscribers']}<br>
    Category: {row['category']}<br>
    Country: {row['Country']}<br>
    Channel Type: {row['channel_type']}<br>
    Year Created: {row['created_year']}<br>
    """
    popup = folium.Popup(popup_content, max_width=300)

    # Add a circle for each point
    folium.Circle(
        location=[row['Latitude'], row['Longitude']],
        radius=15,
        color='blue',
        fill=True,
        fill_color='blue',
        fill_opacity=0.4,
        popup=popup
    ).add_to(marker_cluster)

## Doesnt work yet!!
st_folium(m)