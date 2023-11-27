from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ScoreAggregateappPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ScoreAggregateappPost
from django.views.generic import DetailView
from django.views.generic import DeleteView

class IndexView(ListView):
    template_name = 'index.html'
    queryset = ScoreAggregateappPost.objects.order_by('-posted_at')
    paginate_by = 9
@method_decorator(login_required, name='dispatch')
class CreateScoreAggregateappView(CreateView):
    form_class = ScoreAggregateappPostForm
    template_name = "post_score_aggregateapp.html"
    success_url = reverse_lazy('score_aggregateapp:post_done')
    def form_valid(self, form):
        postdata = form.save(commit=False)
        postdata.user = self.request.user
        postdata.save()
        return super().form_valid(form)
class PostSuccessView(TemplateView):
    template_name = 'post_success.html'
class CategoryView(ListView):
    template_name ='index.html'
    paginate_by = 9
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ScoreAggregateappPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories
class UserView(ListView):
    template_name ='index.html'
    paginate_by = 9
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = ScoreAggregateappPost.objects.filter(
            user=user_id).order_by('-posted_at')
        return user_list
class DetailView(DetailView):
    template_name ='detail.html'
    model = ScoreAggregateappPost
class MypageView(ListView):
    template_name ='mypage.html'
    paginate_by = 9
    def get_queryset(self):
        queryset = ScoreAggregateappPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset
class ScoreAggregateappDeleteView(DeleteView):
    model = ScoreAggregateappPost
    template_name ='score_aggregateapp_delete.html'
    success_url = reverse_lazy('score_aggregateapp:mypage')
    def delete(self, request: HttpRequest, *args: str, **kwargs: Any):
        return super().delete(request, *args, **kwargs)
