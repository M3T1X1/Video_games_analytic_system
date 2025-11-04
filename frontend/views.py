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

def main_analysis(request):
    data = pd.read_csv('data_analysis/vgchartz-2024.csv')

    headers = list(data.columns)[1:-1]


    x_axis = request.GET.get('x')
    y_axis = request.GET.get('y')
    limits = request.GET.get('limits')

    chart_html = None

    if limits and limits.isdigit():
        data = data.head(int(limits))

    if x_axis and y_axis and x_axis in data.columns and y_axis in data.columns:
        figure = px.bar(
            data_frame=data,
            x = x_axis,
            y = y_axis,
            title = "Custom Analysis",
            color_discrete_sequence= ['red', 'green', 'blue']

        )

        figure.update_layout(
            height=600,
            margin=dict(l=40, r=40, b=60, t=40)
        )

        chart_html = figure.to_html(full_html=False)

    context = {
        'headers': headers,
        'chart_html': chart_html,
        'selected_x_axis': x_axis,
        'selected_y_axis': y_axis,
        'limits': limits
    }

    return render(request, 'frontend/main_analysis.html',context)

