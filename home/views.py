from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import writing
import random

latest_heading = writing.objects.all().order_by('-writer_id').values_list('heading', flat=True)[:8]
latest_image = writing.objects.all().order_by('-writer_id').values_list('image', flat=True)[:8]
latest_id = writing.objects.all().order_by('-writer_id').values_list('writer_id', flat=True)[:8]

# random writing for navigation
headings = writing.objects.all().values_list('heading', flat=True)
images = writing.objects.all().values_list('image', flat=True)
categories = writing.objects.all().values_list('category', flat=True)

random_indices = random.sample(range(len(headings)), 4)
random_heading = [headings[i] for i in random_indices]
random_image = [images[i] for i in random_indices]
random_category = [categories[i] for i in random_indices]

# category for main page
# islamic studies quran
islamic_quran_id = writing.objects.filter(category="Islamic Studies", sub_category="Quran").order_by('-writer_id').values_list('writer_id', flat=True)
islamic_quran_heading = writing.objects.filter(category="Islamic Studies", sub_category="Quran" ).order_by('-writer_id').values_list('heading', flat=True)
islamic_quran_image = writing.objects.filter(category="Islamic Studies", sub_category="Quran").order_by('-writer_id').values_list('image', flat=True)
islamic_quran_sub_category = writing.objects.filter(category="Islamic Studies", sub_category="Quran").order_by('-writer_id').values_list('sub_category', flat=True)
islamic_quran_publishing_date = writing.objects.filter(category="Islamic Studies", sub_category="Quran").order_by('-writer_id').values_list('publishing_date', flat=True)
# islamic studies hadees
islamic_hadees_id = writing.objects.filter(category="Islamic Studies", sub_category="Hadees").order_by('-writer_id').values_list('writer_id', flat=True)
islamic_hadees_heading = writing.objects.filter(category="Islamic Studies", sub_category="Hadees" ).order_by('-writer_id').values_list('heading', flat=True)
islamic_hadees_image = writing.objects.filter(category="Islamic Studies", sub_category="Hadees").order_by('-writer_id').values_list('image', flat=True)
islamic_hadees_sub_category = writing.objects.filter(category="Islamic Studies", sub_category="Hadees").order_by('-writer_id').values_list('sub_category', flat=True)
islamic_hadees_publishing_date = writing.objects.filter(category="Islamic Studies", sub_category="Hadees").order_by('-writer_id').values_list('publishing_date', flat=True)
# islamic studies theology and philosophy
islamic_theology_id = writing.objects.filter(category="Islamic Studies", sub_category="Theology and Philosophy").order_by('-writer_id').values_list('writer_id', flat=True)
islamic_theology_heading = writing.objects.filter(category="Islamic Studies", sub_category="Theology and Philosophy" ).order_by('-writer_id').values_list('heading', flat=True)
islamic_theology_image = writing.objects.filter(category="Islamic Studies", sub_category="Theology and Philosophy").order_by('-writer_id').values_list('image', flat=True)
islamic_theology_sub_category = writing.objects.filter(category="Islamic Studies", sub_category="Theology and Philosophy").order_by('-writer_id').values_list('sub_category', flat=True)
islamic_theology_publishing_date = writing.objects.filter(category="Islamic Studies", sub_category="Theology and Philosophy").order_by('-writer_id').values_list('publishing_date', flat=True)
# islamic studies fiqh
islamic_fiqh_id = writing.objects.filter(category="Islamic Studies", sub_category="Fiqh").order_by('-writer_id').values_list('writer_id', flat=True)
islamic_fiqh_heading = writing.objects.filter(category="Islamic Studies", sub_category="Fiqh" ).order_by('-writer_id').values_list('heading', flat=True)
islamic_fiqh_image = writing.objects.filter(category="Islamic Studies", sub_category="Fiqh").order_by('-writer_id').values_list('image', flat=True)
islamic_fiqh_sub_category = writing.objects.filter(category="Islamic Studies", sub_category="Fiqh").order_by('-writer_id').values_list('sub_category', flat=True)
islamic_fiqh_publishing_date = writing.objects.filter(category="Islamic Studies", sub_category="Fiqh").order_by('-writer_id').values_list('publishing_date', flat=True)
# islamic studies family
islamic_family_id = writing.objects.filter(category="Islamic Studies", sub_category="Family").order_by('-writer_id').values_list('writer_id', flat=True)
islamic_family_heading = writing.objects.filter(category="Islamic Studies", sub_category="Family" ).order_by('-writer_id').values_list('heading', flat=True)
islamic_family_image = writing.objects.filter(category="Islamic Studies", sub_category="Family").order_by('-writer_id').values_list('image', flat=True)
islamic_family_sub_category = writing.objects.filter(category="Islamic Studies", sub_category="Family").order_by('-writer_id').values_list('sub_category', flat=True)
islamic_family_publishing_date = writing.objects.filter(category="Islamic Studies", sub_category="Family").order_by('-writer_id').values_list('publishing_date', flat=True)

