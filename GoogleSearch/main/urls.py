from django.urls import path
from . import views

app_name='main'


urlpatterns=[
    path('',views.google_view,name='google_view'),
    path('Terms/of/Service/',views.tos_view,name='tos_view'),
    path('night/mode/',views.night_mode_view,name='night_mode_view'),
    path('light/mode/',views.light_mode_view,name='light_mode_view'),

]