from django.shortcuts import render
import pandas as pd
import plotly.express as px

def home(request):
    return render(request, 'frontend/index.html')

def sales_by_platform(request):
    data = pd.read_csv('data_analysis/vgchartz-2024.csv')

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
    # Analysing game sales based on their genre
    data = pd.read_csv('data_analysis/vgchartz-2024.csv')

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

def sales_by_rating(reqests):
    #Analysin game sales based on their ranking
    data = pd.read_csv('data_analysis/vgchartz-2024.csv')

    avg_score_by_title = (
        data.groupby('title')['critic_score']
        .mean()
        .sort_values(ascending=False)
        .head(30)
    )

    # Wykres słupkowy z plotly.express
    figure_3 = px.bar(
        x=avg_score_by_title.values,
        y=avg_score_by_title.index,
        title='Top 10 Games by Average Critic Score',
        labels={'y': "Game Title", 'x': "Average Critic Score"},
        color=avg_score_by_title.values,
        color_continuous_scale='Viridis'
    )

    chart_sales_by_rating = figure_3.to_html(full_html=False)

    context = {
        'chart_sales_by_rating' : chart_sales_by_rating
    }

    return render(reqests, 'frontend/sales_by_rating.html', context)

#dashboard()
