from django.urls import path
from . import views
from users import views as v2

urlpatterns = [
    #path('', views.index, name="index"),
    path('<int:student_id>', views.student, name="student"),
    path('<int:student_id>/book', views.book, name="book"),
    path('<int:student_id>/drop', views.drop, name="drop"),
    path('logout', v2.logout_view, name='logout'),
    path('<int:student_id>/back', views.back, name="back")


]