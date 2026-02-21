import pandas as pd
import plotly.express as px

df = pd.read_csv('datasets/COVID-19 in Italy province.csv')

df_provinces = df.dropna(subset=['Latitude', 'Longitude']).copy()

df_provinces['Date'] = pd.to_datetime(df_provinces['Date'])
df_provinces = df_provinces.sort_values('Date')
df_provinces['Date_str'] = df_provinces['Date'].dt.strftime('%d-%m-%Y')

max_size = df_provinces['TotalPositiveCases'].max()

fig = px.scatter_geo(
    df_provinces,
    lat="Latitude",
    lon="Longitude",
    color="TotalPositiveCases",
    size="TotalPositiveCases",
    hover_name="ProvinceName",
    hover_data={"TotalPositiveCases": True, "Latitude": False, "Longitude": False},
    animation_frame="Date_str",
    projection="natural earth",
    title="Динамика заражений по провинциям Италии",
    color_continuous_scale="Reds",
    size_max=60,
    range_color=[0, max_size / 5]
)

fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})
fig.show()
