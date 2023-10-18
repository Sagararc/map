from django.urls import path
from .views import show_map,FormData,datashow,success,export_data

urlpatterns = [
    # ... other patterns ...
    path('', show_map, name='show_map'),
    path('form/' , FormData , name='form'),
    path('data/' , datashow , name='data'),
    path('success/' , success , name='success'),
    path('export/', export_data, name='export_data'),
    
]
