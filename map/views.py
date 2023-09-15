from django.shortcuts import render,HttpResponse
from .models import Location
from .forms import LocationForm
# Create your views here.



# def location_input(request):
#     if request.method == 'POST':
#         form = LocationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             HttpResponse('Submitted....')
#     else:
#         form = LocationForm()

#     return render(request, 'lat.html', {'form': form})



def show_map(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations})
