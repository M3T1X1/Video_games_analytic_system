from django.shortcuts import render
import pandas as pd
import plotly.express as px

def home(request):
    return render(request, 'frontend/index.html')

def dashboard():
    data = pd.read_csv('/home/pop_os/PycharmProjects/Video_games_analytic_system/data_analysis/vgchartz-2024.csv')

    #Analysing the sales by each platform

    sales_by_platform = data.groupby('console')['total_sales'].sum().sort_values(ascending=False)
    fighure_1 = px.bar(
        x = sales_by_platform.index,
        y = sales_by_platform.values,
        title = 'Sales by console platform',
        labels = {'x' : "Platform", 'y' : "Sales"},
        color = sales_by_platform.index
    )

    chart = fighure_1.to_html(full_html=False)

#dashboard()
