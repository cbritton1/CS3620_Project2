from . import views
from django.urls import path

app_name = 'story_time'
urlpatterns = [
    path('', views.home, name='home'),
    path('story_one_form/', views.story_one_form, name='story_one_form'),
    path('story_one/', views.story_one, name='story_one'),
    # path('story_delete<int:item_id>/', views.story_delete, name='story_delete')
]
