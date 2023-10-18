from django.shortcuts import render,HttpResponse

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
    formData =  FormModel.objects.all()
    return render(request , 'data.html' , {'usr' : formData})


def success(request):
    return render(request , 'success.html')