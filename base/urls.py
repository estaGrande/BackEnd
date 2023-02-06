from django.urls import path
from . import views

urlpatterns= [
    path('', views.home),
    path('login/', views.loginPage),
    path('register/', views.registerPage),    
    path('logout/', views.logoutPage),
    path('post/', views.post),
    path('post/<int:id>', views.post),
    path('comment/', views.commentPage),
    path('coment/<int:id>', views.coment),
    path('caballos/', views.caballoPage),
    path('baqueros/', views.baqueroPage),
    path('florafauna/', views.florafaunaPage),
]