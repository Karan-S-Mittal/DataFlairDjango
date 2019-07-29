from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'homepage'),
	path('other/', views.other, name = 'otherpage')
]