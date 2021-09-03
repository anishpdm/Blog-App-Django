from django.urls import path, include
from userblogs import views

urlpatterns = [
   
#  Views
    path('login/', views.loginview, name='loginview'),
    path('register/', views.regview, name='regview'),
    path('addpost/', views.addpost, name='addpost'),
    path('blogview/', views.retrievepost, name='retrievepost'),




#    API's 
    path('registerAction/', views.user_create, name='user_create'),
    path('viewprofile/', views.prof_view, name='prof_view'),
    path('addpostAction/', views.post_create, name='post_create'),




   
]