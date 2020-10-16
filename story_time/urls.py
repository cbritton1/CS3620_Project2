from . import views
from django.urls import path

app_name = 'story_time'
urlpatterns = [
    path('', views.home, name='home'),
    path('story_one_form/', views.story_one_form, name='story_one_form'),
    path('story_two_form/', views.story_two_form, name='story_two_form'),
    path('story_war_form/', views.story_war_form, name='story_war_form'),
    path('story_walmart_form/', views.story_walmart_form, name='story_walmart_form'),
    path('story_dragons_form/', views.story_dragons_form, name='story_dragons_form'),
    path('story_love_letter_form/', views.story_love_letter_form, name='story_love_letter_form'),
    path('story_smelly_cat_form/', views.story_smelly_cat_form, name='story_smelly_cat_form'),
    path('story_one/<int:item_id>', views.story_one, name='story_one'),
    path('story_two/<int:item_id>', views.story_two, name='story_two'),
    path('story_war/<int:item_id>', views.story_war, name='story_war'),
    path('story_dragons/<int:item_id>', views.story_dragons, name='story_dragons'),
    path('story_walmart/<int:item_id>', views.story_walmart, name='story_walmart'),
    path('story_love_letter/<int:item_id>', views.story_love_letter, name='story_love_letter'),
    path('story_smelly_cat/<int:item_id>', views.story_smelly_cat, name='story_smelly_cat'),
    path('all_stories', views.all_stories, name='all_stories'),
    # path('story_delete<int:item_id>/', views.story_delete, name='story_delete')
]
