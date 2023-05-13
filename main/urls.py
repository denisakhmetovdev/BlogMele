from django.urls import path
from .views import post_list, post_detail


app_name = 'main'


urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:id>/', post_detail, name='post_detail'),
]
