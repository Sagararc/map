from django.urls import path
from .views import show_map, location_input

urlpatterns = [
    # ... other patterns ...
    path('', show_map, name='show_map'),
    
]
