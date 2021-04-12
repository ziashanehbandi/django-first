from django.urls import path
from .views import project,blog,each_blog

app_name='blog'


urlpatterns= [
    path('',project,name='project'),
    path('blog/',blog,name='blog'),
    path('<int:blog_id>',each_blog,name='each_blog'),
]