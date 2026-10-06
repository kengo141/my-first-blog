from django.contrib import admin
from .models import Post

# モデルをadminに登録
admin.site.register(Post)