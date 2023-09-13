import streamlit as st
import pandas as pd
import seaborn as sns
import altair as alt

st.set_page_config(page_title="Descriptive statistics", page_icon="📊")

st.title("Descriptive statistics")
st.markdown("""
            This page shows the descriptive statistics of the dataset Youtube, with the key variables of interest and their descriptions,
            followed by a table of the minimum, maximum, and average values for each variable. Lastly the table will be presented in boxplots.
            """)

st.header("""
          Key variables of interest:
          - **rank**: Position of the YouTube channel based on the number of subscribers
          - **subscribers**: Number of subscribers to the channel
          - **category**: Category or niche of the channel
          - **Country**: Country where the YouTube channel originates
          - **created_year**: Year when the YouTube channel was created
          - **Gross tertiary education enrollment (%)**: Percentage of the population enrolled in tertiary education in the country
          - **Population**: Total population of the country
          - **Unemployment rate**: Unemployment rate in the country
          - **Urban_population**: Percentage of the population living in urban areas
          - **Latitude**: Latitude coordinate of the country's location
          - **Longitude**: Longitude coordinate of the country's location
          , divider='rainbow'

          """)
st.header("Minimum, maximum, and average values")
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

mean_stats = df.describe().T.round(1)
mean_stats
st.write("   ")
st.markdown("""
- Subscribers vary widely from 12.3 million to 245 million, with an average of approximately 23.07 million.

- The channels were created between 1970 and 2022, with an average creation year of 2012.

- Gross tertiary education enrollment percentages vary from 7.6% to 113.1%, with an average of 63.4%.

- The population spans from 202,506 to 1.4 billion, with an average population of approximately 432.8 million.

- Unemployment rates range from 0.8% to 14.7%, with an average of 9.2%.

- Urban populations vary widely, with an average of approximately 224.6 million.
        """)



st.header("")
st.header("""
            Boxplots
          """)
st.markdown("""
            Shown graphically, this can be represented by the following boxplots for each of the relevant variables.
            """)
boxplot_population = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('Population', title='Population', scale=alt.Scale(domain=[df.Population.min(), df.Population.max()]))  # Set the scale explicitly
).properties(
    width=800,
    height=100
)
boxplot_year = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('created_year', title='Created Year', scale=alt.Scale(domain=[1965, 2025]))  # Set the scale explicitly
).properties(
    width=800,
    height=100
)
boxplot_subscribers = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('subscribers', title='Subscribers', scale=alt.Scale(domain=[10000000.0, df.subscribers.max()]))  # Set the scale explicitly
).properties(
    width=800,
    height=100
)
boxplot_education = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('Gross tertiary education enrollment (%)', title='Gross tertiary education enrollment (%)', scale=alt.Scale(domain=[7, 115]))  # Set the scale explicitly
).properties(
    width=800,
    height=100
)
boxplot_unemployment = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('Unemployment rate', title='Unemployment rate (%)', scale=alt.Scale(domain=[0, 20]))  # Set the scale explicitly
).properties(
    width=800,
    height=100
)
boxplot_urban = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('Urban_population', title='Urban population', scale=alt.Scale(domain=[35588 , 852933962]))  # Set the scale explicitly
).properties(
    width=800,
    height=100
)
boxplot_year
boxplot_population
boxplot_subscribers
boxplot_education
boxplot_unemployment
boxplot_urban