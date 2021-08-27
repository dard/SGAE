from django.urls import path

from appSGAE import views

app_name = 'appSGAE'


urlpatterns = [
    # url home
    path('home/', views.indexView.as_view(), name='home'),
    # url Carrera
    path('carrera/', views.CarreraListView.as_view(), name='CarreraListView'),
    path('carreracreate/', views.CarreraCreateView.as_view(), name='CarreraCreateView'),
    path('carreraedit/<int:pk>/', views.CarreraUpdateView.as_view(), name='CarreraUpdateView'),
    path('carreradelete/<int:pk>/', views.CarreraDeleteView.as_view(), name='CarreraDeleteView'),


    # url Nivel
    path('nivel/', views.NivelListView.as_view(), name='NivelListView'),
    path('nivelcreate/', views.NivelCreateView.as_view(), name='NivelCreateView'),
    path('niveledit/<int:pk>/', views.NivelUpdateView.as_view(), name='NivelUpdateView'),
    path('niveldelete/<int:pk>/', views.NivelDeleteView.as_view(), name='NivelDeleteView'),

    # url Alumno
    path('alumno/', views.AlumnoListView.as_view(), name='AlumnoListView'),
    path('alumnocreate/', views.AlumnoCreateView.as_view(), name='AlumnoCreateView'),
    path('alumnoedit/<int:pk>/', views.AlumnoUpdateView.as_view(), name='AlumnoUpdateView'),
    path('alumnodelete/<int:pk>/', views.AlumnoDeleteView.as_view(), name='AlumnoDeleteView'),

    # url Profesor
    path('profesor/', views.ProfesorListView.as_view(), name='ProfesorListView'),
    path('profesorcreate/', views.ProfesorCreateView.as_view(), name='ProfesorCreateView'),
    path('profesoredit/<int:pk>/', views.ProfesorUpdateView.as_view(), name='ProfesorUpdateView'),
    path('profesordelete/<int:pk>/', views.ProfesorDeleteView.as_view(), name='ProfesorDeleteView'),
]
