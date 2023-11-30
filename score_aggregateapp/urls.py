from django.urls import path
from . import views
app_name = 'score_aggregateapp'
urlpatterns = [
    path('contact/',
        views.ContactView.as_view(),
        name='contact'
        ),
    path('', views.IndexView.as_view(), name='index'),
    path('post/', views.CreateScoreAggregateappView.as_view(), name='post'),
    path('post_done/',
         views.PostSuccessView.as_view(),
         name='post_done'),
    path('score_aggregateapp/<int:category>',
         views.CategoryView.as_view(),
         name='score_aggregateapps_cat'
         ),
    path('user-list/<int:user>',
         views.UserView.as_view(),
         name='user_list'
         ),
    path('score_aggregateapp-detail/<int:pk>',
         views.DetailView.as_view(),
         name='score_aggregateapp_detail'
         ),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('score_aggregateapp/<int:pk>/delete/',
         views.ScoreAggregateappDeleteView.as_view(),
         name= 'score_aggregateapp_delete'
        ),     
    ]