# article - history and culture
article_history_and_culture_id = writing.objects.filter(category="Article", sub_category="History and Culture").order_by('-writer_id').values_list('writer_id', flat=True)
article_history_and_culture_heading = writing.objects.filter(category="Article", sub_category="History and Culture" ).order_by('-writer_id').values_list('heading', flat=True)
article_history_and_culture_image = writing.objects.filter(category="Article", sub_category="History and Culture").order_by('-writer_id').values_list('image', flat=True)
article_history_and_culture_sub_category = writing.objects.filter(category="Article", sub_category="History and Culture").order_by('-writer_id').values_list('sub_category', flat=True)
article_history_and_culture_publishing_date = writing.objects.filter(category="Article", sub_category="History and Culture").order_by('-writer_id').values_list('publishing_date', flat=True)
# article - language and literature
article_language_and_literature_id = writing.objects.filter(category="Article", sub_category="Language and Literature").order_by('-writer_id').values_list('writer_id', flat=True)
article_language_and_literature_heading = writing.objects.filter(category="Article", sub_category="Language and Literature" ).order_by('-writer_id').values_list('heading', flat=True)
article_language_and_literature_image = writing.objects.filter(category="Article", sub_category="Language and Literature").order_by('-writer_id').values_list('image', flat=True)
article_language_and_literature_sub_category = writing.objects.filter(category="Article", sub_category="Language and Literature").order_by('-writer_id').values_list('sub_category', flat=True)
article_language_and_literature_publishing_date = writing.objects.filter(category="Article", sub_category="Language and Literature").order_by('-writer_id').values_list('publishing_date', flat=True)
# article - women and gender
article_women_and_gender_id = writing.objects.filter(category="Article", sub_category="Women and Gender").order_by('-writer_id').values_list('writer_id', flat=True)
article_women_and_gender_heading = writing.objects.filter(category="Article", sub_category="Women and Gender" ).order_by('-writer_id').values_list('heading', flat=True)
article_women_and_gender_image = writing.objects.filter(category="Article", sub_category="Women and Gender").order_by('-writer_id').values_list('image', flat=True)
article_women_and_gender_sub_category = writing.objects.filter(category="Article", sub_category="Women and Gender").order_by('-writer_id').values_list('sub_category', flat=True)
article_women_and_gender_publishing_date = writing.objects.filter(category="Article", sub_category="Women and Gender").order_by('-writer_id').values_list('publishing_date', flat=True)
# article - malabar
article_malabar_id = writing.objects.filter(category="Article", sub_category="Malabar").order_by('-writer_id').values_list('writer_id', flat=True)
article_malabar_heading = writing.objects.filter(category="Article", sub_category="Malabar" ).order_by('-writer_id').values_list('heading', flat=True)
article_malabar_image = writing.objects.filter(category="Article", sub_category="Malabar").order_by('-writer_id').values_list('image', flat=True)
article_malabar_sub_category = writing.objects.filter(category="Article", sub_category="Malabar").order_by('-writer_id').values_list('sub_category', flat=True)
article_malabar_publishing_date = writing.objects.filter(category="Article", sub_category="Malabar").order_by('-writer_id').values_list('publishing_date', flat=True)
# article - art and aesthetic
article_art_and_aesthetic_id = writing.objects.filter(category="Article", sub_category="Art and Aesthetics").order_by('-writer_id').values_list('writer_id', flat=True)
article_art_and_aesthetic_heading = writing.objects.filter(category="Article", sub_category="Art and Aesthetics" ).order_by('-writer_id').values_list('heading', flat=True)
article_art_and_aesthetic_image = writing.objects.filter(category="Article", sub_category="Art and Aesthetics").order_by('-writer_id').values_list('image', flat=True)
article_art_and_aesthetic_sub_category = writing.objects.filter(category="Article", sub_category="Art and Aesthetics").order_by('-writer_id').values_list('sub_category', flat=True)
article_art_and_aesthetic_publishing_date = writing.objects.filter(category="Article", sub_category="Art and Aesthetics").order_by('-writer_id').values_list('publishing_date', flat=True)
# article - politics
article_politics_id = writing.objects.filter(category="Article", sub_category="Politics").order_by('-writer_id').values_list('writer_id', flat=True)
article_politics_heading = writing.objects.filter(category="Article", sub_category="Politics" ).order_by('-writer_id').values_list('heading', flat=True)
article_politics_image = writing.objects.filter(category="Article", sub_category="Politics").order_by('-writer_id').values_list('image', flat=True)
article_politics_sub_category = writing.objects.filter(category="Article", sub_category="Politics").order_by('-writer_id').values_list('sub_category', flat=True)
article_politics_publishing_date = writing.objects.filter(category="Article", sub_category="Politics").order_by('-writer_id').values_list('publishing_date', flat=True)
# article - international
article_international_id = writing.objects.filter(category="Article", sub_category="International").order_by('-writer_id').values_list('writer_id', flat=True)
article_international_heading = writing.objects.filter(category="Article", sub_category="International" ).order_by('-writer_id').values_list('heading', flat=True)
article_international_image = writing.objects.filter(category="Article", sub_category="International").order_by('-writer_id').values_list('image', flat=True)
article_international_sub_category = writing.objects.filter(category="Article", sub_category="International").order_by('-writer_id').values_list('sub_category', flat=True)
article_international_publishing_date = writing.objects.filter(category="Article", sub_category="International").order_by('-writer_id').values_list('publishing_date', flat=True)

