from django.contrib import admin
from main import models

# Register your models here.
admin.site.register(models.Article)
admin.site.register(models.Author)
