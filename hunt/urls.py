from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
        re_path(r'^$', views.index, name="index"),
        re_path(r'^logout/?$', auth_views.LogoutView.as_view(), {'next_page':'login'}, name="logout"),
        re_path(r'^login/?$', auth_views.LoginView.as_view(), name="login"),
        re_path(r'^signup/?$', views.signup, name="signup"),
        re_path(r'^base/?$', views.base, name="base"),
        re_path(r'^leaderboard/?$', views.leaderboard, name="leaderboard"),
        re_path(r'^play/?$', views.play, name="play"),
        re_path(r'^level/(?P<level_number>\d+)/?$', views.level, name="level"),
        re_path(r'^rules/?$',views.rules, name="rules"),
        re_path(r'^userdetails/?$',views.userdetails, name="userdetails"),
]
