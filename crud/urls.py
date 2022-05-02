from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_show, name="add_show"),
    path('delete/<int:id>/', views.delete_user, name='delete_user'),
    path('<int:id>/', views.update_user, name='update_user'),
]