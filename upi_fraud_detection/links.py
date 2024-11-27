from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about,name='about'),
    path('result',views.predict_fraud_risk, name='result'),
]
