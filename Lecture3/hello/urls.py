from django.urls import path

from .import views

urlpatterns = [ 
    path('', views.index, name = 'index' ),
    path( 'lalo', views.lalo, name = 'Lalo' ),
    path( 'juan', views.juan, name = 'Juan' ),
    path( 'pablo', views.pablo, name = 'Pablo' ),
]