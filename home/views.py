from django.http import HttpResponse
from django.template import loader
from .models import writing
import random

def heading_latest(request):
     latest_heading = writing.objects.all().order_by('-id').values_list('heading', flat=True)[:8]
     latest_image = writing.objects.all().order_by('-id').values_list('image', flat=True)[:8]
     latest_id = writing.objects.all().order_by('-id').values_list('id', flat=True)[:8]
     
     # random writing for navigation
     headings = writing.objects.all().values_list('heading', flat=True)
     images = writing.objects.all().values_list('image', flat=True)
     categories = writing.objects.all().values_list('category', flat=True)
     
     random_indices = random.sample(range(len(headings)), 4)
     random_heading = [headings[i] for i in random_indices]
     random_image = [images[i] for i in random_indices]
     random_category = [categories[i] for i in random_indices]


     template = loader.get_template('home.html')
     context = {
          'latest_heading': latest_heading,
          'latest_image': latest_image,
          'latest_id': latest_id,
          'random_heading': random_heading,
     }
     return HttpResponse(template.render(context, request))

def single_writing(request, id):
     single_write = writing.objects.get(id=id)
     template = loader.get_template('single_writing.html')
     context = {
          'single_write': single_write,
     }
     return HttpResponse(template.render(context, request))
     