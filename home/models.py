from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class writing(models.Model):
  languages = [
    ('AR', 'Arabic'),
    ('EN', 'English'),
    ('ML', 'Malayalam'),
    ('UR', 'Urdu'),
  ]
  categories = [
    ('Article', 'Article'),
    ('Essay', 'Essay'),
    ('Fiction', 'Fiction'),
    ('Interview', 'Interview'),
    ('Islamic Studies', 'Islamic Studies'),
    ('Review', 'Review'),
    ('Series', 'Series'),
  ]
  sub_categories = [
    ('Art and Aesthetics','Art and Aesthetics'),
    ('Book','Book'),
    ('Documentary','Documentary'),
    ('Family','Family'),
    ('Fiqh','Fiqh'),
    ('Hadees','Hadees'),
    ('History and Culture','History and Culture'),
    ('History','History'),
    ('International','International'),
    ('Islamic History','Islamic History'),
    ('Islamic Jurisprudence','Islamic Jurisprudence'),
    ('Language and Literature','Language and Literature'),
    ('Malabar','Malabar'),
    ('Movie','Movie'),
    ('National','National'),
    ('Novel','Novel'),
    ('Politics','Politics'),
    ('Quran','Quran'),
    ('Quran and Hadees','Quran and Hadees'),
    ('Series 1','Series 1'),
    ('Series 2','Series 2'),
    ('Series 3','Series 3'),
    ('Series 4','Series 4'),
    ('Society','Society'),
    ('Society and Culture','Society and Culture'),
    ('Story','Story'),
    ('Theology and Philosophy','Theology and Philosophy'),
    ('Translation','Translation'),
    ('Women and Gender', 'Women and Gender'),
  ]


  article_active =[
    ('Yes','Yes'),
    ('No','No'),
  ]

  article_active = sub_category = models.CharField(default='Yes', max_length=3, choices=article_active)
  writer_id = models.IntegerField()
  heading = models.CharField(max_length=255)
  body = HTMLField()
  image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)
  category = models.CharField(default='', max_length=20, choices=categories)
  sub_category = models.CharField(default='', max_length=25, choices=sub_categories)
  language = models.CharField(max_length=2, choices=languages)
  publishing_date = models.DateField()
  address = models.TextField(default='')

  def __str__(self):
    return f"{self.writer_id} {self.publishing_date}"


class writer(models.Model):
  
    writer_id = models.IntegerField()
    writer_name = models.CharField(default='', max_length=255)
    
