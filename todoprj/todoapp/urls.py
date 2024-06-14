from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('delete/<int:id>/', views.DeleteTask, name='delete-task'),
    path('update/<int:id>/', views.Update, name='update-task'),
]












































# gpt
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home-page'),
#     path('register/', views.register, name='register'),
#     path('login/', views.loginpage, name='login'),
#     path('delete-task/<str:name>/', views.DeleteTask, name='delete-task'),
#     path('update-task/<str:name>/', views.Update, name='update-task'),
#     # path('logout/', views.logout_view, name='logout'),
# ]
