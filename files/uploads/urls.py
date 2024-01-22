from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('home', views.home, name='home'),
    path('', CustomLoginView.as_view(), name='login'),
    path('files-upload/', views.upload_file, name='upload_file'),
    path('fileslist/', views.file_list, name='fileslist'),
    path('client/<int:pk>/',views.ClientDetail, name='detail' ),
    path('logout/', views.logout_view, name='logout'),


]