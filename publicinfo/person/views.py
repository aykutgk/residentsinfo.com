from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, ListView

from .models import Page, Person


def index(request):
    return HttpResponse("Search Engine will be implemented soon.")

class PageListView(ListView):
    model = Page


class PageDetailView(DetailView):
    model = Page
    template_name = 'person/page.html'
