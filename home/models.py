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
    ('Article', 'Article'),
    ('Essay', 'Essay'),
    ('Fiction', 'Fiction'),
    ('Interview', 'Interview'),
    ('News', 'News'),
    ('Review', 'Review'),
  ]
  sub_categories = [
    ('Book','Book'),
    ('Culture','Culture'),
    ('Documentary','Documentary'),
    ('Gender Studies', 'Gender Studies'),
    ('History','History'),
    ('International','International'),
    ('Literature','Literature'),
    ('Malabar','Malabar'),
    ('National','National'),
    ('Novel','Novel'),
    ('Philosophy','Philosophy'),
    ('Politics','Politics'),
    ('Religion','Religion'),
    ('Society','Society'),
    ('Story','Story'),
    ('Theology','Theology'),
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
    
