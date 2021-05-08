from django.shortcuts import render
from django.views.generic import TemplateView

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

