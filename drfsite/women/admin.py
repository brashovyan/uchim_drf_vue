from django.contrib import admin
from .models import Category, Women
from django.contrib.auth import get_user_model
User = get_user_model()
from markdownx.admin import MarkdownxModelAdmin


admin.site.register(Category)
admin.site.register(Women, MarkdownxModelAdmin)
admin.site.register(User)