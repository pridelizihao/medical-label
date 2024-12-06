from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, template_name='html/index.html')

def blog_detail(request,blog_id):
    return render(request, template_name='html/blog_detail.html')

def pub_blog(request):
    return render(request, template_name='html/pub_blog.html')