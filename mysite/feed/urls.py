from django.urls import path
from .views import HomePageView, PostDetailView

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/<str:name>/', PostDetailView.as_view(), name='detail'),
]