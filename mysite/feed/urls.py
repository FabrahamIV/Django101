from django.urls import path
from .views import HomePageView, PostDetailView, AddPostView
from .forms import PostForm

app_name = 'feed'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/', AddPostView.as_view(), name='form'),
]