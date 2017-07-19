from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main/main_index.html'


main_view = MainView.as_view()
