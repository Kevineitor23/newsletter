from django.shortcuts import render

from django.views.generic import TemplateView

class DashboardHomeView(TemplateView):
    template_name='dashboard/index.html'
