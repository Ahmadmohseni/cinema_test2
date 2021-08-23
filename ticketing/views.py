from ticketing.models import ShowTime
from django.http.response import HttpResponse
from ticketing.models import Cinema
from ticketing.models import Movie
from django.shortcuts import get_object_or_404, render

# Create your views here.

def movie_list(request):
    movie = Movie.objects.all()
    context = {
        'movielist':movie
    }
    return render(request,'ticketing/movielist.html',context)

def cinema_list(request):
    cinema = Cinema.objects.all()
    context ={
        'cinemas': cinema
    }
  
    return render(request, 'ticketing/cinemalist.html', context)

def movie_details(request , movie_id):
    movie= get_object_or_404(Movie , pk=movie_id)
    context = {
        'movie': movie
    }
    #return HttpResponse(movie)
    return render(request ,'ticketing/movie_details.html', context)

def cinema_details(request , cinema_id):
    cinema= get_object_or_404(Cinema , pk=cinema_id)
    context = {
        'cinema': cinema
    }
    return render(request ,'ticketing/cinema_details.html', context)

def showtime_list(request):
    showtimes=ShowTime.objects.all()
    context={
        'showtimes': showtimes
    }
    return render(request, 'ticketing/showtime_list.html', context)