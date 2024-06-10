from django.urls import path
from .views import get_character, get_all_character

urlpatterns = [
    path('character/<int:id>/', get_character, name='get_character_by_id'),
    path('character/', get_all_character, name='get_all_character')
]