# review - book
review_book_id = writing.objects.filter(category="Review", sub_category="Book").order_by('-writer_id').values_list('writer_id', flat=True)
review_book_heading = writing.objects.filter(category="Review", sub_category="Book" ).order_by('-writer_id').values_list('heading', flat=True)
review_book_image = writing.objects.filter(category="Review", sub_category="Book").order_by('-writer_id').values_list('image', flat=True)
review_book_sub_category = writing.objects.filter(category="Review", sub_category="Book").order_by('-writer_id').values_list('sub_category', flat=True)
review_book_publishing_date = writing.objects.filter(category="Review", sub_category="Book").order_by('-writer_id').values_list('publishing_date', flat=True)
# review - documentary
review_documentary_id = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-writer_id').values_list('writer_id', flat=True)
review_documentary_heading = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-writer_id').values_list('heading', flat=True)
review_documentary_image = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-writer_id').values_list('image', flat=True)
review_documentary_sub_category = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-writer_id').values_list('sub_category', flat=True)
review_documentary_publishing_date = writing.objects.filter(category="Review", sub_category="Documentary").order_by('-writer_id').values_list('publishing_date', flat=True)
# review - movie
review_movie_id = writing.objects.filter(category="Review", sub_category="Movie").order_by('-writer_id').values_list('writer_id', flat=True)
review_movie_heading = writing.objects.filter(category="Review", sub_category="Movie" ).order_by('-writer_id').values_list('heading', flat=True)
review_movie_image = writing.objects.filter(category="Review", sub_category="Movie").order_by('-writer_id').values_list('image', flat=True)
review_movie_sub_category = writing.objects.filter(category="Review", sub_category="Movie").order_by('-writer_id').values_list('sub_category', flat=True)
review_movie_publishing_date = writing.objects.filter(category="Review", sub_category="Movie").order_by('-writer_id').values_list('publishing_date', flat=True)

