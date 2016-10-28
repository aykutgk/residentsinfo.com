from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Search Engine will be implemented soon.")



def page(request, year):
    #a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': 'a_list'}
    return render(request, 'person/page.html', context)
