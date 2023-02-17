from django.db import models

class Language(models.Model):
   language  = models.CharField(max_length=100)

   def __repr__(self):
      return f"language:{self.language}"

class Country(models.Model):
   country  = models.CharField(max_length=100)
   languages = models.ManyToManyField(to=Language)

   def __repr__(self):
      return f"country:{self.country}"
