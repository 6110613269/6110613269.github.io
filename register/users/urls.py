from django.urls import path
from . import views
from students import views as v2

urlpatterns = [
    path('', views.login_view, name="login"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout')
]