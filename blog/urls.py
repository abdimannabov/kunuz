from django.urls import path
from blog.views import *
urlpatterns = [
    path('', ArticleView.as_view(), name="home"),
    path('category/<int:pk>/', ArticleByCategory.as_view(), name="category"),
    path('detail/<int:pk>/', article_detail, name="detail"),
    path('add/', AddArticle.as_view(), name="add"),
    path('edit/<int:pk>/', EditArticle.as_view(), name="edit"),
    path('delete/<int:pk>/', DeleteArticle.as_view(), name="delete"),
    path('save_comment/<int:pk>/', save_comment, name="save_comment"),
    path('register/', user_register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('profile/', user_profile, name="profile"),
    path('search/', SearchResult.as_view(), name="search_result"),
]