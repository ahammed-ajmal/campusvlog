from django.http import HttpResponse
from django.shortcuts import render
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

     # category for main page
     article_religion_id = writing.objects.filter(category="Article", sub_category="Religion").order_by('-id').values_list('id', flat=True)
     article_religion_heading = writing.objects.filter(category="Article", sub_category="Religion" ).order_by('-id').values_list('heading', flat=True)
     article_religion_image = writing.objects.filter(category="Article", sub_category="Religion").order_by('-id').values_list('image', flat=True)
     article_religion_sub_category = writing.objects.filter(category="Article", sub_category="Religion").order_by('-id').values_list('sub_category', flat=True)
     article_religion_publishing_date = writing.objects.filter(category="Article", sub_category="Religion").order_by('-id').values_list('publishing_date', flat=True)

     article_culture_id = writing.objects.filter(category="Article", sub_category="Culture").order_by('-id').values_list('id', flat=True)
     article_culture_heading = writing.objects.filter(category="Article", sub_category="Culture").order_by('-id').values_list('heading', flat=True)
     article_culture_image = writing.objects.filter(category="Article", sub_category="Culture").order_by('-id').values_list('image', flat=True)
     article_culture_sub_category = writing.objects.filter(category="Article", sub_category="Culture").order_by('-id').values_list('sub_category', flat=True)
     article_culture_publishing_date = writing.objects.filter(category="Article", sub_category="Culture").order_by('-id').values_list('publishing_date', flat=True)

     article_society_id = writing.objects.filter(category="Article", sub_category="Society").order_by('-id').values_list('id', flat=True)
     article_society_heading = writing.objects.filter(category="Article", sub_category="Society" ).order_by('-id').values_list('heading', flat=True)
     article_society_image = writing.objects.filter(category="Article", sub_category="Society").order_by('-id').values_list('image', flat=True)
     article_society_sub_category = writing.objects.filter(category="Article", sub_category="Society").order_by('-id').values_list('sub_category', flat=True)
     article_society_publishing_date = writing.objects.filter(category="Article", sub_category="Society").order_by('-id').values_list('publishing_date', flat=True)

     review_book_id = writing.objects.filter(category="Review", sub_category="Book").order_by('-id').values_list('id', flat=True)
     review_book_heading = writing.objects.filter(category="Review", sub_category="Book" ).order_by('-id').values_list('heading', flat=True)
     review_book_image = writing.objects.filter(category="Review", sub_category="Book").order_by('-id').values_list('image', flat=True)
     review_book_sub_category = writing.objects.filter(category="Review", sub_category="Book").order_by('-id').values_list('sub_category', flat=True)
     review_book_publishing_date = writing.objects.filter(category="Review", sub_category="Book").order_by('-id').values_list('publishing_date', flat=True)

     review_documentary_id = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-id').values_list('id', flat=True)
     review_documentary_heading = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-id').values_list('heading', flat=True)
     review_documentary_image = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-id').values_list('image', flat=True)
     review_documentary_sub_category = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-id').values_list('sub_category', flat=True)
     review_documentary_publishing_date = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-id').values_list('publishing_date', flat=True)

     review_movie_id = writing.objects.filter(category="Review", sub_category="Movie").order_by('-id').values_list('id', flat=True)
     review_movie_heading = writing.objects.filter(category="Review", sub_category="Movie" ).order_by('-id').values_list('heading', flat=True)
     review_movie_image = writing.objects.filter(category="Review", sub_category="Movie").order_by('-id').values_list('image', flat=True)
     review_movie_sub_category = writing.objects.filter(category="Review", sub_category="Movie").order_by('-id').values_list('sub_category', flat=True)
     review_movie_publishing_date = writing.objects.filter(category="Review", sub_category="Movie").order_by('-id').values_list('publishing_date', flat=True)


     # template = loader.get_template('home.html')
     context = {
          'latest_heading': latest_heading,
          'latest_image': latest_image,
          'latest_id': latest_id,
          'random_heading': random_heading,
          'article_religion_id': article_religion_id,
          'article_religion_heading': article_religion_heading,
          'article_religion_image' : article_religion_image,
          'article_religion_sub_category' : article_religion_sub_category,
          'article_religion_publishing_date' : article_religion_publishing_date,
          'article_culture_id': article_culture_id,
          'article_culture_heading': article_culture_heading,
          'article_culture_image' : article_culture_image,
          'article_culture_sub_category' : article_culture_sub_category,
          'article_culture_publishing_date' : article_culture_publishing_date,
          'article_society_id': article_society_id,
          'article_society_heading': article_society_heading,
          'article_society_image' : article_society_image,
          'article_society_sub_category' : article_society_sub_category,
          'article_society_publishing_date' : article_society_publishing_date,
          'review_book_id': review_book_id,
          'review_book_heading': review_book_heading,
          'review_book_image' : review_book_image,
          'review_book_sub_category' : review_book_sub_category,
          'review_book_publishing_date' : review_book_publishing_date,
          'review_documentary_id': review_documentary_id,
          'review_documentary_heading': review_documentary_heading,
          'review_documentary_image' : article_society_image,
          'review_documentary_sub_category' : article_society_sub_category,
          'review_documentary_publishing_date' : article_society_publishing_date,
          'review_movie_id': review_movie_id,
          'review_movie_heading': review_movie_heading,
          'review_movie_image' : review_movie_image,
          'review_movie_sub_category' : review_movie_sub_category,
          'review_movie_publishing_date' : review_movie_publishing_date,
     }
     # return HttpResponse(template.render(context, request))
     return render(request, ['home.html', 'master.html'], context)



def single_writing(request, id):
     single_write = writing.objects.get(id=id)
     template = loader.get_template('single_writing.html')
     context = {
          'single_write': single_write,
     }
     return HttpResponse(template.render(context, request))
     