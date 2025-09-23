from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from django.views import View


# Create your views here.
def main_view(request):
    response_data = render_to_string('main/main.html')
    return HttpResponse(response_data)


class MainView(View):
    def get (self, request):
        return render(request, 'main/main.html')
    template_name = "main.html"
