import plotly.express as px
import pandas as pd

# Пример данных
data = pd.DataFrame({
    "city": ["Москва", "Лондон", "Нью-Йорк"],
    "lat": [55.7558, 51.5074, 40.7128],
    "lon": [37.6176, -0.1278, -74.0060],
    "value": [100, 200, 300]
})

# Строим карту
fig = px.scatter_geo(
    data,
    lat="lat",
    lon="lon",
    text="city",
    size="value",
    color="value",
    projection="natural earth",
    title="🌍 Тестовая географическая карта с Plotly"
)

fig.show()