# series - translation
series_translation_id = writing.objects.filter(category="Series", sub_category="Translation").order_by('-writer_id').values_list('writer_id', flat=True)
series_translation_heading = writing.objects.filter(category="Series", sub_category="Translation" ).order_by('-writer_id').values_list('heading', flat=True)
series_translation_image = writing.objects.filter(category="Series", sub_category="Translation").order_by('-writer_id').values_list('image', flat=True)
series_translation_sub_category = writing.objects.filter(category="Series", sub_category="Translation").order_by('-writer_id').values_list('sub_category', flat=True)
series_translation_publishing_date = writing.objects.filter(category="Series", sub_category="Translation").order_by('-writer_id').values_list('publishing_date', flat=True)

# series - series 1
series_1_id = writing.objects.filter(category="Series", sub_category="Series 1").order_by('-writer_id').values_list('writer_id', flat=True)
series_1_heading = writing.objects.filter(category="Series", sub_category="Series 1" ).order_by('-writer_id').values_list('heading', flat=True)
series_1_image = writing.objects.filter(category="Series", sub_category="Series 1").order_by('-writer_id').values_list('image', flat=True)
series_1_sub_category = writing.objects.filter(category="Series", sub_category="Series 1").order_by('-writer_id').values_list('sub_category', flat=True)
series_1_publishing_date = writing.objects.filter(category="Series", sub_category="Series 1").order_by('-writer_id').values_list('publishing_date', flat=True)

# series - series 2
series_2_id = writing.objects.filter(category="Series", sub_category="Series 2").order_by('-writer_id').values_list('writer_id', flat=True)
series_2_heading = writing.objects.filter(category="Series", sub_category="Series 2" ).order_by('-writer_id').values_list('heading', flat=True)
series_2_image = writing.objects.filter(category="Series", sub_category="Series 2").order_by('-writer_id').values_list('image', flat=True)
series_2_sub_category = writing.objects.filter(category="Series", sub_category="Series 2").order_by('-writer_id').values_list('sub_category', flat=True)
series_2_publishing_date = writing.objects.filter(category="Series", sub_category="Series 2").order_by('-writer_id').values_list('publishing_date', flat=True)

# series - series 3
series_3_id = writing.objects.filter(category="Series", sub_category="Series 3").order_by('-writer_id').values_list('writer_id', flat=True)
series_3_heading = writing.objects.filter(category="Series", sub_category="Series 3" ).order_by('-writer_id').values_list('heading', flat=True)
series_3_image = writing.objects.filter(category="Series", sub_category="Series 3").order_by('-writer_id').values_list('image', flat=True)
series_3_sub_category = writing.objects.filter(category="Series", sub_category="Series 3").order_by('-writer_id').values_list('sub_category', flat=True)
series_3_publishing_date = writing.objects.filter(category="Series", sub_category="Series 3").order_by('-writer_id').values_list('publishing_date', flat=True)

# series - series 4
series_4_id = writing.objects.filter(category="Series", sub_category="Series 4").order_by('-writer_id').values_list('writer_id', flat=True)
series_4_heading = writing.objects.filter(category="Series", sub_category="Series 4" ).order_by('-writer_id').values_list('heading', flat=True)
series_4_image = writing.objects.filter(category="Series", sub_category="Series 4").order_by('-writer_id').values_list('image', flat=True)
series_4_sub_category = writing.objects.filter(category="Series", sub_category="Series 4").order_by('-writer_id').values_list('sub_category', flat=True)
series_4_publishing_date = writing.objects.filter(category="Series", sub_category="Series 4").order_by('-writer_id').values_list('publishing_date', flat=True)




