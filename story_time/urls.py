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
    path('story_greeting_earthlings_form/', views.story_greeting_earthlings_form, name='story_greeting_earthlings_form'),
    path('hail_to_the_chief_form/', views.story_hail_to_the_chief_form, name='story_hail_to_the_chief_form'),
    path('story_holiday_festivities_form/', views.story_holiday_festivities_form, name='story_holiday_festivities_form'),
    path('story_pizza_parlor_form/', views.story_pizza_parlor_form, name='story_pizza_parlor_form'),
    path('story_cat_and_the_fiddle_form/', views.story_cat_and_the_fiddle_form, name='story_cat_and_the_fiddle_form'),
    path('storystory_baseball_form/', views.story_baseball_form, name='story_baseball_form'),
    path('story_JJRTolkien_form/', views.story_JJRTolkien_form, name='story_JJRTolkien_form'),
    path('story_jack_and_jill_form/', views.story_jack_and_jill_form, name='story_jack_and_jill_form'),
    path('story_one/<int:item_id>', views.story_one, name='story_one'),
    path('story_two/<int:item_id>', views.story_two, name='story_two'),
    path('story_war/<int:item_id>', views.story_war, name='story_war'),
    path('story_dragons/<int:item_id>', views.story_dragons, name='story_dragons'),
    path('story_walmart/<int:item_id>', views.story_walmart, name='story_walmart'),
    path('story_love_letter/<int:item_id>', views.story_love_letter, name='story_love_letter'),
    path('story_smelly_cat/<int:item_id>', views.story_smelly_cat, name='story_smelly_cat'),
    path('story_greeting_earthlings/<int:item_id>', views.story_greeting_earthlings, name='story_greeting_earthlings'),
    path('hail_to_the_chief/<int:item_id>', views.story_hail_to_the_chief, name='story_hail_to_the_chief'),
    path('story_holiday_festivities/<int:item_id>', views.story_holiday_festivities, name='story_holiday_festivities'),
    path('story_pizza_parlor/<int:item_id>', views.story_pizza_parlor, name='story_pizza_parlor'),
    path('story_cat_and_the_fiddle/<int:item_id>', views.story_cat_and_the_fiddle, name='story_cat_and_the_fiddle'),
    path('story_baseball/<int:item_id>', views.story_baseball, name='story_baseball'),
    path('story_JJRTolkien/<int:item_id>', views.story_JJRTolkien, name='story_JJRTolkien'),
    path('story_jack_and_jill/<int:item_id>', views.story_jack_and_jill, name='story_jack_and_jill'),
    path('all_stories', views.all_stories, name='all_stories'),
    # path('story_delete<int:item_id>/', views.story_delete, name='story_delete')
]
