from django.contrib import admin
from .models import Post, PostImage, Comments

# Register your models here.


admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comments)