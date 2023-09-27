from django.contrib import admin
from .models import Post, Comment

# Models.pyと紐付け
admin.site.register(Post)
admin.site.register(Comment)

