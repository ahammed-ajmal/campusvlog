from django.db import models

# Create your models here.
class writing(models.Model):
  languages = [
    ('AR', 'Arabic'),
    ('EN', 'English'),
    ('ML', 'Malayalam'),
    ('UR', 'Urdu'),
  ]
  categories = [
    ('Aqeeda', 'Aqeeda'),
    ('Fiqh', 'Fiqh'),
    ('History', 'History'),
    ('Interview', 'Interview'),
    ('KvS', 'KvS'),
    ('Language', 'Language'),
    ('Psychology', 'Psychology'),
    ('Politics', 'Politics'),
  ]
  sub_categories = [
    ('Aqeeda_01', 'Genderstudies'),
    ('Aqeeda_02', 'philosophy'),
    ('Aqeeda_03', 'Science'),
    ('Aqeeda_04', 'Sufism'),
    ('Aqeeda_05', 'Theology'),
    ('Fiqh_01', 'Fiqhulaqalliyyath'),
    ('Fiqh_02	', 'Madhab'),
    ('Fiqh_03', 'Maqsid'),
    ('Fiqh_04', 'Modernfiqh'),
    ('Fiqh_05', 'Sex/Health/Family'),
    ('Fiqh_06', 'UsoolulFiqh'),
    ('History_01', 'Culture'),
    ('History_02', 'IslamicHistory'),
    ('History_03', 'Malabar'),
    ('History_04', 'Sociology'),
    ('KvS_01', 'Hadees'),
    ('KvS_02', 'IhjazulQuran'),
    ('KvS_03', 'Quran'),
    ('KvS_04', 'Uloomulquran'),
    ('Language_01', 'BookReview'),
    ('Language_02', 'Cinema  Review'),
    ('Language_03', 'Documentary Review'),
    ('Language_04', 'Fiqhulluga'),
    ('Language_05', 'Lahja'),
    ('Language_06', 'Rateric'),
    ('Language_07', 'Translation'),
    ('Politics_01', 'Indian'),
    ('Politics_02', 'International'),
    ('Politics_03', 'Kerala'),
  ]
  writer_id = models.IntegerField()
  heading = models.CharField(max_length=255)
  body = models.TextField()
  image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)
  category = models.CharField(default='', max_length=10, choices=categories)
  sub_category = models.CharField(default='', max_length=25, choices=sub_categories)
  language = models.CharField(max_length=2, choices=languages)
  publishing_date = models.DateField()
  address = models.TextField(default='')

  def __str__(self):
    return f"{self.writer_id} {self.publishing_date}"


class writer(models.Model):
  
    writer_id = models.IntegerField()
    writer_name = models.CharField(default='', max_length=255)
    
