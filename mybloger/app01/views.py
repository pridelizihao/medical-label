import base64
from django.shortcuts import render, redirect
from app01.forms import Base64ImageForm
from app01.models import Base64Image
 
def upload_base64_image(request):
    if request.method == 'POST':
        form = Base64ImageForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            image_data = base64.b64encode(image.read()).decode('utf-8')
            Base64Image.objects.create(title=title, image_data=image_data)
            return redirect('image_list')
    else:
        form = Base64ImageForm()
    return render(request, 'html/upload_base64_image.html', {'form': form})
 
def image_list(request):
    images = Base64Image.objects.all()
    return render(request, 'html/image_list.html', {'images': images})

def one(request):
    return render(request, 'html/01.html')