def heading_latest(request):
     context = {
          'latest_heading': latest_heading,
          'latest_image': latest_image,
          'latest_id': latest_id,
          'random_heading': random_heading,
          'islamic_quran_id' : islamic_quran_id,
          'islamic_quran_heading' : islamic_quran_heading,
          'islamic_quran_image' : islamic_quran_image,
          'islamic_quran_sub_category' : islamic_quran_sub_category,
          'islamic_quran_publishing_date' : islamic_quran_publishing_date,
          'islamic_hadees_id' : islamic_hadees_id,
          'islamic_hadees_heading' : islamic_hadees_heading,
          'islamic_hadees_image' : islamic_hadees_image,
          'islamic_hadees_sub_category' : islamic_hadees_sub_category,
          'islamic_hadees_publishing_date' : islamic_hadees_publishing_date,
          'islamic_theology_id' : islamic_theology_id,
          'islamic_theology_heading' : islamic_theology_heading,
          'islamic_theology_image' : islamic_theology_image,
          'islamic_theology_sub_category' : islamic_theology_sub_category,
          'islamic_theology_publishing_date' : islamic_theology_publishing_date,
          'islamic_fiqh_id' : islamic_fiqh_id,
          'islamic_fiqh_heading' : islamic_fiqh_heading,
          'islamic_fiqh_image' : islamic_fiqh_image,
          'islamic_fiqh_sub_category' : islamic_fiqh_sub_category,
          'islamic_fiqh_publishing_date' : islamic_fiqh_publishing_date,
          'islamic_family_id' : islamic_family_id,
          'islamic_family_heading' : islamic_family_heading,
          'islamic_family_image' : islamic_family_image,
          'islamic_family_sub_category' : islamic_family_sub_category,
          'islamic_family_publishing_date' : islamic_family_publishing_date,
          'article_history_and_culture_id' : article_history_and_culture_id,
          'article_history_and_culture_heading' : article_history_and_culture_heading,
          'article_history_and_culture_image' : article_history_and_culture_image,
          'article_history_and_culture_sub_category' : article_history_and_culture_sub_category,
          'article_history_and_culture_publishing_date' : article_history_and_culture_publishing_date,
          'article_language_and_literature_id' : article_language_and_literature_id,
          'article_language_and_literature_heading' : article_language_and_literature_heading,
          'article_language_and_literature_image' : article_language_and_literature_image,
          'article_language_and_literature_sub_category' : article_language_and_literature_sub_category,
          'article_language_and_literature_publishing_date' : article_language_and_literature_publishing_date,
          'article_women_and_gender_id' : article_women_and_gender_id,
          'article_women_and_gender_heading' : article_women_and_gender_heading,
          'article_women_and_gender_image' : article_women_and_gender_image,
          'article_women_and_gender_sub_category' : article_women_and_gender_sub_category,
          'article_women_and_gender_publishing_date' : article_women_and_gender_publishing_date,
          'article_malabar_id' : article_malabar_id,
          'article_malabar_heading' : article_malabar_heading,
          'article_malabar_image' : article_malabar_image,
          'article_malabar_sub_category' : article_malabar_sub_category,
          'article_malabar_publishing_date' : article_malabar_publishing_date,
          'article_art_and_aesthetic_id' : article_art_and_aesthetic_id,
          'article_art_and_aesthetic_heading' : article_art_and_aesthetic_heading,
          'article_art_and_aesthetic_image' : article_art_and_aesthetic_image,
          'article_art_and_aesthetic_sub_category' : article_art_and_aesthetic_sub_category,
          'article_art_and_aesthetic_publishing_date' : article_art_and_aesthetic_publishing_date,
          'article_politics_id' : article_politics_id,
          'article_politics_heading' : article_politics_heading,
          'article_politics_image' : article_politics_image,
          'article_politics_sub_category' : article_politics_sub_category,
          'article_politics_publishing_date' : article_politics_publishing_date,
          'article_international_id' : article_international_id,
          'article_international_heading' : article_international_heading,
          'article_international_image' : article_international_image,
          'article_international_sub_category' : article_international_sub_category,
          'article_international_publishing_date' : article_international_publishing_date,
          'review_book_id': review_book_id,
          'review_book_heading': review_book_heading,
          'review_book_image' : review_book_image,
          'review_book_sub_category' : review_book_sub_category,
          'review_book_publishing_date' : review_book_publishing_date,
          'review_documentary_id': review_documentary_id,
          'review_documentary_heading': review_documentary_heading,
          'review_documentary_image' : review_documentary_image,
          'review_documentary_sub_category' : review_documentary_sub_category,
          'review_documentary_publishing_date' : review_documentary_publishing_date,
          'review_movie_id': review_movie_id,
          'review_movie_heading': review_movie_heading,
          'review_movie_image' : review_movie_image,
          'review_movie_sub_category' : review_movie_sub_category,
          'review_movie_publishing_date' : review_movie_publishing_date,
          'series_1_heading' : series_1_heading,
          'series_1_id' : series_1_id,
          'series_1_image' : series_1_image,
          'series_1_publishing_date' : series_1_publishing_date,
          'series_1_sub_category' : series_1_sub_category,
          'series_2_heading' : series_2_heading,
          'series_2_id' : series_2_id,
          'series_2_image' : series_2_image,
          'series_2_publishing_date' : series_2_publishing_date,
          'series_2_sub_category' : series_2_sub_category,
          'series_3_heading' : series_3_heading,
          'series_3_id' : series_3_id,
          'series_3_image' : series_3_image,
          'series_3_publishing_date' : series_3_publishing_date,
          'series_3_sub_category' : series_3_sub_category,
          'series_4_heading' : series_4_heading,
          'series_4_id' : series_4_id,
          'series_4_image' : series_4_image,
          'series_4_publishing_date' : series_4_publishing_date,
          'series_4_sub_category' : series_4_sub_category,
          'series_translation_heading' : series_translation_heading,
          'series_translation_id' : series_translation_id,
          'series_translation_image' : series_translation_image,
          'series_translation_publishing_date' : series_translation_publishing_date,
          'series_translation_sub_category' : series_translation_sub_category,

     }
     return render(request, ['home.html', 'master.html'], context)

