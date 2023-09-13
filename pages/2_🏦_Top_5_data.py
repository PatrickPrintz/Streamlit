import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

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


# Top 5 countries:
count_data = df['Country'].value_counts().nlargest(5).reset_index()
count_data.columns = ['Country', 'Count']
count_chart = alt.Chart(count_data).mark_bar().encode(
    alt.X('Country:N', title = 'Countries', axis=alt.Axis(labelAngle=45)),
    alt.Y('Count', title = 'Amount of Youtube channels'),
    tooltip = # I believe tooltip is a nice addition to all plots we're going to include! (Tip: Hover over the bars)
    [alt.Tooltip('Country:N', title = 'Country'),
     alt.Tooltip('Count:N', title = 'Amount of Youtubers')]
).properties(
    width = 800,
    height = 500,
    title = 'Top five countries with most Youtubers'
)
count_chart.configure( # All of these theme configs might look silly when put together with the others, assuming not all have used Altair. Otherwise they could be the same.
    background='#EFEBE0',
    axis=alt.AxisConfig(
        labelFont='serif',
        labelFontSize = 15,
        titleFont='serif',
        titleFontSize=20,
        gridColor='#535B5C',
        gridDash=[1, 4]
    ),
    title=alt.TitleConfig(
        font='serif',
        fontSize=20
    ))
count_chart