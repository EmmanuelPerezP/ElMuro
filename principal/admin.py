from django.contrib import admin
from .models import Post, Comment, HeaderImage

admin.site.register(Post)
admin.site.register(HeaderImage)
admin.site.register(Comment)
