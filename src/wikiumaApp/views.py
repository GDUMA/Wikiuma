from django.db.models import query
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Centro

# Create your views here.


class BasePageView(TemplateView):
    page_title = ""

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title

        return context


class HomeView(BasePageView):
    page_title = "Home"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["centros"] = Centro.objects.all()
        return context


class CentroView(ListView):
    model = Centro
    template_name = 'centros/centro_list.html'
    page_title = 'Centros😀'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        return context


class CentroDetailView(DetailView):
    model = Centro
    template_name = 'centros/centro_detail.html'
    page_title = 'Centros😀'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        return context
