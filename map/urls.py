from django.urls import path
from .views import show_map

urlpatterns = [
    # ... other patterns ...
    path('', show_map, name='show_map'),
    
]
