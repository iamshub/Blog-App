
from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.ArticleListView.as_view(), name='home1' ),
    path('$/login/^', views.A1.as_view(), name = 'home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_page'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),

]