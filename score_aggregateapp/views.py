
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
from django.views.generic import FormView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
class IndexView(ListView):
    template_name = 'index.html'
    queryset = ScoreAggregateappPost.objects.order_by('-posted_at')
    paginate_by = 15
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
    paginate_by = 15
    def get_queryset(self):
        category_id = self.kwargs['category']
        categories = ScoreAggregateappPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return categories
class UserView(ListView):
    template_name ='index.html'
    paginate_by = 15
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
    paginate_by = 15
    def get_queryset(self):
        queryset = ScoreAggregateappPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return queryset
class ScoreAggregateappDeleteView(DeleteView):
    model = ScoreAggregateappPost
    template_name ='score_aggregateapp_delete.html'
    success_url = reverse_lazy('score_aggregateapp:mypage')
    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs)
        query = self.request.GET

        if q := query.get('q'): #python3.8以降
            queryset = queryset.filter(Q(content__icontains=q)|Q(title__icontains=q))

        return queryset.order_by('-created_at')
class ContactView(FormView):

    template_name ='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('score_aggregateapp:contact')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context['form'])
    #     return context

    def form_valid(self, form):
        
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = 'お問い合わせ:{}'.format(title)

        message = \
            '送信者名: {0}\n メールアドレ: {1}\n タイトル:{2}\n メッセージ:\n{3}' \
            .format(name, email, title, message)
        
        from_email = 'admin@example.com'

        to_list = ['kkr.python9999@gmail.com']

        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                               )

        message.send()

        messages.success(
            self.request, 'お問い合わせは正常に送信されました。')
        
        return super().form_velid(form)  