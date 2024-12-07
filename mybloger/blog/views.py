from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request, template_name='blog/index.html')

def remendations(request):
    return render(request, template_name='blog/remendations.html')

def team(request):
    return render(request, template_name='blog/team.html')

def product(request):
    return render(request, template_name='blog/product.html')

def contact(request):
    return render(request, template_name='blog/contact.html')


def blog_detail(request,blog_id):
    return render(request, template_name='html/blog_detail.html')

def pub_blog(request):
    return render(request, template_name='html/pub_blog.html')