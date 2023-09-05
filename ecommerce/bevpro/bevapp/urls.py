from django.urls import path
from bevapp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage")
    
]
