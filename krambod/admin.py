from django.contrib import admin
from krambod.models import Article, Information, Photo, PhotoTag

# Register your models here.

admin.site.register(Article)
admin.site.register(Information)
admin.site.register(Photo)
admin.site.register(PhotoTag)
