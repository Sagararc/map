from django.shortcuts import render,HttpResponse
from django.db.models.fields.files import FileField, ImageField
from .models import FormModel
from django.http import StreamingHttpResponse
import csv
from django.core.paginator import Paginator
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
    
    return render(request, 'index.html')


from django.shortcuts import render , HttpResponse , redirect
from .forms import Form
from .models import FormModel
# Create your views here.
def FormData(request):
    
  
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            
           
            name = request.POST.get('name')
            mobile = request.POST.get('mobile')
            mail = request.POST.get('mail')
            city = request.POST.get('city')
            counts = request.POST.get('counts')
            
            
            form.instance.name = name
            form.instance.mobile = mobile
            form.instance.mail = mail
            form.instance.city = city
            form.instance.counts = counts
           
            form.save()
            return redirect('success')
        else:
            print(form.errors)   
    return render(request , 'form.html')


def datashow(request) : 
    data =  FormModel.objects.all()
    paginator = Paginator(data, 10)  
    page_number = request.GET.get('page')
    data = paginator.get_page(page_number)
    return render(request , 'data.html' , {'usr' : data})


def success(request):
    return render(request , 'success.html')


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """

    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value

def export_data(request):
    data = FormModel.objects.all()
    model_fields = FormModel._meta.fields
    excluded_fields = ['pwd']
    field_names = [field.name for field in model_fields if field.name not in excluded_fields]

    rows = []

    for row in data:
        new_row = []
        for field_name in field_names:
            value = getattr(row, field_name)
            if isinstance(value, (FileField, ImageField)) and value:
                value = f'http://172.105.41.115:8001{value.url}'
            new_row.append(value)
        rows.append(new_row)

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)

    response = StreamingHttpResponse(
        (writer.writerow(row) for row in [field_names] + rows),  
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    return response