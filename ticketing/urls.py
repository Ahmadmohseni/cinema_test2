from django.urls.resolvers import URLPattern
from django.urls import path
from ticketing import views

app_name= 'ticketing'
urlpatterns = [
    path('movie/list' , views.movie_list, name='movie_path'),
    path('movie/details/<int:movie_id>' , views.movie_details, name='movie_details'),
    path('cinema/list' , views.cinema_list, name='cinema_path'),
    path('cinema/details/<int:cinema_id>' , views.cinema_details, name='cinema_details'),
    path('showtime/list' , views.showtime_list , name='showtime_list')
]