from django.http import HttpResponse
from django.template import loader
from .models import writing

def heading_latest(request):
     latest_heading = writing.objects.all().order_by('-id').values_list('heading', flat=True)[:8]
     latest_image = writing.objects.all().order_by('-id').values_list('image', flat=True)[:8]
     latest_id = writing.objects.all().order_by('-id').values_list('id', flat=True)[:8]
     template = loader.get_template('home.html')
     context = {
          'latest_heading': latest_heading,
          'latest_image': latest_image,
          'latest_id': latest_id,
     }
     return HttpResponse(template.render(context, request))

def single_writing(request, id):
     single_write = writing.objects.get(id=id)
     template = loader.get_template('single_writing.html')
     context = {
          'single_write': single_write,
     }
     return HttpResponse(template.render(context, request))
     