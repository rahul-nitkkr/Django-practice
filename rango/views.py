from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category , Page

def index(request):
    category_list = Category.objects.order_by('likes')[:2]
    context_dict = {'categories': category_list }
    return render(request , 'rango/index.html' , context_dict)

def about(request):
    return HttpResponse("Rango took me here! <a href='/rango/'>Get me Back!</a>")

def category(request , category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        print("debugging {0}".format(category.slug))
        context_dict['category_name'] = category.name

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        pass

    return render(request , 'rango/category.html' , context_dict)