from django.urls import path
from .views import show_map,FormData,datashow,success

urlpatterns = [
    # ... other patterns ...
    path('', show_map, name='show_map'),
    path('form/' , FormData , name='form'),
    path('data/' , datashow , name='data'),
    path('success/' , success , name='success'),
    
]
