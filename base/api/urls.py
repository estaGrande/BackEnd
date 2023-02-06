from . import views
from django.urls import path

urlpatterns = [
    path('', views.routes),
    path('posts/', views.posts),
    path('post/<int:id>', views.post),
    path('baqueros/', views.baqueros),
    path('florafauna/', views.florasfaunas),
]