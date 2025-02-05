
from django.urls import path


from articles import views


urlpatterns = [
    path('articles/', views.article_list, name='article-list'),
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
]
