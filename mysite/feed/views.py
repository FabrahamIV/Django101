from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import PostForm
import logging

logger = logging.getLogger(__name__)


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-created_at')
        return context

class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post

class AddPostView(FormView):
    form_class = PostForm
    template_name = "post_form.html"
    success_url = "/"

    def form_valid(self, form):
        new_post = Post.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            image=form.cleaned_data['image']
        )
        return super().form_valid(form)
        logger.info(f"Form is valid")