def single_writing(request, writer_id):
     single_write = writing.objects.get(writer_id=writer_id)
     context = {
          'single_write': single_write,
          'latest_heading': latest_heading,
          'latest_image': latest_image,
          'latest_id': latest_id,
          'random_heading': random_heading,
          'islamic_quran_id' : islamic_quran_id,
          'islamic_quran_heading' : islamic_quran_heading,
          'islamic_quran_image' : islamic_quran_image,
          'islamic_quran_sub_category' : islamic_quran_sub_category,
          'islamic_quran_publishing_date' : islamic_quran_publishing_date,
          'islamic_hadees_id' : islamic_hadees_id,
          'islamic_hadees_heading' : islamic_hadees_heading,
          'islamic_hadees_image' : islamic_hadees_image,
          'islamic_hadees_sub_category' : islamic_hadees_sub_category,
          'islamic_hadees_publishing_date' : islamic_hadees_publishing_date,
          'islamic_theology_id' : islamic_theology_id,
          'islamic_theology_heading' : islamic_theology_heading,
          'islamic_theology_image' : islamic_theology_image,
          'islamic_theology_sub_category' : islamic_theology_sub_category,
          'islamic_theology_publishing_date' : islamic_theology_publishing_date,
          'islamic_fiqh_id' : islamic_fiqh_id,
          'islamic_fiqh_heading' : islamic_fiqh_heading,
          'islamic_fiqh_image' : islamic_fiqh_image,
          'islamic_fiqh_sub_category' : islamic_fiqh_sub_category,
          'islamic_fiqh_publishing_date' : islamic_fiqh_publishing_date,
          'islamic_family_id' : islamic_family_id,
          'islamic_family_heading' : islamic_family_heading,
          'islamic_family_image' : islamic_family_image,
          'islamic_family_sub_category' : islamic_family_sub_category,
          'islamic_family_publishing_date' : islamic_family_publishing_date,
          'article_history_and_culture_id' : article_history_and_culture_id,
          'article_history_and_culture_heading' : article_history_and_culture_heading,
          'article_history_and_culture_image' : article_history_and_culture_image,
          'article_history_and_culture_sub_category' : article_history_and_culture_sub_category,
          'article_history_and_culture_publishing_date' : article_history_and_culture_publishing_date,
          'article_language_and_literature_id' : article_language_and_literature_id,
          'article_language_and_literature_heading' : article_language_and_literature_heading,
          'article_language_and_literature_image' : article_language_and_literature_image,
          'article_language_and_literature_sub_category' : article_language_and_literature_sub_category,
          'article_language_and_literature_publishing_date' : article_language_and_literature_publishing_date,
          'article_women_and_gender_id' : article_women_and_gender_id,
          'article_women_and_gender_heading' : article_women_and_gender_heading,
          'article_women_and_gender_image' : article_women_and_gender_image,
          'article_women_and_gender_sub_category' : article_women_and_gender_sub_category,
          'article_women_and_gender_publishing_date' : article_women_and_gender_publishing_date,
          'article_malabar_id' : article_malabar_id,
          'article_malabar_heading' : article_malabar_heading,
          'article_malabar_image' : article_malabar_image,
          'article_malabar_sub_category' : article_malabar_sub_category,
          'article_malabar_publishing_date' : article_malabar_publishing_date,
          'article_art_and_aesthetic_id' : article_art_and_aesthetic_id,
          'article_art_and_aesthetic_heading' : article_art_and_aesthetic_heading,
          'article_art_and_aesthetic_image' : article_art_and_aesthetic_image,
          'article_art_and_aesthetic_sub_category' : article_art_and_aesthetic_sub_category,
          'article_art_and_aesthetic_publishing_date' : article_art_and_aesthetic_publishing_date,
          'article_politics_id' : article_politics_id,
          'article_politics_heading' : article_politics_heading,
          'article_politics_image' : article_politics_image,
          'article_politics_sub_category' : article_politics_sub_category,
          'article_politics_publishing_date' : article_politics_publishing_date,
          'article_international_id' : article_international_id,
          'article_international_heading' : article_international_heading,
          'article_international_image' : article_international_image,
          'article_international_sub_category' : article_international_sub_category,
          'article_international_publishing_date' : article_international_publishing_date,
          'review_book_id': review_book_id,
          'review_book_heading': review_book_heading,
          'review_book_image' : review_book_image,
          'review_book_sub_category' : review_book_sub_category,
          'review_book_publishing_date' : review_book_publishing_date,
          'review_documentary_id': review_documentary_id,
          'review_documentary_heading': review_documentary_heading,
          'review_documentary_image' : review_documentary_image,
          'review_documentary_sub_category' : review_documentary_sub_category,
          'review_documentary_publishing_date' : review_documentary_publishing_date,
          'review_movie_id': review_movie_id,
          'review_movie_heading': review_movie_heading,
          'review_movie_image' : review_movie_image,
          'review_movie_sub_category' : review_movie_sub_category,
          'review_movie_publishing_date' : review_movie_publishing_date,
     }
     return render(request, ['single_writing.html', 'master.html'], context)

def category(request):
     total_id = writing.objects.all().order_by('-writer_id').values_list('writer_id', flat=True)
     
     all_content = []

     for x in total_id:
          a = x-1
          heading = writing.objects.all().values_list('heading', flat=True)[a]
          image = writing.objects.all().values_list('image', flat=True)[a]
          publishing_date = writing.objects.all().values_list('publishing_date', flat=True)[a]
          
          current_dict= {'heading': heading, 'image': image, 'publishing_date':publishing_date}
          all_content.append(current_dict)
     

     context={
          'all_content':all_content,
          'total_id': total_id,
     }
     return render(request, ['category.html', 'master.html'],context)



