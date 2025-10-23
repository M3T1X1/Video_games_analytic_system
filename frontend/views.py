from django.shortcuts import render
import pandas as pd
import plotly.express as px

def home(request):
    return render(request, 'frontend/index.html')

def sales_by_platform(request):
    data = pd.read_csv('/home/pop_os/PycharmProjects/Video_games_analytic_system/data_analysis/vgchartz-2024.csv')

    #Analysing the sales by each platform
    data_sales_by_platform = data.groupby('console')['total_sales'].sum().sort_values(ascending=False)
    figure_1 = px.bar(
        x = data_sales_by_platform.index,
        y = data_sales_by_platform.values,
        title = 'Sales by console platform',
        labels = {'x' : "Platform", 'y' : "Sales"},
        color = data_sales_by_platform.index
    )

    chart_sales_by_platform = figure_1.to_html(full_html=False)

    context = {
        'chart_sales_by_platform': chart_sales_by_platform
    }

    return render(request, 'frontend/sales_by_platform.html', context)

def sales_by_genre(request):
    # Analysing game sales based of their genre
    data = pd.read_csv('/home/pop_os/PycharmProjects/Video_games_analytic_system/data_analysis/vgchartz-2024.csv')

    data_sales_by_genre = data.groupby('genre')['total_sales'].sum().sort_values(ascending=False)
    figure_2 = px.bar(
        x=data_sales_by_genre.index,
        y=data_sales_by_genre.values,
        title='Sales by genre',
        labels={'x': "Genre", 'y': "Sales"},
        color=data_sales_by_genre.index
    )

    chart_sales_by_genre = figure_2.to_html(full_html=False)

    context = {
        'chart_sales_by_genre': chart_sales_by_genre
    }
    return render(request, 'frontend/sales_by_genre.html', context)


#dashboard()
