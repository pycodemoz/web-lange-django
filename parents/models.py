from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify



class Parent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
  name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)
  photo = models.ImageField(null=True, blank=True)
  birthday = models.DateField()
  slug = models.SlugField(unique=True, blank=True)
  posted_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    ordering = ['id']
    
  def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # ← Gera automaticamente
        super().save(*args, **kwargs)
  
  def __str__(self):
    return f"{self.name} {self.last_name}" 