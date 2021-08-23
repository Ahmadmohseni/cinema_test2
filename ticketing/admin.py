from ticketing.models import Cinema, Movie, ShowTime
from django.contrib import admin
# Register your models here.
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(ShowTime)

